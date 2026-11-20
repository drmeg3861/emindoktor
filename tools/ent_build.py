import json,re,collections,argparse
from pathlib import Path
# Yollar betiğin konumuna göre çözülür; girdi/çıktı klasörü --girdi ile değiştirilebilir.
TOOLS=Path(__file__).resolve().parent
ap=argparse.ArgumentParser(description="SKRS satırlarından enteral beslenme ürün listesi (ent.json) üretir.")
ap.add_argument('--girdi',type=Path,default=TOOLS/'in',help="rows.json klasörü; ent.json da buraya yazılır (varsayılan: tools/in)")
IN=ap.parse_args().girdi
r=json.load(open(IN/'rows.json',encoding='utf-8'))
v=[x for x in r if (x.get('atc') or '').startswith(('V06DB','V06DX','V06D','V06DA','V06DC','V06B')) ]
FL=r'(CIKOLATA|CILEK|CILEKLI|MUZ|MUZLU|VANILYA|VANILLA|VANILYALI|VANİLYA|KAKAOLU|KAHVE|KAHVELI|KAYISI|SEFTALI|ORMAN|MANGO|TROPIK|TROPIKAL|TROPİKAL|TROPIC|PORTAKAL|KARAMEL|NOTR|NOTRAL|NEUTRAL|AROMASIZ|MULTIFRUIT|CAPPUCCINO|CAPPUCINO|MANDALIN|FINDIK|TAVUK|MANTAR|COFFEE|CHOCOLATE|AHUDUDU|AHUDUDULU|KAYISI-SEFTALI|YABANI|CAFFE|LIMON|PORTAKAL-LIMON|SEFTALI-ZENCEFIL|DRING)'
def split(ad):
    a=ad.replace('İ','I')
    m=re.search(r'\b'+FL+r'\b',a)
    m2=re.search(r'\(?\b\d+(?:[.,]\d+)?\s*(?:X|x)?\s*\d*\s*(ML|GR|G|KG)\b',a)
    cut=min([x.start() for x in [m,m2] if x] or [len(a)])
    # keep caloric descriptors like "2 CAL", "1,5 KCAL", "2.0"
    base=a[:cut].strip(' (-,')
    k=re.match(r'^(.*?\b(?:2 CAL|1,5 KCAL|1.6 KCAL|2 KCAL|2\.0|1,0))\b',a)
    if k and len(k.group(1))>len(base): base=k.group(1)
    rest=a[len(base):].strip(' ,')
    if base.endswith(' CIKOLATALI'): base=base[:-11]; rest='cikolatali '+rest
    base=re.sub(r'\s+',' ',base).strip()
    return base.title().replace('Ii','II'),rest.lower() or 'standart'
def cat(ad):
    a=ad.upper()
    if re.search(r'THICK',a): return 'kivam'
    if re.search(r'PEDIASURE|FORTINI|NUTRINI|JUNIOR|JUNİOR|NEOCATE|EVOLVIA|APTAMIL|BEBELAC|HUMANA|SMA |PRENAN|ALFAMINO|ALTHERA|AL 110|MILUPA|BASIC|COMIDA|PKU|MSUD|HCU|TYR|LYS|HOM|UCD|GA |OS 2|LEU|GALACTOMIN|KETOCAL|MONOGEN|GLYCOSADE|LOPROFIN|LOPRAFIN|LPD|LPF|DALIA|FANTOMALT|PREKUNIL|SIMILAC|ELECARE|RENASTEP|MODULEN|PROTIFAR|CONFORMIL|PREMATIL|EOPROTIN|PEPTISYNEO|PREGOMIN',a): return None
    if re.search(r'NUTRISON|OSMOLITE|JEVITY|ISOSOURCE|NOVASOURCE|OXEPA|DIASON|SURVIMED|RECONVAN|INTESTAMIN|PERATIVE|NUTRENA 500|\b(500|1000|1500) ?ML\b',a) and not re.search(r'ORAL|DRINK|POWDER',a): return 'sonda'
    return 'oral'
def child(a):
    return re.search(r'PEDIASURE|FORTINI|NUTRINI|RESOURCE JUNIOR|PEPTAMEN JUN|ISOSOURCE JUNIOR|NEOCATE JUNIOR',a.upper().replace('İ','I'))
G=collections.defaultdict(lambda:collections.defaultdict(list))
for x in v:
    if 'KETOMINO' in x['ad'] or 'AMINESS' in x['ad'] or 'KETOSTERIL' in x['ad'] or 'KETONEPHRO' in x['ad'] or 'EAS ORAL' in x['ad']: continue
    c='cocuk' if child(x['ad']) else cat(x['ad'])
    if not c: continue
    b,rest=split(x['ad'])
    G[c][b].append([rest,'a' if x['st']=='aktif' else 'p',None])
out={}
for c,d in G.items():
    L=[]
    for b,s in d.items():
        seen=set();ss=[]
        for t in sorted(s,key=lambda t:(t[1],t[0])):
            if t[0] in seen: continue
            seen.add(t[0]);ss.append(t)
        L.append({'ad':b,'s':ss,'a':any(t[1]=='a' for t in ss)})
    out[c]=L
    print(c,len(L),sum(p['a'] for p in L));print('  ',[p['ad'] for p in L if p['a']])
json.dump(out,open(IN/'ent.json','w',encoding='utf-8'),ensure_ascii=False)
