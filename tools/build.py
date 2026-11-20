import json,re
exec(open('/home/claude/map.py').read())
rows=json.load(open('/home/claude/in/rows.json'))
names=json.load(open('/home/claude/in/names.json'))
FORM=[('NEBUL','nebül'),('INHAL','inhaler'),('AEROSOL','inhaler'),('DISKUS','inhaler'),('ENJEK','enjeksiyon'),('AMPUL','enjeksiyon'),('FLAKON','enjeksiyon'),('INFUZ','enjeksiyon'),('KALEM','enjeksiyon'),
 ('SURUP','şurup'),('SUSP','süspansiyon'),('DAMLA','damla'),('SPREY','sprey'),('KREM','krem'),('MERHEM','merhem'),('POMAD','merhem'),('JEL','jel'),('SUPP','supp.'),('FITIL','supp.'),('TRANSDERMAL','flaster'),('FLASTER','flaster'),
 ('EFERVESAN','efervesan'),('SASE','şase'),('GRANUL','granül'),('ORAL COZ','oral çözelti'),('ORAL SOL','oral çözelti')]
FORMWORD=re.compile(r'^(ENJ|ICIN|FILM|TABLET|TB\.?|KAPSUL|SERT|YUMUSAK|DRAJE|SURUP|ENJEKSIYONLUK|AMPUL|FLAKON|KREM|MERHEM|DAMLA|SPREY|GASTRO|UZATILMIS|DEGISTIRILMIS|AGIZDA|EFERVESAN|INHALASYON|INHALER|NEBULIZASYON|ORAL|IV|IM|S\.C\.|KONTROLLU|COZELTI|SUSPANSIYON|TOZ|CIGNEME|DISPERSIBL|RETARD|SR|XR|ER|CR|MR|LA|PR|ODT|PLUS|FORTE)\b')
def brand(ad):
    t=ad.replace('.',' ').split()
    out=[]
    for w in t:
        if re.match(r'^[\d%(]',w) or (out and FORMWORD.match(w) and w not in ('PLUS','FORTE','SR','XR','LA','CR','MR','ER','PR','RETARD','HBS','ZOK')): break
        if not out and FORMWORD.match(w) and w not in ('PLUS','FORTE'): pass
        out.append(w)
        if len(out)>=4: break
    b=' '.join(out).strip(' -,')
    return b.title() if b else ad.split()[0].title()
SRE=re.compile(r'(%\s?\d+(?:[.,]\d+)?|\d+(?:[.,]\d+)?\s*(?:MG|MCG|MIKROGRAM|µG|G|IU|I\.U\.|ÜNITE|U)(?![A-ZÇĞİÖŞÜ])(?:\s*(?:/|\+)\s*\d*(?:[.,]\d+)?\s*(?:MG|MCG|G|ML|IU|I\.U\.|DOZ|ÜNITE|U)?(?![A-ZÇĞİÖŞÜ]))*)',re.I)
def strength(ad):
    m=SRE.search(ad)
    s=m.group(1).strip() if m else ''
    s=re.sub(r'\s+',' ',s).lower().replace('i.u.','IU').replace(' iu',' IU').replace('iu','IU')
    return s
def form(ad):
    u=ad.upper()
    for k,v in FORM:
        if k in u: return v
    return ''
def mgnum(s):
    m=re.fullmatch(r'(\d+(?:[.,]\d+)?)\s*mg',s)
    return float(m.group(1).replace(',','.')) if m else None
def match(code,atc):
    return atc.startswith(code[:-1]) if code.endswith('*') else (atc==code or (len(code)<7 and atc.startswith(code)))
out={}; stats={}; BAR={}
ETK=json.load(open('/home/claude/in/etkin.json'))
for n in names:
    if n not in M: continue
    codes,combo=M[n]
    sel=[r for r in rows if any(match(c,r['atc']) for c in codes)]
    # ayrıştırmalar
    if n=="Levosalbutamol+İpratropium": sel=[r for r in rows if 'IPRALEV' in r['ad']]
    if n=="Mikofenolik asit": sel=[r for r in sel if re.search(r'\b(180|360) ?MG',r['ad'])]
    if n=="Mikofenolat mofetil": sel=[r for r in sel if not re.search(r'\b(180|360) ?MG',r['ad'])]
    if n=="Estradiol+Siproteron": sel=[r for r in sel if 'CLIMEN' in r['ad']]
    if n=="Etinilestradiol+Siproteron": sel=[r for r in sel if 'CLIMEN' not in r['ad']]
    if n in ("Levodopa+Benserazid","Levodopa+Karbidopa"):
        key='benserazid' if n=="Levodopa+Benserazid" else 'karbidopa'
        sel=[r for r in sel if key in ETK.get(str(r['bar']),('',''))[0] or (key=='benserazid' and ('MADOPAR' in r['ad'] or 'DOMIRPA' in r['ad'])) or (key=='karbidopa' and 'DOPADEX' in r['ad'])]
    BAR.setdefault(n,set()).update(str(r['bar']) for r in sel)
    br={}
    for r in sel:
        b=brand(r['ad']); s=strength(r['ad']); f=form(r['ad'])
        lab=(s+(' · '+f if f else '')).strip(' ·') or (f or '—')
        d=br.setdefault(b,{})
        if d.get(lab)!='aktif': d[lab]=r['st']
    l=[]
    for b,d in br.items():
        s=[[lab,st[0],mgnum(lab.split(' · ')[0])] for lab,st in d.items()]
        s.sort(key=lambda x:(x[2] if x[2] is not None else 1e9, x[0]))
        l.append({"ad":b,"s":s,"a":any(x[1]=='a' for x in s)})
    l.sort(key=lambda x:x['ad'])
    cmb=[]
    if combo:
        inn,pre=combo
        cr=[r for r in rows if r['st']=='aktif' and inn in r['atcad'] and r['atcad']!=inn and r['atc'].startswith(pre)]
        BAR.setdefault(n,set()).update(str(r['bar']) for r in cr)
        cb={}
        for r in cr:
            b=brand(r['ad']); cb.setdefault(b,{'w':r['atcad'],'s':set()})['s'].add(strength(r['ad']))
        cmb=[{"ad":b,"w":v['w'],"s":sorted(v['s'])} for b,v in sorted(cb.items())]
    out[n]={"l":l,"c":cmb}
    stats[n]=(sum(x['a'] for x in l),len(l),len(cmb))
json.dump(out,open('/home/claude/in/tp.json','w'),ensure_ascii=False,separators=(',',':'))
low=[(n,v) for n,v in stats.items() if v[0]<2]
print("toplam aktif marka:",sum(v[0] for v in stats.values()),"| kombine:",sum(v[2] for v in stats.values()))
print("aktif <2:",len(low)); print(low)
import os;print(os.path.getsize('/home/claude/in/tp.json'))

json.dump({k:sorted(v) for k,v in BAR.items()},open('/home/claude/in/bar.json','w'))
