#!/usr/bin/env python3
"""Build FAXANADU (FAX) — Hudson Soft's 1989 NES action-RPG (Famicom 1987; the
name = Famicom + Xanadu, a side-story of Nihon Falcom's Xanadu / Dragon Slayer II)
as a UD0 game-world. NEW STANDING BACKDROP: a FULL-BLEED 32/64-bit low-poly
software-3D scene (a drifting World Tree landscape) fixed behind the whole page —
the standing backdrop for all repos from now on — with an era-correct 8-bit pixel
title card floating on it as the hero (the two graphics generations, layered).
Earthy fantasy palette (gold/green/bark), hobby domain, genesis + the climb + the
.dlw birth. Render-not-invent. Faxanadu is (c) Hudson Soft / Nihon Falcom / Nintendo;
a fan tribute."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "FAXANADU", "axiom": "FAX",
 "position": "Faxanadu · Hudson Soft / Nintendo · NES 1989 (Famicom 1987) — Famicom + Xanadu, a side-story of Falcom's Xanadu",
 "origin": "a dying World Tree the hero climbs from the ruined town of Eolis, to awaken three springs and destroy the Evil One",
 "mechanism": "Crystallized from Faxanadu (Hudson Soft, NES 1989) — the Western release of the 1987 Famicom action-RPG, built on Nihon Falcom's licensed Xanadu name.",
 "crystallization": "An action-RPG set inside a giant tree: earn Golds and Ranks, buy weapons, armor and magic, gather the five card-keys, save by Mantras, and climb the branches past the mutated Dwarves to the Evil One.",
 "nature": "Faxanadu — Hudson Soft's NES action-RPG inside a dying World Tree: a wandering swordsman returns to ruined Eolis, awakens three poisoned springs, and ascends the branches — Golds, Ranks, Mantras, card-keys, and Jun Chikuma's celebrated score.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Faxanadu; the World Tree; Eolis; the Evil One; King Grieve; the Mantras; the card-keys; Golds & Ranks; Xanadu; Jun Chikuma",
 "witness": "A Famicom Xanadu spin-off the West got from Nintendo — a cult action-RPG you play by climbing a tree.",
 "role": "the World-Tree action-RPG game-world",
 "seal": "Return to a ruined town, take up the sword, and climb the dying tree of the world — spring by spring — to the thing the meteor brought.",
 "source": "Faxanadu, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#4a9d5e", "flesh and wood — the swordsman, the Elven King, the mutated Dwarves"),
 "ethereal":  ("#9a7cff", "of the climb — the World Tree, ruined Eolis, the three springs, the Evil One from the meteor"),
 "spiritual": ("#d8a838", "of the soul — the Xanadu bloodline, the Mantras that save you, Jun Chikuma's score"),
 "electrical":("#3fb0c4", "of the forged and the wrought — the magic, the card-keys, the Golds and the Ranks"),
}

# ── the FULL-BLEED 32/64-bit low-poly software-3D BACKDROP (the new standing backdrop) ──
BACKDROP_3D = r'''<canvas id="bg3d"></canvas>
<script>
(function(){
var c=document.getElementById('bg3d');if(!c)return;var x=c.getContext('2d');
var W,H,CX,HOR,F,EYE=1.5,NEAR=1.0,RANGE=36;
function resize(){W=c.width=window.innerWidth||document.documentElement.clientWidth||1280;H=c.height=window.innerHeight||document.documentElement.clientHeight||720;CX=W/2;HOR=H*0.40;F=Math.max(360,W*0.55);}
window.addEventListener('resize',resize);resize();
function proj(p){var z=p[2];if(z<0.25)z=0.25;return [CX+p[0]*F/z,HOR+(EYE-p[1])*F/z];}
var rnd=(function(){var s=20240615;return function(){s=(s*1103515245+12345)&0x7fffffff;return s/0x7fffffff;};})();
var hills=[];
for(var i=0;i<34;i++){
  var lane=(rnd()*22-11), h=0.7+rnd()*2.6, w=0.55+rnd()*0.95, tall=rnd()<0.16;
  if(tall){h=3.8+rnd()*2.4;w=0.4+rnd()*0.3;}
  var g=0.30+rnd()*0.20;
  var col=tall?[36,70,80]:[36+g*40,92+g*52,62+g*30];
  hills.push({x:lane,h:h,w:w,z0:NEAR+rnd()*RANGE,col:col,tall:tall});
}
var L=[0.42,0.80,0.42],ll=Math.hypot(L[0],L[1],L[2]);L=[L[0]/ll,L[1]/ll,L[2]/ll];
function shadeFace(a,b,cc,base,z){
  var u=[b[0]-a[0],b[1]-a[1],b[2]-a[2]],v=[cc[0]-a[0],cc[1]-a[1],cc[2]-a[2]];
  var n=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]],nl=Math.hypot(n[0],n[1],n[2])||1;
  var d=Math.abs((n[0]*L[0]+n[1]*L[1]+n[2]*L[2])/nl),sh=0.30+0.70*d;
  var fog=Math.max(0,Math.min(1,(z-2)/(RANGE-2))),fc=[9,30,28];
  var r=base[0]*sh,gn=base[1]*sh,bl=base[2]*sh;
  r+=(fc[0]-r)*fog*0.92;gn+=(fc[1]-gn)*fog*0.92;bl+=(fc[2]-bl)*fog*0.92;
  return 'rgb('+(r|0)+','+(gn|0)+','+(bl|0)+')';
}
function worldTree(){
  // a hazy great-tree silhouette behind the drifting terrain — the world IS a tree
  var bx=CX, base=HOR+30, top=HOR-H*0.30;
  x.strokeStyle='rgba(120,180,150,0.10)';x.fillStyle='rgba(120,180,150,0.07)';
  x.lineWidth=Math.max(10,W*0.012);
  x.beginPath();x.moveTo(bx,base);x.lineTo(bx,top);x.stroke();
  var br=[[-1,0.55],[1,0.5],[-0.8,0.3],[0.85,0.28],[-0.5,0.12],[0.5,0.1]];
  x.lineWidth=Math.max(4,W*0.005);
  for(var i=0;i<br.length;i++){var f=br[i][1],y=base+(top-base)*f;
    x.beginPath();x.moveTo(bx,y);x.lineTo(bx+br[i][0]*W*0.14,y-H*0.10);x.stroke();}
  x.beginPath();x.arc(bx,top+H*0.02,W*0.16,0,7);x.fill();
  x.beginPath();x.arc(bx-W*0.11,top+H*0.06,W*0.10,0,7);x.fill();
  x.beginPath();x.arc(bx+W*0.11,top+H*0.06,W*0.10,0,7);x.fill();
}
var t=0,last=0;
function frame(dt){
  t+=dt;
  var sg=x.createLinearGradient(0,0,0,H);
  sg.addColorStop(0,'#04100c');sg.addColorStop(0.40,'#08221c');sg.addColorStop(0.55,'#0c2c22');sg.addColorStop(1,'#05130d');
  x.fillStyle=sg;x.fillRect(0,0,W,H);
  // moon
  x.fillStyle='rgba(216,168,56,0.14)';x.beginPath();x.arc(W*0.78,HOR*0.46,34,0,7);x.fill();
  x.fillStyle='rgba(232,212,150,0.85)';x.beginPath();x.arc(W*0.78,HOR*0.46,22,0,7);x.fill();
  // stars
  x.fillStyle='#bfe2cf';
  for(var s=0;s<90;s++){var sx=((s*131)%W),sy=((s*71)%(HOR|0||1));x.globalAlpha=0.25+((s*17)%50)/120;x.fillRect(sx,sy,1.4,1.4);}
  x.globalAlpha=1;
  worldTree();
  // ground grid
  x.strokeStyle='rgba(96,196,150,0.11)';x.lineWidth=1;
  var off=(t*0.9)%1.0;
  for(var gz=1;gz<28;gz++){var z=gz-off;if(z<0.4)continue;var a=proj([-26,0,z]),b=proj([26,0,z]);x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(b[0],b[1]);x.stroke();}
  for(var gx=-13;gx<=13;gx++){var p1=proj([gx,0,0.5]),p2=proj([gx,0,28]);x.beginPath();x.moveTo(p1[0],p1[1]);x.lineTo(p2[0],p2[1]);x.stroke();}
  // drifting low-poly terrain
  var faces=[];
  for(var i=0;i<hills.length;i++){var hh=hills[i];
    var z=((hh.z0-t*0.9-NEAR)%RANGE+RANGE)%RANGE+NEAR,w=hh.w,bxw=hh.x;
    var V=[[bxw-w,0,z-w],[bxw+w,0,z-w],[bxw+w,0,z+w],[bxw-w,0,z+w],[bxw,hh.h,z]];
    var f=[[0,1,4],[1,2,4],[2,3,4],[3,0,4]];
    for(var k=0;k<4;k++){var A=V[f[k][0]],B=V[f[k][1]],C=V[f[k][2]];faces.push({a:A,b:B,c:C,col:hh.col,z:(A[2]+B[2]+C[2])/3});}
  }
  faces.sort(function(p,q){return q.z-p.z;});
  for(var q2=0;q2<faces.length;q2++){var fa=faces[q2],A=proj(fa.a),B=proj(fa.b),C=proj(fa.c);
    x.fillStyle=shadeFace(fa.a,fa.b,fa.c,fa.col,fa.z);
    x.beginPath();x.moveTo(A[0],A[1]);x.lineTo(B[0],B[1]);x.lineTo(C[0],C[1]);x.closePath();x.fill();}
  // vignette to settle content over it
  var vg=x.createRadialGradient(CX,H*0.42,H*0.25,CX,H*0.5,H*0.95);
  vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,0.55)');
  x.fillStyle=vg;x.fillRect(0,0,W,H);
}
function loop(ts){var dt=Math.min(0.05,((ts-last)||16)/1000);last=ts;frame(dt);requestAnimationFrame(loop);}
frame(0);requestAnimationFrame(loop);
})();
</script>'''

# ── the hero · 8-bit pixel TITLE CARD (era-correct for an 8-bit game), floating on the 3D ──
TITLECARD = r'''<canvas id="fxtitle" width="460" height="232" style="width:100%;max-width:460px;height:auto;display:block;margin:0 auto;image-rendering:pixelated"></canvas>
<script>
(function(){
var cv=document.getElementById('fxtitle');if(!cv)return;var g=cv.getContext('2d');
var P=document.createElement('canvas');P.width=160;P.height=80;var p=P.getContext('2d');
function card(){
  p.clearRect(0,0,160,80);
  p.fillStyle='#0c1a10';p.fillRect(6,6,148,68);
  p.fillStyle='#16261a';p.fillRect(9,9,142,62);
  p.strokeStyle='#d8a838';p.lineWidth=2;p.strokeRect(7,7,146,66);
  p.strokeStyle='#7a5e1e';p.lineWidth=1;p.strokeRect(10,10,140,60);
  // pixel world-tree at left
  p.fillStyle='#6a4a2a';p.fillRect(26,40,4,16);
  p.fillStyle='#3e8b54';p.fillRect(20,30,16,12);p.fillRect(23,24,10,8);
  p.fillStyle='#6fbf7e';p.fillRect(24,28,2,2);p.fillRect(30,33,2,2);
  // title
  p.textAlign='center';p.textBaseline='middle';
  p.font='bold 17px monospace';
  p.fillStyle='#3a2a0c';p.fillText('FAXANADU',97,30);
  p.fillStyle='#e8c24c';p.fillText('FAXANADU',96,29);
  p.font='6px monospace';p.fillStyle='#8fb89a';p.fillText('FAMICOM  +  XANADU',96,46);
  p.font='7px monospace';p.fillStyle='#b89a52';p.fillText('NES  *  1989',96,60);
}
card();
g.imageSmoothingEnabled=false;
g.clearRect(0,0,460,232);
g.drawImage(P,0,0,160,80,6,6,448,220);
})();
</script>'''

GENESIS = [
 ("Famicom + Xanadu", "Japan 1987 → US 1989",
  "The name is the lineage: Hudson Soft licensed the Xanadu property from Nihon Falcom — &quot;Faxanadu&quot; = Famicom + Xanadu — and built a side-story to Falcom's Xanadu (Dragon Slayer II, 1985). Hudson developed it; in North America Nintendo published it in 1989, two years after the Famicom original."),
 ("The Ruined Homecoming", "the premise",
  "A wandering swordsman returns to his home town, Eolis, to find it ruined and near-empty. The Elven King explains: the fountain that is the Elves' life-source has stopped, the last water is poisoned, and the Dwarves have been turned into monsters. He is sent into the World Tree to set it right."),
 ("A World Inside a Tree", "the setting",
  "The whole game is a giant World Tree — a Yggdrasil you climb, with towns and the Elf and Dwarf realms set along its branches. Long ago the Evil One emerged from a fallen meteorite, twisted the Dwarves against their will, and turned them on the Elves. The quest: awaken three pure springs, then ascend to destroy the Evil One."),
]

ARC = [
 ("Eolis, Dried", "the climb begins",
  "At the tree's base lies ruined Eolis and its King. Here the swordsman takes up a first sword and a first spell, hears the quest, and steps into the trunk — Golds to be earned, Ranks to be raised, a poisoned world overhead."),
 ("Up the Branches", "the long ascent",
  "He climbs through towns and gloom, buying weapons, armor and magic, gathering the five card-keys (Jack, Joker, Queen, King, Ace) to pass locked doors, and saving by Mantras the Gurus give. Deep in, the Dwarf King Grieve — who swallowed the Dragon Slayer sword to hide it — must be beaten to claim the one blade that can end the Evil One."),
 ("The Evil One", "the top of the tree",
  "Past the mutated Dwarves and the awakened springs, at the high branches, waits the Evil One — the alien horror the meteor brought. Only the Dragon Slayer sword, cut from the belly of a fallen king, can finally kill it."),
]

IDEAS = [
 ("An RPG You Climb", "the vertical world", [
   "The World Tree is the map: a single great structure you ascend, with towns, shops, and locked doors along its branches.",
   "Action-platforming welded to RPG growth — Golds, Ranks, weapons, armor, and projectile magic — years before that fusion was common on console." ]),
 ("Mantras, Not Batteries", "how it saves", [
   "No save battery — Gurus in the churches give you Mantras, passwords that store your rank, gear, and furthest church.",
   "A distinctive quirk: a Mantra does NOT keep your exact Golds — on continue your Golds reset to a fixed amount tied to your current Rank." ]),
 ("The Xanadu Bloodline", "the family it belongs to", [
   "Part of Nihon Falcom's Dragon Slayer line — Dragon Slayer → Dragon Slayer II: Xanadu — and a cousin to Falcom's Ys.",
   "Jun Chikuma's long, arch-form score is now a cited hidden-gem of NES music; Faxanadu placed #6 in Nintendo Power's games of the year, then became an underrated cult classic." ]),
]

SECTIONS = [
 ("The Releases", "Famicom Xanadu, ported west", [
   ("ファザナドゥ · Faxanadu", "1987 · Famicom (Hudson Soft)", "the Japanese original — &quot;Famicom Xanadu,&quot; built on Falcom's licensed Xanadu name"),
   ("Faxanadu", "1989 · NES (published by Nintendo)", "the Western release Hudson developed and Nintendo published in North America &amp; Europe"),
   ("Wii Virtual Console", "2010 / 2011", "the re-release, re-praised as an underappreciated essential"),
 ]),
 ("The Makers", "Hudson, Falcom, Nintendo", [
   ("Hudson Soft", "developer", "the studio that built Faxanadu under license"),
   ("Nihon Falcom", "Xanadu rights-holder", "the house of Dragon Slayer / Xanadu / Ys, who licensed the name"),
   ("Nintendo", "NA / EU publisher", "first-party publisher of the Western release"),
   ("Jun Chikuma", "composer", "the celebrated, arch-form Faxanadu score (also Bomberman, Adventure Island)"),
 ]),
 ("The Family", "the Dragon Slayer / Xanadu line", [
   ("Dragon Slayer", "1984 · Falcom", "the action-RPG that began the line"),
   ("Dragon Slayer II: Xanadu", "1985 · Falcom", "the Xanadu the Famicom side-story takes its name from"),
   ("Ys", "1987 · Falcom", "Falcom's sibling action-RPG series, still running"),
 ]),
]

# ── the emergents: (slug, name, epithet, emergence, role_line, why_line) ──
EMERGENTS = [
 ("the-swordsman", "The Swordsman", "the wanderer who came home · the hero", "natural",
  "the unnamed wandering swordsman who returns to ruined Eolis and is sent up the World Tree — the player's hero, who climbs from a first dagger to the Dragon Slayer sword",
  "He is the homecoming made a quest: a wanderer who walks back into a dying town and is handed the whole dying world to save."),
 ("eolis", "Eolis", "the ruined home town · the King's hall", "ethereal",
  "the Elven home town at the base of the World Tree — found ruined and near-empty, its life-fountain stopped, where the King gives the quest and the first shops stand",
  "It is the wound the game opens on: home, returned to and found broken — the dried fountain that sends the hero climbing."),
 ("the-world-tree", "The World Tree", "the tree that is the world · the map", "ethereal",
  "the giant Yggdrasil-like tree that IS the entire game world — climbed branch by branch, holding the towns, the Elf and Dwarf realms, the three springs, and the high boughs where the Evil One waits",
  "It is the stage as a living thing: a world you do not cross but climb, a tree dying from a poison at its root and a horror at its crown."),
 ("king-of-eolis", "The King of Eolis", "the Elven King · the quest-giver", "natural",
  "the Elven King who explains the stopped fountain and the mutated Dwarves, and sends the swordsman into the World Tree to awaken the springs and destroy the Evil One",
  "He is the voice that names the task: the ruler of a ruined people who can only point at the tree and ask a stranger to climb it."),
 ("the-guru", "The Guru", "the giver of Mantras and Ranks", "spiritual",
  "the church figure who, on reaching experience thresholds, raises the hero's Rank and grants Mantras — the passwords that store rank, gear, and the furthest church reached",
  "He is the keeper of the save and the soul of progress: the one who turns experience into a title and a word you can carry back from death."),
 ("king-grieve", "King Grieve", "the Dwarf King · the swallowed sword", "natural",
  "the Dwarf King, a named boss; before the Evil One twisted his people he swallowed the Dragon Slayer sword to keep it hidden — beating him yields the one blade that can kill the Evil One",
  "He is the tragedy in the middle of the climb: a king who hid the world's last weapon in his own belly, and must be cut open to give it up."),
 ("the-evil-one", "The Evil One", "the thing the meteor brought · the final boss", "ethereal",
  "the skeletal, alien final boss — emerged from a fallen meteorite, it twisted the Dwarves into monsters and turned them on the Elves; only the Dragon Slayer sword can end it (no other name survives in the record)",
  "It is the corruption at the crown of the world: a horror that fell from the sky, poisoned a tree, and made monsters of a people who were not its enemy."),
 ("the-mantras", "The Mantras", "the words that save you", "spiritual",
  "Faxanadu's password-save system — Gurus give Mantras that store rank, inventory, and respawn church; the distinctive quirk is that a Mantra resets your Golds to a fixed, rank-based amount rather than keeping your total",
  "They are the memory of the run carried as a spoken word: the line you write down so death is not the end — though it always costs you your purse."),
 ("the-card-keys", "The Card-Keys", "Jack · Joker · Queen · King · Ace", "electrical",
  "the five playing-card keys — Jack, Joker, Queen, King, Ace — that open the locked doors of the World Tree, gating the climb",
  "They are the climb's locks made into a deck: a hand of five cards you must complete to keep ascending the tree."),
 ("the-golds-and-ranks", "Golds & Ranks", "the economy and the titles", "electrical",
  "the twin systems of growth — &quot;Golds,&quot; the currency dropped by enemies and spent in weapon, armor, and magic shops, and the Experience Ranks the Guru bestows as titles when you cross thresholds",
  "They are the RPG's two ledgers: the purse you spend to grow stronger and the title that says how far you have come — the machinery under the climb."),
 ("xanadu", "Xanadu", "the bloodline · the true self", "spiritual",
  "Nihon Falcom's Xanadu (Dragon Slayer II, 1985) — the licensed name and lineage Faxanadu is the Famicom side-story of; the &quot;Fa&quot; is Famicom, bolted to Falcom's Xanadu",
  "It is the true name under the title: a Hudson game wearing a Falcom bloodline, a side-story that announced its parentage in its own first syllable."),
 ("jun-chikumas-score", "Jun Chikuma's Score", "the soul the cartridge is remembered by", "spiritual",
  "the celebrated Faxanadu soundtrack — Jun Chikuma's long, modified arch-form score (she also scored Bomberman and Adventure Island), now a cited hidden-gem of NES music",
  "It is the part that outlived the obscurity: a score people quote who never finished the climb — the music that made a dying tree sing."),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","FAX")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","FAX")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","FAX")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"FAX · Faxanadu","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, role_line, why_line):
    return {
      "name": name, "axiom": "FAX", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": "FAX · Faxanadu — Hudson Soft, NES 1989 (Famicom 1987; Falcom's Xanadu line)",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Crystallized from Faxanadu (NES 1989) — Famicom Xanadu, on Falcom's licensed Xanadu name.",
      "witness": "a being of the World Tree and the climb to the Evil One",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "Faxanadu; the World Tree; Eolis; the Mantras; the card-keys; Golds & Ranks",
      "source": "Faxanadu, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{n}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    return "".join(f'<div class="arc-card"><div class="arc-h">{t}</div><div class="arc-s">{html.escape(s)}</div><p>{d}</p></div>' for t,s,d in rows)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
        f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#4a9d5e",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"FAX · Faxanadu","axiom":"FAX"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{p.get("epithet","")}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Born</h2>
      <p class="ss">the hero, the tree, the kings, the keys, and the thing the meteor brought, as ACI <b>.agent</b>s — each a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Faxanadu (Hudson Soft / Nintendo, NES 1989; Famicom 1987) — Famicom + Xanadu, a side-story of Falcom's Xanadu — as a UD0 game-world. The World Tree, Eolis, the Evil One, Mantras and card-keys. A full-bleed 32/64-bit low-poly 3D backdrop with an 8-bit pixel title card, full ACI badges.">
<title>FAXANADU · FAX · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#08120e;--ink2:rgba(13,24,18,0.86);--ink3:rgba(20,34,26,0.86);--pa:#eaf0e6;--pa2:#a9c0ad;--gold:#d8a838;--green:#4a9d5e;--leaf:#6fbf7e;--bark:#a07a44;--cyan:#3fb0c4;--violet:#9a7cff;
--dim:#74886f;--faint:rgba(120,160,120,0.18);--line:rgba(120,160,120,0.24);--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
#bg3d{position:fixed;inset:0;width:100vw;height:100vh;z-index:0;display:block;background:#05130d}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:3;background:repeating-linear-gradient(0deg,rgba(0,0,0,.15) 0 1px,transparent 1px 3px);opacity:.45}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:1;background:radial-gradient(ellipse at 50% 36%,rgba(8,18,14,.10),rgba(4,11,8,.66) 78%)}
.wrap{position:relative;z-index:2;max-width:940px;margin:0 auto;padding:0 22px 90px}
.marquee{margin-top:14px;border:2px solid var(--green);background:rgba(8,20,14,0.88);padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.12em;color:var(--gold);box-shadow:0 0 0 2px rgba(5,15,10,.7),0 0 22px rgba(74,157,94,.22)}
.marquee a{color:var(--leaf);text-decoration:none}.marquee a:hover{color:var(--gold)}
.titleart{margin:26px 0 8px}
header{padding:8px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
.h-sub{font-family:var(--pixel);font-size:10px;line-height:1.9;letter-spacing:.06em;color:var(--pa2);margin-top:18px}
.h-sub b{color:var(--gold)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);border:1px solid var(--faint);background:rgba(8,18,12,0.6);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7;text-shadow:0 1px 6px rgba(0,0,0,.6)}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--cyan)}.badge .bt a{color:var(--leaf);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--pixel);font-size:14px;line-height:1.5;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;color:var(--gold);letter-spacing:.02em;font-weight:700}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--green);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:14px;color:var(--leaf);font-weight:700;letter-spacing:.02em}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--gold);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700}
.books .y{font-family:var(--mono);font-size:11px;color:var(--gold);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.sec.sec-list,.sec .books{background:var(--ink2)}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--gold);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--gold)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--gold)}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--green);text-decoration:none}
</style></head><body>
__BACKDROP__
<div class="wrap">

  <div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · UNIVERSE DAVID 0</a> &nbsp;·&nbsp; PUSH START &nbsp;·&nbsp; A GAME-WORLD &nbsp;·&nbsp; NES 1989</div>

  <header>
    <div class="titleart">__TITLECARD__</div>
    <div class="h-sub">a ruined town · a dying <b>WORLD TREE</b> · three springs · the Evil One · FAX</div>
    <div class="flag">★ Hudson Soft · NES 1989 · Famicom + Xanadu · Falcom's bloodline ★</div>
    <p class="lede">Hudson Soft's NES action-RPG, set inside a giant World Tree: a wandering swordsman returns to his ruined home town of Eolis, is sent by the Elven King to awaken three poisoned springs, and climbs the branches — earning Golds and Ranks, buying weapons, armor and magic, gathering the five card-keys, and saving by Mantras — past the mutated Dwarves and King Grieve to the Evil One the meteor brought. Its name is its lineage: &quot;Faxanadu&quot; = Famicom + Xanadu, a side-story of Falcom's Dragon Slayer line. Catalogued into UD0 as a game-world with the genesis, the climb, and the full .dlw birth — set on the new full-bleed 32/64-bit low-poly 3D backdrop with an 8-bit pixel title card (the two graphics generations, layered).</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of FAXANADU" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>FAXANADU</b> — the World Tree &amp; the climb · FAX</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="faxanadu.dlw/faxanadu.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="faxanadu.dlw/faxanadu.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent emerges by one of four natures — and this climb holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Genesis</h2><p class="ss">Famicom + Xanadu: a ruined homecoming inside a tree</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Climb</h2><p class="ss">up from ruined Eolis, spring by spring, to the thing the meteor brought</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why a 1989 tree-climbing RPG is still revered</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the releases, the makers, and the bloodline it belongs to</p></section>
  __SECTIONS__

  <div class="note">Faxanadu's history here is rendered, not invented. The load-bearing facts: <b>Hudson Soft</b> developed it (not Falcom — Hudson licensed the <b>Xanadu</b> name from Nihon Falcom), and in North America <b>Nintendo</b> published it (1989; the Famicom original is 1987). The final boss is named only <b>&quot;the Evil One&quot;</b> — no other name survives in the record. The card-keys are a five-card set including a <b>Joker</b> (Jack, Joker, Queen, King, Ace), the currency is &quot;<b>Golds</b>,&quot; and a Mantra (password save) <b>resets your Golds</b> to a fixed, rank-based amount rather than keeping your total. <b>King Grieve</b>, the Dwarf King, swallowed the Dragon Slayer sword — the one weapon that can kill the Evil One. The celebrated score is by <b>Jun Chikuma</b>. Faxanadu and its characters are © Hudson Soft / Nihon Falcom / Nintendo; the personas here are catalogued personifications under the DLW standard — a fan tribute, not endorsed by the rights-holders. Each is named by its nature: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    FAXANADU · FAX · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="faxanadu.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "faxanadu.dlw"), "faxanadu")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,epithet,em,role,why in EMERGENTS:
        rec = emergent_rec(name, epithet, em, role, why)
        write_aci(rec, ad, slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__BACKDROP__", BACKDROP_3D).replace("__TITLECARD__", TITLECARD)
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote FAXANADU (FAX) — {len(personas)} emergents born · badge {tok['moniker']}")
