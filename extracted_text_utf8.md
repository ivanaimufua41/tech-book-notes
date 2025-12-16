--- Dumping all text for system_design_tips.pdf ---


[Page 1]
VOLUME2 
Alex Xu & Sahn Lam 


[Page 2]
System Design Interview 
An Insider's Guide 
Volume 2 
Alex Xu I Sahn Lam 
6' ByteByteGo 


[Page 3]
SYSTEM DESIGN INTERVIEW - AN INSIDER'S GUID E (VOLUME 2) 
Copyright ⌐2022 Byte Code LLC 
All rights reserved . This book or any portion thereof may not be reprodu ce d or used in 
any manner whatsoever without the express writt en permi ssion of the publi sh e r except 
for the use of brief quotati ons in a book review. 
Join the community 
We crea ted a members -only Discord group . It is design ed for communit y disc u ssio n s on 
the following topics : 
ò System design fundamentals . 
ò Showcasing design diagr ams and gettin g feedback. 
ò Finding mock intervi ew buddies . 
ò General chat with community members. 
Come join us and introduce yourself to the community, today! Use the link b elow or 
scan the barcode . 
Invite link: http ://bit.ly /systemdiscord 
-


[Page 4]
ontents 
Foreword iii 
Acknowledgements v 
Chapter 1 Proximity Service 1 
Chapter 2 Nearby Friends 35 
Chapter 3 Google Maps 59 
Chapter 4 Distributed Message Queue 91 
Chapter 5 Metrics Monitoring and Alerting System 131 
Chapter 6 Ad Click Event Aggregation 159 
Chapter 7 Hotel Reservation System 195 
Chapter 8 Distributed Email Service 225 
Chapter 9 53-like Object Storage 253 
Chapter 10 Real-time Gaming Leaderboard 289 
Chapter 11 Payment System 315 
Chapter 12 Digital Wallet 341 
Chapter 13 Stock Exchange 379 
Afterword 415 
Index 417 
I i 


[Page 5]
Foreword 
We are delighted you are joining us to become better equipped for system design inter ¡
views. System design interviews are the most difficult to tackle of all techni cal interview 
questions . The questions test the interviewees' ability to design a scalable software sys¡
tem. This could be a news feed, Google search, chat application , or any other system . 
These questions are intimidating and there is no fixed pattern to follow when tackling 
them. The questions are usually very broad and vague. They are open-ended , with sev¡
eral plausible angles of attack, and often no perfect answer. 
Many companies ask system design interview questions because the communication and 
problem-solving skills they test for are similar to the skills that software engineers use 
in their daily work. A candidate is evaluated on how they analyze a vague problem and 
how they solve it, step by step. 
System design questions are open-ended. As in the real world, a design can have numer ¡
ous variations . The desired outcome is an architecture that satisfies the agreed design 
goals. The discussions may go in different directions. Some interviewers may choose 
high -level architecture to cover all aspects of the challenge, whereas others might focus 
on one or more specific areas . Typically, system requirements, constraints , and bottle¡
necks should be well understood by the candidate , to shape the direction of the inter ¡
view. 
The objective of this book is to provide a reliable strategy and know ledge base for ap¡
proaching a broad range of system design questions. The right strategy and knowled ge 
are vital for the success of an interview . 
This book also provides a step-by-step framework for how to tackle a system design 
question . It provides many examples to illustrate the systematic approach, with detail ed 
steps that you can follow. With regular practice , you will be well-equipped to tackle 
syste m design interview questions. 
This book can be seen as a sequel to the book : System Design Interview - An Insider's 
Guide (Volume 1: https ://bit.ly/systemdesigning). Although reading Volume 1 is helpful , 
it is not a necessity to do so before you read this. This book should be accessible to readers 
who have a basic understanding of distributed systems. Let's get started! 
I iii 


[Page 6]
Addi onal oun 
'Ihi'l hook cont~im rf'C rC'nu╖~ ~I th<'"'"' of <'i\ch C'h~ptn 'Thr following< ,1th11b repoòntnr y 
contAm all thr ( lick:thl Jmk'l. 
hllps ://bit.ly /sy l m esignLmk 
You can connect with Alex on social media, w here he shares system design in t<r11i~ 
tip s every week. 
twitte r.com/alexxubyte 
fm bit.ly/link edinaxu 


[Page 7]
Acknowledgements 
We wish we could say all the designs in this book are original. The truth is that most 
of th e ideas discussed here can also be found elsewhere; in engin eering blog s, research 
papers , code, tech talks, and other places . We have collected these elegant ideas and 
considered them , then added our personal experiences, to present them here in an easy¡
to-understand way. Additionally, this book has been written with the significant input 
and reviews of more than a dozen engineers and managers, some of whom made large 
writing contributions to the chapters. 1hank you so much! 
ò Proximity Service, Meng Duan (Tencent) 
ò Nearby Friends, Yan Guo (Amazon) 
ò Google Maps , Ali Aminian (Adobe, Google) 
ò Distributed Message Q_ueue, Lionel Liu (eBay) 
ò Distributed Message Qyeue, Tanmay Deshpande (Schlumberger) 
ò Ad Click Event Aggregation , Xinda Bian (Ant Group) 
ò Real-time Gaming Leaderboard , Jossie Haines (Tile) 
ò Distributed Email Servers, Kevin Henrikson (Instacart) 
ò Distributed Email Servers,]] Zhuang (Instacart) 
ò S3-like Object Store, Zhiteng Huang (eBay) 
We are particularly grateful to those who provided detailed feedback on an earlier draft 
of this book : 
ò Darshit Dave (Bloomberg) 
ò Dwaraknath Bakshi (Twitter) 
ò Pei Nan (Gusto, Airbnb) 
ò Richard Hsu (Amazon) 
ò Simon Gao (Google) 
ò Stanly Mathew Thomas (Microsoft) 
I v 


[Page 8]
ò Wenhnn Wimp: (Tiktok) 
ò Sh1wakant Rharti (Amanm) 
. huRc thnnk. to om <'dilnrs. Dominic TOVC'r ~md Doug WArrcn. Your frr dh:irk w;i ~ 
mvalu hi . 
1 st hut not 1 A$l , e1 special thanks to ╖ lvis R 11 and J Iua Li for their invaluable ron 
tribuhon . . TI1i book wouldn 't be what it is wHhout them. 
J 


[Page 9]
1 Proximity Service 
In this chapter, we design a proximity servic e. A pro ximity service is used to discover 
nearby places such as restaurants , hotels, thea ters, museums, etc., and is a core com¡
ponent that powers features like finding the best restaurant s nearby on Yelp or finding 
k-near est gas stations on Google Maps. Figure 1.1 show s the user interface via which 
you can search for nearby restauran ts on Yelp [1]. Note the map tiles used in this book 
are from Stamen Design [2] and data are from OpenStreetMap [3]. 
Distan ce 
Bod'"' P"f'!' Vif'!W 
Drrvmg(S ml.) 
bloing (2 mo.) 
Wailoflg I 1 mi.) 
W1th1n 4 blocks 
1. Mantia Bowl 
aaaa ,,. 
" --~-ll~ ... ....... ~., 
~ [.., ~~╖ 
O .,.,,.~ ,, t.o- ........ ..,,1,.1 . ...... u,:.r f)Ñ:"\oò~k.╖'J!~.,:~ .. -1. 
_..,._ .ò , 'ò\'" " --.. ......... v _ _.....,....,_, ╖~╖ . ._,.._ .. ,,.╖l'I~ 
2. WlngSlut 
DQOQt .. 
ò:╖1 ò\~ 
0 "!r.- ò F-"V'>"~ ..-.; .... .-nò╖-.~ ,.,..,.,,.... ~,._,_,,..,,.,,.,._ ("I, 
:-0....C- .f'Iò' ,..-, .,.. ,. ~╖ 1╖ .. 1 ."'IL....._ j ,...,, I~ò-. i-J"╖ ,. r-m" 
Figure 1.1: Nearby search on Yelp 
t 
ò 
,,,..,,. ;.. vJ1~1Vt" fX3 
1lò~f")i\ I~ 
.. 
~-..., :i. V1'""':.. '4, e 
DC1 4 
, q, .. ., 
0 
/ 
.i' 
0 0 
/ 
Step 1 - Understand the Problem and Establish Design Scope 
Yelp supports many features and it is not feasible to design all of them in an interview 
session, so it's important to narrow down the scope by asking question s. The inter actions 
between the interviewer and the candidate could look like this: 
Candid ate: Can a u ser specify the search radius? If there are not enough businesses 
within the search radius, does the system expand the search? 
I 1 


[Page 10]
Interviewer: ll1al 's a great que$ti on. Let ╖ ~ a~~mne we nn l c;:ire ::\ho11t h11'>mf" """ 1 lfhtn 
a specified radius . If time allows, we ran then dis cuss ho\! to expand the '\e rrh 1f rh .. , .. 
arc not enoug h businesses within the rndius . 
Candidate : Wh at's the maximal radius aJlowed? Can J assum e it's 20km ( 12 :-, m1lfò(╖ 
Interviewer : That's a reasonable assumpti on. 
Candi date: Can a user change the search radius on the UI? 
Intervi ewer: Yes, we have the following options : 0.5km (O.:n mile). 1 km (0 .fl2 mil~J . 
2km {l.24 mile), Skm (3.1 mile), and 20km (12.42 mile). 
Candidate : How does business information get added , delet ed. or updat ed? Do we need 
to reflect these operations in real-tim e? 
Interviewer : Business owners can add, delete or update a business . Assume we have 
a busines s agre ement upfront that newl y added/upd ate d businesses will be effective the 
next day. 
Candidate: A user might be moving while using the app/website, so the search results 
could be slightly different after a while. Do we need to refr esh the page to keep the results 
up to date? 
Interviewer : Let's assume a user 's moving speed is slow and we don 't n eed to constantl y 
refresh the page. 
Functional requirements 
Based on this conversation , we focus on 3 key features : 
ò Return all businesses based on a user's location (latitude and longitude pair) and 
radius . 
ò Business owners can add, delete or update a business , but this inform ation doesn't 
need to be reflected in real-time. 
ò Customers can view detailed information about a business . 
Non-functional requirements 
From the business requirements , we can infer a list of non-functional requirem ents. You 
should also check these with the interviewer. 
ò Low latency . Users should be able to see nearby businesses quickly . 
ò Data privacy . Location info is sensitive data. When we design a location -based ser¡
vice (LBS), we should always take user privacy into consideration . We need to com¡
ply with data privacy laws like General Data Protection Regulation (GDPR ) [4] and 
California Consumer Privacy Act (CCPA) [5], etc. 
ò High availability and scalability requir ements . We should ensur e our sys tem can 
handle the spik e in traffic during peak hours in densely populat ed areas. 
2 I Chapter 1. Proximity Service 
' 


[Page 11]
Back-of-the-envelope estimation 
Let's lake a look a t some back-of-the-envelope calculations lo determin e the polenti al 
scale and challenges our solution will need lo address . Assume we have 100 million daily 
active users and 200 million businesses . 
Calculate QPS 
ò Seconds in a day = 24 x 60 x 60 = 86,400. We can round it up to 105 for easier 
calculation. 105 is used thro ughout this book to represent seconds in a day. 
ò Assum e a user makes 5 search queries per day. 
100 million x 5 ò Search QPS = = 5 000 10s ' 
Step 2 - Propose High-level Design and Get Buy-in 
In this section , we discuss the following: 
ò API design 
ò High-leve l design 
ò Algorithms to find nearby businesses 
ò Data model 
API design 
We use the RESTful API convention to design a simplified version of the APis. 
GET /v1/search/nearby 
This endpoint returns businesses based on certain search criteria . In real -life applications, 
search results are usually paginated . Pagination [6] is not the focus of this chapter, but 
is worth mentioning during an interview . 
Request Parameters: 
Field Descrip tion Type 
latitude Latitude of a given location decimal 
l ongitude Longitude of a given location decimal 
radius Optional . Default is 5000 meters (about 3 miles) int 
Table 1.1: Request parameters 
{ 
11
total
11
: 10 , 
11
businesses
11
: [ { business object }] 
} 
The business object contains everything needed to render the search result page, but we 
may still need additional attributes such as pictures , reviews , star rating , etc., to rend er 
Step 2 - Propose High-level Design and Get Buy-in I 3 


[Page 12]
the busine ss detail page. l herefore. when a user clicks on the husiness dcltii l P"-fl.e. :.s ""'" 
endpoin t ca.JI to fetch lhe detailed information of a business is usually requir ed. 
APls for a business 
l11e APis related to a business object are shown in the table below. 
-API Detail ╖-GET / v1 /businesses/:id Return detailed information about a busine ss 
POST /v1/businesses Add a business 
PUT /v1/businesses/:id Update details of a business 
DELETE /v1/businesses/:id Delete a business 
Table 1.2: APis for a business 
If you are interested in real-world APis for place/business search , two examples are 
Google Places API [7] and Yelp business endpoints [8]. 
Data model 
In this section , we discuss the read/write ratio and the schema design . The scalability of 
the database is covered in deep dive. 
Read/ write ratio 
Read volume is high because the following two features are very commonly used: 
ò Search for nearby businesses. 
ò View the detailed information of a business . 
On the other hand, the write volume is low because adding, removing, and editing busi¡
ness info are infrequent operations. 
For a read-heavy system, a relational database such as MySQL can be a good fit. Let's 
take a closer look at the schema design. 
Data schema 
The key database tables are the business table and the geospatial (geo) index table. 
Business table 
The business table contains detailed information about a business . It is shown in Table 
1.3 and the primary key is business_id. 
- ---------
4 I Chapter 1. Proximity Service 


[Page 13]
business 
business_ld PK 
address 
city 
state 
country 
latitude 
longtitude 
Table 1.3: Business table 
Geo index table 
A geo index table is used for the efficient processing of spatial operations . Since this table 
requires some know ledge about geohash, we will discuss it in the "Scale the databas e" 
section on page 24. 
High-level design 
The high- level design diagram is shown in Figure 1.2. The system comprises two parts : 
location-based service (LBS) and business-re lated service. Let's take a look at each com¡
pone nt of the system . 
Step 2 - Propose High-level Design and Get Buy-in I 5 


[Page 14]
ò 
/search/nearby /businesses/ {: id} 
LBS 
Read Read Read 
Replicate 
Replicate 
Replica 
Replicate 
Database Cluster 
Figure 1.2: High-level design 
Load balancer 
Business 
Service 
Write 
Primary 
The load balancer automatically distributes incoming traffic across multiple services. 
Normally, a company provides a single DNS entry point and internally routes the API 
calls to the appropriate services based on the URL paths . 
Location-based service (LBS) 
The LBS service is the core part of the system which finds nearby businesses for a given 
radius and location . The LBS has the following characteristics: 
ò It is a read-heavy service with no write requests. 
ò QPS is high, especially during peak hours in dens e areas . 
ò This service is stateless so it's easy to scale horizontally. 
Business service 
Busine╖ss service mainly deals with two types of requests : 
ò Business owners create , update, or delete businesses. Those request s are mainl y write 
operations, and the QPS is not high . 
ò Customers view detailed information about a business. QPS is high durin g peak 
hours. 
6 I Chapter 1. Proximity Service 


[Page 15]
Database cluster 
1l1c databa c duster can use the primar y-seco ndary setup . In thi s se tup , the prim ary 
database hand les all the write o perations, and multip le replicas are used for read oper¡
ations . Data is saved t o the primary data base first and then rep l.icated to rep licas. Du e 
to th e rep lication d elay, th ere might be some discrepancy between da ta read by the LBS 
and the data writt en lo the primary data base . This inconsistency is usually no t an issue 
beca u e business information doesn 't n eed to be upd ated in real-tim e. 
Scalability of business service and LBS 
Both the business service and LBS are stateless services, so it's easy to automatically add 
mor e servers to accom modate peak traffic (e.g. mealtim e) and remov e servers durin g off¡
peak hours (e.g. sleep time). If the system operates on the cloud , we can set up different 
regions and availa bilit y z ones to further improve availability [9]. We discuss thi s more 
in the deep dive. 
Algorithms to fetch nearby businesses 
In real life, companies might use existing geospatial databases such as Geohash in Redis 
[10] or Postgres with PostGIS extension [11]. You are not expected to know the int er¡
nals of those geospatial databases during an interview . It's better to demonstrate your 
problem-solving skills and technical knowledge by explaining how the geospatial index 
works , rather than to simply throw out database names . 
The next step is to explore different options for fetching nearby busi nesses . We will list 
a few options , go over the thought process , and discuss trade -offs. 
Option 1: Two-dimensional search 
The most intuitive but naive way to get near by businesses is to draw a circle with the pre¡
defined radius and find all the businesses within the circle as shown in Figure 1.3. 
Figure 1.3: Two dimensional search 
Step 2 - Propose High-level Design and Get Buy-in I 7 


[Page 16]
'll1is pro cess ca n br trans lalrd into lh<' following psruc.ln SQ!. qu er y: 
sr Irr 1 business _id, l atit ude, longitude, 
rRflM business 
WIH.. R[. (latitude B[!WfEN {:my _lat} - ra dius AND {:my _l at } + radJu~J 
ANO 
(longitude BETWf:EN { : my _long} - radius AND {:my _long} - ~ radiu~) 
This query is not efficient because we need to scan the who le table . What if we bu1 ~ 
indexes on longitude and latitude column s? Would this improve th e e fficiency? ╖1~ 
answer is not by much. The problem is that we have two -dim ensio nal data and the dat;i,1 
returned from each dimension could still be huge. For example , as shown in Figure I .4, 1111 
can quickly retrieve dataset 1 and dataset 2, thanks to indexes on longitude and lat iluct~ 
columns . But to fetch businesses within the radius , we need to p erfo rm an intersei:i 
operation on those two datasets. This is not efficient because each datas et contains lot1 
of data . 
90 
I :? 
~ o j,---~~.Jt!Wil .. rt+i..,.........~~-!...r.---+---:::-;~~~~~~~~~ 
Cll 
~ i---1 --~~1---
-90 -╖╖--╖╖╖ -╖-╖ 
-160 -90 0 
Longitude (degrees) 
90 
Figure 1.4: Intersect two dataset s 
-.-' dataset 1 
_L 
180 
The problem with the previous approach is that the database index can only improve 
search speed in one dimension . So naturally , the follow-up question is, can we map two¡
dimensional data to one dimension? The answer is yes. 
Before we dive into the answers , let 's take a look at different types of indexing methods. 
8 I Chapter 1. Proximity Service 


[Page 17]
In a broad sense, there arr two types of geospatia l indexing approa ches, ns shown in 
Figure 1.5. 1he highligh ted ones are the algorit hms we discuss in detai l because they arC' 
common! used in Lhe indus try. 
ò Hash: even grid, geohas h, car tesian tiers [1 2], etc. 
ò Tree: quadt ree, Google S2, RTree [1 3], etc. 
Hash 
Geohash Cartesian 
Tiers 
Inde x 
Quadtree Google S2 
Figure 1.5: Different types of geospatial indexes 
RTree 
Even though the underlying implementations of those approaches are different , the high¡
level idea is the same, that is, to divide the map into smaller areas and build indexes 
for fast search . Among those , geohas h, quadtree, and Google S2 are most widely used 
in real-world applications . Let's take a look at them one by one. 
Reminder 
In a real interview, you usually don't need to explain the implementation details of 
indexing options. However, it is important to have some basic understanding of the 
need for geospatial indexing , how it works at a high level, and also its limitations. 
Option 2: Evenly divided grid 
One simple approach is to evenly divide the world into small grids (Figure 1.6). 1his way, 
one grid could have multiple businesses , and each business on the map belongs to one 
grid. 
Step 2 - Propose High-level Design and Get Buy-in I 9 


[Page 18]
75 
u;- so 
Q) 
!!? 25 
~ 
e. 0 
Q) 
~ -25 
3 -50 
-75 
Global Map - Geographic Coordinate System WGS84 Datum 
Units Degrees - Latitude I Longitude 
I 
òò. 1╖ .. t _ 
-150 -100 
I 
l . ~ - - -
-so 0 50 
Longitude (Degrees) 
100 
Figure 1.6: Global map (source: [14]) 
' . 
-
╖ - ! 
150 
This approach works to some extent, but it has one major issue: the distribution of busi¡
nesses is not even. There could be lots of businesses in downtown New York, while other 
grids in deserts or oceans have no business at all. By dividing the world into even grids, 
we produce a very uneven data distribution. Ideally, we want to use more granular grids 
for dense areas and large grids in sparse areas. Another potential challenge is to find 
neighboring grids of a fixed grid. 
Option 3: Geohash 
Geohash is better than the evenly divided grid option. It works by reducing the two¡
dimensional longitude and latitude data into a one-dimensional string of letters and dig¡
its. Geohash algorithms work by recursively dividing the world into smaller and smaller 
grids with each additional bit. Let's go over how geohash works at a high level. 
First, divide the planet into four quadrants along with the prime meridian and equa¡
tor. 
10 I Chapter 1. Proximity Service 


[Page 19]
00 
/ 
Antarcticò 
(-180,-90) (180,-90) 
Figure 1. 7: Geo hash 
ò Latitude range [- 90, OJ is represented by 0 
ò Latitude range [O, 90] is represented by 1 
ò Longitude range [- 180, OJ is represented by 0 
ò Longitude range [O, 180J is represented by 1 
Second, divide each grid into four smaller grids. Each grid can be represented by alter¡
naling between longitude bit and latitude bit. 
Step 2 - Propose High-level Design and Get Buy-in I 11 


[Page 20]
Figure 1.8: Divide grid 
Repeat this subdivision until the grid size is within the precision desired. Geohash usually 
uses base32 representation [15]. Let's take a look at two examples. 
ò geohash of the Google headquarter (length = 6): 
1001 10110 01001 10000 11011 11010 (base32 in binary) ---+ 
9q9hvu (base32) 
ò geohash of the Facebook headquarter (length = 6): 
1001 10110 01001 10001 10000 10111 (base32 in binary) ---+ 
9q9jhr (base32) 
Geohash has 12 precisions (also called levels) as shown in Table 1.4. The precision factor 
determines the size of the grid. We are only interested in geohashes with lengths between 
4 and 6. 1his is because when it's longer than 6, the grid size is too small, while if it is 
smaller than 4, the grid size is too large (see Table 1.4). 
------ -- -------
12 I Chapter 1. Proximity Service 


[Page 21]
geohas h lengt h Grid width x hei.ght 
1 5,009.4km x 4,U92.6km (the size of the planet) 
2 l,252 .3km x 624.lkm --
3 156.5km x 156km 
4 39.lkm x 19.5km 
5 4.9k.m x 4.9km 
6 l.2km x 609.4.m 
7 152.9m x 152.4m 
8 38.2m x 19m 
9 4.8m x 4.8m 
10 l.2m x 59.5cm 
11 14.9cm x l 4.9cm 
12 3.7cm x l.9cm 
Table 1.4: Geohash length to grid size mapping (source: [16]) 
How do we choose the right precision? We want to find the minimal geohash length that 
covers the whole circle drawn by the user-defined radius. The corresponding relationship 
between the radius and the length of geohash is shown in the table below. 
Radius (Kilometers) Geohash length 
0.5km (0.31 mile) 6 
lkm (0.62 mile) 5 
2km (1.24 mile) 5 
5km (3.1 mile) 4 
20km (12.42 mile) 4 
Table 1.5: Radius to geohash mapping 
This approach works great most of the time, but there are some edge cases with how the 
geohash boundary is handled that we should discuss with the interviewer. 
Boundary issues 
Geohashing guarantees that the longer a shared prefix is between two geohashes, the 
closer they are. As shown in Figure 1.9, all the grids have a shared prefix: 9q8zn. 
Step 2 - Propose High-level Design and Get Buy-in I 13 


[Page 22]
Figure 1. 9: Shared prefix 
Boundary issue 1 
However, the reverse is not true: two locations can be very close but have no shared 
prefix at all. This is because two close locations on either side of the e quator or prime 
meridian belong to different "halves" of the world. For example, in France, La Roche¡
Chalais (geohash: u000) is just 30km from Pomerol (geohash: ezzz) but their geohashes 
have no shared prefix at all ( 17]. 
Figure 1.10: No shared prefix 
Because of this boundary issue, a simple prefix SQL quer y below would fail to fetch all 
nearby busin esses. 
SELECT * FROM geohash_index WHERE geohash LIKE 1 9q8zn% 1 
14 I Chapter 1. Proximity Service 


[Page 23]
Boundary issue 2 
Another boundary issue is that tw o positions can have a long shared prc Ox, but they 
belong to different geohashes as shown in Figure 1. 11 . 
Figure 1.11: Boundary issue 
A common solution is to fetch all businesses not only within the current grid but also 
from it s neighbors. The geohashes of neighbors can be calculated in constant time and 
more details about this can be found here [17]. 
Not enough businesses 
Now let 's tackle the bonus question. What should we do if there are not enough busi¡
nesses returned from the current grid and all the neighbors combined ? 
Option 1: only return businesses within the radius . This option is easy to implement, but 
the drawback is obvious . It doesn 't return enough results to satisfy a user 's needs. 
Option 2: increase the search radius . We can remove the last digit of the geohash and 
use the new geohash to fetch nearb y businesses . If there are not enough businesses , 
we continue to expand the scope by removing another digit. This way, the grid size is 
gradually expanded until the result is greater than the desired number of results. Figure 
1.12 shows the conceptual diagram of the expandin g search process. 
-Increase search Increase search ' 
area area ...... - ... 
I !II ~ 
r r -~ 
òò l 
Figure 1.12: Expand the search pro cess 
Step 2 - Propose High-leve l Design and Get Buy-in I 15 


[Page 24]
O ti n 4: Quadtree 
n th~r popular solution is quadtre e. A quad tree [ t 8) is a data structur e that i.ci com. 
m nly used to partition a two -dimensional space by recursive ly subdiv iding it into fo1Jr 
qundrants (grids) until the contents of the grids meet certain crit eria. For example, th, 
criterion can be to keep subdividing until the number of businesses in the grid is not morp 
than 100. This number is arbitrary as the actual number can be determin ed by busine"~ 
needs . With a quadtree, we build an in-memory tree structure to answer querie s. Note 
that quadtree is an in-memory data stru cture and it is not a database solutfon . It runs on 
each LBS server, and the data structure is built at server start-up time. 
The following figure visualizes the conceptual process of subdividing the world into a 
quad tree. Let 's ass ume the world contains 200m (million) businesses . 
10m 11m 
1'('# (40m) NE (30m) 
4m Sm 
..!'-... _1'.. 
200m 
v v 
SW (70m) SE (60m) 
Figure 1.13: Qyadtree 
Figure 1.14 explains the quadtree building process in more detail. The root node repr e¡
sents the whole world map. The root node is recursively broken down into 4 quadran ts 
until no nodes are left with more than 100 businesses . 
16 I Chapter 1. Proximity Service 


[Page 25]
~ nw n sw s 
òom U:m ?omO ~ 
12mc/~c{ s:Q "~ 
, I \ ' 
,' ' ' ....... 
,' ,' ', ' ......... 
I \ 
I \ 
I 
I 
0 
50 
60 80 
Figure 1.14: Build quadtree 
The pseudocode for building quadtree is shown below: 
public void buildQuadtree(TreeNode node) { 
Represent many layers 
Q Internal node 
0 eafnode 
if (countNumberOfBusinesseslnCurrentGr{d(node) > 100) { 
node.subdivide(); 
for (TreeNode child : node.getChildren()) { 
buildQuadtree(child); 
} 
} 
} 
How much memory does it need to store the whole quadtree? 
To answer this question , we need to know what kind of data is stored. 
Data on a leaf node 
Name Size 
Top left coordinates and bottom-right 32 bytes (8 bytes x 4) coordinates to identify the grid 
List of business IDs in the grid 8 bytes per ID x 100 (maximal number 
of businesses allowed in one grid) 
Total 832 bytes 
Table 1.6: Leaf node 
Data on internal node 
Step 2 - Propose High -level Design and Get Buy -in I 17 
l 


[Page 26]
Name - --Size 
Top left coordinates and bottom-right ~2 bytes (8 bytes x 4) Coordinates to identify the grid 
Pointers to 4 children 32 bytes (8 bytes x 4) 
Total 64 bytes 
Table 1.7: Internal node 
Even though the tree-building process depends on the numb er of busin esses .within a 
grid, this number does not need to be stored in the quadtr ee node becaus e it can he 
inferred from records in the database. 
Now that we know the data structure for each node, let's take a look at the memory 
usage . 
╖ò Each grid can store a maximal of 100 businesses 
200 million 2 milli ò Number of leaf nodes =rv = rv on 100 
ò Number of internal nodes= 2 million x ~ = rv 0.67 million. If you do not know why 3 the number of internal nodes is one-third of the leaf nodes, please read the reference 
material [ 19]. 
ò Total memory requirement= 2 million x 832 bytes+ 0.67 million x 64 bytes="" 
1. 71 GB. Even if we add some overhead to build the tree , the memory requirement to 
build the tree is quite small. 
In a real interview, we shouldn't need such detailed calculations. The key takeaway here 
is that the quadtree index doesn't take too much memory and can easily fit in one server. 
Does it mean we should use only one server to store the quadtree index? The answer is 
no. Depending on the read volume, a single quadtree server might not have enough CPU 
or network bandwidth to serve all read requests. If that is the case, it will be necessary 
to spread the read load among multiple quadtree servers . 
How long does it take to build the whole quadtree? 
Each leaf node contains approximately 100 business IDs. The time complexity to build 
the tree is 1~0 log 1 ~0 , where n is the total number of businesses. It might take a few 
minutes to build the whole quadtree with 200 million businesses. 
How to get nearby businesses with quadtree? 
1. Build the quadtree in memory. 
2. After the quadtree is built, start searching from the root and traverse the tree, until 
we find the leaf node where the search origin is. If that leaf node has 100 businesses, 
return the node. Otherwise , add businesses from its neighbors until enough busi¡
nesses are returned. 
18 I Chapter 1. Proximity Service 


[Page 27]
Operational considerations for quadtree 
As mentioned abovr, it may taJ<r a few minu tes lo build a quadtrec with 200 million busi¡
nesses at the server start -up time. It is important to consider the opera tiona l implication s 
of such a long server start-up time. While the quad tree is being built, the server cannot 
serve traffic. 1herefore, wr should roll ou t a new release of the server incrementally to 
a small subset of servers al a lime. This avoids taking a large swat h of the serve r cluster 
offline and causes service brownout. Blue/green deploym ent [20] can also be used. but 
an entire cluster of new servers fetching 200 million businesses at the same time from 
the database service can put a lot of strain on the system . This can be done, but it may 
complicate the design and you shou ld mention that in the interview. 
Another operational consideratio n is how to updat e the quadtree as busin esses are added 
and removed over time. The easiest approach would be to incrementall y rebuild the 
quadtree , a small subset of servers at a time, across the entire cluster. But this would 
mean some servers would return stale data for a short period of time. However , this 
is generally an acceptable compromise based on the requirements . This can be further 
mitigated by setting up a business agreement that newly added /updated businesses will 
only be effective the next day. This means we can update the cache using a nightly job. 
One potential problem with this approach is that tons of keys will be invalidated at the 
same time , causing heavy load on cache servers . 
It's also possible to update the quadtree on the fly as businesses are added and removed . 
This certainly complicates the design , especially if the quadtree data structure could be 
accessed by multiple threads. This will require some locking mechanism which could 
dramatically complicate the quadtree implementation . 
Real-world quadtree example 
Yext [21] provided an image (Figure 1.15) that shows a constructed quadtree near Denver 
[21]. We want smaller , more granular grids for dense areas and larger grids for sparse 
areas. 
Step 2 - Propose High-level Design and Get Buy-in I 19 


[Page 28]
I -, rmu';Vl 1 
.... Be ulder, 
r--- Ila . 
l 
p l - ò 
. .~ ~ _i \& ~ .." .. 
1; .... ... 
" 
'. 
.. 
r ~ 
t-' 1 ... _ , .. 
╖ ~ 
w1k A Nf r'i.!> " ~VJ ,, . 
I',., I ~ - -
--~ 
mit-. ' 
~ I iar ';Jt. r . . Watk ns -~╖ j truburq_ 
- ╖ 
. M: r.... ~╖ - Byerò . r.J ~,---
. h~ b' - ,,. . De 
\ .. . (loan ... ò ..... . 1 . . I òò .. 
r~ 
' -~ Pa !<er .. ~ 
ò ., . ò 
li:'Y I ) I 'ii, 
Figure 1.15: Real-world example of a quadtree 
Option 5: Google 52 
Google S2 geometry library [22] is another big player in this field . Similar to Qyadtree , 
it is an in-memory solution. It maps a sphere to a lD index based on the Hilbert curve 
(a space-filling curve) [23]. The Hilbert curve has a very important property: two points 
that are close to each other on the Hilbert curve are close in lD space (Figure 1.16) . Search 
on lD space is much more efficient than on 2D. Interested readers can play with an online 
tool [24] for the Hilbert curve. 
- --- - ----- --- --- -
20 I Chapter 1. Proximity Service 
j 


[Page 29]
.. J 
4 _, ╖-
0 0.125 0.250 0.375 0.500 0.625 0.750 0.675 
Figure 1.16: Hilbert curve (source: [24]) 
52 is a complicated library and you are not expected to explain its internals during an 
interview. But because it's widely used in companies such as Google, Tinder , etc., we 
will briefly cover its advantages. 
ò 52 is grea t for geofencing because it can cover arbitrary areas with varying levels 
(Figure 1.17). According to Wikipedia , "A geofence is a virtual perimeter for a real¡
world geographic area. A gee-fence could be dynamically generated - as in a radius 
around a point location , or a gee-fence can be a predefined set of boundaries (such 
as school zones or neighborhood boundaries)" [25]. 
Geofencing allows us to define perimeters that surround the areas of interest and to 
send notifications to users who are out of the areas. This can provide richer fun c¡
tionalities than just returning nearby businesses . 
Step 2 - Propose High-level Design and Get Buy-in I 21 


[Page 30]
Geotence 
Figure 1.17: Ge of ence 
ò Another advantage ofS2 is its Region Cover algorithm [26]. Instead of having a fixed 
level (precision) as in geohash, we can specify min level , max level, and max ~ells in 
52. The result returned by S2 is more granular because the cell sizes are flexible. If 
you want to learn more, take a look at the S2 tool [26]. 
Recommendation 
To find nearby businesses efficiently, we have discussed a few options: geohash, quadtree 
and 52. As you can see from Table 1.8, different companies or technologies adopt different 
options. 
Geo Index Companies 
geohash Bing map (27], Redis [10], MongoDB [28], Lyft [29] 
quad tree Yext (21] 
Both geohash and quadtree Elasticsearch (30] 
52 Google Maps, Tinder (31] 
Table 1.8: Different types of geo indexes 
During an interview, we suggest choosing geohash or quadtree because 52 is more 
complicated to explain clearly in an interview. 
Geohash vs quadtree 
Before we conclude this section , let's do a quick comparison between geohash and 
quad tree. 
Geo hash 
ò Easy to use and implement. No need to build a tree. 
ò Supports returning businesses within a specified radius. 
ò When the precision (level) of geohash is fixed, the size of the grid is fixed as well It 
cannot dynamically adjust the grid size, based on population density . More complex 
logic is needed to support this. 
ò Updating the index is easy. For example , to remove a business from the index, 
22 I Chapter 1. Proximity Service 


[Page 31]
we just need to remove it from th e r orrespondin g row w ith th e srimc geohash and 
busi ness_id . See Figure l.1 8 for a concrete example. 
geohash business_ld 
9q8zn 3 
- - ~ 
v\.jU.C.I v 
9q8zn 4 
Figure 1.18: Remove a business 
Quadtree 
ò Slightly harder to implement because it needs to build the tree. 
ò Supports fetching k-nearest businesses . Sometimes we just want to return k-near est 
businesses and don 't care if businesses are within a specified radius . For example, 
when you are traveling and your car is low on gas, you just want to find the nearest 
k gas stations . These gas stations may not be near you, but the app needs to return 
the neares t k results. For this type of query, a quadtree is a good fit because its 
subdividing process is based on the number k and it can automatically adjust the 
query range until it returns k results . 
ò It can dynamically adjust the grid size based on population density (see the Denver 
example in Figure 1.15). 
ò Updating the index is more complicated than geohash. A quadtree is a tree structure . 
If a business is removed , we need to traverse from the root to the leaf node, to remove 
the business . For example, if we want to remove the business with ID = 2, we 
have to travel from the root all the way down to the leaf node, as shown in Figure 
1.19. Updating the ind ex takes 0 (log n), but the implementation is complicated if the 
data structure is accessed by a multi-thread ed program , as locking is required . Also, 
rebalancing the tree can be complicated. Rebalancing is necessary if, for example , 
a leaf node has no room for a new addition. A possible fix is to over-allocate the 
ranges. 
Step 2 - Propose High-level Design and Get Buy-in I 23 
l 


[Page 32]
~ nw ne sw se 
40m ~m 70mb ~ 
nw ne sw se 
12m~ ~~~t smb ~ 
,' , \ ...... 
,'' ,' \ ',, 
,' I ' 
,,,.,' ,' ' ......... 
,"' I \ ', 
o- O 340 ---o 
50 
buslness_ids: [2, 6, 7) 
Figure 1.19: Update quadtree 
Step 3 - Design Deep Dive 
-
Represent many 1a;;rs 
Q Internal node 
0 Leafnod e 
By now you should have a good picture of what the overall system looks like . Now let's 
dive deeper into a few areas. 
ò Scale the database 
ò Caching 
ò Region and availability zones 
ò Filter results by time or business type 
ò Final architecture diagram 
Scale the database 
We will discuss how to scale two of the most important tables: the business table and the 
geospatial index table. 
Business table 
The data for the business table may not all fit in one server, so it is a good candidate 
for sharding. The easiest approach is to shard everything by business ID. This sharding 
scheme ensures that load is evenly distributed among all the shards, and operationally it 
is easy to maintain . 
24 I Chapter 1. Proximity Service 
-


[Page 33]
Geospatial index table 
Both geohash and quadtre are wid ly us d. Due log ohash's simplicity , we use it as an 
exampl . 1here are two ways to struclur th tabl . 
ption 1: For each g ohash key, th r i a] N array of b .sin ss I s in a single row. 
TI1i, means all busine ID within a geohash are stored in one row. 
geospatlal _lndex 
geohash 
list_ of_ business _ids 
Table 1.9: list_of_business _ids is a ] SON array 
Option 2: If there are multiple businesses in the same geohash , there will be multipl e 
rows, one for each business. This means different business IDs within a geohash are 
stored in different rows. 
geospatial_index 
geohash 
business_id 
Table 1.10: business_id is a single ID 
Here are some sample rows for option 2. 
geohash business_id 
32f eac 343 
32f eac 347 
f3lcad 112 
f 3lcad 113 
Table 1.11: Sample rows of the geospatial index table 
Recommendation: we recommend option 2 because of the following reasons: 
For option 1, to update a business, we need to fetch the array of business_ids and scan 
the whole array to find the business to update . When inserting a new business , we have 
to scan the entire array to make sure there is no duplicate. We also need to lock the row 
to prevent concurrent updates . There are a lot of edge cases to handle. 
For option 2, if we have two columns with a compound key of (geohash, business_id) , 
the addition and removal of a business are very simple. There would be no need to lock 
anything. 
Scale the geospatial index 
One common mistake about scaling the geospatial index is to quickly jump to a shard ing 
scheme without considering the actual data size of the table. In our case, the full dataset 
Step 3 - Design Deep Dive I 25 


[Page 34]
fi r th g o J atiaJ ind table is not IArge (quadtr ec inc.lex only tnke s l .7 1 G memory and 
t rag requiremen t for geohas h ind<'x is similar). The whole geospa tial ind ex can easily 
fit in th orking set of a modern database server. I Iowcver, depcndi ng o n the read 
lume , a single databa e server might not have enough CPU or network bandwidth to 
handl all read r quests. If tha t is the case, it is necessary to spread the read load among 
multiple databa e servers. 
1here are two general approaches for spreading the load of a relational databa se server. 
We can add read replicas, or shard the database. 
Many engineers like to talk about sharding during interview s. However , it might not be 
a good fit for the geohash table as sharding is complicated. For instance, the sharding 
logic has to be added to the application layer. Sometimes, sharding is the only option. In 
this case, though , everything can fit in the working set of a database server , so there is 
no strong technical reason to shard the data among multiple servers . 
A better approach, in this case, is to have a series of read replicas to help with the read 
load. This method is much simpler to develop and maintain. For this reason , scaling the 
geospatial index table through replicas is recommended . 
Caching 
Before introducing a cache layer we have to ask ourselves , do we really need a cache 
layer? 
It is not immediately obvious that caching is a solid win: 
ò The workload is read-heavy, and the dataset is relatively small. The data could fit in 
the working set of any modern database server. Therefore , the queries are not I/O 
bound and they should run almost as fast as an in-memory cache. 
ò If read performance is a bottleneck, we can add database read replicas to improve the 
read throughput. 
Be mindful when discussing caching with the interviewer , as it will require careful bench¡
marking and cost analysis. If you find out that caching does fit the business requirements , 
then you can proceed with discussions about caching strategy. 
Cache key 
The most straightforward cache key choice is the location coordinates (latitude and lon¡
gitude) of the user. However, this choice has a few issues: 
ò Location coordinates returned from mobile phones are not accurate as they are just 
the best estimation (32]. Even if you don't move, the results might be slightly differ¡
ent each time you fetch coordinates on your phone . 
ò A user can move from one location to another , causing location coordinates to change 
slightly. For most applications , this change is not meaningful. 
Therefore, location coordinates are not a good cache key. Ideally, small changes in loca-
-- --- --- - ~------- ---------- --- ------
26 I Chapter 1. Proximity Service 


[Page 35]
lion should still map lo th e same cache kr y. 1he gcohash/quadlree so luti o n ment ion ed 
earlier handles this problem well beca use all businesses wit hin a grid map lo the same 
geoha h. 
Types of data to cache 
As shown in Table 1.12, there are two types of data that can be cached to improve the 
overall perfor mance of th e system: 
Key Value 
geohash List of business IDs in the grid 
business_ id Business object 
Table 1.12: Key-value pairs in cache 
List of business IDs in a grid 
Since business data is relatively stable, we precomput e the list of business IDs for a given 
geohash and store it in a key-value store such as Redis. Let's take a look at a concrete 
example of getting near by businesses with caching enabled . 
1. Get the list of business IDs for a given geohash. 
SELECT busine ss_id FROM geohash _i ndex WHERE geohash LIKE ' {: 
geohash}%' 
2. Store the result in the Redis cache if cache misses. 
public List<String > getNearbyBusinesslds(String geohash) { 
String cacheKey = hash(geohash); 
} 
List<string> listOfBusinesslds = Redis.get(cacheKey); 
if (listOfBusinessIDs == null ) { 
} 
listOfBus inesslds = Run the select SQL query above; 
Cache. set(cacheKey, listOfBusinesslds, 
11
1 d
11
); 
return listOfBusinesslds; 
When a new business is added , edited , or deleted , the database is updated and the cache 
invalidated. Since the volume of those operations is relatively small and no locking mech¡
anism is needed for the geohash approach , update operations are easy to deal with . 
According to the requirements , a user can choose the following 4 radii on the client: 
500m, lkm, 2km, and 5km. Those radii are mapped to geohash lengths of 4, 5, 5, and 
6, respectively . To quickly fetch nearby businesses for different radii, we cache data in 
Redis on all three precisions (geohash _ 4, geohash _S, and geohash _6). 
As mentioned earlier, we have 200 million businesses and each business belongs to 1 grid 
in a given precision. 111erefore the total memory required is: 
ò Storage for Redis values : bytes x 200 million x 3 precisions = rv 5GB 
ò Storage for Redis keys: negligible 
Step 3 - Design Deep Dive I 27 


[Page 36]
ò Total memory required: ,....., fiGB 
We can get away with one modern Redis server from the memo ry usage pers pective, but 
to ensure high availability and reduce cross contin ent late ncy, we depl oy th e Redis cluster 
across the globe. Given the estimated data size, we can have the s ame copy o f cache data 
deploye d globally. We call this Redis cache "Geoha sh" in our final arch itec ture diagram 
(Figure 1.21). 
Business data needed to render pages on the client 
This type of data is quite straightforw ard to cache. The key is the business _id and the 
value is the business object which contains the business name, address, image URLs, 
etc. We call this Redis cache "Business info " in our final architecture diagram (Figure 
1.21). 
Region and availability zones 
We deploy a location-based service to multiple regions and availability zones as shown 
in Figure 1.20. This has a few advantages: 
ò Makes users physically "closer" to the system . Users from the US West are connected 
to the data centers in that region, and users from Europe are connected with data 
centers in Europe . 
ò Gives us the flexibility to spread the traffic evenly across the population . Some re¡
gions such as Japan and Korea have high population densities. It might be wise 
to put them in separate regions , or even deploy location-based services in multiple 
availability zones to spread the load_ 
ò Privacy laws. Some countries may require user data to be used and stored locally. 
In this case, we could set up a region in that country and employ DNS routing to 
restrict all requests from the country to only that region . 
------- -
28 I Chapter 1. Proximity Service 
I 
I 
I 
I 


[Page 37]
Users !tom 
Eui;ope 
╖╖╖╖╖╖-. . ╖-╖-╖╖╖╖-- 140ms 115ms 
10ms òòòò òòò ╖ ò 
Users from ╖ ╖ - òòò òòòòòòò 
US west O ╖╖╖╖ ╖╖ ╖╖╖ iiQ 
00 
0 
0 0 
0 Regions 
0 
Figure 1.20: Deploy LBS "closer" to the user 
Follow-up question: filter results by time or business type 
0 
0 
0 
The interviewer might ask a follow-up question : how to return businesses that are open 
now, or only return businesses that are restaurants ? 
Candidate: When the world is divided into small grids with geohash or quadtree , the 
number of businesses returned from the search result is relatively small. Therefore, it is 
acceptable to return business IDs first, hydrate business objects, and filter them based on 
opening time or business type. This solution assumes opening time and business type 
are stored in the business table. 
Final design diagram 
Putting everything together , we come up with the following design diagram . 
---- ----- -- -- -
Step 3 - Design Deep Dive I 29 


[Page 38]
ò 
« /search/nearby 
:J 
/businesses/{:id} 
<ID @I LBS 
@ i 
« Read Read Write 
Replicate 
ò ò Business Info Geohash n """"' ... ---
Replica Primary 
-sync 
Replica Redis Cluster 
Database Cluster 
Figure 1.21: Design diagram 
Get nearby businesses 
1. You try to find restaurants within 500 meters on Yelp. The client sends the user 
location (latitude= 37. 776720, longitude= -122.416730) and radius (500m) to the 
load balancer. 
2. The load balancer forwards the request to the LBS. 
3. Based on the user location and radius info, the LBS finds the geohash length that 
matches the search . By checking Table 1.5, 500m map to geohash length = 6. 
4. LBS calculates neighboring geohashes and adds them to the list. The result looks 
like this: 
list_of _geohashes = [my_geohash, neighbor1_geohash, neighbor2_geohash, 
.. . , neighbor8_geohash]. 
5. For each geohash in list_of _geohashes, LBS calls the "Geohash" Redis server to 
fetch corresponding business IDs. Calls to fetch business IDs for each geohash can 
be made in parallel to reduce latency. 
6. Based on the list of business IDs returned, LBS fetches fully hydrated business in¡
formation from the "Business info" Redis server, then calculates distances between 
a user and businesses, ranks them , and returns the result to the client. 
30 I Chapter 1. Proximity Service 


[Page 39]
Vie , u da , add or d let a u ines 
ll l usinrs , -rclatrd Al Is arr sepiuat d from thr LRS. To vie the clet::\iled information 
about a husinrss . th husinPss ~ervice first checks if the data is stored in the "Buc;inec; 
info~ Redi. ach . lfit is. cached data will he returned to the client. If no. dattt is fetch d 
fr m th dalahase cluster and lhen stored in the Redis cache. allowing subsequent re¡
quests to g I re. ults from th cache directly . 
inc \: ha an upfront bu ines agreement that newly added /updated bu inesses will 
b effective th n xt da . cached business data is updated by a nightly job. 
Step 4 - Wrap Up 
In this chapter, we have presented the design for proximity service . The system is a typi¡
cal LB that leverages geospatial indexing. We discussed several indexin g options: 
ò Two -dimensional search 
ò Evenly divided grid 
ò Geohas h 
ò Qyadtree 
ò Google S2 
Geohash, quadtree, and S2 are widely used by different tech companies . We choose geo¡
hash as an example to show how a geospatial index works . 
In the deep dive , we discussed why caching is effective in reducing the latency , what 
should be cached and how to use cache to retrieve nearby businesses fast. We also dis¡
cussed how to scale the database with replication and sharding. 
We then looked at deploying LBS in different regions and availability zones to improve 
availability, to make users physically closer to the servers, and to comply better with 
local privacy laws . 
Congratul ations on getting this far! Now give yourself a pat on the back. Good job! 
Step 4 - Wrap Up I 31 
- , 


[Page 40]
Chapter Summary 
step 1 
step 2 
Proximity Service 
step 3 
rf'tllrn nparby bus inPsses 
functional req L add/delete/upd ate a business 
~ view a business 
low latency 
non-functional <eq L data p<ivacy 
~ 5,000 searc h qps 
L api fm semh 
api design ~ apis foe businesses 
pagination 
< 
read/ write rat io 
data model 
data schema 
high-level design diagram 
two-dimensional search 
evenly divided grid 
geohash 
algorithms 
quad tree 
google S2 
geohash vs quadtree 
< 
business table 
scale the databas e 
geospatial index table 
<
cache key 
caching 
types of data 
region and availability zone 
filter results 
final design diagram 
step 4 --wrap up 
32 I Chapter 1. Proximity Service 
--


[Page 41]
Reference Material 
[ l] Yelp. https ://\V\vw.yelp.com/. 
[2] Map tiles by Stamen Design. http ://maps.stamen.com/. 
[3] OpenStree tMap. http s://www .openstreetmap .org. 
[ 4) GDPR. https: //en.wikipedia .org/wiki/General_Data _Protection _Regulation . 
[ 5] CCP A. h ttps: // en. wikipedia.o rg/wiki/California_ Consume r _Privacy _Act. 
[ 6] Pagination in the REST APL http s://developer.atlassian.com/serve r/confluence /pa 
gination-in-the- rest-api/. 
[7] Google places APL http s://developers.google .com/maps/documentation/places/we 
b-service /search. 
[8] Yelp business endpoints . https ://www.yelp.com/developers /documentati on/v3/bus 
iness_search. 
[ 9] Regions and Zones. https ://docs.aws.amazon.com / A WSEC2/latest/UserGuide /usin 
g-reg ions-availability-zones.html . 
[10] Redis GEOHASH. https ://redis.io /commands /GEOHASH. 
[11] POSTGIS. https: //postgis.net /. 
[ 12] Cartesian tiers. http: //www.nsshutdown.com /projects /lucene /whitepaper /localluc 
ene v2.html. 
[13] R-tree. https: //en.wikipedia.org /wiki/R-tree. 
[14] Global map in a Geographic Coordinate Reference System. https ://bit.ly /3DsjAwg . 
[15] Base32. https: //en.wikipedia.org/wiki /Base32. 
[16] Geohash grid aggregation. https://bit.ly/3kK14e6. 
[ 17] Geohash . https: //www.movable-type.co .uk/scripts /geohash.html. 
[ 18] Q}ladtree. https :// en. wikipedia .org/wiki/Quadtree. 
[19] How many leaves has a quadtree. https: //stackoverflow.com/questions /35976444/h 
ow-many-leaves-has -a-quadtree. 
[20] Blue green deployment. https ://martinfowler.com /bliki /BlueGreenDeplo yment.h 
tml. 
[21] Improved Location Caching with Q}ladtrees. https: //engblog.yext.com /post /geoloc 
ation -caching. 
[22] S2. https ://s2geometry.io /. 
[ 23] Hilbert curve. https:/ / en. wikipedia.org /wiki/Hilb ert_ curve. 
Reference Material I 33 


[Page 42]
[24 J Hilbert mapping . http ://hit -player.org /extras /hilh cr l/hilb ert - mappin g.h1 ml. 
f 25 J Geo-fence. https ://en. wikipedia .org/wiki/Geo -fen ce. 
(26] Region cover. https ://s2.sidewalkJabs.com/regioncoverer /. 
(27] Bing map . https ://bit.ly /30ytSfG. 
(28] MongoDB . https ://docs.mongodb.com /manual/tutorial /build -a-2 d-index /. 
(29] GeospatiaJ Indexing : The 10 Million QPS Reclis Architecture Powering Lyft. https: 
//www.yout ube.comJwa tch ?v=cSFWlF96Sds&t=215Ss. 
[30] Geo Shape Type. https :/ /www.el astic .co/ guide /en/ elas ticsearch /refer ence/1.6/ma 
pping-geo-shape-type.html. 
(31] Geosharded Recommendations Part 1: Sharding Approach. https ://medium .com/t 
inder-engineering /geosharded-recommendations-part - 1-sharding -approach -dsds 
4e0ec77a. 
[32] Get the last known location . https: //developer .android.com /training /location /retr 
ieve-current#Challenges . 
- - --- ----
34 I Chapter 1. Proximity Service 


[Page 43]
2 Nearby Friends 
In this chapter , we design a scalable backend system for a new mobile app feature called 
"Nearby Friends ". For an opt-in user who grants permission to access their location , the 
mobile client presents a list of friends who are geographically nearby. If you are looking 
for a real-world example, please refer to this article [1] about a similar feature in the 
Facebook app. 
òòò 10 G2 ,. 82t)(i; - ) 
( Nearby Fnonds Q 
NEAR SAN FRANCISCO . CA 
r-i::\, Mallow Smith 
\!!!) 0.51YJ 
.. AUce 
~1Jmo 
Q Oliver 
Q , ... 
ò Frank 
.. ,~ 
Figure 2.1: Facebook's nearby friends 
If you read Chapter 1 Proximity Service, you may wonder why we need a separate chapter 
for designing "nearby friends" since it looks similar to proximity services. If you think 
carefully though , you will find major differences. In proximity services , the address es for 
businesses are static as their locations do not change , while in "nearby friends '', data is 
more dynamic because user locations change frequently. 
I 35 


[Page 44]
Step 1 - Understand the Problem and Establish Design Scope 
An backend system at the Facebook scale is complicated. Before starting wit h the de¡
sign. we need to a k clarification questions to narrow down th e scope. 
Candidate : How geographically close is considered to be "near by"? 
Interviewer : 5 miles. This number should be configurable. 
Candidate : Can I assume the distance is calculated as the straight -line distan ce between 
two users? In real life there could be, for example , a river in betwe en the users, resulting 
in a longer travel distance. 
Interviewer : Yes, that 's a reasonable assumption. 
Candidate : How many users does the app have? Can I assume 1 billion users and 10% 
of them use the nearby friends feature? 
Interviewer: Yes, that's a reasonable assumption. 
Candidate: Do we need to store location history? 
Interviewer : Yes, location history can be valuable for different purposes such as ma¡
chine learning. 
Candidate: Could we assume if a friend is inactive for more than 10 minutes , that friend 
will disappear from the nearby friend list? Or should we display the last known location? 
Interviewer : We can assume inactive friends will no longer be shown . 
Candidate: Do we need to worry about privacy and data laws such as GDPR or CCPA? 
Interviewer: Good question. For simplicity, don't worry about it for now. 
Functional requirements 
ò Users should be able to see nearby friends on their mobile apps . Each entry in the 
nearby friend list has a distance and a timestamp indicating when the distance was 
last updated . 
ò Nearby friend lists should be updated every few seconds. 
Non-functional requirements 
ò Low latency. It's important to receive location updates from friends without too 
much delay. 
ò Reliability. The system needs to be reliable overall, but occasional data point loss is 
acceptable . 
ò Eventual consistency. The location data store doesn 't need strong consistency . A 
few seconds delay in receiving location data in different replicas is acceptable . 
Back-of-the-envelope estimation 
Let's do a back-of-the-envelope estimation to determine the potential scale and chal¡
lenges our solution will need to address. Some constraints and assumptions are listed 
below : 
---------------36 I Chapter 2. Nearby Friends --- --- -- ---
--


[Page 45]
ò Nearby friends are defined as friends whose locations are within a 5-mile radius . 
ò The location refresh interval is 30 seconds. The reason for this is that human walking 
speed i slow (average 3 f',.J 4 miles per hour). The distan ce trav eled in 30 seconds 
does not make a significant difference on the "nearby friends " feature. 
ò On average, 100 million users use the "nearby friends " featu re every day. 
ò Assume the number of concu rrent users is 103 of DAU (Daily Active Users), so the 
number of concurrent users is 10 million . 
ò On average, a user has 400 friends. Assume all of them use the "nearby friends" 
feature . 
ò The app displays 20 nearby friends per page and may load more nearby friends upon 
request. 
Calculate QPS 
ò 100 million DAU 
ò Concurrent users: 103 x 100 million = 10 million 
ò Users report their locations every 30 seconds . 
. 10 million ò Location update QPS = = rv334,000 30 
Step 2 - Propose High-level Design and Get Buy-in 
In this section, we will discuss the following: 
ò High-level design 
ò API design 
ò Data model 
In other chapters , we usually discuss API design and data model before the high-level de¡
sign. However, for this problem , the communication protocol between client and server 
might not be a straightforward HTTP protocol, as we need to push location data to all 
friends. Without understanding the high-level design, it's difficult to know what the 
APis look like. Therefore , we discuss the high-level design first. 
High-level design 
At a high level, this problem calls for a design with efficient message passing . Concep¡
tually, a user would like to receive location updates from every active friend nearby. It 
could in theory be done purely peer -to-peer , that is, a user could maintain a persistent 
connection to every other active friend in the vicinity (Figure 2.2). 
Step 2 - Propose High-level Design and Get Buy-in I 37 


[Page 46]
Figure 2.2: Peer-to -peer 
This solution is not practical for a mobile device with sometimes flaky connections and 
a tight power consumption budget, but the idea sheds some light on the general design 
direction. 
A more practical design would have a shared backend and look like this: 
Friend A 
...___-@Friend 8 
User 
@FriendC 
Figure 2.3: Shared backend 
What are the responsibilities of the backend in Figure 2.3? 
ò Receive location updates from all active users. 
ò For each location update, find all the active friends who should receive it and forward 
it to those users' devices. 
ò If the distance between two users is over a certain threshold , do not forward it to the 
recipient 's device. 
This sounds pretty simple. What is the issue? Well, to do this at scale is not easy. We 
have 10 million active users. With each user updating the location information every 30 
seconds, there are 334K updates per second. If on average each user has 400 friends, and 
we further assume that roughly 103 of those friends are online and nearby , every second 
the backend forwards 334K x 400 x 103 = 14 million location updates per second . That 
is a lot of updates to forward. 
38 I Chapter 2. Nearby Friends 


[Page 47]
Proposed design 
We will first come up wi lh a high-level design for the backend al a lower scale. Later in 
the de p dive section, we will optimi ze lhe design for s ale. 
Figme 2.4 hows the basic design that should satisfy the functional requirements. Let's 
go over each component in the design. 
Redis Pub/Sub 
Load balancer 
Web Socket 
Servers 
Mobile Users 
A 
WebSocket h ttp 
01'/S) 
Load Balancer 
Bi-directional 
location info 
API 
Servers 
~---.--
User management 
Friendship management 
Auth, etc 
Locat ion 
Cache 
Location 
History 
Database 
Figme 2.4: High-level design 
User 
Database 
User profile, 
Friendship 
The load balancer sits in front of the RESTful API servers and the stateful, bi-directional 
WebSocket servers . It distribut es traffic across those servers to spread out load 
evenly. 
RESTful API servers 
This is a cluster of stateless HTTP servers that handles the typical request /respons e traf¡
fic. The API request flow is highlighted in Figure 2.5. This API layer handles auxiliary 
tasks like adding/removing friends , updating user profiles, etc. These are v ery common 
and we will not go into more detail. 
Step 2 - Propose High -level Design and Get Buy-in I 39 


[Page 48]
Redis Pub/Sub 
WebSocket servers 
Mobile Users 
A WebSocket hit 
(WS) p 
Load Balancer 
WebSocket Bi-directional 
Servers location Info 
API 
Servers 
~--~--
User management 
Friend ship management 
Auth , etc 
Cache 
Location 
Cache 
Location 
History 
Database 
Figure 2.5: RESTful API request flow 
User 
Database 
User profi le, 
Friendship 
Th.is is a cluster of stateful servers that handles the near real -time update of friends' 
locations. Each client maintains one persistent WebSocket connection to one of these 
servers . When there is a location update from a friend who is within the search radius, 
the update is sent on this connection to the client. 
Another major responsibility of the WebSocket servers is to handle client initializati on 
for the "nearby friends" feature. It seeds the mobile client with the locations of all nearby 
online friends. We will discuss how this is done in more detail later . 
Note "WebSocket connection" and "WebSocket connection handler " are interchangeabl e 
in this chapter. 
Redis location cache 
Redis is used to store the most recent location data for each active user. There is a Time 
to Live (TIL) set on each entry in the cache. When the TTI expires , the user is no longer 
active and the location data is expunged from the cache. Every update refreshes the TTL. 
Other KV stores that support TTL could also be used. 
------ ---- ---- -
40 I Chapter 2. Nearby Friends 


[Page 49]
User database 
"fo e user database stores user data and user friendship dala. Either a relational database 
or a NoSQL database can b e used for this. 
Locatio n history database 
Thi d atabase stores users╖ historic al location data. It is not directly related to the "near by 
friends" feature. 
Redis Pub/ Sub server 
Redis Pub/Sub [2] is a very lightw eight message bus. Channels in Redis Pub/Sub are 
very cheap to create. A modern Redis server with GBs of memory could hold millions of 
channels (also called topics). Figure 2.6 shows how Redis Pub/Sub works. 
Users publish location update 
1------- ------------ ----, 
I 
I 
I 
I 
Redis Pub/Sub 
--------------------------, I I 
I I 
I I 
I 
I 
I 
Publisher 1 1---!--- --r' +1 User 1 's channel 
Publisher 2 >--~-~-╖ User 2's channel 
I 
I I 
I I 
------------------------╖ 
I 
~- - - - - --------------------
Figure 2.6: Redis Pub/Sub 
Friends 
Subscriber 1 
Subscriber2 
Subscriber 3 
I 
I 
------- --------------- ----╖ 
In this design, location updates received via the WebSocket server are published to the 
user's own channel in the Redis Pub/Sub server. A dedicated WebSocket connection han¡
dler for each active friend subscribes to the channel. When there is a location update , 
the WebSocket handler function gets invoked , and for each active friend , the function 
recomputes the distance. If the new distance is within the search radius, the new loca¡
tion and timestamp are sent via the WebSocket connection to the friend's client. Other 
messag e buses with lightweight channels could also be used. 
Now that we understand what each component does, let's examine what happens when 
a user 's location changes from the system's perspective. 
Periodic location update 
The mobile client sends periodic location updat es over the persistent WebSocket connec¡
tion. The flow is shown in Figure 2.7. 
Step 2 - Propose High-level Design and Get Buy-in I 41 


[Page 50]
MA 
f.\WebSocket http 
\.!../ (WS) 
Load Balancer 
2 
WebSocket Bi-directional API User management 
----...,(j) Servers location Info Servers Friendship management 
'----~-~ Auth , etc 
Redis Pub/Sub Location 
Cache 
Location 
History 
Database 
Figure 2.7: Periodic location update 
User 
Database 
1. The mobile client sends a location update to the load balancer. 
User profile, 
Friendship 
2. The load balancer forwards the location update to the persistent connection on the 
WebSocket server for that client. 
3. The WebSocket server saves the location data to the location history database . 
4. The WebSocket server updates the new location in the location cache. The update 
refreshes the TTL. The WebSocket server also saves the new locat ion in a variable in 
the user's WebSocket connection handler for subsequent distance calculations . 
5. The WebSocket server publishes the new location to the user's channel in the Red.is 
Pub/Sub server. Steps 3 to 5 can be executed in parallel. 
6. When Redis Pub/Sub receives a location update on a channel , it broadcasts the update 
to all the subscribers (WebSocket connection handlers) . In this case , the subscribers 
are all the online friends of the user sending the update. For each subscriber (i.e., for 
each of the user's friends), its WebSocket connection handler would receiv e the user 
location update. 
7. On receiving the message, the WebSocket server , on which the connection handler 
lives, computes the distance between the user sending the new location (the location 
42 I Chapter 2. Nearby Friends 


[Page 51]
data 1s in th e mec;MA ) ~nd the subsc riber (the location d~ta is stored in a v::1riable 
w1lh the WcbSo kct connectio n handler for the subscri ber). 
8. This st<-p is not drawn on th di.agram. If the distance doeli not excee d t he searc h 
radiu . the new location and the last updat ed timestamp are sent to th e s ubscriber's 
di("nt. Oth erwi , the update is dropped . 
ince und erstanding this flow is extremely important , let's exami ne it agai n with a 
concrete example , as shown in Figure 2.8. Before we start , let's make a few ass ump ¡
tions. 
ò User 1 's friends : ser 2, User 3, and User 4. 
ò User 5 's friends: User 4 and User 6. 
UQ 1 U~serS 
G) User 1 's location 
~ -- -- -- --- -- --- - --- - -- - ------ ---------------------------- ------------------: , I 
WebSocket : User 1 's WS User S's WS 
I 
I 
Servers connection connection 
l ___________________________ -----------------------------i __________________ : 
Red is 
Pub/Sub 
@ Publish Publish 
r---------------------------- ---------------------------- ------------------, ' ' , 
I 
' , 
I 
I , User S's channel i 
' I I 
'----------------------- ---- ----- -------------------- ----- ---------------' 
@ Subscribe Subscribe Subscribe Subscribe Subscribe 
r------------- -------------- ------------- ------- ------------- -----------. 0 I 
I I 
WebSocket : User 2's WS User 3's WS User 4's WS User 6's WS ' , 
Servers : connection connection connection connection 
' , ╖-------- ------------------- -------------------------------------- --- ----- ~ 
⌐ Friends' location update 
6 
User2 User3 User 4 User6 
Figure 2.8: Send location update to friends 
1. When Us r 1' s location chan ges, their location updat e is sent to the WebSocket server 
whlch holds User 1 's connection. 
2. The locatio n is published to User l 's channel in Redis Pub/Sub server. 
3. Redi Pub/Sub server broadcasts the location updat e to all subscribers. In this case, 
Step 2 ò Propose High-level Design and Get Buy-in I 43 


[Page 52]
-
. uh cribrr at W bSocket connection handlers (User l 's friends). 
4. If the di tnnc betwee n the user sending the location (User J) and lhe subsrrihrr 
(U er 2) do sn'l exceed the search radius, the new location is sent to the client (Oser 
2). 
111is computation is repeated for every subscriber to the channel. Since there are 400 
friends on average, and we assume that 103 of those friends are online and nearby, there 
are about 40 location updates to forward for each user's location updat e. 
API design 
Now that we have created a high-level design, let's Hst APis needed. 
WebSocket : Users send and receive location updates through the WebSocket protocol 
At the minimum , we need the following APis. 
t. Periodic location update 
Request: Client sends latitude , longitude, and timestamp. 
Response: Nothing . 
2. Client receives location updates 
Data sent: Friend location data and timestamp. 
3. WebSocket initialization 
Request: Client sends latitude , longitude, and timestamp. 
Response: Client receives friends ' location data. 
4. Subscribe to a new friend 
Request: WebSocket server sends friend ID. 
Response: Friend's latest latitude, longitude, and timestamp. 
5. Unsubscribe a friend 
Request: WebSocket server sends friend ID. 
Response. Nothing. 
HTTP requests: the API servers handle tasks like adding/removing friends, updating 
user profiles, etc. These are very common and we will not go into detail here. 
Data model 
Another important element to discuss is the data model. We already talked about the 
User DB in the high-level design, so let's focus on the location cache and location history 
database. 
Location cache 
The location cache stores the latest locations of all active users who have had the nearby 
friends feature turned on. We use Red.is for this cache. The key/value of the cache is 
shown in Table 2.1. 
44 I Chapter 2. Nearby Friends 
j 


[Page 53]
key ___ value-- - ---- ---~] 
user _id - {latitude , longitude , limestamill 
Table 2.1: Location cache 
Why don't we use a database to store location data? 
Th "nearb friends " feature only cares about the current location of a user. Therefore, 
we only n eed to store one location per user. Red.is is an excellent choice because it pro ¡
vide super-fast read and writ e operations . It supports TTL, which we use to auto-purge 
u ers from the cache who are no longer active. The current locations do not need to be 
durabl stored . If the Redis instance goes down, we could replace it with an empty new 
instance and let the cache be filled as new location updates stream in. The active users 
could miss location updates from friends for an update cycle or two while the new cache 
warms . It is an accepta ble tradeoff. In the deep dive section , we will discuss ways to 
lessen the impact on users when the cache gets replaced. 
Location history database 
The location history database stores users ' historical location data and the schema looks 
like this : 
I user_id latitude longitude time stamp 
We need a database that handles the heavy-write workload well and can be horizontally 
scaled. Cassandra is a good candidate . We could also use a relational database. However, 
with a relational database , the historical data would not fit in a single instance so we need 
to shard that data. The most basic approach is to shard by user ID. This sharding scheme 
ensures that load is evenly distributed among all the shards, and operationally , it is easy 
to maintain. 
Step 3 - Design Deep Dive 
The high -level design we created in the previous section works in most cases, but it will 
likely break at our scale. In this section, we work together to uncover the bottlenecks 
as we increase the scale, and along the way work on solutions to eliminate those bottle¡
necks. 
How well does each component scale? 
API servers 
The methods to scale the RESTful API tiers are well understood . These are stateless 
servers, and there are many ways to auto-scale the clusters based on CPU usage, load, or 
1/0 . We will not go into detail here. 
WebSocket servers 
For the WebSocket cluster, it is not difficult to auto-scale based on usage. However, the 
WebSocket s ervers are stateful , so care must be taken when removing existing nodes . 
Before a node can be removed, all existing connections should be allowed to drain. To 
Step 3 - Design Deep Dive I 45 


[Page 54]
achieve tllRl , we can mark a node as "draining" at the load bal a ncer so th 3t. n? new W<'h 
ockel conn ections will be routed to the draining serv er. Once all th e cXIstmg connet 
Lions a re clos ed (or aft er a reasonably long wait) , the server is then remove d. 
Releasing a new version of the application software on a WebSocket server requires the 
same level of care . 
It is worth notin g that effective auto-scaling of stateful servers is the job of a good load 
bahm cer. Most cloud load balancers handl e this job very well . 
Client initialization 
The mobile client on startup establishes a persistent WebSo cket conne ction with one of 
the WebSocket server instances . Each connection is long-running. Most modern lan. 
guages are capable of maintaining many long-running connections with a reasonably 
small memory footprint. 
When a WebSocket connection is initialized , the client sends the initial locati on of the 
user , and the server performs the following tasks in the WebSocket connection han. 
dler . 
1. It updates the user 's location in the location cache. 
2. It saves the location in a variable of the connection handler for subsequent calcula¡
tions . 
3. It loads all the user 's friends from the user database. 
4. It makes a batched request to the location cache to fetch the locatio ns for all the 
friends . Note that because we set a T11. on each entry in the locatio n cache to match 1 
our inactivity timeout period , if a friend is inactive then their locatio n will not be in 
the location cache . 
5. For each location returned by the cache, the server computes the distance between 
the user and the friend at that location . lf the distance is within the search radius, 
the friend 's profile , location , and last upd ated timestarnp are returned over the Web¡
Socket connection to the client. 
6. For each friend , the server subscribes to the friend's channel in the Redis Pub/Sub 
server . We will explain our use of Redis Pub/ ub shortly. Since creating a new chan╖ 
nel is cheap, the user subscribes to all active and inactive friends. The inactive friends 
will take up a small amount of memory on the Redis Pub/Sub serve r, but they will 
not consume any CPU or I/O (since they do not publish updates) until they come 
online . 
7. It sends the user 's current locatio n to the user's channel in the Redis Pub /Sub server. 
User database 
The user database holds two distin ct sets of data : user profiles (user ID, username , pro¡
file URL, etc.) and friendships . These datasets at our design scale will likely not fit in a 
single relational database instanc e. The good news is that the data is horizontall y seal╖ 
46 l Chapter 2.. Nearby Friends 


[Page 55]
able by sharding based on user ID. Relation"] databas e shardin g is a very common tech¡
nique . 
As a side note . at the scale we are designing for, the user and friendship datasets will likely 
be managed by a dedicated team and be available via an internal APL Jn this scenario , 
the Web ocket servers will use the int ernal API instead of queryi ng the database directly 
to fetch user and friends hip -related data. Whether accessing via API or direct database 
queries, it does not make much difference in terms of functionality or performan ce. 
Location cache 
\Ve choose Redis to cache the most recent locations of all the active users. As mentioned 
earlier, we also set a TTL on each key. The TTL is renewed upon every location upd ate. 
1his puts a cap on the maximum amount of memory used. With 10 million active users 
at peak, and with each location talting no more than 100 bytes, a single modern Redis 
server with many GBs of memory should be able to easily hold the location information 
for all users . 
However, with 10 million active users roughly updating every 30 seconds , the Redis 
server will have to handle 334K updates per second. That is likely a little too high, even 
for a modern high-end server . Luckily, this cache data is easy to shard. The location data 
for each user is independent , and we can evenly spread the load among several Redis 
servers by sharding the location data based on user ID. 
To improve availability , we could replicate the location data on each shard to a standby 
node. If the primary node goes down , the standby could be quickly promoted to minimize 
downtime. 
Redis Pub/Sub server 
The Pub/Sub server is used as a routing layer to direct messages (location updates) from 
one user to all the online friends . As mentioned earlier, we choose Redis Pub/Sub because 
it is very lightweight to create new channels . A new channel is created when someone 
subscribes to it. If a message is published to a channel that has no subscribers , the mes ¡
sage is dropped, placing very little load on the server . When a channel is created , Red.is 
uses a small amount of memory to maintain a hash table and a linked list (3) to track the 
subscribers. If there is no update on a channel when a user is offiine, no CPU cycles are 
used after a channel is created . We take advantage of this in our design in the following 
ways: 
1. We assign a unique channel to every user who uses the "nearby friends" feature. A 
user would , upon app initialization , subscribe to each friend's channel , whether the 
friend is online or not. 1his simplifies the design since the backend does not need to 
handle subscribing to a friend's channel when the friend becomes active, or handlin g 
unsubscribing when the friend becomes inactive . 
2. The tradeoff is that the design would use more memory. AB we will see later, mem¡
ory use is unlikel y to be the bottleneck. Trading higher memory use for a simpler 
architecture is worth it in this case. 
Step 3 - Design Deep Dive I 4 7 


[Page 56]
How many Redis Pub/Sub servers do we need? 
Le do ome math on memory and CPU usage. 
Memory usage 
Assuming a channel is allocated for each user who uses the nearby friends feature, 'N~ 
need 100 million channels (1 billion x 103 ). Assuming that on average a user has 11)(1 
active friends using this feature (this includes friends who are nearby , o r n ot), and 11 
takes about 20 bytes of pointers in the internal hash table and linked list to track e:ich 
subscriber , it will need about 200GB (100 million x 20 bytes x 100 friends I 109 == 200GB) 
to hold all the channels. For a modern server with lOOGB of memory , we will need about 
2 Redis Pub/Sub servers to hold all the channels. 
CPU usage 
As previously calculated, the Pub/Sub server pushes about 14 million updates per second I 
to subscribers. Even though it is not easy to estimate with any accura cy how many 1 
messages a modern Red.is server could push a second without actual benchmarking, it 
is safe to assume that a single Red.is server will not be able to handle that load. Let's 
pick a conservative number and assume that a modern server with a gigabit network 
could handle about 100,000 subscriber pushes per second. Given how small our location 
update messages are, this number is likely to be conservative. Using this conservative 
estimate, we will need to distribute the load among 14 million / 100 ,000 = 140 Redis 
servers. Again , this number is likely too conservative , and the actual number of servers 
could be much lower. 
From the math, we conclude that : 
ò The bottleneck of Red.is Pub/Sub server is the CPU usage , not the memory usage. 
ò To support our scale, we need a distributed Red.is Pub/Sub cluster. 
Distributed Redis Pub/Sub server cluster 
How do we distribute the channels to hundreds of Redis servers? The good news is that 
the channels are independent of each other. This makes it relatively easy to spread the 
channels among multiple Pub/Sub servers by sharding , based on the publisher 's user 
ID. Practically speaking though , with hundreds of Pub /Sub servers , we should go into a 
bit more detail on how this is done so that operationally it is somewhat manageable, as 
servers inevitably go down from time to time. 
Here, we introduce a service discovery component to our design. There are many service 
discovery packages available , with etcd [ 4] and ZooKeeper [5] among the most popular 
ones. Our need for the service discovery component is very basic. We need these two 
features: 
1. The ability to keep a list of servers in the service discovery component, and a simple 
UI or API to update it. Fundamentally, service discovery is a small key-value store 
for holding configuration data . Using Figure 2.9 as an example. the key and value for 
48 I Chapter 2. Nearby Friends 


[Page 57]
the ha h nng could look Hke thi s: . '-
1'ey: /config /pub_sub_ring 
\"al . [" 1" "p 2" "p 3
11 
"p 4"] ue. p_ , _ , - , -
2. The ability for clients (in this case, the WebSocket servers) to subscribe to any updates 
to the "\ alue- (Redis Pub/Sub servers). 
L nder the '"Key"' mentioned in point 1, we store a hash ring of all the active Redis Pub/Sub 
erYers in the service discovery component (See the consistent hashing chapter in Volume 
1 of the ystem Design Interview book or [ 6] on details of a hash ring). The hash ring 
i used by the publishers and subscribers of the Red is Pub/Sub servers to determine the 
Pub ub erver to talk to for each channel. For example, channel 2 lives in Redis Pub/Sub 
erver 1 in Figure 2.9. 
Redis Pub/Sub server 1 is responsible 
for hash values in this range 
hash{channel_name2) 
I p_x: Redis Pub/Su b server X I 
Figure 2. 9: Consistent hashing 
Figure 2.10 shows what happens when a WebSocket server publishes a location update 
to a user 's channel. 
Step 3 - Design Deep Dive I 49 


[Page 58]
( _____ _--..::.....,() 
hash(chann el_name2) 
Figure out which Redis 
G) Pub/Sub server to publish 
location to 
Channel 2 
Publish 
,_+-----1 2 l .ocatlon ----1 
WebSocket 
Servers update 
(_~() 
Redis Pub/Sub 
Figure 2.10: Figure out the correct Redis Pub/Sub server 
1. The WebSocket server consults the hash ring to determine the Redis Pub/Sub server 
to write to. The source of truth is stored in service discovery, but for efficiency, a 
copy of the hash ring could be cached on each WebSocket server. The WebSocket 
server subscribes to any updates on the hash ring to keep its local in-memory copy 
up to date . 
2. WebSocket server publishes the location update to the user's channel on that Redis 
Pub /Sub server. 
Subscribing to a channel for location updates uses the same mechanism . 
Scaling considerations for Redis Pub/Sub servers 
How should we scale the Redis Pub/Sub server cluster? Should we scale it up and down 
daily, based on traffic patterns? This is a very common practice for stateless servers 
because it is low risk and saves costs. To answer these questions, let's examine some of 
the properties of the Redis Pub/Sub server cluster. 
50 I Chapter 2. Nearby Friends 
'. 


[Page 59]
I. The messages sent o n a Pub /Sub chann el are not persis ted in memory or 0 11 di k. 
They are sent to all subscribers of the channel and removed imm ediate ly after . If 
there are no subscribers , the messages are just dropped . ln this sense , the da ta goin g 
through Lhe Pub /Sub channel is stateless . 
2. However. there are indeed states store d in the Pub/Sub serve rs for the c hannels. 
pecifically, the subscriber list for each chann el is a key piece of the states trac ked by 
the Pub/Sub servers. If a channel is move d, which could happen when the channel's 
Pub/Sub server is rep laced, or if a new server is added or an old server r emoved on 
the hash ring , then every subscr iber to the moved chann el must know about it, so 
they could unsubscribe from the channel on the old server and resubs crib e to the 
replacement channel on the new server. In this sens e, a Pub/Sub server is s tateful , 
and coordination with all subscrib ers to the server must be orchestrated to minimi ze 
service interruptions. 
For these reasons, we should treat the Redis Pub/Sub cluster more like a stateful clus¡
ter, similar to how we would handle a storage cluster . With stateful clusters , scaling 
up or down has some oper ational overhead and risks , so it should be done with care ¡
ful planning. The clus ter is normally over-provisioned to make sure it can handle daily 
peak traffic with som e comfortable headroom to avoid unnecessary resizing of the clus¡
ter. 
Whe n we inevi tabl y have to scale, be mindful of these potential issues : 
ò Wh en w e resize a cluster, many channels will be moved to different servers on the 
hash ring. When the service discovery component notifies all the WebSocket servers 
of the hash ring update , there will be a ton of resubscription requests . 
ò Durin g these mass resub scription events, some location updates might be missed by 
the c lients. Although occasional misses are acceptable for our design, we should 
minimi ze the occurrences. 
ò Because of the potential interruptions , resizing should be done when usage is at its 
lowest in the day. 
How is resizing actually done? It is quite simple . Follow these steps : 
ò Determin e the new ring size, and if scaling up, provision enough new servers. 
ò Update the keys of the hash ring with the new content. 
ò Monitor your dashboard. There should be some spike in CPU usage in the WebSocket 
cluster . 
Using the hash ring from Figure 2.9 above , if we were to add 2 new nodes, say, p_5, and 
p_6, the hash ring would be updat ed like this: 
Old: ["p_1", "p_2", "p_3", "p_4"] 
New: ["p _ 1 ", "p_2", "p_3
11
, "p_4", "p_5", "p_6"] 
Step 3 - Design Deep Dive I 51 


[Page 60]
I con id rations for Redis Pub/Sub servers 
The rntional ri k of rep lacing an e isling Red is Pub/Sub server is mu ch. much lo~er 
fl doe not u a large number of channels to be moved. Onl y the channels on th . e 
n r being replared will need to be handle d. This is good because server s inevitably go 
down and nf'~ to be replaced regularly. 
\\Then a Pub ' ub server goes down, the monitoring software should alert the on-call 
operator. Precisely how the monitoring software monit ors the h ealt h of a Pub /Sub server 
is beyond the scope of this chapter, so it is not covere d. The o n-call operator updates 
the hash ring key in service discovery to replace the dead nod e with a fresh standby 
n ode. The WebSocket servers are notified about the upd ate and each one then notifies 
its connectio n handlers to re-subscribe to the channels on the new Pub /Sub server. Each 
WebSocke t handler keeps a list of all channels it has subscr ibed to, and upon receiving J 
the notification from the server, it checks each channel against the hash ring to determine I 
if a channel needs to be re-subscribed on a new server . 
Usin g the hash ring from Figure 2.9 above, if p_ 1 went down , and we replace it with 
p1 _new, the hash ring would be updated like so: 
Old: [ np_ 111 , 11 p_211 , 11p_311 , "p_ 411 ] 
New: ["p_1_new", 11 p_211 , 11 p_3
11
, 
11
p_4
11
] 
~-------- - --------------- - -- - -- - - - - - -- - ---, . . 
: I 
. . . . . . . . 
. . . . . . 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
- ----- - ------- ---------------------------╖ 
r--------------------------------------------... 
I 
p_1_new : 
' I 
. . 
I 
I 
I 
I 
I 
I 
I 
I 
. 
I 
------------ -----------------------------------╖ 
Figure 2.11: Replace Pub/Sub serverver 
Adding/removing friends 
What should the client do when the user adds or removes a friend ? When a new friend ' 
is add ed, the client's WebSocket connection handler on the server needs to be notified, 
so it can subscribe to the new friend's Pub/Sub channel. 
Since the "nearby friends" feature is within the ecosystem of a larger app , we can assume 
that the "nearby friends" feature could register a callback on the mobile client whenever 
a new frie nd is added. The callback, upon invocation , sends a mess age to the WebSocket 
server t o subscribe to the new friend's Pub/Sub channel. The WebSock et server also 
----- --- - -- - -
52 I Chapter 2. Nearby Friends 


[Page 61]
retur ns a message containing the new friend 's latest location and timestamp, if Lhey are 
active. 
Likewise, the client could register a callback in the application whenever a friend is re¡
moved. The callback would send a message to the WebSocket server to unsubscribe from 
the friend's Pub/Sub channel. 
This subscribe/unsubscribe callback could also be used whenever a friend has opted in 
or out of the location update. 
Users with many friends 
It is worth discussing whet her a user with many friends could cause performance 
hotspots in our design. We assume here that there is a hard cap on the number 
of friends . (Facebook has a cap of 5,000 friends , for example). Friendships are bi¡
directional . We are not talking about a follower model in which a celebrity could hav e 
millions of followers. 
In a scenario with thousands of friends , the Pub/Sub subscribers will be scattered amon g 
the many WebSocket servers in the cluster. The update load would be spread among 
them and it's unlikely to cause any hotspots. 
The user would place a bit more load on the Pub/Sub server where their channel lives. 
Since there are over 100 Pub/Sub servers , these "whale" users would be spread out 
among the Pub/Sub servers and the incremental load should not overwhelm any single 
one. 
Nearby random person 
You might call this section an extra credit, as it's not in the initial functional requirements. 
What if the interviewer wants to update the design to show random people who opted-in 
to location-sharing? 
One way to do this while leveraging our design is to add a pool of Pub/Sub channels 
by geohash. (See Chapter 1 Proximity Service for details on geohash) . As shown in 
Figure 2.12, an area is divided into four geohash grids and a channel is create d for each 
grid. 
Step 3 - Design Deep Dive I 53 


[Page 62]
Geohaah 
9q8zn6 
() --~ 
9q8211<1 
> () Geohaòtj 9q8znl 
() 
GeohaOh J 9q8zn3 
Redis Pub/Sub 
Figure 2.12: Redis Pub/Sub channels 
Anyone within the grid subscribes to the same channel. Let's take grid 9q8znd for exam¡
ple as shown in Figure 2.13. 
------------- ------- ---' ' 
~--L I.\ Location 
~update 
' ' ' ----------- ------------WebSocket connections 
Geohash: 
9q8zn6 
Geo hash: 
9q8znd 
( 
Geohash: ( ) 
'-----9-qSznf ~ 
( 
Geohash: ( ) 
~9-q8zn3~ 
Aedls Pub/Sub 
Users in geohash: 9q8nzd 
r- - -- - - - - - - ---- - ----- , 
User 1 
User3 
' 
' ' 
' ' ' 
WebSocket connections 
Figure 2.13: Publish location update to random nearby person 
1. Here , when user 2 updates their location , the WebSocket connection handler com╖ 
putes the user's geohash ID and sends the location to the channel for that geohash. 
2. Anyone nearby who subscribes to the channel (exclude the sender) will receive a 
location update message. 
To handle people who are close to the border of a geohash grid, every client could sub╖ 
scribe to the geohash the user is in and the eight surrounding geohash grids. An example 
with all 9 geohash grids highlighted is shown in Figure 2.14. 
54 I Chapter 2. Nearby Friends 


[Page 63]
\ 
\ 
I 
~Sznf 
Figure 2.14: Nine geohash grids 
Alternative to Redis Pub/Sub 
Is there any good alternative to using Red.is Pub/Sub as the routing layer? The answer 
is a resounding yes. Erlang [7] is a great solution for this particular problem . We would 
argue that Erlang is a better solution than the Redis Pub/Sub proposed above. However , 
Erlang is quite a niche, and hiring good Erlang programmers is hard . But if your team 
has Erlang expertise , this is a great option. 
So, why Erlang? Erlang is a general programming language and runtime environment 
built for highly distributed and concurrent applications. When we say Erlang here, we 
specifically talk about the Erlang ecosystem itself. This includes the language compo¡
nent (Erlang or Elixir [8]) and the runtime environment and libraries (the Erlang virtual 
machine called BEAM [9] and the Erlang runtime libraries called OTP [10]). 
The power of Erlang lies in its lightweight processes. An Erlang process is an entity 
runnin g on the BEAM VM. It is several orders of magnitude cheaper to create than a Linux 
process . A minimal Erlang process takes about 300 bytes , and we can have millions of 
these processes on a single modern server. If there is no work to do in an Erlang process, 
it just sits there without using any CPU cycles at all. In other words , it is extremely 
cheap to model each of the 10 million active users in our design as an individual Erlang 
process . 
Erlang is also very easy to distribut e amon g many Erlang servers . The operational over¡
head is very low, and ther e are great tools to support d ebugging live production issues, 
safely. The deployment tools are also very stron g. 
How would we use Erlang in our design ? We would implement the WebSocket service in 
Erlang, and also replace the entir e cluster of Red.is Pub/Sub with a distributed Erlang ap¡
plication. In this application, each user is modeled as an Erlang pro cess. The user process 
would receive updates from the WebSocket server when a user's location is updated by 
the client The user process also subscribes to updates from the Erlang processes of the 
Step 3 - Design Deep Dive I 55 


[Page 64]
-
user 's friends . Subscription is native in Erlang/OTP and it's easy to build . This forrn 
mesh of connectio ns that would efficiently rou te location upd ates from one user to rnaR a 
fri d ny en s. 
Step 4 - Wrap Up 
In this chapter , we presented a design that supports a nearby friends feature. Conceptu. 
ally, we want to design a system that can efficiently pass location upd ates from one user 
to their friends. 
Some of the core components include: 
ò WebSocket: real-time communication between clients and the server . 
ò Redis: fast read and write of location data. 
ò Redis Pub/Sub: routing layer to direct location updates from one user to all the online 
friends. 
We first came up with a high-level design at a lower scale and then discussed challenges 
that arise as the scale increases. We explored how to scale the following: 
ò RESTful API servers 
ò WebSocketservers 
ò Data layer 
ò Reclis Pub/Sub servers 
ò Alternative to Redis Pub/Sub 
Finally, we discussed potential bottlenecks when a user has many friends and we pro¡
posed a design for the "nearby random person " feature . 
Congratulations on getting this far! Now give yourself a pat on the back. Good job! 
--------------- -- --
56 I Chapter 2 Nearby Friends 


[Page 65]
Chapter Summary 
step 1 
step 2 
Nearb y Friends 
step 3 
< 
view nearby friends 
funct ional req 
update nearby friend list 
non-fun ctional req - - low latency 
L 5-mile radius 
estimation ~ location refresh intervaL 30s 
locate update qps: 334k 
restful api servers 
websocket servers 
high-level design diagram redis location cache 
location history database 
periodic location update 
redis pub/sub server 
api design 
< 
location cache 
data model 
location history database 
api servers 
websocket servers 
user database 
scale each component 
location cache 
addin g/removing friends redis pub/sub server 
users with many friends altern ative to redis pub/sub 
nearb y random person 
step 4 --wrap up 
-------
Chapter Summary I 57 


[Page 66]
Reference Material 
[ 1 J Fare book Launches "Nearby Frirnds ". hl.lps:// trc hcnm ch.com/2014/01/ 17 /fo<'f'ho 
ok-nearb -friends /. 
[21 R dis Pub/Sub. hllp s://redis.io/topics/ pubsub. 
(3) Redis Pub/Sub under the hood . https ://making.pu sher.com/rcdi s- pubsub-under-t 
he-hood /. 
(4) etcd. hlt'ps://etcd.io /. 
[ 5] Zoo Keeper. https: //zookeeper.apache.org /. 
[ 6] Consistent hashingones . http s://www .toptal .com/big- data/consistent -hashing. 
[7] Erlang. https :/ /www.erlang.org/. 
(8] Elixir. https ://elixir-lang .org/. 
(9] A brief introduction to BEAM. https: //www.erlang .org/blog/a- brief-beam -primer/. 
[ 10] OTP. https ://www.erlang.org / doc/ design_princip les/ des _princ .html. 
58 I Chapter 2. Nearby Friends 


[Page 67]
'f╖ ~ 
3 Google Maps 
In this chapt er, we design a simple version of Google Maps. Before we proceed t o the 
syste m design, let's learn a bit about Google Maps. Google started Project Google Maps 
in 2005 and developed a web mapping service . It provides many service s such as satellite 
imagery, street maps , real-time traffic conditions, and route planning [1]. 
Google Maps helps users find directions and navigate to their destination. As of March 
2021, Google Maps had one billion daily active users, 993 coverage of the world , and 
25 million updates daily of accurate and real-time location information [2]. Given the 
enormous complexity of Google Maps, it is important to nail down which features our 
version of it supports. 
Step 1 - Understand the Problem and Establish Design Scope 
The interaction between the interviewer and the candidate could look like this: 
Candidate: How many daily active users are we expecting? 
Interviewer: 1 billion DAU. 
Candidate: Which features should we focus on? Direction, navigation, and estimated 
time of arrival (ETA)? 
Interviewer: Let's focus on location update, navigation , ETA, and map rendering. 
Candidate: How large is the road data? Can we assume we have access to it? 
Interviewer: Great questions. Yes, let's assume we obtained the road data from different 
sources . It is terabytes (TBs) of raw data. 
Candidate: Should our system take traffic conditions into consideration? 
Interviewer: Yes, traffic conditions are very important for accurate time estimation. 
Candidate: How about different travel modes such as driving, walking , bus, etc? 
Interviewer: We should be able to support different travel modes. 
Candidate : Should it support multi-stop directions? 
Interviewer: It is good to allow a user to define multiple stops, but let's not focus on it. 
I 59 


[Page 68]
Can didate : How about business places and photos? How many photos are we expect¡
ing? 
Interviewer : I am happy you asked and consid red these. We do not need to design 
those . 
In the rest of the chapter, we focus on thr ee key featur es. 1he main devices lhat we need 
to support are mobile phones. 
ò User location update. 
ò Navigatio n service, including ETA service. 
ò Map rendering. 
Non-functional requirements and constraints 
ò Accura cy: Users should not be given the wrong directions. 
ò Smooth navigation: On the client-side, users should experience very smooth map 
rend ering. 
ò Data and battery usage: The client should use as little data and battery as possible. 
This is very important for mobile devices. 
ò General availability and scalability requirements. 
Before jumping into the design, we will briefly inh╖oduce some basic concepts and termi¡
nologies that are helpful in designing Google Maps. 
Map 101 
Positioning system 
The world is a sphere that rotates on its axis. At the very top, there is the north pole, and 
the very bottom is the south pole. 
60 I Chapter 3. Google Maps 


[Page 69]
Figure 3.1: Latitude and longitude (source: [3]) 
Lat (Latitude) : denotes how far north or south we are 
Long (Longitude): denotes how far east or west we are 
Going from 30 to 20 
The process of translating the points from a 3D globe to a 2D plane is called "Map Pro¡
jection". 
There are different ways to do map projection , and each comes with its own strengths 
and limitations. Almost all of them distort the actual geometry . Below we can see some 
examples. 
Step 1 - Understand the Problem and Establish Design Scope I 61 


[Page 70]
Figure 3.2: Map projections (source: Wikipedi a [ 4] [5] [ 6] [7]) 
Google Maps selected a modified version of Mercator proje ction called Web Mercator. 
For more details on positionin g systems and projections, please refer to [3]. 
Geocoding 
Geo coding is the pro cess of converting addresses to geographic coordinates . For instance, 
"1600 Amphith eatre Parkway , Mountain View, CA" is geocode d to a latit ude/longitude 
pair of (latitude 37.423021 , longitude -122 .0 3739). 
In the other direction , the conversion from the latitude /longi tud e pair to the actual 
human -readable addr ess is called reverse geocoding. 
One way to geocode is interpolation [8]. This method leverages the data from differ¡
ent sources such as geograp hic information systems (GIS) wher e the street network is 
mapped to the geographic coordinate space. 
Geohashing 
Geohashing is an encoding system that encodes a geog raphic area into a short string of 
letters and digits. At its core, it depicts the eart h as a flattened surfa ce and recursively 
divides the grids into sub-grids, which can be square or rectangu lar. We represent each 
grid with a string of numbers betw een 0 to 3 that are created recursi vely. 
62 I Chapter 3. Google Maps 


[Page 71]
Let's assume lhe initial flattened surface 1s of siu 20J)00km x 10.000km . After the flr<>l 
division. we would Jrnve 4 grids of siZC' HU100km x !).(100km . We rC'pre~rnr them ~s 00. 
01 , 10, and J 1 as shown in Figure' 3.1. Wc- furthC'r <livid<' rnrh ~rid into 1 ~rids 11nd ll 1'E' I hfò 
same naming slrat('gy . Each sub-grid is now of size !l.OllOkm "< 2.!">00km. We rcrm~ivrly 
divide th e grids until each grid reaches a cer t Rin size thrrshold . 
Figure 3.3: Geohashing 
Geohashing has many uses. In our design, we use geohashing for map tiling. For more 
details on geohashing and its benefits, please refer to [9]. 
Map rendering 
We won't go into a lot of detail about map rendering here, but it is worth mentioning 
the basics. One foundational concept in map rendering is tiling. Instead of rendering th e 
entire map as one large custom image, the world is broken up into smaller tiles. The client 
only downloads the relevant tiles for the area the user is in and stitches them together 
like a mosaic for display. 
Step 1 - Understand the Problem and Establish Design Scope I 63 


[Page 72]
"focre are di ti net se ts of Liles at different zoom leve ls. 1he clirnt chooses th r srt of lilf'~ 
appropriate for the zoom level of the map vicwpor l on th e client. 111is provides the right 
le el of map details wit bout consuming excess bandwidt h. To illus trate wi th fln cxtrrrnr 
xample , wh en tJ1e clien t is zoo med all the way out Lo show thr entire wo rld , we don't 
want to have to download hundr ds of thou sands of Liles for a very hi gh zoo m level. All 
th e detai ls would go to waste . Instead, 1-he client wou ld down load one tile al the lowr~t 
zoom level , which repre sent s the entire world with a sing le 256 x 2G6 pixe l image. 
Road data processing for navigation algorithms 
Mo t routing algorithms are aria tions of Dijkstra 's or A* path.find ing algor ithms. The ex¡
act algorithm choi ce is a complex topic and we wo n' t go into muc h d etail in this chapter. 
What is inlportan t to note is that all these algori thms ope rate o n a graph data structure, 
where intersections are nodes and roads are edges of th e graph. See Figure 3.4 for an 
example: 
Figure 3.4: Map as a graph 
The pathfinding performan ce for most of these algorithms is extremely sensitive to the 
size of the graph . Representin g the entire world of road net works as a single graph would 
consume too much memory and is likely too large for any of these algorithms to run 
efficiently. The graph needs to be brok en up into manageable unit s for these algorithms 
to work at our design scale . 
One w ay to breal< up road network s around the world is very similar to the tiling con¡
cept we discussed for map renderin g. By emp loying a simi lar sub divi sio n t echnique as 
geohashing , w e divide the world into small gri ds. For eac h grid , we convert the roads 
within the grid into a small graph data structure that consis ts of the nodes (intersections) 
and edges (roads) inside the geographical area covered by the grid. We call these grids 
routing tiles . Each routing tile holds referenc es to ali Lhe other tiles it connects to. This is 
how the routing algorithms can stitch together a bigger road grap h as it traverse s these 
interconnected routing tiles . 
By breaking up road networks into routing tiles that can be load ed on demand, the rout-
64 I Chapter 3. Google Maps 


[Page 73]
ing algoriLhms can significantly reduce memory consumpLion nnd improve pAthfinding 
performance by o nly consuming a small subset of the rouling Liles at a Lime, and only 
loading additional t ilcs as needed. 
Figure 3.5: Routing tiles 
Remind er 
In Figure 3.5, we call these grids routing tiles. Routing tiles are similar to map tiles in 
that both are grids covering certain geographical areas. Map tiles are PNG images , 
while routi ng tiles are binary files of road data for the area covered by the tiles. 
Hierarchical routing tiles 
Efficient navigation routing also requires having road data at the right level of detai l. For 
examp le, for cross country routing, it would be slow to run the routing algorithm against 
a highly detailed set of street-level routing tiles. The graph stitched together from these 
detailed routing tiles would likely be too large and consume too much memory. 
There are typically three sets of routing tiles with different levels of detail . At the most 
detailed level, the routing tiles are small and co ntain only local roads . At the next level, 
the tiles are bigger and contain only arterial roads connecting districts together . At the 
lowest level of detail , the tiles cover large areas and contain only major highways con¡
necting cities and states together . At each level, there could be edges connectin g to tiles 
at a different zoom l evel. For examp le, for a freeway entranc e from local street A to 
freeway F, there would be a reference from the node (street A) in the small tile to the 
node (freeway F) in the big tile. See Figure 3.6 for an example of routing tiles of varying 
sizes. 
Step 1 - Underst and the Problem and Establish Design Scope I 65 


[Page 74]
Figure 3.6: Routing tiles of varying sizes 
Back-of-the-envelope estimation 
Now that we understand the basics, let's do a back-of-the-envelope estimation. Since 
the focus of the design is mobile, data usage and battery consumption are two important 
factors to consider. 
Before we dive into the estimation, here are some imperial/metric conversions for refer¡
ence. 
ò 1 foot = 0.3048 meters 
ò 1 kilometer (km)= 0.6214 miles 
ò 1km=1 ,000 meters 
Storage usage 
We need to store three types of data. 
ò Map of the world: A detailed calculation is shown below. 
ò Metadata: Given that the metadata for each map tile could be negligible in size, we 
can skip the metadata in our computation . 
ò Road info: The interviewer told us there are TBs of road data from external sources. 
We transform this dataset into routing tiles, which are also likely to be terabytes in 
size. 
66 I Chapter 3. Google Maps 
ò 


[Page 75]
M ap of the world 
W discussed the concrp t of map tiling i11 the "Map 101" section on page 60. There are 
many ets of map tiles. with one al ach zoom level. Tog tan idea of thr storage require¡
m nt for the ntire collec1ion of map tile images. it would he informative to estimate the 
size of the lArgesl tile set at the highest zoom level fi rst. At zoom level 21, there are about 
4.3 trillion tiles (Table 3.1). Let's assume that ach tile is a 2!J() Y 2!J6 pixel compresse d 
PN image , with the image size of about 1 OOKB. The entir e set at the highest zoom level 
would need about 4.4 trillion x 1 OOKB = 440PB. 
In Table 3.1, we show the progression of tile counts at every zoom level. 
Zoom Numb er of Tile s 
0 1 
1 4 
2 16 
3 64 
4 256 
5 1 024 
6 4 096 
7 16 384 
8 65 536 
9 262 144 
10 1 048 576 
11 4194 304 
12 16 777 216 
13 67 108 864 
14 268 435 456 
15 1 073 741 824 
16 4 294 967 296 
17 17 179 869 184 
18 68 719 476 736 
19 27 4 877 906 944 
20 1 099 511 627 776 
21 4 398 046 511 104 
Table 3.1: Zoom levels 
However , keep in mind that about 903 of the world's surface is natural and mostly un¡
inhabited areas like oceans , deserts, lakes, and mountains. Since these areas are highly 
compressible as images , we could conservatively reduce the storage estimate by 80 rv 
903. That would reduce the storage size to a range of 44 to 88PB. Let's pick a simpl e 
round number of 50PB. 
Next, let's estimate how much storage each subsequent lower zoom level would take. At 
each lower zoom level, the numb er of tiles for both north -south and east -west directions 
drops by half. This results in a total reduction of the number of tiles by 4x, which drop s 
Step 1 - Understand the Problem and Establish Design Scope I 67 


[Page 76]
the storage size for the zoom level also by 4x. With the storage size reduced by 4x Rt each 
lower zoom level, the math for lhe total size is a series: fiO + ~o + ~g + ~~ + ╖ ╖ ╖ = ..... , ()7PB. 
This is just a rough estimate. It is good enou gh to know that we need roughly about lOOPil 
to store all the map Liles at varyin g levels of detail. 
Server throughput 
-
To estimate the server throughput , let's review the types of requ ests we need to support. 
There are two main types of requests. The first is navigation requests . These are sent by 
the clients to initiate a navigation session. TI1e second is location update requests. These 
are sent by the client as the user moves around during a navigation session. The location 
data is used by downstream services in many different ways. For examp le, location data 
is one of the input s for live traffic data. We will cover the use cases of location data in 
the design deep dive section . 
Now we can analyze the server throughput for navigation requests . Let's assume we 
have 1 billion DAU, and each user on average uses navigation for a total of 35 minutes per 
week. This translates to 35 billion minutes per week or 5 billion minutes per day. 
One simple approach would be to send GPS coordinates every second , which re¡
sults in 300 billion (5 billion minutes x 60) requests per day, or 3 million QPS 
( 300 billion requests . . ) ╖ d d GPS d 
105 = 3 rrullion . However, the client may not nee to sen a up ate 
every second. We can batch these on the client and send them at a m uch lower 
frequency (for example, every 15 seconds or 30 seconds) to reduce the write QPS. The 
actual frequency could depend on factors such as how fast the user moves. If they are 
stuck in traffic, a client can slow down the GPS updates. In our design, we assume GPS 
updates are batched and then sent to the server every 15 seconds. With this batched 
approach, the QPS is reduced to 200,000 ( 3 rrt~ion). 
Assume peak QPS is five times the average. Peak QPS for location updates= 200,000 x 
5 = 1 million . 
Step 2 - Propose High-level Design and Get Buy-in 
Now that we have more knowledge about Google Maps, we are ready to propose a high¡
level design (Figure 3.7). 
High-level design 
68 I Chapter 3. Google Maps 


[Page 77]
Navigation 
Service 
Mobile User 
Load Balancer 
Geocoding DB Routing Tiles 
(Object storage) 
Location 
Service 
User Location DB 
Figure 3.7: High-level design 
CON 
Precomputed Map Images 
(Origin) 
The high-level design supports three features. Let's take a look at them one by one . 
1. Location service 
2. Navigation service 
3. Map rendering 
Location service 
The location service is responsible for recording a user's location update . The architecture 
is shown in Figure 3.8. 
Step 2 - Propose High-level Design and Get Buy-in I 69 


[Page 78]
Load Balancer 
Loca tion 
Service 
User Location DB 
Figure 3.8: Location service 
The basic design calls for the clients to send location updates every t seconds, where 
t is a configurable interval. The periodic updates have several benefits. First, we can 
leverage the streams of location data to improve our system over time. We can use the 
data to monitor live traffic, detect new or closed roads, and analyze user behavior to 
enable personalization , for example. Second, we can leverage the location data in near 
real-time to provide more accurate ETA estimates to the users and to reroute around 
traffic, if necessary. 
But do we really need to send every location update to the server immediatel y? The 
answer is probably no. Location history can be buffered on the client and sent in batch 
to the server at a much lower frequency. For example, as shown in Figure 3.9, the location 
updates are recorded every second, but are only sent to the server as part of a batch every 
15 seconds. This significantly reduces the total update traffic sent by all the clients. 
-----------------------------------------------------------------------------------------i 
I 
I 
Batch 3 
fic;lo~~ 
~--- ~~ 
Client 
Batch 2 
~o~fic;l 
~ -- ╖~~ 
Batch 1 
i , .. 15s I I 15s I I ò 15s .. , 
I ò 
I 
I 
I 
~---- -- --- - - -- ---- --- - - - ----- -- -- - ----- -- ----- - ------- - --- - - - - - - - -- - ---- ---- -- -- --- - -- --- -
Figure 3. 9: Batch requests 
For a system like Google Maps, even when location updates are batched , the write volume 
is still very high. We need a database that is optimized for high write volume and is 
highly scalable, such as Cassandra. We may also need to log location data using a stream 
70 I Chapter 3. Google Maps 
' .╖ 
.╖ 


[Page 79]
procc-ssing t" n~inc such as Kafka for furth er proc-rssirtA. We di ~cu.qs this in o('f~i l in th<> 
deep diVl" section. 
Wh al c-ommunic ation protocol might br a good nt here? HTTP with th e keep-alive op¡
tion [ 10] is a good choice hccause it is very efficient. 1he HTTP request might loo k like 
thi : 
POST / v1 / lo cat i ons 
Parameters 
l ocs: JSON encode d ar ra y of (latit ude , l ongitude, timesta mp) 
tuples. 
Navigation service 
This component is responsi ble for finding a reaso nably fast route from p oint A to point 
B. We can tolerat e a little bit of latency. The calculated route does not h ave to be the 
fastest, but accuracy is critical. 
As shown in Figure 3.8, the user sends an HTTP reque st to the navigation servic e thro ugh 
a load balancer . The request includ es origin and destin ation as the paramet ers. The API 
might look like this : 
GET /v1/nav?origin=1355+market+street,SF&destination= 
Disneyland 
Here is an example of what the navigation result could look like: 
{ 
} 
'distance' : { 1 text' : ' 0. 2 mi' , 1 value' : 259} , 
'duration' : { 'text' : ' 1 min 1 , 'value' : 83} , 
1
end_location' : { 'lat' : 37 . 4038943 , 'Ing' : - 121 . 9410454} , 
'html_instructions' : 'Head <b>northeast</b> on <b>Brandon St 
</b> toward <b>Lumin Way</b><div style="font-size : 0 . 9em
11
> 
Restricted usage road</ div>' , 
'polyline' : { 'points' : '_fhcFjbhgVuAwDsCal ' }, 
'start_location' : { 'lat' : 37. 4027165, 'lng' : - 121 . 9435809} , 
'geocoded_waypoints ': [ 
{ 
'\. 
J ' 
{ 
} 
J' 
"geocoder_status" : "OK" , 
"partial_match" : true , 
"place _id" : "ChIJwZNMti1fawwR02aVVVX2yKg" , 
"types" : [ "locality" , "political" ] 
11 geocoder_status
11 
: "OK" , 
"partial_match" : true , 
"place_id" : "ChIJ 3aPgQGtXawwRLYeiBMUi7bM" , 
"types" : [ "locality" , "political" ] 
1 traveLmode 
1
: 'DRIVING' 
Please refer to [11] for more details on Google Maps' official APis. 
So far we have not taken reroute and traffic changes into consideration. Those problems 
are tackled by the Adaptive ETA service in the deep dive section. 
Step 2 - Propose High-level Design and Get Buy-in I 71 


[Page 80]
M ap rendering 
As we discussed in t hr back-of-the-envelope cslimalion, I he entire collection of map ti l <-~ 
al various zoom levels is A.bout a hund red pelabytcs in size. It is no t practical lo hold th 
entire datase t on the client. The map tiles must be fetched on-demand from LhC' 11crver 
based on the client 's location and the zoom level of the client viewporl. 
When should the client fetch new map tiles from the server? Here a re some scenar 
ios: 
ò l11e user is zooming and pan ning the map viewpoint on the client to explore their 
surroundings . 
ò During navigation, the user moves out of the current map tile into a nearby tile. 
We are dealing with a lot of data. Let's see how we could serve these map tiles from the 
serve r efficiently. 
Option 1 
The server builds the map tiles on the fly, based on the client location and zoom level of the 
client viewport. Considering that there is an infinite number of location and zoom level 
combinations, generating map tiles dynamically has a few severe disadvantage s: 
ò It puts a huge load on the server cluster to generate every map tile dynami cally. 
ò Since the map tiles are dynamically generated, it is hard to take advantage of caching. 
Option 2 
Another option is to serve a pre-generated set of map tiles at each zoom level. The map 
tiles are static, with each tile covering a fixed rectangular grid using a subdivision scheme 
like geohashing. Each tile is therefore represented by its geohash . In other words , there 
is a unique geohash associated with each grid. When a client needs a map tile, it first de¡
termines the map tile collection to use based on its zoom level. It then computes the map 
tile URL by converting its location to the geohash at the appropriate zoom level. 
These static , pre-generated images are served by a CDN as shown in Figure 3.10. 
72 I Chapter 3. Google Maps 
I 
1 


[Page 81]
Mobi le User 
CON 
Precomputed Map Images 
(Origin) 
Figure 3.10: Pre-generated images are served by a CDN 
In the diagram above, the mobile user makes an HTTP request to fetch a tile from the 
CDN. If the CDN has not yet served that specific tile before, it fetches a copy from the 
origin server , caches it locally, and returns it to the user. On subsequent requests , even 
if those requests are from different users, the CDN returns a cached copy without con¡
tacting the origin server. 
This approach is more scalable and performant because the map tiles are served from the 
nearest point of presence (POP) to the client , as shown in Figure 3.11. The static nature 
of the map tiles makes them highly cacheable . 
Step 2 - Propose High-level Design and Get Buy-in I 73 


[Page 82]
╖----------------~-
Wi1hou1 CON 
- - 300 ms 
D 
With CON 
, , 
, , , 
, 
,l!l-10ms 
. POP 
~-------- - -----~~:----- - ----- -- -- ~!~ 
POP 
Origin Servef- ',,,', ,,',, , l!~OP 
POP 
Figure 3.11: Without CDN vs with CDN 
ò ~ 
It is impo rtant to keep mobile data usage low. Let's calculate the amount of data the 
client nee ds to load during a typical navigation session. Note the following calculations 
don 't take client-side caching into consideration . Since the routes a user takes could be 
similar each day, the data usage is likely to be a lot lower with client-side caching. 
Data usage 
Let's assume a user moves at 30km/h, and at a zoom level where each image covers a 
block of 200m x 200m (a block can be represented by a 256-pixel by 256-pixel image 
and the average image size is IOOKB). For an area of lkm x lkm, we need 25 images 
or 2.5MB (25 x lOOKB) of data. Therefore, if the speed is 30km/h, we need 75MB 
(30 x 2.5MB) of data per hour or l.25MB of data per minute. 
Next , we estimate the CDN data usage. At our scale, the cost is an important factor to 
consider. 
7 4 I Chapter 3. Google Maps 


[Page 83]
Trroflc through N 
As menti oned arlier, IVE' serve !) billion minut es of nAvigation per day. lhis tran s¡
lat to G bUlion x l .21iMR = <l.2r) billion MB per dfly. I fence. we serve o2,GOOMR 
( 
6╖25 hill~on ) of map dAla I) r sc oncl. Wlth A ON thr . r map images nre go-1 0ò1 srcond~ in n dn ò 
ing Lob erved from lhe P Ps All over lh world. Let' s ass ume tht
1
re are 200 POPs. 
ach POP wou ld on ly need to erve a few hundr ed MI3s ( n;╖~'i'1JO) per seco nd. 
--- - -- - -- - -- - - - - -
There i one final detail in the map rendering design we have only briefly touched on. 
How does the clien t know whi ch URLs to use to fetch the map tiles from the CON? Keep 
in mind that we are using option 2 as discusse d above . With that option , the map tiles 
are static and pre -ge nerated based on fixed sets of grids, with each set repres entin g a 
discrete zoom level. 
Since we encode the grids in geohash, and there is one uniqu e geohash per grid , 
computationally it is very efficient to go from the client's location (in latitud e and 
longitude) and zoom level to the geohash, for the map tile. This calculatio n can 
be done on the client and we can fetch any static imag e tile from the CDN. For 
examp le, the URL for the image tile of Google headquart er could look like this: 
https://cdn.map-provider.com/tiles/9q9hvu.png 
Refer to Chapter 1 Proximity Service on page 1 o for a more detaile d discussion of geohash 
encoding. 
Calculating geohash on the client should work well. However, keep in mind that this 
algorithm is hardcoded in all the clients on all different platforms . Shipping changes to 
mobile apps is a time-consuming and somewhat risky process. We have to be sure that 
geohashing is the method we plan to use long -term to encode the collection of map tiles 
and that it is unlikely to change . If we need to switch to another encoding method for 
some reason , it will take a lot of effort and the risk is not low. 
Here is another option worth considering. Instead of using a hardcoded client -side algo¡
rithm to convert a latitude /longitude (lat/lng) pair and zoom level to a tile URL, we could 
introduce a service as an intermediary whose job is to construct the tile URLs based on 
the same inputs mentioned above. This is a very simple service . The added operational 
flexibility might be worth it. This is a very interesting tradeoff discussion we could have 
with the interviewer. The alternative map rendering flow is shown in Figure 3.12. 
When a user moves to a new location or to a new zoom level, the map tile service de¡
termines which tiles are needed and translates that information into a set of tile URLs to 
retrieve . 
Step 2 - Propose High-level Design and Get Buy-in I 75 


[Page 84]
Mobil e User 
~ Download tiles 
G) Fetch URLs of tiles 
Load Balancer 
« Forward Request 
« 
Construct 
URLs of tiles 
Map Tile Service 
Figure 3.12: Map rendering 
CON 
1. A mobile user calls the map tile service to fetch the tile URLs. The request is sent to 
the load balancer. 
2. The load balancer forwards the request to the map tile service. 
3. The map tile service takes the client's location and zoom level as inputs and returns 
9 URLs of the tiles to the client. These tiles include the tile to render and the eight 
surrounding tiles. 
4. The mobile client downloads the tiles from the CDN. 
We will go into more detail on the precomputed map tiles in the design deep dive sec¡
tion. 
Step 3 - Design Deep Dive 
In this section, we first have a discussion about the data model. Then we talk about 
location service, navigation service, and map rendering in more detail. 
Data model 
We are dealing with four types of data: routing tiles, user location data, geocoding data, 
and precomputed map tiles of the world. 
Routing tiles 
As mentioned previously, the initial road dataset is obtained from different sources and 
authorities. It contains terabytes of data. The dataset is improved over time by the lo¡
cation data the application continuously collects from the users as they use the applica¡
tion. 
1his dataset contains a large number of roads and associated metadata such as names, 
county, longitude, and latitude. This data is not organized as graph data structures and 
7 6 I Chapter 3. Google Maps 


[Page 85]
is not Hsable by most routing algorithms. We run a periodic oflline processing pipeline, 
called rou ting tile processing service, to tran sform this dataset into the routin g tiles we 
introduced . 111e service run s periodically lo captur e new changes lo the road data. 
111e output of the routin g tile processing service is routing tiles. There a re three sets 
of these tiles at different resolutions , as described in the "Map 101" section on p age 60. 
Each tile contains a list of graph nodes and e dges representing the intersections a nd 
road within the a rea covered by the t ile. It also contains references to other tiles its 
road connect to. These tiles toge ther form an interconnected network of roads that the 
routing algorithms can consume incrementally. 
Where should the routin g tile processing service store these tiles? Most graph dat a is 
repr esented as adjacency lists [12] in memory. There are too many t iles to keep the 
entire set of adjacency lists in memory. We could store the nodes and edges as rows in a 
database , but we would only be using the database as storage , and it seems an expensive 
way to store bits of data. We also don 't need any database features for routing tiles. 
The more efficient way to store these tiles is in object storage like S3 and cache it ag¡
gressively on the routing service that uses those tiles. There are many high-performan ce 
software packages we could use to serialize the adjacency lists to a binary file. We could 
organize these tiles by their geohashes in object storage. This provides a fast lookup 
mechanism to locate a tile by lat/lng pair. 
We discuss how the shortest path service uses these routing tiles shortly. 
User location data 
User location data is valuab le. We use it to update our road data and routing tiles. We 
also use it to build a database of live and historical traffic data. This location data is also 
consumed by multiple data stream processing services to update the map data. 
For user location data, we need a database that can handle the write-heavy workload well 
and can be horizontally scaled. Cassandra could be a good candidate. 
Here is what a single row could look like: 
user _id times tamp user_mode driving_ mo de location 
101 1635740977 active driving (20.0, 30.5) 
Table 3.2: Location table 
Geocoding database 
This databas e stores places and their corresponding lat/lng pair. We can use a key-value 
database such as Redis for fast reads , since we have frequent reads and infrequent writes. 
We use it to convert an origin or destination to a lat/lng pair before passing it to the rout e 
planner service. 
Precomputed images of the world map 
When a device asks for a map of a particular area , we need to get nearby roads and 
comput e an image that represents that area with all the roads and relat ed details . These 
Step 3 - Design Deep Dive I 77 


[Page 86]
ompu ti uld be heavy and redund ant, so it co uld be h elpfu l l o compute 
n d then cache the images. We prccompu te images at differe nt zoo m l evel~~~ll'i 
lb m n CD . whirh is backed b y cloud storage such as Amazo n S3. Here i lld 
'---''CLUò.vl of such an image: ,q illl 
Figure 3.13: Precomputed tiles 
Services 
Now that we have discussed the data model, let's take a close look at some of the most im╖ 
portant services: location service, map rendering service, and navigation service. 
Location service 
In the high-level design, we discussed how location service works . In this section, we 
focus on the database design for this service and also how user location is used in de¡
tail 
In Figure 3.14, the key-value store is used to store user location data. Let 's take a dose 
look. 
18 f Olapt.er 3. Google Maps - -- -- - --- - -
1 


[Page 87]
Mobile User 
Load Balancer 
Location 
Service 
User Location DB 
Figure 3.14: User location database 
Given the fact we have 1 million location updates every second, we need to have a 
database that supports fast writes. A NoSQL key-value database or column -oriented 
database would be a good choice here. In addition, a user's location is continuously 
changing and becomes stale as soon as a new update arrives. Therefore, we can prior¡
itize availability over consistency. The CAP theorem [13] states that we could choose 
two attributes among consistency, availability, and partition tolerance. Given our con¡
straints, we would go with availability and partition tolerance. One databas e that is a 
good fit is Cassandra. It can handle our scale with a strong availability guarantee. 
The key is the combination of (user _id, timestamp) and the value is a lat/lng pair. In 
this setup , user _id is the primary key and timestamp is the clustering key. The advantage 
of using user _id as the partition key is that we can quickly read the latest position of a 
specific user. All the data with the same partition key are stored together, sorted by 
times tamp. With this arrangement, the retrieval of the location data for a specific user 
within a time range is very efficient. 
Below is an example of what the table may look like. 
key (user_id) time stamp lat long user_mode navigation _mode 
51 132053000 21.9 89.8 active driving 
Table 3.3: Location data 
How do we use the user location data? 
User location data is essential. It supports many use cases. We use the data to detect new 
and recently closed roads. We use it as one of the inputs to improve the accuracy of our 
map over time. It is also an input for live traffic data . 
To support these use cases, in addition to writing current user locations in our data -
Step 3 - Design Deep Dive I 79 


[Page 88]
Ntc;t>. wr Ill!( thi.s information into a message queue, sue ~ as Kafka. Kr1 ~a i.q a tttiifie<l 
lc..-╖-latf'ncy. high -throughput data streaming plat fo rm des ig ned fo r real-time data feed~ 
F1gu"" 3.1 S shows how Kafka is used in the impro ved d esig n. 
Load Balancer 
Location 
Service 
User Location DB 
Kafka 
Traffic Updat e 
Service 
Machine Learning 
Traffic DB 
Service for 1----~ 
Personalization 
Routing Tile 
Processing 
Service 
Analytics 
Personalization DB 
Routing Tiles 
(Object storage) 
Analytics DB , 
' ----- - -------- -- ---- -- -- -- ---------------------~ 
Figure 3.15: Location data is used by other services 
OtJ1er services consume the location data stream from Kafka for various use cases. For 
instance , the live traffic service digests the output stream and updates the live traffic 
database . The routing tile processing service improves the map of the world by detect¡
ing new or closed roads and updating the affected routing tiles in object storage. Other 
services can also tap into the stream for different purposes. 
Rendering map 
In this section, we dive deep into precomputed map tiles and map rendering optimization. 
They are primarily inspired by the work of Google Design [3]. 
Precomputed tiles 
As mentioned previously, there are different sets of precomputed map tiles at various 
distinct zoom levels to provide the appropriate level of map detail to the user, based on 
the client's viewport size and zoom level. Google Maps uses 21 zoom levels (Table 3.1). 
This is what we use , as well. 
Level 0 is the most zoomed-out level. The entire map is represented by a single tile of 
size 256 x 256 pixels. 
With each increment of the zoom level, the number of map tiles doubles in both north¡
south and east-west directions, while each tile stays at 256 x 256 pixels. As shown in 
Figure 3.16, at zoom level 1, there are 2 x 2 tiles, with a total combined resolution of 
1>12 x 512 pixels. At zoom level 2, there are 4 x 4 tiles, with a total combined resolution 
of 1024 x 1024 pixels. With each increment, the entire set of tiles has 4x as many pixels 
80 I Chapter 3. Google Maps 


[Page 89]
A 1he prl'nom lc-vel The increased pixel count provides an increasin~ level 0f <leta1l tn 
the U . t>T. Ttus aJ)ows the client fo render th(' map at the best granulantit>S dependmtz 
on the d1C'nt░$ zoom level. without consuming excessive band idth to download tiles in 
C'Xres"1 \ e detail. 
Zoom leÑel0 
Zoom level 1 
Zoom level 2 
Figure 3.16: Zoom levels 
Optimization: use vectors 
With the development and implementation of WebGL, one potential improvement is to 
change the design from sending the images over the network , to sending the vector in¡
formation (paths and polygons) instead . The client draws the paths and polygons from 
the vector information. 
One obvious advantage of vector tiles is that vector data compresses much better than 
images do. The bandwidth saving is substantial . 
A less obvious benefit is that vector tiles provide a much better zooming experience . 
With rasterized images , as the client zooms in from one level to another , everything gets 
Step 3 - Design Deep Dive I 81 


[Page 90]
--
Shortest -path service 
1he shorte st-path scr ice receives the origi n and the destin ation in lat/Ing p;:iirs and re 
turns th e top-k shortest paths without considering traffic or curr <'nl conditions . ╖rh;, 
computation onl depends on the stru cture of the roads . Herc, cachin g the rout es could 
be benefi cial because the grap h rarely changes. 
l11e hortest -path service rw1s a variation of A* pathfinding algorithm s aga inst the rout¡
ing tile in object storage. Here is an overv iew: 
ò The algorithm receives the origin and destination in lat/lng pairs . The lat/lng pairs 
are converted to geohashes which are then us ed to load the star t an.d end -points of 
routing tiles . 
ò The algorithm starts from the origin routing tile, trav erses the graph dat a structure, 
and hydrates additional neighboring tiles from object storage (or its local cache if it 
has loaded it before) as it expands the search area . It's worth noting that there are 
connections from one level of tile to another covering the same area . This is how 
the algorithm could "enter" the bigger tiles containing only highways , for example. 
The algorithm continues to expand its search by hydrating more neighboring tiles 
(or tiles at different resolutions) as needed until a set of best routes is found. 
Figure 3.18 (based on [ 14]) gives a conceptual overview of the tiles used in the graph 
traversal. 
Figure 3.18: Graph traversal 
ETA service 
Once the route planner receives a list of possible shortest paths , it calls the ETA service 
for each possible route and gets a time estimate . For this , the ETA service uses machine 
learning to predict the ETAs based on the current traffic and historical data 
One of the challenges here is that we not only need to have real -time traffic data but also 
to predict how the traffic will look like in 10 or 20 minutes. These kinds of challenges 
need to be addressed at an algorithmic level and will not be discussed in this section. If 
84 I Chapter 3. Google Maps 


[Page 91]
you RTe interest d. refer lo [15] and (16). 
Ranker service 
Finall . after the route plann r obtains the ETA pr dictions, it passes Lhis info to the 
ranker t appl po ibl filters as defined by the user. Some example filters include op¡
ti n t a oid toll roads or to avoid freeways . The rank r service then rank s the possible 
rout from fastest to slowest and returns top-k results to the navigation serv ice. 
Update r services 
111ese ervices tap into the Kafka location u pdate stream and asynchronous ly updat e 
ome of the important data bases to keep them up-to -date. The traffic database and the 
routing tiles are some examples. 
1he routing tile proces sing service is responsibl e for transformin g the road dataset with 
newly found roads and road closur es into a continuousl y upd ated set of routing tiles. 
111is helps the shortest path service to be more accuTate. 
The traffic update ser vice extracts traffic conditions from the streams of location updates 
sent by the active users . This insight is fed into the live traffic database. This enables the 
ETA service to provide more accurate estimates . 
Improvement : adaptiv e ETA and rerouting 
The current design does not support adaptive ETA and rerouting . To address this, the 
server needs to keep track of all the active navigating users and update them on ETA 
continuously , whenever traffic conditions change . Here we need to answer a few impor¡
tant questions: 
ò How do we track actively navigating users? 
ò How do we store the data , so that we can efficiently locate the users affected by traffic 
changes among millions of naviga tion routes ? 
Let's start with a naive solution . In Figure 3.19, user_ 1 's navigation route is repres ented 
by routing tiles r _ 1, r _2, r _3, ... , r _ 7 . 
. ------- --,----- -- -,--------,---------. 
: r_1 : r_2 : r_3 : r_4 : 
: (origin) : : : : 
l------- - -'-------- -' -- -- ----- ~ l l 
l 
r_5 : 
I l 
...._ ___ ..._L. _____ - - - -
' ' ' : r_6 : r_7 : : l (destinatio n) : 
'- - -- - -- - - L- ---- - --- 1 
Figure 3.19: Navigation route 
The database stores actively navigating users and routes information whi ch might look 
like this : 
user_1: r_1, r_2, r_3, ... , r_k 
-------------- -- - - - - - -
Step 3 - Design Deep Dive I 85 


[Page 92]
user _2 : r _4, r _6, r _9, 
user _3 : r _2, r _8, r_9, 
... ' 
... , 
r_n 
r_m 
user _n: r_2, r_10, r_21, . . . , r _l 
Let's say there is a traffic incident in rou tin g Lile 2 (r _2). To flgure oul which user~ arr 
affec ted, we scan throu gh each row and check if rou tin g Lile 2 is in our lisl of routing tilrq 
(see exampl e below). 
user_1: r _ 1, r_2 , r_3, ... , r_k 
user_2: r_4, r_6, r_9 , ... , r_n 
user_3: r_2 , r_8, r _ 9, ... , r_m 
user_n: r_2 , r_10, r_21, ... , r_l 
Assume the number of rows in the table is n and the average length of the navigation 
route ism .. The time complexity to find all users affected by the traffi c change is O(n x 
rn). 
Can we make this process faster? Let's explore a different approach. For each actively 
navigating user , we keep the current routing tile, the routing tile at the next resolution 
level that contains it, and recursively find the routing tile at the next resolution level until 
we find the user 's destination in the tile as well (Figure 3.20). By doing this, we can get 
a row of the database table like this. 
user_1, r_1, super(r_1), super(super(r_1)), ... 
86 I Chapter 3. Google Maps 


[Page 93]
I 
: This routing tile only contains origin 
I 
Origin 
0 Origin 
Routing tile 
Level 1 
Routing tile 
I 
--------' 
r------------------ ----------- ---- -- ------------------------ --------, 
0 Origin 
Destination 0 
Level 2 
Routing tile 
I 
I 
This routing tile contains 
both origin and destination 
I 
I I 
'----------------------------------------------------------------------
Figure 3.20: Build routing tiles 
To find out if a user is affected by the traffic change, we need only check if a routing tile 
is inside the last routing tile of a row in the database. If not , the user is not impact ed. If 
it is, the user is affected . By doing this, we can quickly filter out many users. 
This approach doesn 't specify what happens when traffic clears. For example, if routing 
tile 2 clears and users can go back to the old route , how do users know rerouting is 
available ? One idea is to keep track of all possible routes for a navigating user, recalculate 
the ETAs regularly and notify the user if a new route with a shorter ETA is found . 
Delivery protocols 
It is a reality that durin g navigation , route conditions can change and the server needs 
a reliable way to push data to mobile clients . For delivery protoco l from the server to 
the client, our options include mobile push notification, long polling , WebSocket , and 
Server -Sent Events (SSE). 
ò Mobile push notifi cation is not a great option because the payload size is very limit ed 
(4,096 bytes for iOS) and it doesn 't support web applications. 
ò WebSocket is generally considered to be a bett er option than long polling because it 
has a very light footprint on servers . 
ò Since we have ruled out the mobile push notification and long polling , the choice is 
mainly betwe en WebSocket and SSE. Even though both can work, we lean towards 
WebSocket because it supports bi-directional communicati on and features such as 
Step 3 - Design Deep Dive I 87 


[Page 94]
las L-mil e delivery m.ight require bi-dire ction al rea l-lim e communi ca tio 11 . 
For m ore deLails a bout ETA and rerouting , please refer Lo [15]. 
N o w w e have every piece of the design toge ther. Please see the upd ated d es ign in Fig 
3.2 1. lit( ò 
Mobile User 
f===1 .. ___,_J Geocodlng l L_J l Service _- ---1 
Geocod lng DB '---.-- - .....,....... 
Navigation 
Service 
Ranker 
Filter Service 
(Avoid tolls, ... ) 
Route Planer 
Servloe 
Shortest Patil 
Service 
Routing Tiles 
(Object storage) 
ETA Service 
Traffic DB 
Update Traffic 
Service 
LJ 
Location DB 
Figure 3.21: Final design 
Step 4 - Wrap Up 
Adapt ive ETA and 
Rerouting 
Active Users 
In this chapter , we designed a simplified Google Map application with key features such 
as location update , ETAs, route planning, and map r ndering. If you are interested in 
expanding the system , one potential improvement would be lo provide multi-stop navi¡
gation capability for enterprise customers. For examp l , for a given set of destinations, 
we have to find the optimal order in which to visit lhem all and provide proper naviga¡
tion, based on live traffic conditions. This could be helpful for delivery services such as 
DoorDash, Uber, Lyft, etc. 
Congratulations on getting this far! Now give yourself a pat on the back. Good job! 
88 Chapter 3. Google Maps 


[Page 95]
Chapter Summary 
step I 
step 2 
Google Maps 
step 3 
L 11~rr lou1tion 11pcl.lt,. 
fmu ,;,.,,,I coq '\_ "" 'ò' tinn "" '" 
map rrnrlrrin g 
L highly accurnlr 
non-fu nclion'I "'I '\_ òmooth "'"'g>tmo 
data usage 
<
storag e 
estimation 
server traffic 
positioning system 
goin g from 3d to 2d 
map 101 geocoding 
geohashing 
routing tiles 
location service 
high-level design navigat ion servi ce 
map rendering 
routing tiles 
user location 
data 
places 
precomputed images 
. < locat ion service -- how location data is used 
serVJces < precomputed tiles 
rendering map 
use vectors 
geocoding 
route planner 
navigation service shortest-path 
step 4 -- wrap up ETA service 
adaptive ETA and rerouting 
- -
Chapter Summary I 89 
--


[Page 96]
Reference M aterial 
[ l] Google faps. https ://devclopcrs.googlc.com /maps ?hJ=cn __ US. 
[2] Gooirle Maps Platform . h ll.ps://cloud.goog le.com/map s-p Jalform /. 
[3) Prototyping a Smoother Map. https :// medium .com/goog le-design /google-ma _ 
b0326d165fS. ps c 
[ 4] Mercator projectio n. https ://en. wik.ipedia.org/wiki /Merca tor_projection. 
[5] Peirce quin cuncial projection. http s://en.wikipedia.org/wik.i/Pei rce_qui ncunciaJ 
rejection . - P 
[ 6] Gall-Pete rs proj ection. https ://en.wik.ipedia.org/wiki/Gall- Peters_proj ection. 
[7] Winkel trip el projection . https ://en.wikipedia .org/wiki/Wink el_trip el_proj ection. 
[ 8] Address geocoding . https: // en. wikipedia .org/wild/ Address _geocodin g. 
[9] Geohashing . https ://kousiknath .medium .com/system -design-design -a-geo- spatial 
-index-for-real-time-location-search-10968fe62b9c. 
[ 10 J HTTP keep-alive . https: // en. wikipedia.org /wild/HTTP _persistent_ connection. 
[ 11 J Directions APL https: //developers.google.com /maps / documentation / directions /st 
art ?hl=en_ US. 
[12] Adjacency list. https: //en.wikipedia.org /wik.i/Adjacency _list. 
[13] CAP theorem . https: //en.wikipedia .org/wild/CAP _theorem . 
[ 14] Routing Tiles. https :/ /valhalla.readthedocs.io /en/lates t/mjolnir /why _tiles/. 
[15] ETAs with GNNs. https: //deepmind .com/blog/article /traffic-prediction-with-adva 
need-graph-neural-networks . 
[16] Google Maps 101: How AI helps predict traffic and determine routes. https: //blog 
.google /products /maps /google-maps-101-how -ai-helps-predict - traffic-and-deter 
mine-routes /. 
90 I Chapter 3. Google Maps 
..... ___ _ 
t 


[Page 97]
4 Distributed Message Queue 
In this chap ter, we explore a popular question in system design interviews: design a 
distributed message queue . In modern architecture , systems are broken up into small and 
independent building blocks with well-defined interfaces between them . Message queues 
provid e communication and coordination for those building blocks . What benefits do 
message queues bring? 
ò Decoupling. Message queues eliminate the tight coupling between components so 
they can be updated independently . 
ò Improved scalability . We can scale producers and consumers independently based 
on traffic load. For example, during peak hours , more consumers can be added to 
handle the increased traffic. 
ò Increased availability. If one part of the system goes offline, the other components 
can continue to interact with the queue. 
ò Better performan ce. Message queues make asynchronous communication easy. Pro¡
ducers can add messages to a queue without waiting for the response and consumers 
consum e messages whene er they ar available. They don 't need to wait for each 
other . 
Figure 4-.1 shows some of h most popular di tributed m ssage queues on the mar¡
ket. 
~ Apache Kafka 
~ Apache Pulsar 
~ Apache RocketMO 
'~ .. ò 
Apache ActlveMO 
ll::a RabMMQ 
0 ZeroMQ 
Figure 4.1: Popular distributed message queues 
I 91 


[Page 98]
Message queues vs event streaming platform s 
Strictly speaking, Apache Kafka and Pulsar are not message queues as lhC'y arr <'Ve╖ 
streaming platforms. However, there is a converge nce of featur es that starts lo blur 1~; 
distinction between message queu es (RocketMQ , AcliveMQ, RabbitMQ , ZcroMQ, etc 
and event streaming platforms (Kafka, Pulsar). For example , RabbitMQ , which is a lyPiq~ 
message queue , added an optiona l strea ms feature to allow rep eated message consurnp. 
tion and long message retention, and its implementation uses an append -only log, much 
like an event streaming platform would. Apache Pulsar is primarily a Kafka competitor 
but it is also flexible and performant enoug h to be used as a typical distribut ed messag~ 
queue. 
In this chapter , we will design a distributed message queu e with additional f ea tu res 
) 
such as long data retenti on, rep eated consumption of messages , etc ., that are typ. 
ically only available on event streaming platforms . These additional features make the 
design more complicated. Throughout the chapter , we will highlight places where the de¡
sign could be simplified if the focus of your interview centers around the more traditional 
distributed message queues . 
Step 1 - Understand the Problem and Establish Design Scope 
In a nutshell , the basic functionality of a message queue is straightforward: producers 
send messages to a queue, and consumers consume messa ges from it. Beyond this basic 
functionality , there are other considerations including performan ce, message delivery se¡
mantics , data detention , etc. The following set of questions will help clarify requirements 
and narrow down the scope. 
Cand idate : What 's the format and average size of messages? Is it text only? Is multi¡
media allowed? 
Inte rview er: Text messages only. Messages are generally meas ured in the range of 
kilobytes (KBs). 
Candidate : Can messages be repeat edly consumed? 
Intervie wer: Yes, messages can be repeatedly consumed by different consumers. Note 
that this is an added feature . A traditional distribut ed m essage queue does not retain 
a message once it has been successfully delivered t o a consumer. Therefore, a message 
cannot be repeatedly consumed in a tradi tional message queue. 
Candidate : Are messages consumed in the same order they were produced? 
Intervi ewer: Yes, messages should be consum ed in the same order they were produced. 
Note that this is an added feature . A traditional distribut ed m essage queue does not 
usually guarantee delivery orders . 
Candid ate: Does data need to be persisted and what is the data re tentio n? 
Inte rvi ewer: Yes, let's assume data retention is two weeks. This is an adde d feature. A 
traditional distributed message queue does not retain messages. 
Candi date: How many producers and consumer s are we going to support? 
92 I Chapter 4. Distributed Message Queue 


[Page 99]
Interv iewer : The more the bcller. 
Candidate: Wha t's the data delivery seman tic we need to support ? For example, al¡
most-once, at-least-once, and exactly once. 
Interviewer : We definit ely wan t t o support at-least-once. Ideally, we should support 
all of them and make them configm able. 
Candidate : What's the targe t throu ghput and end-to-end latency? 
Interviewer : It should support high throughput for use cases like log aggregatio n. It 
should also support low latency delivery for more traditional message queue use cases. 
With the above conversation , let's assume we have the followin g functional require¡
ments: 
ò Producers send messages to a message queue. 
ò Consumers consume messages from a message queue. 
ò Messages can be consumed repeatedly or only once. 
ò Historical data can be truncated. 
ò Message size is in the kilobyte range . 
ò Ability to deliver messag es to consumers in the ord er they were added to the queue . 
ò Data delivery semantics (at-least once, at-most once, or exactly once) can be config¡
ured by users. 
Non-functional requirements 
ò High throu ghput or low latency, configurabl e based on use cases . 
ò Scalable. The sys tem should be distributed in natur e. It should be able to suppo rt a 
sudden surge in message volume . 
ò Persistent and durab le. Data should be persisted on disk and replicated across mul ¡
tiple nodes. 
Adjustments for traditional message queues 
Traditional me sage queue like RabbitMQ do not have as trong a retention requirement 
as event streaming platfi rms. Traditiona l qu u r tain me sages in memory just long 
enough for them to b con um . Th y provid n-di k overflow capacity [1] which 
is several orders of magnitud mall r than th pa ity required for event streaming 
platforms . Traditional m g qu u d n t typica lly maintai n message ordering. The 
messages can be con um d in a diffi r nt ord r than they were produ ced. These differ¡
ences greatly simplify th d ign which w will discuss where appropriate. 
Step 2 - Propose High-level Design and Get Buy-in 
Fir t let di cu the basic functionalities of a message queue. 
Figure 4.2 how the key components of a message queue and the simplified inte ractions 
between the e components. 
Step 2 - Propose High -level Design and Get Buy-in I 93 


[Page 100]



[Page 101]
Producer ~a. pmd "c' 
- b2. consume - \ 
Consumer 
Message queue b1. subscribe _ j 
4 - -
l l 1 ll I I I I I I I I ; 
Figure 4.2: Key compon ents in a message queue 
ò Produ cer sends messages to a message queue. 
ò Consumer subscribes to a q ueue and consumes the subscribed messages. 
ò Message queue is a service in the middle that decouples the producers from the con¡
sume rs, allowing each of them t o opera te and scale ind ependently. 
ò Both pro ducer and consumer are clients in the client/server mod el, whil e the message 
queue is the server. The clients and servers communi cate over the network. 
Messaging models 
The most popular messaging models are point -to-point and publish-subscribe . 
Point-to-point 
This model is commonly found in traditional message queues. In a point -to-point model, 
a message is sent to a queue and consum ed by one and only one consumer. There can 
be multiple consumers waiting to consume messages in the queue, but each message can 
only be consumed by a single consumer . In Figure 4.3, message A is only consume d by 
consumer 1. 
Consumer 1 
Message A 
0 
Producer 
Message Queue 
. 0000000000 
Consumer2 
Figure 4.3: Point -to-point model 
Once the consumer acknowl edges that a messag i consum d, it is removed from the 
queue. There is no data retention in the point-to-point mod L In contrast , our design in¡
cludes a persistence layer that keeps the m ssag ~ r two weeks, which allows messages 
to be repeatedly consum ed. 
While our design could simulat e a point -to-point model, its capabiliti es map more natu¡
rally to the publish -subscrib e model. 
Publish-subscribe 
First, let's introduc e a new concept, the topic. Topics are the catego ries used to organize 
messages. Each topic has a name that is uniqu e across the entir e message queue service. 
94 I Chapter 4. Distributed Message Queue 


[Page 102]
╖-
Me sages arc sen t to and rrad from a sp<'rifir topic . 
In the publi. h-subscribe model , a message is srnt to a topic and rrcrivcd by the rnn 
. umers subscribi ng to thi topic. /\s shown in Figure tl.'1 , messa ge A is consume d hy both 
consum er 1 and con umer 2. 
Producer 
Message A 
~ 
Message A 
~ 
Consumer 1 
Message Queue 
~ ~ ~ ~ ~~ ~ ~~~ 
~ 
Message A Consumer 2 
Figure 4.4: Publish-subscribe model 
Our distributed message queue supports both models . The publish -subscrib e model is 
implemented by topics , and the point-to -point model can be simulated by the concept of 
the consumer group , which will be introduced in the consumer group section . 
Topics, partitions, and brokers 
As mentioned earlier, messages are persisted by topics. What if the data volume in a 
topic is too large for a single server to handle? 
One approach to solve this problem is called partition (sharding). As Figure 4.5 shows , 
we divide a topic into partitions and deliver messages evenly across partitions. 1hink 
of a partition as a small subset of the messages for a topic. Partitions are evenly dis¡
tributed across the servers in the message queue cluster. These servers that hold parti¡
tions are called brokers. The distribution of partitions among brokers is the key element 
to support high scalability . We can scale the topic capacity by expanding the number of 
partitions. 
Topic-A 0000000 Topic-A D DD D D DD Partition-1 
Partition-2 
Figure 4.5: Partitions 
Each topic partition operates in the form of a queue with the FIFO (first in, first out) mech ¡
anism. 1his means we can keep the order of messages inside a partition. The position of 
a message in the partition is called an off set. 
When a message is sent by a producer , it is actually sent to one of the partit ions for 
the topic . Each message has an optional message key (for example, a user 's ID), and all 
messages for the same message key are sent to the same partition. If the message key is 
absent , the message is randomly sent to one of the partitions . 
Step 2 - Propose High-level Design and Get Buy-in I 95 


[Page 103]
When a consumer subscribes to a topic , it pulls da tfl from one or more of llw <;<' P'1rl1l1(1nòi 
\AThrn there arr multiple consumers subscribing lo a topic , c<ich co nsumer is rC'sponsihlr 
for a subset of the par titions for the lopic. 'DH' cons umers rorm a consumer gJ'oup for 
a topic . 
1he mes age queue cluster with brokers and par lil ions is rep rcscn lc<l in Figure 4.6. 
Broke rs 
ProducòIB ~ ~~a prnducò ~ [ J[ lUIJUf llJ 
__ b1. subscribe -{ 
b2. consume -I 
Consume rs 
--- -
D[JODDUll 
~r-"-----::-
Figure 4.6: Message queue cluster 
Consumer group 
As mentioned ear lier, we need to support both point -to-point and subscribe -publish mod¡
els. A consumer group is a set of consumers , working together to consume messages 
from topics. 
Conswner s can be organized into groups . Each consumer group can subscribe to multiple 
topics and maintain its own consuming offsets. For example , we can group consumers 
by use cases, one group for billing and the other for accounting. 
The instances in the same group can consume traffic in parallel , as in Figure 4. 7. 
ò Consumer group 1 subscribes to topic A. 
ò Consumer group 2 subscribes to both topics A and B. 
ò Topic A is subscribed by both consum er groups -1 and group -2, which means the 
same message is consumed by multiple consumers . This pattern supports the sub¡
scribe /publish model. 
Topic-A 
Partition-1 0 0 0 
Consumer group -1 
- ---- - ;-....( Consumer-1 
' ' 
Partition-2 0 DD o--~---r--.~onsumer-2 
'-- -- ---- ----------J 
Consumer group-2 
Topic-8 Partition-1 0 D 0 D 0 0 0 Consumer -3 
Consumer-4 
Figure 4.7: Consumer groups 
However , there is one problem . Reading data in parallel improves the throughput , but 
96 I Chapter 4. Distributed Message Queue 


[Page 104]
the consumption order of messages in the same par tition cannot be guara nteed. For 
examp le, if Cons umer-1 and Consumer -2 both read from Partilion -1, we will not be able 
to guarantee the message consumpti on order in Par tilion -1. 
The good news is we can fix this by addin g a constraint , that a single partiti on can only 
be consum ed by one consumer in the same group . If the numb er of consumers of a group 
is larger than the number of partitions of a topic, some consumers will not gel dat a from 
this topic. For exam ple, in Figure 4.7, Consumer-3 in Consumer group -2 cannot consume 
messages from topi c B becau se it is consumed by Consumer-4 in the same consumer 
gro up, already . 
With this constraint , if we put all consumers in the same consumer gro up, then mes¡
sages in the same partition are consumed by only one consumer , which is equival ent to 
the point -to-point model. Since a partition is the smallest storage unit , we can allocat e 
enough p artitions in advance to avoid the need to dynamical ly i ncrease the number of 
partitions. To hand le high scale, we just need to add consumers . 
High-level architecture 
Figure 4.8 shows the updated high-level design . 
; Metadata storage 
: [--:J 
Brokers 
Data storage 
r -
l 1 J I ~LUU ' 
Producers 
State storage 
Coordinat ion 
service 
,--
Consumers 
(Consume r groups) 
╖ 1 ur 4. : Hi h-1 I d ign 
lien ts 
ò Produ c r: u h m t 
ò on um r r oup: ub ri t p1 ╖ n n um m s. 
ore ervi e and torag 
ò Brok r: h ld multi pl part iti n . A p rlit i n h Id a ubs t of messages for a topic. 
ò tora : 
o Data tora 
Step 2 - Propose High-level Design and Get Buy-in I 97 


[Page 105]
o St<1 te storage: consumer stales arc mana ged by st al e stornp;c. 
o Metadata storage: configuration and prop erties of topi cs arc p<'rsiste<l in meta. 
data storage . 
ò Coord inati on service: 
o Service discovery: which brokers are alive. 
0 Leader election: one of the brokers is selected as the ac tive controller. There is 
only one active controll er in the cluster . 11.1e active controll er is respo nsible for 
assigning partitio ns. 
0 Apache ZooKeeper [2] or etcd [3] are common ly used to elect a controll er. 
Step 3 - Design Deep Dive 
To achieve high throughput while satisfying the high d ata retention requirement , we 
made three important design choices, which we explain in detail now. 
ò We chos e an on-disk data structure that takes advantage of the great sequential ac¡
cess performance of rotational disks and the aggressive disk caching strategy of mod¡
ern operating systems. 
ò We designed the message data structur e to allow a message to be passed from the 
producer to the queu e and finally to the consumer, with no modifications . 1his mini¡
mizes the need for copying which is very expensive in a high volume and high traffic 
system. 
ò We design ed the system to favor batching . Small VO is an enemy of high through¡
put. So, wher ever possible, our design encourages batching. The producers send 
messa ges in batches . The message queue persists messages in eve n larger batches. 
1he consumers fetch messages in batches when possible, too. 
Data storage 
Now let 's explore the optio ns to persis t messages in more detail. In order to find the best 
choice , let 's conside r the traffic pattern of a message queue. 
ò Writ e-heavy, read-heavy . 
ò No upd ate or delete operations . As a ide note , a traditional mess ge queue does not 
persist messages unless the queue falls behind , in which ca e ther e will be .. deleteò 
operations when the queue catches up. Whal w ar I lkin g b ut h re i the per¡
sistence of a data streaming platform. 
ò Predominantly sequential read/write ace ss. 
Option 1: Database 
The first option is to use a database . 
ò Relational database: create a topic table and write messa ges to the table as rows. 
98 I Chapter 4. Distri buted Message Queue 


[Page 106]
ò NoSQL data base: crea te a collection as a topic ~rnd write mrss::igrs ::lS document s. 
Databases cru1 handle the storage requiremen t, hut they circ' not idea.I hecau sc ii is hard 
Lo de ign a database that suppor ts both write -heavy and read -heavy access pattern s <1t 
a large scale. Th e database soluli on d oes not fit our specific da ta usage pallerns very 
well. 
TI1is means a dat╖abase is not the best choi ce and could become a bolllencck of the sys¡
tem . 
Option 2: WrHe-al1ead log (WAL) 
The second option is write -ahead log (WAL). WAL is just a plain file where new entri es 
are appended to an app end -only log. WAL is used in many systems , such as the redo log 
in MySQL [ 4] and the WAL in ZooKeeper . 
We recommend persisting messages as WAL log files on disk. WAL has a pure sequential 
read /write access pattern . The disk performance of sequential access is very good [5]. 
Also, rotational disks have large capacity and they are pretty affordable. 
As shown in Figure 4.9, a new message is appended to the tail of a partition, with a 
monotonically increasing off set. The easiest option is to use the line number of the log 
file as the offset. However , a file cannot grow infinitely, so it is a good idea to divide it 
into segments. 
With segments, new messages are appended only to the active segment file. When the 
active segment reaches a certain size, a new active segment is created to receive new 
messages , and the currently active segment becomes inactive, like the rest of the non¡
active segments. Non-active segments only serve read requests. Old non-active segment 
files can be truncated if they exceed the retention or capacity limit. 
Topic-A Partition -1 
1st record 
l 
I l i I 
0 1 
I 
2 I 3 4 I 5 6 
I I I I I 
~--
7 8 9 10 11 12 13 
Next record written 
' ' ' 
14 : 
' ' ' 
J __ , 
' ' ' 15 : 
f-+-----------------segment -1 ╖ - - - - - - - - - - - - - -- - -.\ò - - - - -- - - - - - ╖ segment-2 --- - - - - - - - -.j 
Figure 4. 9: Append new messages 
Segment files of the same partition are organized in a folder nam ed Pa rti ti on-{: pa rti 
tion_id}. The structure is shown in Figure 4.10. 
Step 3 - Design Deep Dive I 99 


[Page 107]
/roplc -A 
1 Partition-1 Partltlon -2 
I l I 1 
I I segment-11
1 
segment -2 l 
I , , . 
[ segment-3 l [ . .. J 
I segrnent~ 1 1 / segmen l-2 j 
I 
l f I . 
segment -3 l . . . j 
Figure 4.10: Data segment file distributio n in topic partitions 
A note on disk performance 
To meet the high data retention requirement, our design relies heavily on disk drives to 
hold a large amount of data. 1here is a common misconception that rotational disks are 
slow, but this is really only the case for random access. For our workload, as long as we 
design our on-disk data structure to tal<e advantage of the sequential access pattern , the 
modern disk drives in a RAID configuration (i.e., with disks striped together for higher 
performance) could comfortably achieve several hundred MB/sec of read and write speed. 
This is more than enough for our needs, and the cost structure is favorable. 
Also, a modern operating system caches disk data in main memory very aggressively, so 
much so that it would happily use all available free memory to cache disk data . The WAL 
takes advantage of the heavy OS disk caching, too, as we described above. 
Message data structure 
The data structure of a message is key to high throughput. It defines the contract between 
the producers , message queue, and conswners. Our design achieves high performance 
by eliminating unnecessary data copying while the messages are in transit from the pro-
ducers to the queue and finally to the conswners . If any parts of the system disagree on J 
this contract, messages will need to be mutated which involves expensive copying. It 
could seriously hurt the performance of the system. 
Below is a sample schema of the message data structure: 
Field ame 
key 
value 
topic 
partition 
off set 
time stamp 
size 
ere 
Table 4.1: Data ch ma of am g 
100 I Chapter 4. Distributed Message Queue 


[Page 108]
Message key 
The key of the message is used lo determine the par tition of the message. If the key 
is not defined , the partition is random ly chosen . Otherwi se. the partition is c hosen by 
has h( key) % numPart itio ns. If we need more fl exibility. the producer can define ils own 
mapping algor ith m to choos partiti ons. Please note that the key is not equiva lent to the 
partition number. 
The key can b e a s trin g or a numb er. It usually carries some business informa tion . The 
parti tion numb er is a concept in the message queue, which should not b e explicitly ex¡
posed to clients. 
With a prop er mappin g algorithm , if the numb er of parli tions change s, messages can still 
be evenly sent to all the partitions. 
Message value 
The message value is the payload of a message. It can be plain text or a compressed 
binary block. 
Remind er 
The key and value of a message are different from the key-val ue pair in a key-value 
(KV) store . In the KV store , keys are uni que, and we can find the value by key. In 
a message, keys do not need to be unique . Somet imes they are not even m andatory, 
and we don 't need to find a value by key. 
Other fields of a message 
ò Topic: the name of the topic that the message belongs to. 
ò Partition : the ID of the partition that the message belongs to. 
ò Offset: the position of the message in the partition . We can find a message via th e 
combination of three fields: topic, partition , offset. 
ò Times tamp: the times tamp of when thi s message is stored. 
ò Size: the size of this message . 
ò CRC: Cyclic redundan cy check (CRC) is used to ensure the integrity of raw data . 
To support additio nal feature , some optional fields can b added on demand. For exam¡
ple, messag es can be filtered by tag , if tags are part of the optional fields. 
Batching 
Batching is per asi e in thi d ign. W b at h m sag in the producer , the consumer , 
and the message queue its lf. atching i criti cal to th p rformance of the system. In 
this section we focu primaril y o n batchin g in th m age queue. We discuss batching 
for producer and consum er in more d tail, shortly. 
Batching is critical to improvin g p r forrnan ce because: 
Step 3 - Design Deep Dive I 101 


[Page 109]
ò ,, ll ' I hr òJ 1 r<i'inr '' <.11 nl ,, rrr 'llP Ill(<.~ lf'I < lnpr thr r 11' I 
"lfl╖I :-ii╖~ ,tt 17rc. th1 n1q nt rvprnqu nrl" nrk rrn11vl trip.: 
,, 
ò n1r h~nh I ~TllC<: mrc.c:agrt. I<' !hr :-ipprnd lnp.:c: !Tl L:ngr ( h1111ki; \\ li1r h 1, 1,jq I I I 
:It hind<: 111 <:l'q11rnl1~l \\╖Tit( c; :md lflrp.:n 1 nnhp.:111111<; hlo< kc; n( rl1<:k r M Ii<╖ rn~ll'lf╖ò I'> 
' ~ttt~~ ò 
the nrrrnlmg "' c:trm T\oth lr;:id In mnrh p.rratn c;c1p1<'nt1;1I d1c:k "H r<╖c:~ thrr,,, h 
~ ~╖11 
lhrrr 1c: R trndrnfl he IW( <'n th rnng hput anrl latrnry. Tf thr c;vc:t<'rn 1<; drpl nyrd ~q a 
. ò t I r~╖lr t 1nna I mt c;c:RE!C' q11rm╖ whrn╖ latrnrv 1mght hr morr 1 mport ant. t rH' <\VC:t<╖m rnul d ht' 
' . . . "'"" l 10 11c;1 R c.mrillt r hatch c;i7<' Drc:k prrforman rr will s11ffrr a httlr hit in this ll'\r c 
h f 
;i~,. ╖r !tm1╖rl fc11 thrrnwhput. there might nf'rd to hr a higher num rr o p::irtit1ons prr to 
╖' p1r In 
mah╖ up for thr c.lowrr <;rqurnl1al disk write throughput. 
Sn far. v.╖e ╖n ro \'Crrd the mam d1c;k storage subsystem and its associated on disk d 
~trnrturr Now )rt' s w.1trh gears and discuss the producer and consum er flows. Th:ii~ 
we╖ will come back and finish the deep dive into the rest of th e message queue . rn 
Producer flow 
If a producer wants to send messages to a partition , which broker shou ld it connect t , 
The first option is lo introduce a rou tin g layer . All messages sent to the routing fayer 0 
routed to the "correct " broker. If the brokers are replicated , the "correct " broker is ~e 
leader replica. We will cover replication later. e 
l_ 
Producer - --1 
~.-- --
c=-Routing 
~~,~~~~~~~~~~ 
1 
Broker-1 
, , , , 
I - -- - - --
Broker-2 
Figure 4.11: Routing layer 
As shown in Figure 4.11 , the producer tries to send messa ges to Partition-1 of Topic¡
A. 
1. The producer sends messages to the routing layer . 
2. The routing layer reads the replica distribution plan 1 from the metadata storage and 
caches it locally. When a message arrives , it routes the message to the leader replica 
of Partition-1, which is stored in Broker -1. 
1
The distribution of replicas for each partition is called a replica distribution plan 
102 I Chapter 4. Distributed Message Queue 
't╖ 
I 
., 


[Page 110]
3. 111e lead er r eplica receives lhc message a nd follower rc pli c<1s pull cl ala from I he 
leader . 
4. When "enough " replicas have synchroni zed the message , th e leader com mil s the daln 
(persisted on disk) . which mean s the dala can be consumed. 'lhen i l respond s lo th e 
producer. 
You migh t be wondering why we need both leader and follower replicas. TI1e reaso n 
is faul t tolerance. We dive deep into this process in Lhe "In-sync repli cas" sec tion on 
page 113. 
This approac h wor ks, but it h as a few drawbacks : 
ò A new routing layer mean s additional networ k latency caused by over h ead and ad¡
ditional network h ops . 
ò Request batchin g is one of the big drivers of efficiency. This design d oes n 't take t hat 
into con sidera tion. 
Figure 4.12 shows the impro ved design. 
Producer 
,- - ---- ╖-- -
I 
I 
I 
Buffer 
Routing 
- ~ 
, '¡
I 
I Top-ic--A 
I
J Partition - 1 ..,..,......, .... 
Broker-1 
L--
- -- - -;~;~~:~- i 'l,r;riri-0-J 
Partrtion-1 Jl 
Broker-2 
Figure 4.12: Producer with buffer and rou ting 
The routin g layer is wrapped int o the produc r and a bu~ r compone n t is added lo the 
pro ducer. Both can be installed in th produc r as part of th producer cli nt Library. This 
change brings several ben fi : 
ò Fewer n twork hop m an J w r lat nc . 
ò Prod ucers can ha th ir own logic to d l rmin whi h partiti nth m ag should 
be sent to. 
ò Bat hing buff er ag in m m or nd nd ul larg r t che in a ingle re-
throughput. 
The choi e of th bat h i z i a cl ic trad off b tween throughput and latency (Figure 
Step 3 - Design Deep Dive I 103 


[Page 111]
4. 13). \Vit h a large bat ch size, th e throughput increases but late ncy '" higher, due 
a longer wail time to accumul ate th e bat ch . Wilh a small bat ch size , requests arc lo sent 
soo ner so the latency is lower, bnl lhrou ghput suffers . Produ cer s can lun e the batch . 517(' 
base d on use cases . . 
Latency 
High 
, , , , 
, , , , 
Low 
Consumer flow 
, , , , , , , , , , 
, , , , , 
, , , , 
, , 
, , , 
, 
, , , , 
, , , , 
, -:f Batch size 
High 
Figur e 4.13: The choice of the batch size 
Throughput 
The consumer specifies its o ffset in a partition and receives back a c hunk of events be¡
ginning from that position . An exampl e is shown in Figur e 4.14. 
consumer 1: 
last consumed offset " 6 
Iò --╖ Consumer 1 consumed -- -
0 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
I+------------------- Consumer 2 oonsumed 
C01'1$UmOl'2 
t consumed off 1 ò 13 
Figu re 4.14: Co nsumer flo\ 
Push vs pull 
An important question to answer is wh cth r brokers hould push dnla to consum ers, or 
if consumers should pull data from the brokers. 
Push model 
Pros: 
104 I Chapter 4. Distributed Message Queue 
' .ò 
' I 
' I 


[Page 112]
-
ò Low latency. 'TI1c broker cru1 push messrigcs lo lhr cnnsuincr imm rd iri tely up on re¡
ceiving Lhrm. 
Cons: 
ò If the ra te of consumpti on falls below Lhe ralc of p roduction, consumers c ould b e 
overwh elmed . 
ò It is difficult to deal with consum ers with diverse pro cessing power because the bro¡
kers control the rale at which data is transferred. 
Pull model 
Pros: 
ò Consumers control the consumption rate . We can have one set of consumers process 
messages in real-time and another set of consumers process messages in batch mode . 
ò If the rate of conswnption falls below the rate of production, we can scale out the 
consumers , or simply catch up when it can. 
ò The pull model is more suitable for batch processing . In the push model , the broker 
has no knowledge of whether consumers will be able to process messages immedi¡
ately. If the broker sends one message at a time to the consumer and the consumer 
is backed up, new messages will end up waiting in the buffer. A pull model pulls 
all available messages after the consumer 's current position in the log (or up to the 
configurable max size). It is suitable for aggressive batching of data. 
Cons: 
ò When there is no message in the broker, a consumer might still keep pulling data, 
wastin g re o urces. To overcome this issue, many messag e queues support long 
polling mode, whi ch allow pulls to wait a specified amount of time for new messages 
[ 6]. 
Based on the e considerations . mo l mes ag queues choose the pull model. 
Figure 4. 15 hows the workflow of the ons umer pull model. 
Step 3 ò Design D eep D ive I 105 


[Page 113]
Consumer A Coordinator 
r 
' :----- 1n. Heartbeat ~╖m A in the group) __ ., 
._ ___ 1b. Heor1beot acked ___ ___, 
' 
Consumer 0 
' ' :- 2. JolnGroup (I'm B. I want to join) --! 
I 
, 3a. Heartbeat (I'm A In the group) , 
I I 
;.._ 3b Hear1beat (Sorry A, group needs 1 
ò to rebalance. Please rejoin) ----; 
I I 
I I 
'--- 4a JolnGroup (I'm A. I want to join group) - : 
I 
4b JoinGroup (A Joins group success fully. ___; 
You are a follower) ò 
5. SyncGroup (Wait for the 
leader to dispatch partitions) 
:__ 4b. JolnGroup (8 joins the group success fully . ._. 
: You are the leader. Group members : A, 8) : 
I 
I 
I I 
:..- 5. SyncGroup (partition dispatch plan) ---{ 
I 1 I 
:+- 6 SyncGro up (A should consume partition 1, 3) -{ 
I I I 
; I- G. SyncGroup (8 should consume part1t1on 2, 4) +: 
r---~: --- I I 
Con sumer A Coordinator I Cons~~ 
Figure 4.18: New consumer joins 
1. Initially , only C onsumer A is in the group . It consume s all the partition s and keeps 
the heartb eat with the coordinat or. 
2. Consumer B sends a request to join the group. 
3. The coordina tor knows it's time to rebalance, so it notifies all the consumers in the 
group in a passive way. When Consum er A's hear tbeat is received by the coordinator, 
it asks Consumer A to rejoin the group . 
4. Onc e all the consumers have rejoined tJ1e group , the coordin ator chooses one of thern 
as the leader and inform s all the consumers about the elec tion r esull. 
5. The leader consumer generates the partition dispatch plan and sends it to the coor¡
dinator . Follower consumers ask the coordin ator about the par tition dispatch plan. 
6. Consumers start consuming messages from newly assigned partitions. 
Figure 4.19 shows the flow when an existing Consumer A leave th e group. 
108 I Chapter 4. Distributed Message Queue 


[Page 114]
1 
Consumer A Coordinator Consume r 8 
~-- 1 a Heartbeat (I'm A In the group) ----
,.__ _ ___ 1 b. Heartbeat acked ___ _ ___, 
:.,. _ _ 1 a. Heartbeat Wm B in the group) - ----. 
I 
: ;-1 ----- 1 b. Heartbeat acked - --- -
~ 2a. LeaveGroup (I'm A in the group. I quit) - ...-! 
I I 
I 
~--- 2b. LeaveGroup (goodby e A) ---~ 
:.,. __ 3a. Heartbeat (I'm B In the group) , 
, 3 b. Heartbeat (Sorry B, group needs -.! 
:- to rebalance. Please rejoin) : 
I I 
I J ò )_______l :- 4a. JolnGroup (I'm B. I want to 01n : 
: 4b. JoinGroup (B joins the group success fully. ~ 
r-- You are the leader. Group members : B) : 
I I 
I I 
i-5. SyncGroup (partition dispatc h plan) ----: 
: 6. SyncGroup (B should 
consume partition 1, 2, 3, 4) 
Consumer A Coordinator Consumer B 
Figure 4.19: Existing consumer leaves 
1. Consumer A and B are in the same consumer group. 
2. Consumer A needs to be shut down , so it requests to leave the group . 
3. The coordinator knows it's time to rebalance . When Consumer B's heartbeat is re¡
ceived by the coordinator , it asks Consumer B to rejoin the group. 
4. The remaining steps are the same as the ones shown in Figure 4.18. 
Figure 4.20 shows the flow when an existin g Consumer A crashes . 
Step 3 - Design Deep Dive I 109 


[Page 115]
Consumer A Coordinator 
1 
~ 1 a Henrtbeat O'm A In 1110 group) __ ., 
- --- l b. Heartbeat acked ___ __, 
2. No heartbeat from consumer A. 
Consumer A seems 
to be lost. Need to rebalance 
- -- l a. Heartbeat (I'm B In the group) _ ~ 
' ,__ ___ 1 b. Heartbeat acked -----.. 
' ' ' ' 
- -- 3a. Heartbeat (I'm Bin the group) ---J 
3b. Heartbeat (Sorry B, group needs 
:-- to rebalance . Please rejoin) 
I 
I I 
:- 4 a. JoinGroup O'm B. I want to join group) -l 
: 4b. JoinGroup (B joins the group success fully. : 
;---- You are the leader. Group members : B) ..., 
:- 5. SyncGroup (partition dispatch plan) ~ 
: 6. SyncGroup (B should 
consume partition 1, 2, 3, 4) I 
I 
,----._ 
Consumer A Coordinator Consumer B 
Figure 4.20: Existing consumer crashes 
1. Consumer A and B keep heartbeats with the coordinator. 
2. Consumer A crashes, so there is no heartbeat sent from Consumer A to the coordina¡
tor. Since the coordinator doesn't get any heartbeat signal within a specified amount 
of time from Consumer A, it marks the consumer as dead. 
3. The coordinator triggers the rebalance process. 
4. The following steps are the same as the ones in the previous scenario. 
Now that we finished the detour on producer and consumer flows , let's come back and 
finish the deep dive on the rest of the message queue broker . 
State storage 
In the message queue broker, the state storage stores: 
ò The mapping between partitions and consumers . 
ò The last consumed offsets of consumer groups for each partition. As shown in Figure 
4.21, the last consumed offset for consumer group -1 is 6 and the offset for consumer 
group-2 is 13. 
110 I Chapter 4. Distributed Message Queue 


[Page 116]
consumer group 1 ╖ 
last consumed offset 6 
Iò ---- group -1 consumed Topic A Partition 1 
0 I 2 3 I 4 5 I 6 I 7 I 8 9 10 11 12 13 14 15 
I I I I 
I ~╖ --------------------- group -2 consumed ╖ - - - - - - - - - - - - - - - - - - - - - - òt 
consumer group -2: 
last consumed offset = 13 
Figui-e 4.21: Last consumed offset of consumer groups 
Fore ample, as shown in Figure 4.21, a consumer in group -1 consumes messages from 
the partiti on in sequence and commit s the consumed offset 6. This means all the messages 
before and at offset 6 are already consumed. If the consumer crashes, another new con¡
sumer in the same group will resume consumpti on by reading the last consumed offse t 
from the state storage. 
The data access patt erns for consum er state s are: 
ò Frequent read and writ e operation s but the volume is not high. 
ò Data is updated frequently and is rarely deleted. 
ò Random read and write operations. 
ò Data consistency is important. 
Lots of storage solutions can be used for storing the consumer state data. Considering the 
data consistency and fast read /write requirements, a KV store like ZooKeeper is a great 
choice. Kafka has moved the offset storage from ZooKeeper to Kafka brokers . Interested 
readers can read the reference material [8] to learn more. 
Metadata storage 
The metadata storage stores the configmat ion and properties of topics, including a num¡
ber of partitions , retention period , and distribution of replicas. 
Metadata does not change frequently and the data volume is small, but it has a high 
consistency requirement. ZooKeeper is a good choice for storing metadata . 
ZooKeeper 
By reading previous sections , you probably have already sensed that ZooKeeper is 
very helpful for designing a distributed message queue. If you are not familiar with 
it, ZooKeeper is an essential service for distributed systems offering a hierarchical 
key-value store. It is commonly used to provide a distributed configuration service , 
synchronization service , and naming registry [2]. 
ZooKeeper is used to simplify our design as shown in Figure 4.22. 
Step 3 - Design Deep Dive I 111 


[Page 117]
ZooKeepe r 
Metadala Storage State Storage 
l 
Brokers 
Producers Data Storage 
I JlJI )[ 111' l~ I 
II' 
I! 
t 
Coordina tion 
service 
Figure 4.22: ZooKeeper 
Let 's briefly go over the change . 
ò Metadata and state storage are moved to ZooKeeper . 
Consumers 
(Consumer Groups) 
ò The broker now only needs to maintain the data storage for messages. 
ò ZooKeeper helps with the leader election of the broker cluster . 
Replication 
In distributed systems , hardware issues are common and can not be ignored . Data gets 
lost when a disk is damaged or fails permanently . Replicat ion is the classic solution to 
achieve high availability . 
As in Figure 4.23 each partition has 3 replicas , distribut ed a cross different broker nod es. 
For each partition , the highlighted replicas are the lead ers and the other s are followers. 
Producers only send me ages to the I ader repli ca. The followe r replicas keep pulling 
new messa ges from the leader. nee me ag are s rnchronized to e nough replicas, the 
leader returns an acknowledgment to the producer. e ' ill go into detail about how to 
define "enough" in the In- nc RepUc ction on p gc 11 3 . 
'--
Top6c-B 
Parbbon ╖ l 
. , ò 
I ' 
fagur 4.2 : R plic o n 
' r 
╖3 
The di tri bution of r plic for ch partill on 1 call~d r plic di tribution plan. For 
112 I Chapter 4. Distributed ~sage Qua1e 
;I' 


[Page 118]
' 
e. amp le. the replica distribution plan in Pigur<' 1. 2╖~ rrin hf' dcscrih<' d as : 
ò Par titi on-1 of Topic -A: :3 replicas, kfldcr i11 Broker 1 fo llowers in 8roker 2 and 3; 
' 
ò Partition -2 of Topic -A: ;3 replicas, leader in Brokr r-2, followers in Brok er-3 and 4; 
ò Partition -I ofTopic -B: :3 rep licas, leader in Broker-3, follower s in Brokcr -4 and I. 
Who mal es the replica distribution plan? IL work s as follows ; with th e help of the coor¡
rlinalion service , one of the broker nodes is e lected as the leader. IL generates the repli ca 
rli tribution plan and persis ts the plan in m etadata storage. All the broker s now can work 
according to the p lan. 
If ou are interes ted in knowing more about replications, check out "Chap ter 5. Replica ¡
tion " of the book "Design Data-Int ensive Appli cation s" [9]. 
In-sync replicas 
We mention ed that messages are persisted in multiple partitions to avoid sin gle node 
failure, and each partition has multiple replicas . Messages are only written to the leader , 
and follow ers synchronize data from the leader . One problem we need to solve is keeping 
them in sync . 
In-sync replicas (ISR) refer to replicas that are "in-sync " with the leader. The defi ¡
nition of "in-sync " depends on the topic configuration . For example , if the value of 
replica.lag .max.messages is 4, it means that as long as the follower is behind the leader 
by no more than 3 messages , it will not be removed from ISR [10]. The leader is an ISR 
by default. 
Let's use an example as shown in Figure 4.24 to shows how ISR works. 
ò The committed offset in the leader replica is 13. Two new messages are written to 
the leader , but not committed yet. Committed offset means that all messages before 
and at this offset are already synchronized to all the replicas in ISR. 
ò Replica-2 and replica -3 have fully caught up with the leader , so they are in JSR and 
can fetch new messag es. 
ò Replica -4 did not fully catch up with th leader within the configured lag time, so it 
is not in ISR. When it catches up again , it can be added to JSR. 
Step 3 - Design Deep Dive I 113 


[Page 119]
not caught up 
committed offset = 13 ' 
' 
ISR: {replica-1, replica-2, replica-3} 
' ' 
replica-? (followP-r) 
10 111 2 113 1'1 
I 
repllca -3 {follower) 
10 11 12 13 
replica-4 (follower) 
10 11 
Figure 4.24: How ISR works )~ 
h c I ,\I W Y do we need ISR? The reason is that ISR reflects the trad e-off between periormance 
and durability . If producers don't want to lose any messages, the safest way to do that is 
to ensure all replicas are already in sync before sending an acknow ledgment. But a slow 
replica will cause the whole partition to become slow or unavai lable. 
Now that we've discussed ISR, let's take a look at acknowl edgment settings. Producers 
can choose to receive acknowledgments until the k number of ISRs has received the 
m essage, where k is configurable. 
ACK=all 
Figure 4.25 illustrates the case with A K=all. With ACK=al1, the producer gets an ACK 
when all ISRs have received lhe me ag . Tiii mean it tak a longer time to send a 
messa ge because we need to wait for U1e lo\! st I R, but it gives the strongest message 
durabili ty. 
114 I Chapter 4. Distributed Message Queue 


[Page 120]
replica-1 'I ]1 ll follower I [ I J 
Broker-1 
Producer 
I 
' \ 
' 
1. produ ce \ 
2. fetch 
- 3╖ synced -- -Broker-2 
I 
ISR: {replica-1, replica -2}, ack=all 
Figure 4.25: ACK=all 
ACK=1 
replica-3 
follower 
not caught up 
Broker-3 
With ACK=l, the producer receives an ACK once the leader persists the mess age. The 
latency is improved by not waiting for data synchronization . If the leader fails immedi¡
ately after a message is acknowledged but before it is replicated by follower nodes, then 
the message is lost. This setting is suitab le for low latency systems where occasional data 
loss is acceptable . 
Producer 
\ 
fetch 
\ 
\ 
\ 
l replica-2 
I leader .... .,.. ....... 
Broker-1 - - ╖ synced - - - -Broker-2 
'--------------' '-- --- ------' 
ISR: {replica-1 , replica-2} , ack=1 
Figure 4.26: ACK= 1 
not caught up 
replica-3 ODO 
follower 
Broker-3 
Step 3 - Design Deep Dive I 115 


[Page 121]
ACK =O 
111c prod ucer I ecps sending messages lo lhe leader wilh oul wai tin g for m1y ;1('knowi 
cdg menl. and it never r etries. '.this method p rovides the lowes t latency nl the cost 
r I' I 11 1 ╖ '1f po tenti al message loss. TI1is setting might be goo d 1or use cases 1 <C' co re tng rnctric 
or loggi ng data since data volume is high and occas ional d ata loss is accep table. q 
replica-1 oonoo follower 1J 
Producer 
I 
1. produce 
without ack 
fetch 
r-:plica-2 
j . -
1 
leader w. .......... 
Broker-1 --. synced -- --Broker-2 
ISR: {replica-1, replica-2}, ack=O 
Figure 4.27: ACK=O 
Configurable ACK allows us to trade durabili ty for performance . 
not caught up 
replica -3 ODO 
follower 
----
Broker-3 
I 
Now let's look at the consumer side. 'foe easiest setup is to let consumers connect to a 
leader replica to consum e me age . 
You might be wonderin g if the lead r r eplica would b o en h elmed by this design and 
why messa ges are nol read from I R . Th r a on ar : 
ò Desi gn and operational implicit . 
ò ince mes age in on parhti n are di p 
sumer group, thi limit th num r f 
ò The num ber of conn ction 
topi c is not up r hot. 
ò If a topic i hot. w can 
nl n 
nn ti n th I 
on um r within a con¡
er r p lica. 
n t large as long as a 
r p titian and consumers. 
In ome cenario . r ding fr m th ~ r rcplk nught not b the best option. For 
e 'ample, if a consum r i l at d in differ nr d ll c nt r from th leader replica, the 
read performanc ~ r . Jn lhi c , it 1 w rthwhil to en bJe consum rs to read 
from th d o t I Rs. Int r l d r d r c n ch ck out the r fi renc matenaJ about th1S 
[11). 
I R i ery important. How do it d termin if a replica is I R or not? Usually, the leader 
116 I Chapter 4. Distributed Message Queue 
,, 
.f 1 I.( 
( 
' 
l' 
.~ 
r 


[Page 122]
for every partition tracks I he JSR list by cnmput ing lhr lag n( eve ry rcplicFI from ilscll' ff 
you are interested in detailed algorithms , you can rlnd the impl r mentations in rdc rcncr 
materials [12] [13]. 
Scalability 
By now we h ave made grea t progress desig ning the distributed message queue syst em. 
In the next step, let's evaluate the scalability of differe nt sys tem component s: 
ò Producers 
ò Conswners 
ò Brokers 
ò Partitions 
Producer 
The producer is conceptually much simpler than the consumer because it doesn 't need 
group coordination . The scalability of producers can easily be achieved by adding or 
removing producer instances . 
Consumer 
Consumer groups are isolated from each other , so it is easy to add or remove a conswner 
group. Inside a conswner gro up, the rebalancing mechanism helps to handle the cases 
where a consumer gets added or removed , or when it crashes. With consumer groups 
and the rebalance mechani sm, the scalability and fault tolerance of consumers can be 
achieved . 
Broker 
Before discussing calability on th broker ide, let' fu t consider the failure recovery of 
brokers. 
Step 3 - Design Deep Dive I 117 


[Page 123]
r'~~~~ ~ 11111111 
Top1c-B 
Partition 1 
Broker -1 
I To pic-B 0000000 
Lrtit i o::~ker-1 
Pa~~f ~~~~ 11111111 
Pa~~j~~~~ ODDO 
Pa~~j~~~~ DDDOOOO ---"'---=-
Broker- 1 
Topic A 
Partrtron 1 
Pa~~j~~ ~ 111111 fl 
Broker-2 
Pa~~j~~~~ lJ[Jf JI llJIJ[ J 
Broker -2 
Pa~~j~~~~ 11111111 
Pa~~fi~~~~ DODOO 
Broker-2 
Topic A 
Partition 1 
Topic A I 111 J 
Partltion -2 , I ' 
Pa~~t?~~~~ u 111111 
Broker 3 
I ' 
Broker-3 
Figure 4.28: Broker node crashes 
Topic A 
Partition ? 
Topic B 
Partitlon -1 
Broker-ti 
Topic-A f ][l ]' rtit ion-2 ' [, j 
Topic-8 ~ 
1 
rt ltio;~,~,~O~ 
Topic -A DD 
Partltion -1 
---
Topic -B lIIIIlil 
Partition -1 
Broker -4 ______ _, 
Let's use an examp le in Figure 4.28 to explain how failure recovery works . 
1. Assume there are 4 brokers and the partition (replica) distribution plan is shown 
below: 
ò Partition-1 of topic A: replicas in Broker -1 (leader) , 2, and 3. 
ò Partition-2 of topic A : replicas in Broker -2 (leader) , 3, and 4. 
ò Partition-1 of topic B: replicas in Broker -3 (leader) , 4, and 1. 
2. Broker-3 crashes, which means all the partitions on the node are lost. The partition 
distribution plan is changed to: 
ò Partition-1 of topic A: replicas in Broker -1 (leader) and 2 . 
ò Partition-2 of topic A: replicas in Broker -2 (leader) and 4. 
ò Partition-1 of topic B: replicas in Broker-4 and 1. 
118 I Chapter 4. Distributed Message Queue 


[Page 124]
3. Th bro! er contro ller delec ts Brok -r-3 is down and gencra lcs an w partition distri-
bution plan for th remaining broker nodes : 
ò Partition -I of lopic A: r p licas in Broker -1 (lrader) , 2, 8n<l 4 (new). 
ò Parlition -2 of topic A: replicas in Brokcr -2 (leader), 4, and 1 (new). 
ò Parti tion-I of topic B: replicas in Brok r-4 (leader), 1, and 2 (new) . 
4. 1h e new replicas work a followers and catch up wilh the leader. 
To make the brok er fault-tolera nt, here ar additi onal consideratio ns: 
ò The minimum numb er ofISRs specifies how many replicas the producer must receive 
before a mess age is consider ed to be successfully committe d. The higher the numb er, 
the safer. But on the other hand, we need to balance latency and safety. 
ò If all replicas of a partition are in the same brok er node , then we cannot tolerat e the 
failure of this node . It is also a waste of resources to replicate data in the same node . 
Therefore , replicas should not be in the same node. 
ò If all the replicas of a partition crash, the data for that partition is lost forever . When 
choosing the number of replicas and replica locations , there's a trade -off between 
data safety , resourc e cost , and latency . It is safer to distribute replicas across data 
centers, but this will incur much more latency and cost, to synchronize data between 
replicas. As a workaround , data mirroring can help to copy data across data centers, 
but this is out of scope. The reference material [I4] covers this topic. 
Now let's get back to discussing the scalability of brokers. The simplest solution would 
be to redistribut e the r plicas when broker nodes are added or removed. 
However , there is a better approach . The brok r controller can temporarily allow more 
replicas in the s stem than th numb r of r plicas in the config file. When the newly 
added broker catch up can r m o th on s that are no longer needed. Let's use 
an example a hown in Figur 4 .29 t un r tand th approach . 
Step 3 - Design Deep Dive I 119 


[Page 125]
.- - -----
Topic-A[]]]]]] 
Partltlon-1 
Topic-A , Li1!1 j[]Li J lj 
Partitlon-2 I 1 
Broker-1 
I - Topic-A[]]]]]]] 
Partition -1 
Broker-1 
Topic-A[]]]]]]] 
Partitlon-1 
Broker-1 
Topic-A r 01 "I ll If In I Partitlon-1 1 I J I 
Topic-A []]]]]]] 
l-
Partltion-2 
Broker-2 
Topic-A[]]]]]]] 
Partltion-2 
Broker-2 
Topic-A DDOOODD Partition-1 ' 
Topic-A []]]]]]] 
Partltion-2 
Broker-2 
Pa~ftf~~~~ l Ji JI JI II ii jj j 
Pa~ftf~~~~ [ J[ J[ JI Ill! J[ J 
Broker-3 
-
Broker-4 added , Partitlon-2 should be 
distributed In broker (2, 3, 4) 
Pa~ftf ~~~~ OODDrJDD 
Pa~~f ~~~~ DDDDDDD 
Broker-3 --- _____ ___, 
Pa~~f~~~~ oornu l 
, ___ Broker-4 J 
After the replica in Broker-~ catches up, 
remove the redundan t replica In Broker-1 
-----
Topic-A OOOODOJ l 
Topic-A DDOOOOO Partltion-1 
Topic-A OOOODDD Partltlon-2 _ __ Partrtron-2 
Broker-3 Broker-4 
Figure 4.29: Add new broker nod e 
1. The initial setup : 3 brokers , 2 partitions , and 3 replicas for each partition . 
2. New Broker -4 is added. Assume the broker con troller chan ges the replica distribu¡
tion of Partition-2 to the broker (2, 3, 4). The new repUca in Broker -4 starts to copy 
data from leader Broker-2. ow the numb er of replica for Partition-2 is temporarily 
more than 3. 
3. After the replica in Broker-4 catches up, Lh redundant parti tion in Broker-1 is grace¡
fully removed . 
By following this process , data loss while adding broker cnn b 
cess can be applied to remove broker a~ ly. 
Partition 
ided . A imilar pro-
For various operational reason s, such a scaling th topic . throughput tuning. balancing 
availability / throughput , etc., we may change th numb r of p rtitlons. When the num¡
ber of partitions changes, the producer will be noli i d er il communicates with any 
broker , and the consumer will trigger consumer r balancing . Therefore, it is safe for both 
the producer and consumer. 
Now let' s consider the data storage layer when the number of partitions changes . As in 
Figure 4.30, we have added a partition to the topic. 
120 I Chapter 4. Distributed Message Queue 


[Page 126]
~--..... ... ..... ..._ .... ..... -~. 
partltion-1 
partition-2 I 
Figure 4.30: Partition increase 
ò Persisted messages are still in the old partitions, so there's no data migration . 
ò After the new part ition (partition-3) is added, new messages will be persisted in all 
3 partitions. 
So it is straig htforwar d to scale the topic by increasi ng partitio ns. 
Decrease the number of partitions 
Decreasin g partiti ons is more compli cated, as illustrat ed in Figure 4.31. 
~------- - ---------------- - -- - ----------- -, 
i I Persisted messages 0 New messages 1 
I I 
partition -1 II I II I 00 partition-1 
partition-2 Ill 1110 0 partition-2 
-----------
partition-3 1 II 
rò r1r 1 
I I I 11 I 
paiiition-3 I I I 11 I 
I I I 11 I 
-' - .r- J 
-----------
Figure 4.31: Partition decrease 
ò Partition-3 is decommissioned so new messages are only received by the remaining 
partitions (partition-1 and partition -2). 
ò The decommissioned partition (partition-3) cannot be removed immediately because 
data might be currently consumed by consumers for a certain amount of time. Only 
after the configured retention period passes , data can be truncated and storage space 
is freed up. Reducing partitions is not a shortcut to reclaiming data space. 
ò During this transitional period (while partition -3 is decommissioned) , producers only 
send messages to the remaining 2 partitions , but consumers can still consume from 
all 3 partitions . After the retention period of the decommissioned partition expires , 
Step 3 - Design Deep Dive I 121 


[Page 127]
consumer groups nerd rclrn land ng. 
Data delivery semantics 
Now that we unders tand the differenl components of a dis tributed mcssng<' q11('uc╖, lrt' 
disrnss different delivery seman bcs: at-mos l once, at-leas l once, and exactly once. ~ 
At-most once 
As the name suggests, at-mosl once means a message will be delivered not more than 
once. Messages may be lost but are not r edelivered. This is h ow at-mos t once delivery 
works at the high level. 
ò Th e pro ducer sends a message asynchron ously to a topic with out waiting for an 
acknowledgment (ACK=O). If message delivery fails, there is no retry. 
ò Consumer fetches the message and commits the offset before the data is processed. 
If the consum er crashes just after offset commit , th e mess age will not be re¡
consumed . 
l - Messageq~ 
J.__ may lose msg - 0000000 - may lose msg 
~-----
-----
Producer 
Figure 4.32: At-most once 
It is suitable for use cases like monitoring metrics, where a small amount of data loss is 
acceptable. 
At-least once 
With this data delivery semantic, it's acceptabl to d liver a message more than once, but 
no mess age should be lost. Here is how it work at a high le el. 
ò Produ cer sends a mes age synchronou I or a nchronou I with a response call-
back, settin g ACK= I or ACK=all, to make ur m gc nr delivered to the broker. 
If the message delivery fail or lim out . lh produc r ill keep retrying . 
ò Consum er fetches the me ag and commit th off t onl after the data is success¡
fully processed. If the con umer fails to pro th mtò òò ~e. it v 111 re-cons ume the 
mess age so the re won 't be da tn lo s. nth olhrr h nd. if a con umcr processes the 
messag e but fails to commit th off: I to Lh br k r . th mr ge \ 111 b re-consumed 
when the consumer restart . r ultin g in dupli c t . 
ò A m essage might be deliver ed more th n one le> th br k r n co nsume rs. 
122 I Chapter 4. Distributed Message Queue 
t 


[Page 128]
Producer 
1--- may have 
dup licate 
Message queue 
I ! II l !i 1
1 
111 
Consumer 
Figure 4.33: AL-lcasl once 
Use ases: With at-leas t once, messages won 'l be Jost but the same message might be 
delivered multipl e times. Whil e not ideal from a user perspective, at-leas t once delivery 
sema nti cs are usually goo d enough for use cases where data dupli cation is not a big issue 
or dedupli cation is possible on the consum er side. For exampl e, with a uniqu e key in each 
me sage, a m essage can be rejected when writin g dupli cate data to the databa se. 
Exactly once 
E actly once is the most difficult delivery semantic to implement. It is friendly to users , 
but it has a high cost for the system's performance and complexity. 
Figure 4.34: Exactly once 
Use cases : Financial -related use cases (payment, trading , accounting , etc.). Exact ly once 
is especially important when dupli cation i s not acceptab le and the downstream servi ce 
or third party doesn 't supp ort id mpotenc . 
Advanced features 
In this section we talk bri efl r about om ad anced features, such as message filtering, 
delayed mess ages , and chedul d m e ag s. 
Message filtering 
A topic is a logicaJ ab tractio n that contains m ....... ,... ..... am type . Howeve r, some 
rtain ubtyp s. For examp le, 
rd r t a t pi . but th payme nt 
r fund. 
consum er group ma onl 
the ord ring t m 
tern onl car 
ò What if th r 
d dicat d t pi 
an th topic for the 
me n rn . 
w n d to build 
It i f ic . 
, ~ n t 
ry hm n w r n um r r uir m nt com , a the 
' tightJ C'OU } d. 
h thi r uirem nt using differ nt app roach . Luckily, m s-
S ep 3 ò Design Deep Dive I 123 


[Page 129]
------------
sage filtcrmg <'Otn<'S to th<.> rescue. 
A nain" solution for message filtering is that the consumer fetches th e full <;rt qf nl <'s<;iig<╖l 
and filters out unne cessary messages during pro cessing Lime. 1hi s approrich '" fl c╖xiblc¡
but introduces unnecessary traffic that will affect syst em perform ance. 
A better solution is to filter messages on the broker side so that con sum ers w ill only get 
messages the care about. Implementing this requires some careful consideration. If data 
filtering requires data decryption or deserialization , it will degrade the perf ormancc of 
the brokers . Additfonally. if messages contai n sensitive data , they should not be readable 
in the message queue. 
Therefore , the filtering logic in the broker should not extract the message payload. It 
is better lo put data used for filtering int o the metadata of a message , which can be 
efficiently read by the broker . For example, we can attac h a tag to each message. With 
a message tag, a broker can filter messages in that dimension. If more tags are attached, 
the messages can be filtered in multiple dim ensions . Therefo re, a list of tags can support 
most of the filtering requirements . To support more complex logic such as mathematical 
formulae, the broker will need a grammar parser or a script executor, which might be too 
heavyweig ht for the message queue. 
With tags attached to each message, a consum er can subscribe to messages based on 
the specified tag, as shown in Figure 4.35. Interested readers can refer to the reference 
mate rial [ 15). 
-, 
I subscribe with tags --.__; -- - -- - - . 
Tag 
filter '---
fetch messages 
Consum er 
Broker 
Figure 4.35: ie age filt ring b tag 
Delayed messages & schedu(ed messages 
Sometimes you w ant to dela th dehv ╖ of m lo con um r for pecificd 
period of time. For example, an ord r hould bed d tf not p td w1lhm ;U) 1n1nutes afttr 
the order is created. A delayed venfi hon m {(~ (rh ck af tht' p ymE"nt t compltltd) is 
sent immediat ely but is delive-red to th consumrr 0 nunult' I 1ta Wht>n tht con umn 
receives the message. il chec the paym nt t tu . J thr pnymrnt a n t compldtd . tht 
order will be closed. 0th rwi . the me ~e wtU a~nort'd 
Differen t from sending mslant m g . Wl' ~ to ttmpora.ry 
storage on the broker ide mste d of to lhr t pie 1m Ja tel ò. d th~n d~Lvtr them to 
the topics when time's up. The h1fth╖J~ Id tgn for l}us a sho n tn fagure 4.36. 
124 I Chapter 4. Distributed Message ~ 


[Page 130]
I 
I I 
Produ cer 
/ 
delayed messages ,. ' 
I 
Temporary 
storag e 
, 
~ deliver when - ò 11111 \IJrJ , time's up __.:: 1_! t I 
I ' Broker - _J 
L._ ______ _ 
Figure 4.36: Delayed messages 
Core components of the s stem include the temporary storage and the timing func¡
tion. 
ò The temporary storage can be one or more special message topics. 
ò The timing function is out of scope, but here are 2 popular solutions: 
o Dedicated dela queues with predefined delay levels [16]. For example , Rock¡
etMQ doesn 't support dela ed messages with arbitrary time precision , but de¡
layed messages with specifi c le els are supported . Message delay levels are ls, 
5s, 10s, 30s lm 2m, 3m, 4m, Gm, m, 9m, lOm, 20m, 30m, lh, and 2h. 
o Hierarchical time wheel [1 7]. 
A scheduled me age means a m age hould be delivered to the consumer at the sched¡
uled time. The overall de ign i very imilar to delaye d messages. 
Step 4 - Wrap Up 
In this chapter . have pre nted the d ign of a distribu ted message queue with some 
advanced features rommonJ found in d la trearning platfo rms. If there is extra time at 
the end of the intervi ò here are m additional taJkjng points: 
ò Protocol : it d fin 
transfer data ~..,,ru_"" 
hould b abl to: 
0 0 
0 
tax. d API on h to exchange informatio n and 
. In di tribut d m queue, the protoco l 
mpti n, h lb at, etc. 
uing Protocol (AMQP) [18] 
Step 4 , Wrap Up I 125 


[Page 131]
ò Rel n ╖ cnnc;11mp1 ion. If some mrssrtgrs rn 1111<>t hr ro11<.;1111wd <.; tJ< '<'f' <.,<;f idl y Wr╖ 
'''r╖rj to retry the Oj)Crnlion . ln order not lo hlnrk incom ing mcssagn . how C";111 Wr╖ 
╖ r1╖1 the oprra1ion after ;:i cer tain limr period ? One idr;.i is lo se nd f'ailcd 111ròc.;<; agc╖ ~ ,,:Y 
dedicated retry topi c. so they can be co nsumed l<l lrr. ~ 
ò Historical data archive. Assume there is a lim e-based or capaci ty-based log rC'lcnu 
mechanism. If a consumer needs lo rep lay some hislorica l messages lh al arc ah<t:;n 
truncated, how can we do it? One possib le soluli on is lo use sloragc systems \ii yh 
l l . . l It arge capaci ties, such as HDFS (20 J or object storage, to store uslonca data. 
Congra tul atio ns on getting this far! Now give yours elf a pa t on th e back. Good job! 
126 I Chapter 4. Distributed Message Queue 


[Page 132]
Chapter Summary 
step 1 
step 2 
Message Qyeue 
lep 3 
ep4--
prod1wcrn sr11d mr~sngrs to m~g q11r11r 
consumers ro nsumr messl'lgr11 from th <' msg queue 
r1111clioJ1al rcq 
messagrs con be repea ted ly consumrd 
message orde ring 
. . L oonflgurnb l< thrnughput aod lot<noy 
non-funotoonò I "q ~ .oo loble 
persistent and durab le 
< 
point-to-point 
message models 
publish-subscribe 
topics, partition s, brokers 
producer 
consum er consumer group 
high-level design 
< 
data storage 
broker 
state storage 
metadata storage 
data storage 
coordination service 
message data structure 
mtr rtb 
< push model 
pull model 
In 
mAOl ~ ::: t onoe 
pup e ctJy once 
Chapter Summary I 127 


[Page 133]
..... 
╖ .-'-ò'-╖ . ..,., ._òtrò """ nHi1tmqtiim m.~xkn~th html 
\;--..: "'- ò : ...._, f't"l'llt ò \\ ! lpt"\hl\ http< rn w1k1pt drn cirg w1k1 1\p~' J I v,, ;_,.. 
,, ò Lò . 
. . * 
' . -J. . 
ò rull I~-
nd 1t'ffiNY pcrfonnanct' . httpc;. dchvrrvim;igt>~ ;urn '''1. 11 
- .a taC'\ b ~-JP!! 
at a arache .org docume ntation =dcsign_pull. 
a 2 il _ :'1..-i.u...~tatll. n httr s kafka.apac he.org 20 documentation .htmlòum-v, 
me;-\."'\: iip: 
ò ò ò - :a _ -, i."-df'C- e\}UJI"eS Z0cii\eeper. https : towardsd atasci ence.com 'Jr..afh-rj(, 
k-~-ei--~es-z ... ╖eeper- ebfui3 62104. 
~fa..-ti:::;. ,Eppffia.IlIL Replicatio n. In Designing Data-Intensive Applications. ~~ 
i: - 1 - _ 0 eilh- :\ledia. 2017. 
~. iIL\pa.ch e :- - http . wwv;.cloud.karafkac om/bl og what-does-in-sync-in-~ 
pache-Mika- reallY-r:ieanJitmL 
l '" Global raan in a geo2JQDhic Coordinate Reference SysteITL https ://cwiki.ap achtr> 
~~ conflu~ce d.L~la;- KAFK .. A 1JP-392~c3A+Allow+consumers+to+fetch-fro:r, 
-closest - :cplira.. 
[12] Hands -free Kafka Replication. https: //W\\1-W.confluent.io/bloglhands-free -kafka.r 
eplirati on-a-lesson -in-operatio nal-simplicity /. 
[ 3 ~high waten:nark.. https: ' rongrinblog.wo rdpress.com/2016 /07 /29/katka -hig 
h-watermark . 
14-] Kafka mirroring. https: C\\ikiapache.o rg confluence /pages /viewpage .action?IY'ag 
eld=27846330 . 
[ 15] - 1essage filtering in RockeL\ IQdtree.. http s: ' partners-intl.aliyun..com/help /doc-de 
tail 29543.htm. 
[ 16] Scheduled messag es and dela yed messages in Apache RocketM Q. https ://partners 
-intlaliyun..com.lhetp doc-detail/43349 .btm. 
[17) Hashed and hierarchi cal timing wheels . http :/ www.cs.columbiaed ul-nah Umtw69 
98 papers sosp87 -timi ng-wheels.pdf. 
[18] A<h-anced ~tessage Q:!teuing Protocol https : en.wikipedia.org/wiki/Advanced_~t 
essag e_Queuing_ Protocol 
[19] Kafka protocol guide. https: /kafka.a pache.org/protocol 
128 I Chapter 4. Distributed Message Queue 
-╖ 


[Page 134]
-
[20) HDFS. https ://hadoop .apache .org /<lnrs/rl .2.1 /heirs clrsign.hl ml. 
Reference Mater ial I 129 


[Page 135]
5 Metrics Monitoring and Alerting Sys¡
tem 
In this chapter , we explore the design of a scalable metrics monitoring and alerting sys¡
tem. A well-designed monitoring and alerting system plays a key role in providing clear 
visibility into the health of the infrastructure to ensure high availability and reliabi l¡
ity. 
Figure 5.1 shows some of the most popular metrics monitoring and alerting services in 
the marketplace . In this chapter , we design a similar service that can be used inter nally 
by a large company. 
DATA DOG 0 inf1u11dh 
Prometheu 
igur 
Am lri m 
t 
~agios╖ 
Graf an a 
rinf( and aJ rting rvic 
╖ D sign Scope 
jlfi r nt 
rvi wer. 
b rv r 
' 131 


[Page 136]
Candidate : Who are we building the syslem for? A rc we building 3 11 111 h<J i 
J\ (ò \y 
for a large corporation ill<e Faccbook or Google, or are we designing a Sriri ~ \<╖ ' 11╖11, 
rvrr <╖ I k t Datadog (1). Splunk [2]. etc? 1 r╖ 
Interviewer : That's a great question. We are building it for internal use only. 
Candidate : Which metrics do we want to collect? 
Interviewer : We want to collect operational system metrics. These can be low-I ev.1 usage data of the operating system, such as CPU load, memory usage, and disk s t 
b h ╖ h 1 1 h ╖ Pact consumption . They can also e ig - eve concepts s ue as requests per second of 
service or the running server count of a web pool. Business metrics are not in the s a 
of this design. cope: 
Candidate : What is the scale of the infrastructure we are monitoring with this system? 
Interviewer 100 million daily active users, 1,000 server pools, and 100 machines p ╖ ╖ er 
pool. 
Candidate : How long should we keep the data? 
Interviewer : Let's assume we want 1 year retention . 
Candidate : May we reduce the resolution of the metrics data for long-term storage? 
Interviewer : That's a great question. We would like to be able to keep newly received 
data for 7 days. After 7 days, you may roll them up to a 1 minut e resolution for 30 days. 
After 30 days, you may further roll them up at a 1 hour resolution . 
Candidate : What are the supported alert channels? 
Interviewer : Email, phone, PagerDuty [3], or webhook (HTTP endp oints). 
Candidate : Do we need to collect logs, such as error log or acce l og? 
Interviewer : o. 
Candidate : Do we need to support di tributed tern tracing? 
Interviewer: o. 
High-level requirements and assumptions 
Now you have finished gathering requiremen ~ m the intervit' r nd h vr n ckM 
scope of the design_ The requirements are: 
ò The infrastructure being monitored i.s larg~╖ 
o l 00 million daily active users 
0 Assu~e we have J .000 ~ poolt, 1 
machine ~ ""' Jo rnilhon IJ'lt'trin 
0 l year data rctenti on 
I. 100 mrt 
o Data retention polirv : raw fonn "or 7 da 1 -I 11 ò mtnut rr tuh n (i r :k) hour resolution for J year. 
ò A variety of metrics can bt" moru1ore'd. for t'OJ'npl . 
o CPU usage 
132 / Chapter 5. Metrics Monitoring and Aletti"8 System 
> . l 


[Page 137]
o Reque st co unt 
o Memory usage 
o Messa ge coun t in m essage qu eues 
Non -functional requirements 
ò calab ility. 1h e sys tem should be scalable lo accommod ate gro wing metrics and alert 
volume. 
ò Low latency. The sys tem needs to have low query latency for das hboards a nd alerts. 
ò Reliabilit y. TI1e sys tem should be highly reliable to avoid missing c riti cal alerts. 
ò Flexibility . Techn ology keeps changing, so the pip elin e sh ould be flexi ble enough t o 
easily integrate new t eclrnol ogies in the futur e. 
Whi ch requirement s are out of scope ? 
ò Log monitoring . The Elasticsearch , Logstash , I<ibana (ELK) stack is very popular for 
collecting and monitoring logs [ 4). 
ò Distributed system tracing [5] [6]. Distributed tracing refers to a tracin g solution 
that tracks service requests as they flow through distributed systems . It colle cts data 
as requests go from one service to another. 
Step 2 - Propose High-level Design and Get Buy-in 
In this section , we discuss some fundamentals of building the system , the data mo del, 
and the high -leve l design . 
Fundamentals 
A metrics monitorin g and alertin g y stem generally contains five compone nts , as illus ¡
trated in Figure 5.2. 
ò Data collectio n: c llect m etric data from different sources. 
ò Data transmis ion: tcan fer data from urce lo the metri cs monitorin g system . 
ò Data storage: organize and tore incomi n g data. 
ò Alerting: anaJY7~ incoming data. detect anomali s. and ge n rate alerts. The system 
must be abl to nd al rts to diff; r nt mmunic tio n chan n l s. 
ò isualization; p nt 
patt ms. tttmls . or p bl 
tion functionali . 
s 2 . Propose 
bette r at identifying 
we n d visualiza -
I Des gn and Get Buy-In I 133 


[Page 138]
Mct rir~ mon 
itorin(Z And 
al rhng sys t rm 
4 /\} C'r ti n~ 
5. Visualiza tion 
Figure 5.2: Five components of the system 
Data model 
Metrics data is usually recorded as a Lime series that contains a set of v alues with th ╖ I 'd 'fi d b ╖t eir associated timestamps . l11e series itself can be uniqu e Y i ent1 e Y 1 s n ame, and op. 
tionally by a set of labels. 
Let ò s take a look at two examp les. 
Example 1: 
What is the CPU load on production server instance i631 at 20: 00? 
~t 
0 .626 
0 .313 
0 
18:00 18:30 19:00 19:30 20:00 20:30 21 :OO 21 :30 22:00 22:30 23:00 23:30 00:00 00:30 
Figure 5.3: Popular metrics monitoring and alerting services 
The data point highlighted in Figure 5.3 can be represented by Table 5.1. 
metric_name cpu.load 
labels host:i63 l ,env:prod 
tiòestaòp 1613707265 
value 0.29 
Table 5.1: The data point represented by a table 
In this ~xample, the time series is represented by the metric name, the labels 
(host:1631,env:prod), and a single point value at a specific time. 
134 I Chapter 5. Metrics Monitoring and Alerting System 


[Page 139]
Example 2: 
\VhAI is th e a crage CPU lon d across a ll we b sc-rvcrs in 1 he us-west region for the la s l 1 O 
minute ? Conccp lu ::i lly, we wou ld pull up som elhin g lik r thi s from s torage where th e 
metric 1rnnw is CPU.load a nd the r C'gion labe l is us-west: 
CPU. l oad host=webserver01,region =us-west 161 3707265 50 
CPU.load host=webse rver01,region =us-west 161 3707265 62 
CPU. load host =webse rver02, region =us-west 161 3707265 43 
CPU .load host =webserver0 2,regio n=us-west 161 3707265 53 
... 
CPU. load host =webserver01,region =us-west 1613707265 76 
CPU.load host=webserver01,region =us- west 1613707265 83 
The average CPU load co uld be comput ed by averaging the values at the e nd of eac h 
Linc. The format of the lines in the above example is called the line pro tocol. It is a 
common input format for many monitoring software in the market. Prometheus [7] and 
OpenTSDB [8] are two examp les. 
Every time series consists of the following [9]: 
Name Type 
A metric name String 
A set of tags /lab els List of <key: value> pairs 
An array of values and their An array of <value, time stamp> pairs timestamps 
Tab le 5.2: Time series 
Data access pattern 
ln Figure 5.4. each label on the -axis represent a time series (uniquely identified by the 
nam and labels) hil th -axis r presenls time. 
I Design nd Get Buy-in I 135 


[Page 140]
!!l 
~ 
.5 
~ E e ò ~ 
~ . 
╖c: 
5l 
Q) 
E F e ò 
http_ error_ count{"servlcepool"~~.~ 1 \ ò ò 
"methocl"╖"GEl ,"machinename ╖ m2 }--~ ò 
ò 
12 
---~- . 
http_ error_ countfservi cepool"~╖.~ 1 "ò, 
╖ method ":"GET","machinename : m1} 
11 
ò ò ò ò 
ò ò ò ò 
ò ò ò 
ò ò ò 
ò ò ò ò ò ò ò ò 
ò ò ò ò ò -
15 16 17 18 
13 14 
Query to get errors on 
servicepool=s1 and method=GET 
across all machines 
between time t4 and t7 
Figure 5.4: Data access pattern 
ò 
ò 
ò 
ò 
t9~ 
Time 
ti -series data points written 
The writ e load is heavy. As you can see, there can be many . me t ,, ectio n on page 132 
. d . th "H. h 1 el reqwr emen s s ' at any moment As we ment:J.one m ╖ e ig - ev etrics are collected 
about 10 million operational metrics are written per day, and many m 
at high frequency , so the traffic is undoubtedly write-heavy. 
. . . d alerting services send 
At the same time, the read load is spiky. Both visualizauon an h 1d alerts 
queries to the database, and depending on the access patterns of the grap s a i ' 
the read volume could be bursty. 
. l d rule the read load is In other words , the system is under constant heavy wnte oa ò w 
spiky. 
Data storage system 
The data storage system is the heart of the design. It's not recommended to build your 
own storage system or use a general-purpose storage system (for example, MySQL [ lO]) 
for this job. 
A general-purpose database , in theory, could support time- ries data. but il would re╖ 
quire expert-level tuning to make it work at our scale. Specifically. a rel tion l d tnbn e 15 
not optimized for operations you would commonly perform against tim - eri dat ╖ for 
example , computing the moving average in a rolling time window require s complic ttd 
SQL that is difficult to read (there is an example of this in the d ep div ction). B ╖ 
sides , to support taggin g/labelin g data , we need to add an index for each t g. for eover. 
a general-purpose relational datab ase does not perform well under con l the wy write 
load. At our scale, we would need to expend significant effort m tuning the dut b 
and even then , it might not perform well. 
136 I Chapter 5. Metrics Monitoring and Alerting System 


[Page 141]
llm: Abou t NoSQL? In theory . a few NnSQ L tlatnha -;cc; 1111 th e mnrk cl C'Cltild lrnndl r lim f' 
srries data dfrc livrly. For cxa mplr , C:issnndrn and Bigl;dik [ 11] n 111 both be used for 
time srries dAla. Il owevcr . th is would req uire deep knowledge ol lhc inl ernal working s 
of rar h NoSQL lo devise H sca!F1 hlr srhcmr-1 for cllccl ivcly slonn g an<l qucr ying lim e 
series data. With indu slrial-sca k Lime-ser ics daLAbases readi ly :ivailablc. using R gcneral ¡
pu1pose NoSQL dF1 tabasc is not appealing. 
TI1ere are many s torage sys tems available that arc opti mized for time -series data. The 
optimi zation lets us use far fewe r servers Lo handle the same volume of data. Many of 
these databases a lso have custom query int erfaces specially designed for the a nalysis of 
time-se ries d ata lhal are much eas ier lo use than SQL. Some even p rov ide f ea lur es lo 
mana ge data retention and data aggrega tion . Here are a few exampl es of tim e-se ries 
databases . 
OpenTSDB is a distributed time -series dat abase, but since it is base d on Hadoop and 
HBase, rwmin g a Hadoop /HBas e cluster adds complexity . Twitt er uses MetricsDB [12], 
and Amazon offers Timestream as a time-series databa se [13]. Accordin g to DB-engines 
[14), the two most popular time -series databases are InfluxDB [15] and Prometheu s, 
which are designed to store large volumes of time-series data and quickly perform real ¡
tim.e analysis on that data. Both of them primarily rely on an in-memory cache and 
on-disk storage. And they both handle durability and performance quite well. As shown 
in Figure 5.5, an InfluxD B with 8 cores and 32GB RAM can handle over 250 ,000 writes 
per second. 
I 
vCPU or RAM IOPS Writes per Queriesò per 1 Unl~ue 
CPU second second sen es 
2-4 cores 2-4 GB 50 0 < 5.000 < 5 < 100.000 
4 -6cores 8-32 500 <25 < 1.000.000 
GB iooo 
< 250.000 
8.,cores 32ò GB 1000ò > 250000 >25 > 1.000.000 
Figure 5.5: lnfluxDb benchmarking 
i a p~1aliz d d taba . you are not expec ted to W1derstand 
uni ou t' Xpllc1ll mentioned it in your resume . For the 
mce a time - rie da b 
the int mals in an mt 
purpo of an inl rv1 ò 1t ò important to under t nd the metric data are time -series 
I l h~╖~rttò ~ d l b t uch a tnfluxDB for torage to store in n.arure and w ran 
them. 
Anoth r f. hire of a 
a ~e mount of t1 
exampl~. lnfluxDB build 
by I ls (15). lt pnwid 
O\'t"rl ding th 
rte l lm <' i rffiricnt gp g tion and analysis of 
b 1 b l . 11 o knmvn i t g m ome dat abases . For 
cm 1 bd to h ctht llt' thtò f l lookup of time -series 
I ╖pr r hcr l(utdrhnrc; on how to u lab els, without 
╖ a to urr c \ch I b I i of low cardinality (having 
2 ò ProPCK Hlgh╖ ~I Design and Get Buy-in I 137 


[Page 142]
a s1nall set of poss ible valu es). Thi s featur e is criti cal for vis ua lization , nnd it woidd l;ik 
a Jo t of effort to build this with a general-purpo se d a ta base . <╖ 
High -level design 
The high -level design diagram is shown in Figure 5.6. 
Metrics Source f----i Metrics Collector 1-----i 
nme series DB 
Send Queries 
Query Service 
Send Queries 
Visualization 
System 
Figure 5.6: High -level design 
Page~ 
HTTPS Endpoints 
ò Metrics source. This can be application servers , SQL databases , nle ssage queues, 
etc. 
╖ ╖ d ╖ d ta into the time-series ò Metrics collector. It gathers metncs data an wntes a 
database . 
ò Time-series database. This stores metrics data as time series. It usually provid es a 
╖ f: c ╖ d ╖ ╖ l ge amount of time-se ries custom query mter ace ior analyzmg an summ an zmg a ar . 
data It maintains indexes on labels to facilitate the fast lookup of time -sene s data 
by labels . 
ò Q!lery service. The quer y service makes it easy to query and r etrieve data from 
the time-seri es dat abase. This should be a very thin wrapper if we choose a good 
time-series database. It could also be entirely replaced by the time -se ries dat abase's 
own query interface . 
ò Alerting system . This sends alert notifi cations to various alerting destin a tion s. 
ò Visualization system. This shows metric s in the form of various graphs /chart s. 
Step 3 - Design Deep Dive 
In a system design interview, candidates are expected to dive deep into a few key com¡
ponents or flows . In this section , we investigate the following topics in detail: 
ò Metrics collection 
ò Scaling the metrics transmission pipeline 
138 I Chapter 5. Metrics Monitoring and Alerting System 


[Page 143]
ò Q}1cry service 
ò Storage li:iyer 
ò Alerting system 
isuali zation sys tem 
Metrics collection 
for metrics collection like count ers or CPU usage. occasio nal data loss is not the e nd of 
the wor ld. IL 's accep table for clients to fi re and forget. Now let's take a look at the metr ics 
collection flow. This par t of the sys tem is inside the dashed box (Figure 5. 7). 
--- --------- - - -- - -- - -- - ----- - --- - - -- -- - --- - - - - - - - -- - 1 
' . 
Metrics Source .___ _ _.... Metrics Collector ,.._..... _ _.... 
llme series DB 
Send Queries 
Query Service 
Send Queries 
Visualization 
System 
Email 
Page Duty 
H TTPS Endpo ints 
Figure 5.7: Metrics collection flow 
Pull vs push models 
There are two ways metrics data can be collected , pull or push . It is a routine debate as 
to whic h one is bett er and there is no clear answer. Let's take a close look. 
Pull model 
Figure 5.8 shows data co Uection with a pull model over HTTP . We hav e dedi cate d metric 
collector whi ch puJI metnc value from the runnin g applica tions periodically . 
Step 3 - Design Deep Dive I 139 


[Page 144]
.-------~.-
-... ----- -- - ----.. --------, 
l 
Service Discove1y 1 
etcd 11 Zookeeper J 
: Metrics Source 
1 
Web Servers 
.---------i Pull metrics 
DB Clusters I .-----__.___ __ _ .___ ____ ___.,.....,__:-- Pull metrlcs- ____ J 
, Metrics Collector 
I 
~Pull metrics 
Queue Clusters 
I 
I 
: Pull metrics 
.-----------.~ 
I 
Cache Clusters : 
I 
I 
I 
I I 
~ --- - -- - -- -- - --- - ----- - ' 
Figure 5.8: Pull model 
In this approach , the metrics collector needs to know the complete list of service end¡
points to pull data from. One naive approach is to use a file to hold DNS/IP information 
for every service endpoint on the "metric collector" servers . Whil e the ide a is simple, 
this approach is hard to maintain in a large-scale environment where servers are added 
or removed frequently, and we want to ensure that metric collectors don 't miss out on 
collecting metrics from any new servers. The good news is that we have a reliable, scal¡
able, and maintainable solution available through Service Discovery, provided by etcd 
[16) , ZooKeeper [17], etc., wherein services register their availability and the metrics 
collector can be notified by the Service Discovery component whenever the list of ser¡
vice endpoints changes. 
Service discovery contains configuration rules about when and where to collect metrics 
as shown in Figure 5.9. 
Service Discovery 
etcd 11 Zookeeper I 
Figure 5. 9: Service discovery 
Figure 5.10 explains the pull model in detail. 
- ~---
140 I Chapter 5. Metrics Monitoring and Alerting System 


[Page 145]
I~ Service Discovery 
IJ;; etcd ~ [ Zookeeper 
CD Discover Targets 
Web Servers l╖---«HTIP Requests---< 
/metrics endpoint L--------' 
I 
Metric s Collector 
Figure 5.10: Pull model in detail 
1. 1he metrics collector fetches configuration metadata of service endpoints from Ser¡
vice Discovery. Metadata include pulling interval , IP addresses , timeout and retry 
parameters , etc . 
2. The metrics collector pulls metrics data via a pre-defined HTTP endpoint (for exam¡
ple , /metrics) . To expose the endpoint, a client library usually needs to be added to 
the service . In Figure 5.10, the service is Web Servers. 
3. Optionally , the metrics collector registers a change event notification with Service 
Discovery to receive an update whenever the service endpoints change . Alterna¡
tively , the metrics collector can poll for endpoint changes periodically . 
At our scale , a singl e metrics collector will not be able to handle thousands of servers. We 
must use a pool of metri c collectors to handle the demand. One common problem when 
there are multiple collector i that multiple instan ces might try to pull data from the 
same res ource and prod uc duplicate dat a There must exist some coordination scheme 
amon g the in tance to avoid thi . 
ne potential approach i to de ignate each collec tor to a range in a consist ent hash ring , 
and then map every ingl rv r being monitored by it uniqu e name in the hash ring. 
Thi ensure one metric rver i handled by one collector only. Let's take a look 
al an exampl 
As hown in Figure 5.11, lh r 
coll or is ibl for coll 
re on 1bl for coU in m n 
four coU ctor and ix m tric source servers. Each 
ing m tnc- from distinct el of e.rvers. Collector 2 is 
fr m r l n 
Step 3 - 06Jgn Deep Dive I 141 


[Page 146]
Collt'MOI ? Is responslbl
1 
for servers In this range 
Collocl<>< 1 \__ ) 
I 
Collector 4 
Push model 
colle ctor 2 
Figure 5.11: Consistent hashing 
00 Server I 
(s~) Serv~r , 
G= Server3 
G Sorvo14 
G= servers 
G =Servere 
As shown in Figure 5.12 , in a push model various metrics sources , such as web servers, 
database servers , etc., directly send metrics to the metrics collector . 
1-------- --------------t 
: Metrics Source ' 
I 
I 
I 
I 
ò Web Servers 
I 
. 
DB Clusters ,.~~l --: = ---=:::- - ----.., 
ò M lllC$ Collector 
I 
~aus- h 
Push melricS 
Cache Ousters 
I < 
~-- ---- -------------- - -' 
Figure 5.12: Pu. h modd 
In a push model, a collection agent is commonJ 1ns1all...d on t ╖ r ~ rvtòr being m ni╖ 
tored. A collection agent is a piece of long-runnfo f( ftw ll'<" 1h t oUt"r t mdnc~ from 
the services running on the server and push tho~╖ m trac pc-rt tr ill , tu thtò m ╖tncs 
collector . The collection agent may also aggr gate ln<'l!l (t.< prct ll ' ample counter) 
locally, before sending them to metric collector: . 
142 I Chapter 5. Metrics Monitoring and Alerting System 


[Page 147]
Aggrrgn tion is an r flrc tivr way l o rcdtlC'<' the volnnir of data srn t to thr rnr tric <; collr ctor. 
1 f t hr pllsh traffic is hi gh and I he metrics col lcr t or n ╖jrc l ~ I he pu 'lh wit h "n error . I he agcn l 
colllci J rrp a small buffer of dntn lncrilly (poss ibly hy stori ng th em lon 1lly on disk), and 
rrsr nd them later. I lowr vr r, if the servers arc in an auto scaling gro up w here they arC' 
rot<1 ted out frequ entl y, then h oldin g data locally (even tcmp oni ril y) might result in data 
Jos, when the metri cs collector fo ils behind . 
To pre ent Lhe metri cs collec tor from falling behind in a push mod el. the me tri cs collcc¡
tor shou ld be in an auto -scalin g clus ler wilh a load b alance r in fronl of il (fi g ure 5.13). 
111e cluster should scal e up and down based on the CPU load of the me tri c co llec tor 
servers. 
-------------------------------------------- --------, 
Metrics Source 
Metrics 1 
' ' ' ' ' I 
' ' ' ' 
I 
Web Servers Metrics 2 
: , Push Load L-----t Metrics Collectors 
:-:- Messages - Balancer ' ' ' I 
I 
Metrics 3 ' ' ' ' : _________ ____ _______ __ J : 
I I 
--------------------------------------------------------' 
Figure 5.13: Load balan cer 
Pull or push? 
So, whi ch one is the better choice for u s? Just like man y thin gs in life , there is no clear 
answer. Both sides have wide ly adop ted real-wo rld use cases . 
ò Exan1ples of pull architecture include Prome theus. 
ò Exan1ples of push archit clure in lude Amazo n l oudWa tch (18] and Graphit e [19]. 
Knowing the ad antage and di ad antages of each approac h is mor e important than 
picking a winner during an int rvi w. Tab le 5.3 ompares the pros and co ns of push and 
pull archjtectur s {20] (21] {22] (2 ]. 
Step 3 - Design Deep Dive I 143 


[Page 148]
╖-
Easy debugging 
Pull 
rfo e /melrics endp oin t 
on appli cation servers 
used for p ullin g met-
rics can b e use d t o 
view metrics al any 
time. You can even 
Pull wins . 
Push 
do thi s on your laptop. I 
l----+--=--------:---:---1----~ 
If an appli cation 
Health check 
Short-lived jobs 
Firewall 
plicated 
setups 
or com¡
network 
serv er doe sn ' t re¡ If th e metri cs collec¡
tor doesn 't receive 
metrics , the problem 
might be caused by 
network issue s. 
spond to the pull , you 
can quickly figure 
out if an app lication 
server is down . Pull 
wins. 
Having servers 
pulling metrics re-
quires all metri c 
endpoints to be 
reachable. This is 
potentially prob -
lematic in multipl e 
data center setups. It 
might require a m ore 
elaborate network 
infras tru ctu re. 
Some of the batch jobs 
might be short-li ved 
and don't last long 
enough to be pull ed. 
Push wins. This can 
be fixed by introduc ¡
ing push gateway s for 
the pull model [24). 
If the metrics collec¡
tor is se t up with a 
load balan cer and an 
auto -scalin g gro up, it 
is pos sibl e to receive 
data from anywhere. 
Push wins . 
144 I Chapter 5. M~tri~ Monitori~g ~d Al;rting Syst~m 


[Page 149]
........__ -
Perfor mance 
Data authenticity 
Pull methods typically 
use TCP. 
Application servers to 
collect metrics from 
are defined in con¡
fig files m advance. 
Metrics gathered from 
those servers are guar¡
anteed to be authentic. 
Table 5.3: Pull vs push 
Push methods 
cally use UDP. 
the 
typi¡
'lhis 
push tnC' ans 
method provid es 
lowcr -lalency tran s¡
ports of metrics. The 
count erargument here 
is that the cff ort of 
establishing a TCP 
connection is small 
compared to sending 
the metrics payload . 
Any kind of client 
can push metri cs to 
the metrics collector. 
This can be fixed by 
whitelisting servers 
from which to accept 
metrics , or by requir¡
ing authentication. 
As mentioned above, pull vs push is a routine debate topic and there is no clear answer. 
A large organization probably needs to support both, especially with the pop ularity of 
serverless [25] these days . There might not be a way to install an agent from which to 
push data in the first place . 
Scale the metrics transmission pipeline 
Send Queries 
Query Service ..____M_ern_╖cs_ So_u_rce___.'--_,__ __.. , Metncs Collector Ii---~. LJ-_._~ 
nme seti DB ~--.---' 
' ----------╖-----------╖╖╖--╖----------------' 
Send Queries 
Visualizat ion 
System 
Figure 5.14: Metrics transmission pipeline 
Email 
Text Message 
Page Duty 
HTTPS Endpoints 
Step 3 - Design Deep Dive I 145 


[Page 150]
l C't'c; 7nnm 111 on the metrics rnllcclnr rt nd lim e series drit<1 1>rtscs. Whc lhcr yrn1 11 ,<. 11 rt(' 
push nr pull model. the metrics co llrrtn r is rt clu ster of servers. and the cluslcr rc╖cc╖ivr 
<'nnnnnus :'lmmm ts of drtta. For eith er 11ush nr pull Ilic metrics co llector clu<;lc╖r jo SC't ' , . " . llp 
fnr aut0 -scaling. to ernmrc tlrnt th ere r1re an r1dequalc num ber of co llcclor in<;tflnc<'s l() 
}umdk the dema nd. 
l h1wc,╖cr. there is a risk of data loss if lh e lim e-series dC1 labasc is unavai lC1hlc. To mili~atr 
this proble m. we introduce a queueing componcnl as shown in Figure 5.15. 
~---------- ----------------------- - ---- --- ---- - - ---i Send Queries 
' ' ' ' Kafka Consumers ò ò Me1rlcs Source Query Service Metrics Collector 
! LJ i 
''----~-~ 
: Time series OB : 
' I 
~ ------------------------------------------------ ---
Figure 5.15: Add queues 
Send Queries 
Visualization 
System 
In this design , the metrics collector sends metrics data to queuing systems like Kafka. 
Then consumers or streaming processing services such as Apache Storm, Flink, and 
Spark , process and push data to the time-series database . This approach has several ad¡
vantages: 
ò Kafka is used as a highly reliable and scalable distributed messaging platform . 
ò It decouples the data collection and data processing services from each other. 
ò It can easily prevent data loss when the database is unavailable , by retaining the data 
in Kafka. 
Scale through Kafka 
There are a couple of ways that we can le rag Kafka's built-in partition mechanism to 
scale our system. 
ò Configure the number of partition ba ed n throughput r quir ements . 
ò Partition metrics data by metric nam . o consum 
names . 
ò Further partition metrics dat.a with l g /label . 
n (J ggr gate data by metrics 
ò Categorize and prioritize melri cs o lh l imp rta nt m tri can be pro cessed first. 
146 I Chapter 5. Metrics Monitoring and Alerting System 
-


[Page 151]
I --
r------------------- -
Kafka 
Partition O (metric 1) 
Partition 1 (metric 2) 
M etrics Collec tor 1----- -
Partition 2 (metric 3) 
ò ò ò 
I òòò 
I 
I 
I 
~--- -- ----- - ---- -- ----- --- --' 
Figure 5.16: Kafka partition 
Alternative to Kafka 
Maintaining a production-scale Kafka system is no small undertaking. You might get 
pushback from the interviewer about this. TI1ere are large-scale monitoring ingestion 
systems in use without using an intermediate queue. Facebook's Gorilla [26] in-memory 
time-series database is a prime example ; it is designed to remain highly available for 
writes , even when there is a partial network failure. It could be argued that such a design 
is as reliable as having an intermediat e queue like Kafka. 
Where aggregations can happen 
Metrics can be aggregated in different places; in the collection agent (on the client-side) , 
the ingestion pipeline (before writing to storage) , and the query side (after writing to 
storage) . Let's take a closer look at each of them. 
Collection agent. The collection agent installed on the client-side only supports simple 
aggregation logic. For example , aggregate a cow1ter every minute before it is sent to the 
metrics collector . 
Ingestion pipelin e. To aggregate data before writing to the storage, we usually need 
stream processing engines such as Flink. The write volume will be significantly re¡
duced since only the calculated result is written to the database . However, handling 
late-arriving events could be a challenge and another downside is that we lose data pre¡
cision and some flexibility because we no longer store the raw data. 
Qgery side . Raw data can be aggregated over a given time period at query time . There is 
no dat a loss with this approach, but the query speed might be slower becaus e the query 
result is computed at query time and is run against the whole dataset. 
Step 3 - Design Deep Dive I 147 


[Page 152]
Query service 
1h e query service comprises a clusler of query servers, whi ch access the time-series 
databases and handle requests from the visualization or alertin g system s. Having a dedi¡
cated set of query servers decouples time-series databases from the clients (visualization 
and alerting systems). And this gives us the flexibility to change the time-series database 
or the visualization and alerting systems, whenever needed. 
Cache layer 
To reduce the load of the time-series database and make query service more performant, 
cache servers are added to store query results, as shown in Figure 5.17. 
Metrics Source Metrics CoUecior Kafka Consumers 
Tune series DB 
Figure 5.17: Cache layer 
The case against query service 
---------- -----------: 
~--'-----,' 
Send 
L--ou_ery~Se<v~lc-e _, : Queries 
Cache 
' ---------------------╖ 
Text Message 
PageOuty 
HTIPS Endpoints 
Visualization 
System 
There might not be a pressing need to introduc e our own abstraction (a query service) 
because most industrial -scale visual and alerting systems have powerful plugins to in¡
terface with well-known time-series databases on the market. And with a well-chosen 
time-series database , there is no need to add our own caching, either . 
Time-series database query language 
Most popular metrics monit oring systems like Prometheus and InfluxDB don't use SQL 
and have their own query languages. One major reason for this is that it is hard to build 
SQL queries to query time-series data. For example, as mentioned here [27], computing 
an exponential moving average might look like this in SQL: 
148 I Chapter 5. Metrics Monitoring and Alerting System 
-


[Page 153]
select id, 
temp, 
avg (te mp ) ove r ( pa rtition by grou p_nr ord er by 
time_ read) 
as ro lling _avg 
from ( 
select id, 
t emp , 
time _ read, 
interval_group, 
id - row _number() over (partition by inter val_group 
o r╖de r 
by time_read) as group_nr 
from ( 
select id, 
time_ read, 
11
epoch
11
:: times tamp + 
11
908 second s ":: interval * ( 
extract (epoch from time_read)::int4 / 900) as interval _group, 
temp 
) t2 
from readings 
) t1 
order by time_read; 
While in Flux, a language that's optimized for time-series analysis (used in InfluxDB) , it 
looks like this . As you can see, it's much easier to understand. 
from ( db : 11 telegraf
11
) 
I> range ( start :-1h) 
I> filter ( fn : (r) => r._measure ment == 
11
foo
11
) 
I> exponentialMovingAverage ( size :-10s) 
Storage layer 
Now let 's dive into the storage layer . 
Choose a time-series database carefully 
According to a research paper published by Facebook [26], at least 853 of all queries 
to the operational data store were for data collected in the past 26 hours. If we use a 
time-series database that harnesses this property , it could have a significant impact on 
overall system performance. If you are interested in the design of the storage engine , 
please refer to the design document of the InfluxDB storage engine [28]. 
Space optimization 
As e>..rplained in high-level requirements , the amount of metri c data to store is enormous . 
Here are a few strategies for tackling this . 
Data encoding and compression 
Data encoding and compression can significantly reduce the size of data. Those feature s 
are usually built into a good time-series database. Here is a simple example . 
- - - -- - - ----
Step 3 - Design Deep Dive I 149 


[Page 154]
Double-delta Encoding 
TO TO TO TO TO 
1610087371 1610087381 1 61008739 1 1610087400 16100874 11 
vv 
10 10 9 11 
Figure 5.18: Data encoding 
As you can see in the image above, 1610087371 and 1610087381 differ by only 10 sec¡
ond s, which takes only 4 bits to represent , instead of the full timestamp of 32 bits. So, 
rather than storing absolute values , the delta of the values can be stored along with one 
base value like: 1610087371, 10, 10, 9, 11. 
Downsampling 
Downs ampling is the process of converting high -resolution data to low-resolution to 
reduce overall disk usage. Since our data retention is 1 year, we can downsample old 
data. For exampl e, we can let engineers and data scientists define rules for different 
metri cs. Here is an example: 
ò Retention : 7 days, no sampling 
ò Retention : 30 days, downsample to 1 minute resolution 
ò Retention : 1 year, downsample to 1 hour resolution 
Let's take a look at another concrete example. It aggregates 10-second resolution data to 
30-second resolution data . 
metric time stamp hostname metric _ value 
cpu 2021-10-24Tl9:00:00Z host -a 10 
cpu 2021-10-24Tl 9:00:10Z host-a 16 
cpu 2021-10-24Tl 9:00:20Z host -a 20 
cpu 2021-10-24Tl 9:00:30Z host -a 30 
cpu 2021-10-24Tl 9:00:40Z host-a 20 
cpu 2021-10-24Tl 9:00:50Z host -a 30 
Table 5.4: 10-second resolution data 
Rollup from 10 second resolution data to 30 second resolution data. 
150 j Chapter 5. Metrics Monitoring and Alerting System 


[Page 155]
metric tim es tamp hostnarne Metric_ val ue (avg) 
cpu 2021-10-24T l 9:00:00Z host-a 19 
cpu 2021-10-24Tl 9:00:30Z hos t-a 25 
Table 5.5: 30-seco nd resolution data 
Cold storage 
Cold storage is the storage of inactive data that is rarely used. The finan cial cost for cold 
storage is much l ower. 
In a nutsh ell, we should probably use third -party visualization and alertin g sys tems, in¡
stea d of buildin g our own. 
Alerting system 
For the purpose of the interview, let's look at the alerting system, shown in Figure 5 .19 
below. 
Cache 
Rule config files Email 
Text Messag e 
Alert Manage r Kafka Alert Consumer 
Alert store PageD uty 
HTTPS Endp oints 
Query Service 
Figure 5.19: Alerting system 
The alert flow works as follows : 
1. Load config files to cache servers . Rules are defined as config files on the disk. YAML 
[29] is a commonly used format to define rules. Here is an example of alert rules: 
- name: instance _down 
rules : 
# Alert for any instance that is unreachable for >5 
minutes. 
- alert: instance_down 
expr: up== 0 
fo 1' : Sm 
labels: 
severity: page 
2. The alert mana ger fetch es alert configs from the cache. 
Step 3 - Design Deep Dive I 151 


[Page 156]
3. Based on config mies. the alert mana ge r calls th e qu <" ry sC'r vice fl t ri prf'drflnrd 1ntc╖r 
val . If the value violates the threshold, an alert eve nt is crC'ated. ╖rh c alert JTifl n .:ig1-r 
is responsib le for the following: 
ò Filter. merge, and dedupe alerts. Here is an ex<1mplc of tnC'rgi ng ri lr r t <; thflt :it( 
triggered w1thin one instan ce wi thin a short amoun t of Lime (in c;ta ncc I ) (f 1g11rr¡
S.20). 
Event 1 
Instance 1 ,..___ 
disk_usage > 90% 
Event 2 
Instance 1 Merge - ò 1 alert o n Instance 1 
disk_usage > 90% 
Event 3 
Instance 1 -
disk_usage > 90% 
Figure 5.20: Merge alert s 
ò Access control. To avoid human error and keep the system secure, it is essential 
to restrict access to certain alert management operation s to auth orized individ¡
uals only. 
ò Retry. The alert manager checks alert state s and ensure s a notifi cation is sent at 
least once. 
4. The alert store is a key-value database , such as Cassandra , that keep s the s tate (in¡
active , pending , firing, resolved) of all alerts. It ensures a notificati on i s sent at least 
once. 
5. Eligible alerts are inserted into Kafka. 
6. Alert consumers pull alert events from Kafka. 
7. Alert consumers process alert events from Kafka and send notificati ons over to dif¡
ferent channels such as email, text message , PagerDuty , or HTTP endp oint s. 
Alerting system - build vs buy 
There are many industrial-scale alerting systems available off-the -sh elf, and most provide 
tight integration with the popular time-series databas es. Many of these alerti ng systems 
integrate well with existing notification channe ls, such as email and Page rDuty . In the 
real world , it is a tough call to justify building your own alerting system . In interview 
settings , especially for a senior position, be ready to justify your decision. 
152 I Chapter 5. Metrics Monitoring and Alerting System 


[Page 157]
Visualizati on system 
Visuali zation is built on top of the data layer. Metrics can be shown on the metri cs das h ¡
boa rd over various time scales and alerts ca n be shown on the alerts dashho<ird. Figu re 
5.2 1 shows a dashboard th at disp lays some of the metrics like the curr ent server req ues t<;, 
memory/CPU utili zation . page load time, tniffic. and login infnnn alion [ :~ OJ . 
Figure 5.21: Grafana UI 
A high- quality visualization system is hard to build. The argument for using an off¡
the-shelf sys tem is very strong. For exampl e, Grafana can be a very good system fo r 
this purpose . It integrates well with many popular time-series databases whic h you can 
buy. 
Step 4 - Wrap Up 
In this chapter, we presented the design for a metrics monitorin g and alerting system. 
At a high level , we talked about data collection , time -series database, alerts, and visu ¡
alizatio n . Then we went in-depth into some of the most important techniqu es/compo¡
nents: 
ò Pull vs pull model for collecting metrics data. 
ò Utilize Kafka to scale the system. 
ò Choose the right time-series databas e. 
Step 4 - Wrap Up I 153 


[Page 158]
ò Use downsampling to reduce di:i ta size. 
ò Build vs buy options for alerting and visualiza tion sys tems. 
W e w en t through a few iterations lo refine the des ign, :rnd our flna l des ign looks like 
thi s: 
M otrics Source H Metncs Collector ~8 B-0 
Time series DB 
Figure 5.22: Final design 
Query Sorvico 
Cache 
Send - [ ~~~f] 0Ufll'i<!9 5ys1Sm 
Congratulations on getting this far! Now give yourself a pat on the back. Good job! 
154 I Chapter 5. Metrics Monitoring and Alerting System 


[Page 159]
I 
╖-
Chapter Summary 
step 1 
step 2 
Metric Monitoring 
step 3 
L collect a v11riety of metric s 
funcUona l "q ~ ale<t 
vis11a liza lion 
L \0<ge-<00\e syst<m 
non -functionol <eq ~ ½liab le so we don 't miss c<itko \ ok<U 
flexibility 
data collection 
data transmissi on 
five compo nents of the system data storage 
alert 
visualiz atio n 
< 
write heavy 
< 
data access patern 
read bursty data model 
data stora ge system -- time-series database 
high -level design 
metrics collection --pull vs push 
< 
scale throu gh kafka 
scale metrics tr~srnission pipeline 
alterna tive to kafka 
where aggregations can happen 
< 
cache layer 
query service 
time-series databa se quer y 
data encoding and 
< 
time-series databas~ compression ╖ 
storage layer 
space optimi zation downsamplin g 
alertin g system 
cold storage 
visualization 
step 4 -- wrap up 
--- ----- ---- - --╖-
Chapter Summary I 155 


[Page 160]
Referen ce Material 
[ 1] Datadog . hllps://www.cialadoghq.com/. 
(2] Sphmk. ht tps://www.splunk.com/. 
(3] PagerD uty. hllps://www.pagcrdut y.com/. 
[ 4] Elasti c slack. https://www.elaslic.co/elastic-slark. 
-
[SJ Dapper , a Large-Scale Distributed Systems Tra cing Infr astru r lurc. h ttp s:// rese::lrrh 
.goog le/pubs/pub36356/. 
[ 6 J Distribut ed Systems Tracing with Zipkin. h ttp s:// blog. t wi ttcr.com/cngi ncerinp;/t> 
n_ us/a/201 2/distributed-systerns-tracing-wi tb-zi pkin .h tml. 
[7] Prom etheus. https://prometheus..io/ docs/introduction/ ove rview I. 
[8] OpenTSDB - A Distributed, Scalable Monitor ing System. http ://opentsdb .net/. 
[9] Data model. :http s://prometheus.io/docs/concep ts/data_m odel/. 
[10] .MySQL. http s://www.mysql.com/. 
[11] Schema design for time-series data I Cloud Bigtable Documen tation . htt ps://cloud. 
google.com!bigtable/ docs/ schema-design-time-series. 
[12] Metr icsDB. TimeSeriesDatabasefo rstoringmetricsa tTwitt er :http s://blog.twitter.c 
om/e nginee ring/en_us/topics/infrastru ctur e/2019/metri csdb.html . 
[13] Amazon Timestream. https://aws.amazo n.com/timestr eam/. 
[14] DB-Engines Ranking of time-series DBMS. h ttps://db-engines. com/en /ra nking/ti 
me+se ries+ dbms. 
[15] Influ xDB. http s://www.influxdata.com/. 
[16] etcd. https ://etcd.io/. 
[17] Servi ce Discovery with ZooKeeper. http s://cloud.spring.io/spri ng-cl oud-zookeep 
er/1.2.x/multi/multi_spring-cloud- zookeeper-di scove ry.html. 
[18] Amazon CloudWatch. https://aws.amazon.com/cloudwatc h/ . 
[19] Graphite . https ://graphiteapp.org/. 
[20] Push vs Pull. http ://bit.ly/3aJEPxE. 
[21] Pull doesn't scale - or does it? http s://prometheus.io/blog/2016/07/23/pull-d oes-no 
t-scal e-or-does-it/. 
[22] Monitoring Architecture. http s://developer.lightb end.com/ guides/moni toring-at-s 
cale/monitorin g-architecture/architecture.html . 
[23] Push vs Pull in Monitoring Systems. https ://giedriu s.blog/2019/ 05/1 1/push-vs-pul 
I-in-m onitoring -systems/. 
156 I Chapter 5. Metrics Monitoring and Alerting System 


[Page 161]
[24] Pushgateway . https: //github .com/prometheus /pushgateway. 
[25] Building Applications with Serverless Architectur es. http s://aws.amazon.com/lam 
bdaJserverless -architectures -learn -more /. 
[26] Gorilla. AFast ,Scalable ,ln-MemoryTimeSerie sDatabase: http ://www .vldb.org /pvl 
db/vol8/p 1816-teller. pdf. 
[27] Why We're Building Flux, a New Data Scripting and Qyery Language. hltp s://ww 
w.influxdata.com /blog /why-were -building -flux-a-new-data-scrip ting-and-query ¡
language /. 
[28) InfluxDB storage engine. https: //docs.influxdata .com/influxdb/v2.0/reference/i nte 
rnals / storage-engine /. 
[29) YAML. https: //en.wikipedia .org/wiki/YAML. 
[30] Grafana Demo. https:/ /play .grafana.org /. 
.... _~ __ ._. __ . .. 
- - -- 7 
Reference Material I 15 


[Page 162]



[Page 163]
6 Ad Click Event Aggregation 
With the rise of Facebook , You Tube , TikTok, and the online media economy, digital ad¡
vertising is taking an ever- bigger share of the total advertising spending . As a result, 
tracking ad click events is very imp ortant. In this chapter, we explore how to design an 
ad click event aggregation system at Facebook or Google scale. 
Before we dive into technical design , let's learn about the core concepts of online ad¡
vertising to better understand this topic. One core benefit of online a dvertising is its 
measurability, as quantified by real-time data. 
Digital advertis ing has a core proces s called Real-Time Bidding (RTB), in which digital 
advertising inventory is bought and sold. Figure 6.1 shows how the online advertisin g 
process works . 
: ----------------╖15e,n-0,;CisiCie ____ ----------╖ --╖: ~ -╖ -╖ --------------╖suppiy side-------------------: 
: ' 
' l SSP _ -~ 
: ( Supply Side Platform ) ~ 
DSP 
(Demand Side Platfonn) Ad Exchange : Advertiser 
' : '------' 
t _ --- - ---- - - - - - - - - - - - --- - - - - - --- - - - - - -- - - - -- - ... - - _, ╖------------------------------------------- -----
Figure 6.1: RTB process 
The speed of the RTB process is important as it usually occurs in less than a second. 
Data accuracy is also very important . Ad click event aggregation plays a critical role in 
measuring the effectiveness of on.line advertising, which essentially impacts how much 
money advertisers pay. Based on the click aggregation results, campaign manage~s 
can control the budget or adjust bidding strategies , such as changing targe~ed a~di-
. d ╖ li d ertising includmg click-ence groups, keywords , etc. The key metrics use m on ne a v ' . 
through rate (CTR) [1] and conversion rate (CVR) [2], depend on aggregated ad click 
data. 
Step 1 -Understand the Problem and Establish Design Scope 
to Clarl.fy requirements and narrow down the The following set of questions helps 
scope. 
I 159 


[Page 164]
Ca ndidate: Wlrnl is thr format of the i11put di-l ta? 
Inter viewer : lt 's a log fl k located in different serve rs ;rnd lh c h l c<..I <Ii< k event~ ~r 
app r ndrd to the e nd of the log file. 111r rvenl has the followi 11g ;1tt11h11lc<;. acl_i; 
click _ t imestamp. user _id, ip, and country. 
Candidate : What's the data volume? 
Interviewer : 1 billion ad clicks per d ay and 2 million ads in to tal. lhc numhcr of ad 
click events grows 303 year-over-year. 
Candi date : What are some of the most╖ imp ortant qu eri es to supp ort'! 
Interviewer : The system needs to supp ort the followi ng 3 q ueries: 
ò Return the number of click events for a particular ad in the last 1'1 minut es. 
ò Return the top 100 most clicked ads in the past 1 minut e. Both param eters should be 
configurab le. Aggregation occurs every minu te. 
ò Supp ort data filtering by ip, user _id, or count ry for the ab ove two queries. 
Candidate : Do we need to worry about edge cases? I can thin k of the following: 
ò There might be events that arrive later than expe cted. 
ò There might be duplicate d events. 
ò Different part s of the system might be down at any tim e, s o we need lo consider 
syste m recovery. 
Interviewe r: That's a good list. Yes, take these into considera tion. 
Candidate: What is the latency requir ement? 
Inte rviewer : A few minute s of end-to-end latency . Note t hat latency requirements 
for RTB and ad click aggregation are very different. Whil e latency for RTB is usually 
less than one second due to the respon siveness requir emen t, a few minu tes ofla tency ts 
acceptable for ad click event aggregation because it is prim arily u sed for ad billing and 
reporting . 
With the information gathered above, we have both functional and non-functional re¡
quirements . 
Functional requirements 
ò Aggregate the number of clicks of ad_id in the last ]\If min ut es. 
ò Return the top 100 most clicked ad_id every minut e. 
ò Support aggregation filtering by different attribu tes. 
ò Datas et volume is at Facebook or Google scale (see the back-of-envell)pe estimation 
section below for detailed system scale requir ements). 
Non-functional requirements 
ò Correctness of the aggregation result is important as the data is used for RTB and 
ads billing. 
160 I Chapt er 6. Ad Click Event Aggregation 


[Page 165]
ò Prope rly handle delayed or duplicate events. 
ò Robustness . The system should be resilient to parlial failures. 
ò Latency requirement. End-to-end latency should be a few minutes, at most. 
Back-of-the-e nvelope estimation 
Let's do an estimation to under stand the scale of the system and the potential challenges 
we will need to a ddress. 
ò 1 billion DAU (Daily Active Users). 
ò Assume on average each user clicks 1 ad per day. That's 1 billion ad click events per 
day. 
109 events ò Ad click QPS = 5 . = 10,000 10 seconds m a day 
ò Assume peak ad click QPS is 5 times the average nwnber. Peak QPS = 50,000 QPS. 
ò Assume a single ad click event occupies O.lKB storage. Daily storage requir ement 
is: O.lKB x 1 billion= lOOGB. The monthly storage requir ement is about 3TB. 
Step 2 - Propose High-level Design and Get Buy-in 
In this section, we discuss query API design, data model, and high-level design . 
Query API design 
The purpose of the API design is to have an agreement between the client and the server. 
In a consumer app, a client is usually the end-user who uses the product. In our case, 
however, a client is the dashboard user (data scientist, product manager, advertiser , etc .) 
who runs queries against the aggregation service. 
Let's review the functional requirements so we can better design the APis: 
ò Aggregate the number of clicks of ad_id in the last l\lf minutes. 
ò Return the top N most clicked ad_ids in the last M minute . 
ò Support aggregation filtering by different attributes. 
We only need two APis to support those three use cases because filtering (the last re¡
quirement) can be supported by adding query parameters to the requests . 
API 1: Aggregate the number of clicks of ad_id in the last l\lf minutes. 
API 
GET /v1/a ds/{:ad_i d}/aggregated_count 
Detail 
Return aggregated event count for 
a given ad_id 
Table 6.1: API for aggregating the number of clicks 
Request parameters are: 
Step 2 - Propose High-level Design and Get Buy- in I 161 


[Page 166]
Fie ld 
from 
to 
Description 
S tart 1;:;Triu~efauTlis now minu s I 111i1111tc) 
End minu te (default is now) 
I ) pc 
1011 1~ 
I ( l ) l II 
I' 
An ident╖ifier for differen t fi lter i1w sl r<l tC'giC's. h l1 t'> l<l11g 
example, filter = 001 filters out non -US click s filter 
Tab le 6.2: Request para meters for /v1/a ds/{:ad _id}/ aggregaL ecl_count 
Response : 
I
r ,,~,~~c ~ 
I o n~ J 
Field Description -
ad_id The identifier of the ad 
count 1h e aggregated count between the start and e nd 
minut es 
Table 6.3: Response for /v1 /ads/ {:ad _ id}/ aggregate d_count 
API 2: Return top N most clicked ad_ids in the last M minutes 
API Det ail 
GET /v1/ads/popular_ads 
Return top N m ost clicked ads in the 
last M minut es 
Table 6.4: API for /v1 /ads / popular _ads 
Request parameters are: 
Field Descr iption Type 
count Top N most clicked ads integer 
window The aggregation window size (l\tf) in minutes integer 
filter An identifier for different filtering s trategies long 
Table 6.5: Request parameters for /v1 / ads/ popula r _ads 
Response: 
-╖-Field Description Type 
ad_ids A list of the most clicked ads array 
Table 6.6: Response for /v1/ads / popul ar _ads 
Data model 
There are two types╖ of data in the system: raw d ata and agg rega ted data . 
Raw data 
Below s hows what the raw data looks like in log files: 
[AdClickEvent] ad001, 2021-01-01 00:00:01, user 1, 207. 148.22 .22, USA 
162 I Chapter 6. Ad Click Event Aggregation 


[Page 167]
Table 6.7 lists wh at th e dala fields look like in a structu red way. Data is sca tter ed o n 
different appli cation s ervers. 
ad_ id click _timestamp user _id ip country 
ad001 2021-01-01 00:00:01 user1 207.148.22.22 USA 
ad001 2021-01-01 00:00:02 user1 207.148.22.22 USA 
ad002 2021-01 -01 00:00:02 user 2 209.153.56.11 USA 
Table 6.7: Raw d ata 
Aggregated data 
Assume that ad click event s are aggregated every minut e. Table 6.8 shows the agg regated 
result. 
ad_id click _minute count 
ad001 202101010000 5 
ad001 202101010001 7 
Table 6.8: Aggr egated data 
To support ad filtering, we add an additional field called filter _id to the tabl e. Reco rds 
with the same ad_id and click_minute are grouped by filter _id as shown in Tabl e 6.9, 
and filters are defined in Table 6.10. 
ad_id click_minute filter_id count 
ad001 202101010000 0012 2 
ad001 202101010000 0023 3 
ad001 202101010001 0012 1 
ad001 202101010001 0023 6 
Table 6. 9: Aggregated data with filters 
filter _id region lp user_id 
0012 us 0012 * 0013 * 0023 123.1.2.3 
Table 6.10: Filter table 
To suppor t the query to return the top N most clicked ads in the last M minut es, the 
following structure is used. 
Step 2 - Propose High-level Design and Get Buy-in I 163 


[Page 168]
~----╖ 
. -- ---.. 
l,r - -- _-z...; 
ò .. ... ~ -.:::=--.-
ò -~<e.:a ni rh ~ 7:e st.1,o:3 as...& 1l:f ~ s!zc o: +r ~ .-:~ -;:: :s i--_;-~ 
...::E ~ s!Le -::bs c::::a: .:.___ ~ò ~ d!rertk- n=rT !neffi.cie=L . o _:_::.;::-~~ ~ - .. - - - -
- ò t3~ ..-e !G:3. :rd.~ c:@iegc 1t=d &ta 
like? Is the de.ta reJati.onal? Is it a document or a blob? 
ò -~ ~ ~ ~-, write-heaYy, OT both? 
.. - c ~ suppcn oeedro? 
ò J.: :.:::z _~-5 rel}╖ en many online analrtical processing (OLAP) functions {3} like 
7_1"~ COC'T? 
........ 


[Page 169]
Let's examine the raw data first. Even though we don 't need to query the raw data during 
normal operatio ns, it is useful for data scienti sts or machine learn ing engineers to s tudy 
user response prediction, behavi oral tai╖geting, relevance feedback, etc. [ 4]. 
As shown in the back of the envelope estimation, the average write QPS is 10,000 , and 
the peak QPS can be 50,000, so the syst em is writ e-heavy. On the read side, raw data is 
used as backup and a source for recal culation, so in theory, the read volume is low. 
Relational databases can do the job, but scaling the write can be challenging. NoSQL 
databases like Cassandra and InfluxDB are more suitable because they are optimized for 
write and time -range queries. 
Another option is to store the data in Amazon S3 using one of the column ar data formats 
like ORC [5], Parquet [ 6], or AVRO [7). We could put a cap on the size of each file (say, 
lOGB) and the stream processor responsible for writin g the raw data could handl e the 
file rotatio n when the size cap is reached. Since this setup may be unfamiliar for many, 
in this design we use Cassandra as an examp le. 
For aggregated data, it is time-series in nature and the workflow is both read and write 
heavy. This is because, for each ad, we need to query the database every minute to display 
the latest aggregation count for customers. This featur e is useful for auto-refreshi ng the 
dashboard or triggering alerts in a timely manner . Since there are two million ads in 
total , the workflow is read-heavy. Data is aggregated and writt en every minute by the 
aggregation service, so it's write-heavy as well. We could use the same type of databas e 
to store both raw data and aggregated data. 
Now we have disc ussed query API design and data model, let's put together the high-level 
design. 
High-level design 
In real-time big data [8] processin g, data usually flows into and out of the pro cess ing 
system as unbounded data streams. The aggregation service works in the same way; the 
input is the raw data (unbounded data streams), and the output is the aggregated results 
(see Figure 6.2). 
Input 
' ' 
Process Output 
' ' AJJ COlJ"lt : 
Display 
~Pus~data 
Data 
Aggrega tion 
Service 
! Databas --Qu~ry~ 
(AggregatefNorym ln) E : ~ 
ToP 100 most cllci<od Ads , 
.___ __ __. (Aggn>Qale fN&ry min) : 
' ' ' ' 
Figure 6.2: Aggregation workflow 
Asynchronous processing 
╖ tl h ╖ synchronou s This is not good because the capacity of The design we curren y ave is ╖ ╖ ╖ . . . 
d ╖ t alwa ys equal Consider the followmg case; if there is a producers an consumers is no ╖ . ╖ ╖ affi d th umb er of events produced 1s far beyond what con -sudden increase m tr c an e n . 
dl ╖ ht get out-of-memory errors or expenenc e an unex -sumers can han e, consumers nug 
Step 2 _ Propose High-level Design and Get Buy-in I 165 


[Page 170]
prctrd shutdown. Jf one component in the synchron ous link 1c:; do w n. !he whole systrrn 
stops workin g. 
A common solution is lo adopl a message queue (Kafka) to decouple producer s and ron 
sumers. lhis makes the whole process async hronous and prnou ce rs/consumers can he 
scaled independen tly. 
Pul1ing everyth ing we have discussed together, we come up wi lh th e high-level design 
as shown in Figure 6.3. Log watcher. aggrega tion service, and dritabase arc decoupled by 
two message queues. The database writer polls data from the message queue , transforms 
Lhe data into the database formal, and writes it to the database. 
Log Watcher ,__ _ _ Message 
Queue 
Raw data 
database 
Database 
Writer 
Data 
Aggregation 
Service 
Ad count 
(Aggregate every min) 
Top 100 most clic ked Ads 
(Aggregat e every min) 
Figure 6.3: High-level design 
Message 
Queue 
Pull aggregation results 
Databa se 
Writer 
Aggregation 
database 
Query aggreg ation results 
I 
Query 
Service 
(Dashboa rd) 
W h at i s s tored in the first message queue? It contain s a d click event data as shown in 
Tab le 6.13. 
ad_id click_timestamp user_id ip country 
Table 6.13: Data in the first messag e queue 
What is s tored in the second message queue? The second message queue contains two 
typ es of data; 
1. Ad click counts aggregated at per-minute granularity . 
I ad_id I click_minut e I count I 
Table 6.14: Data in the second message queue 
166 I Chapte r 6. Ad Click Event Aggregation 
ad 


[Page 171]
. -
2. Top .rv╖ most clicked ads aggregated at pcr -minutr granu larity. 
I upda.t e_time _ynhmtr l most_clirkrd _ads l 
Table 6.15: Data in th e second message queue 
You migh t be won dering why we don 't write the aggregated results to the dat(lha sc di ¡
rt'rtly . 1l1e sh ort answer is that we need th e second message queue like Kafka lo Rchi eve 
rnd -to-cnd exac tJy once semantics (atomic comm it) [9]. 
,------------ -------------- ------------ -------------------------------------- - -- - ~ 
Atomic commit ' 
Log Watcher 1----'-- ..i 
Message 
Queue 
Ad count 
(Aggregate IYVery min) 
Message 
Queue 
Data 
Aggregation 
Service Top 100 most clocked Ads __......__-r- _ _,._,, 
(Aggrega1e every min) ' ' ' ---------------------- -------------------------------------- ----------ò 
Raw data 
database 
Database 
Writer 
Figure 6.4: End -to- end exactly once 
Next, let's dig into the details of the aggregation service. 
Aggregation service 
Pull aggregation results 
Database 
Writer 
Aggregation 
database 
Query aggregation results 
I 
Query 
Service 
(Dashboard) 
The MapReduce framework is a good option to aggrega te ad click events. The directed 
acyclic graph (DAG) is a good model for it [10]. The key to the DAG mod el is to break 
down the system into small computing unit s, like the Map/Aggregate /Reduc e nodes, as 
shown in Figure 6.5. 
Step 2 - Propose High-level Design and Get Buy-in I 16 7 


[Page 172]
Data 
Input 
' ' 
Data 
Input 
Aggregate every minute 
~~òAd count 
' ,_ -- ----- -- - - ---- -.. -------- ------ - -- -- -
Aggregation Service 
Top 100 aggregati on 
------------------------------------------------------------- ' 
, _____ ____________________________ ____________________________ . 
Aggregation Service 
Figure 6.5: Aggregation service 
Each node is responsible for one single task and it sends the proces sing result to its 
downstream nodes. 
Map node 
A Map node reads data from a data source, and then filters and transfo rms the data. For 
example, a Map node sends ads with ad_id 3 2 = 0 to nod e 1, and the other ads go to 
node 2, as shown in Figure 6.6. 
168 I Chapter 6. Ad Click Event Aggregation 


[Page 173]
1--
ad_id %2 = 0 
ad_ld %2 = 1 
Figur e 6.6: Map operation 
You might be wondering why we need the Map node. An alternative option is to set 
up Kafka partitions or tags and let the aggregate nodes subscribe to Kafka directly . This 
works, but the input data may need to be cleaned or normalized, and these operations 
can be done by the Map node . Another reason is that we may not have contro l over how 
data is produced and therefore events with the same ad_id might land in different Kafka 
partitions. 
Aggregate node 
An Aggregate node counts ad click events by ad_id in memory every minute. In the 
MapReduce paradigm, the Aggregate node is part of the Reduce. So the map-aggregate¡
reduce process really means map -reduc e-redu ce. 
Reduce node 
A Reduce node reduces aggregated results from all "Aggregate" nodes to the final result. 
For example, as shown in Figure 6. 7, ther e are three aggregation nodes and each contains 
the top 3 most clicked ads within the node . The Reduce node reduces the total number 
of most clicked ads to 3. 
Step 2 - Propose High-level Design and Get Buy -in I 169 


[Page 174]
Aggregate Reduce 
ad1: 12 
ad3: 5 
ad2: 3 
ad?: 9 ad1 : 12 
Task: get top 3 ad10: 4 ~--1 ad?: 9 ~--_. 
ad8: 3 ad13: 8 
ad13: 8 
ad11: 4 
ad15: 3 
Figure 6.7: Reduce nod e 
Outpu t 
Top 3 most clic ked 
ads from the last 
min ute are ad 1, ad? 
and ad 13 
111e DAG model represents the well-known MapReduce paradigm. I l i s desig ned to take 
big data and use parallel distributed computin g to turn big data in lo littl e- or regular-sized 
data . 
In the DAG model, intermediate data can be stored in memory and different nodes com¡
municate with each other through either TCP (nodes runnin g in different processes) or 
shared memory (nodes running in different thread s). 
Main use cases 
Now that we understand how MapReduce works at the high level, let 's take a look at 
how it can be utilized to support the main use cases: 
ò Aggregate the number of clicks of ad_id in the last Alf mins. 
ò Return top N most clicked ad_ids in the last Jvf minut es. 
ò Data filtering. 
Use case 1: aggregate the number of clicks 
As shown in Figure 6.8, input events are partitioned by ad_id (ad_id 3 3) in Map nodes 
and are then aggregated by Aggregation nodes . 
1 70 I Chapter 6. Ad Click Event Aggregation 


[Page 175]
"\ Events with ad_ld = 3 Inputs Map Aggregate Outputs 
('> Events with ad_ld = 1 
' 
0 Events with ad_ld = 2 ' 
00 ' 
J-: 00 0000 ad3 was clicked 4 times 
In the past 1 minute 
' ' 
00 Cilek count 
000 I-+ .. ad 1 was clicked 3 times (Minute interval All Events 
OD aggregation) : In the past 1 minut e 
' ' I 
' ' 
DO ~ ad2 was clicked 5 time!! 
DO 
In the past 1 minute 
I 
Figure 6.8: Aggregate the number of clicks 
Use case 2: retu rn top N most clicked ads 
Figure 6.9 shows a simplified design of getting the top 3 most clicked ads, which can 
be extended to top N. Input events are mapped using ad_id and each Aggregate nod e 
maintains a heap data structure to get the top 3 ads within the node efficiently. In the 
last step, the Reduce nod e reduces 9 ads (top 3 from each aggregate node) to the top 3 
most clicked ads every minut e. 
Inputs 
Top 3 most 
clicked ads 
(Minute interval 
aggregation) '---~~ 
Map Aggregate 
ad3: 12 
ad6: 5 
Events: ad3, ad6, ,____,._.__.. adS: 3 ad9, ad12,ad15 ed12. 1 
Events: ed1 , ad4, 1---;.-...i 
ad7,ad10, ad13 
Events: ad2,ad5, 1---;.-...i 
ad8,ad11 , ad14 
ae16: 1 
ad1: 9 
ad4: 4 
ad7: 3 1--...;..._ ...i ..... ..u....-..4... 
ad10 . 2 
ed13. 1 
ad2: 8 
ad5: 4 
ed8: 3 
0011 : 2 
aa14 : 1 
Outputs 
Top 3 most clicked 
ads in the past 1 
minutes are ad3 , 
ad1 and ad2 
Figure 6.9: Return top N most clicked ads 
Use case 3: data filtering 
To support data filtering like "show me the aggregated click count for adOOl within the 
USA only", we can pre -define filtering criteria and aggregate based on them. For example , 
the aggregatio n results look like this for ad001 and ad002: 
Step 2 - Propose High-level Design and Get Buy-in I 171 
-


[Page 176]
ad_id click _minute 
ad001 202101010001 
ad001 202101010001 
ad001 202101010001 
ad002 202101010001 
ad002 202101010001 
ad002 202101010001 
-
country 
USA 
GPB 
-
others 
USA 
GPB 
-
others 
~ 
count 
I 00 
20() 
:moo 
1 () 
2G 
12 
Table 6.16: Aggregation results (filter by countr y) 
1his technique is called the star schema [11], w hich is widely used in data warehouses 
The filtering fields are called dimensions . This approach has the followin g hcncfils: 
ò It is simple to understand and build . 
ò The curre nt aggregation service can be reused to create more djm ensions in the star 
schema . No additional compon ent is need ed. 
ò Accessing data based on filtering c riteria is fast because the result is pre-calculated. 
A limitation with this approach is that it creates many mor e bucket s and records, espe¡
cially when we have a lot of filtering criteria . 
Step 3 - Design Deep Dive 
In this section, we will dive deep into the followin g: 
ò Streaming vs batching 
ò Time and aggregation window 
ò Delivery guarantees 
ò Scale the system 
ò Data monitoring and correctness 
ò Final design diagram 
ò Fault tolerance 
Streaming vs batching 
The high -level architecture we proposed in Figure 6.3 is a typ e of stream processing sys¡
tem. Table 6.17 shows the comparison of thre e typ es of systems [ 12] : 
172 I Chapter 6. Ad Click Event Aggregation 
-


[Page 177]
Services Batch system Streaming system 
(Online (offlin e system) (near real -time 
system) system) 
Respon d to No respon se to the No response to the Responsiveness the client 
quickly client needed client needed 
Bounded input with Input has no 
Inp ut User requests finite size. A large boundary (infinite 
amoun t of data streams) 
Responses to Materialized views, Materialized views, 
Output aggrega ted metrics, aggregated metrics, clients etc. etc. 
Performance Availability, Throughput Throughput , latency measurement latency 
Example Onlin e MapReduce Flink [13] shopping 
Table 6.17: Comparis on of three types of systems 
In our design, both stream processing and batch processing are used. We utilized stream 
processing to process data as it arrives and generates aggregated results in a near real ¡
time fashion. We utilized batch processin g for historical data backup. 
For a system that contains two pro cessing paths (batch and streaming) simultaneously, 
this architecture is called lambda [14]. A disadvantage of lambda architecture is t hat 
you have two processing paths , meanin g there are two codebases to maintain. Kappa 
architecture [15], which combines the batch and streaming in one processing path, solves 
the problem. The key idea is to handle both real-time data processing and continu ous data 
reprocessing using a single stream processing engine. Figure 6.10 shows a compar ison 
of lambda and kappa architecture. 
Step 3 - Design Deep Dive I 173 


[Page 178]
Lambda Architec ture 
0 1- -
' 
iLJ 
: Raw Data 
Batch Layer 
..-------~ 
Batch Engine 
---------- - ---- -' '. Streaming Layer 
'.------.....,..-
Data Storage 
' ' 
' ' 
Serving Layer 
: I Serv ing Backend J .. : 
Result s 
'--------- ----------------------------------------------------------------
Kappa Architect ure 
r--- -- --------~--
Streaming Layer Serving Layer 
[ OueryJ 
' 
01--- +1ò ( ( )t---_..,~.;-1 -Re-a-1-t-im_e_E-ng-ln-e~J~~ -------.-1~ .. 1 Serv ing Backend , ... ,~--.! Query I 
~--~ ╖---------╖--╖--------' . -- - --- ----- -- ---- ----
---------------------------- ---------------------------------- -------------╖ ' ' 
\ LJ Data Storage LJ : 
: ~~ ~~ : 
~----------------------- ---------------------------------------- -- --- ------' ' ' --- ---- ------ ------------- ------------------ ----------- ------------ -------------------------- ----------------- ---------╖ 
Figure 6.10: Lambd a and Kappa architec tu r es 
Our high-level design uses Kappa architectur e, where the repro cess ing o f historical data 
als o g oes through the real-time aggregation service . See the "Data recalc ulation" section 
below for details. 
Data recalculation 
Sometimes we have to recalculate the agg regated data, also call ed historical data replay. 
For example , if we discover a major bug in the agg rega tion servi ce, we wo uld need to 
recalculate the aggregated data from raw d ata s tartin g a t the po int where t he bug was 
introduced. Figure 6.11 shows the data recalculation flow: 
1. The recalculation service retriev es data from raw data s torage. 1hi s is a batched job. 
2. Retrieved data is sent to a dedicated aggregation service so that the real-Lime pro¡
cessing is not impact ed by histori cal data replay. 
3. Aggregated results are sent to the second message queue, then u pda ted in the aggre¡
gation database. 
174 I Chapter 6. Ad Click Event Aggregation 


[Page 179]
~-╖ ~ Messag e 
[~ Queue 
Raw data 
database 
Data 
Aggregatio n 
Service 
Databa se 
Writer 
Tap \00 motl còd(M Ad~-"'----~~ 
(llggrog1\1 òvory mini 
Data Aggregation 
Service 
_ fl:le_ca!~~╖~ot!o~ only) 
Figure 6.11: Recalculation service 
Poll 
aggregation 
result 
.I Database j L Writer 
l 
1 11ggreq11tlon 
J databll9P. 
Query eggreqAtlon result 
1he recalculation process reuses the data aggregation service but uses a different dat a 
ource (the raw data) . 
Time 
We need a timestamp to perform aggregation. The timestamp can be genera ted in two 
different places: 
ò Event time: when an ad click happens. 
ò Processing time: refers to the system time of the aggregation server that proc esses 
the click event. 
Due to network delays and asynchronous environments (data go through a message 
queue), the gap between event time and processing time can be large. As shown in Figure 
6.12, event 1 arrives at the aggregation service very late (5 hours later). 
5 hours later 
90 Second 
Event Time 
Processing Time ..-----..---- -,..-,«-@-r-- --11 .. - ------ ------ 1 _.,.. 
Figure 6.12: Late events 
If event time is used for aggregation , we have to deal with delayed events. If processing 
time is used for aggregation, the aggregation result may not be accurate . There is no 
perfect solution, so we need to consider the trade-offs. 
Step 3 - Design Deep Dive I 175 
-


[Page 180]
- - -Pros Cons -It depend s on Lhc time slamp 
Aggregation results are more generated on the clienl -side. 
Event accurate because Lhe client Clien ts might have the wrong 
time knows exactly when an ad is time, or the limestamp might 
clicked be genera ted by mali cious 
users 
Processing Server timestamp is more 1he timestamp is nol accura te 
if an even t reaches the sys tem time reliable at a much lat er lim e 
Table 6.18: Event time vs pro cessing tim e 
Since data accuracy is ve1y important , we recommend using eve nt time for aggrega tion. 
How do we properly process delayed events in this case ? A techniqu e called "wa termark" 
is commo nly utilized to handle slightly delayed events. 
In Figure 6.13, ad click events are aggregated in the one-minute tumblin g wind ow (see 
the "Aggregation window" section on page 177 for more detail s). If even t time is used 
to decide whether the event is in the window , wind ow 1 misses eve nt 2, and window 3 
misses event 5 because they arrive slightly later than the e nd of their aggregatio n win¡
dows. 
0 90 120 180 Second 
Event Time ' 
I I 
I 
I 
Process ing Time ' 
I 4 5 
I 
I 
I I 
Window 1 I CD I 
I 
l 
Window2 : « 
I 
I 
0 Window3 
I 
I 
I 
I 
Figure 6.13: Miss events in an aggregation window 
One way to mitigate this problem is to use "watermark " (the extended rectang les in Fig¡
ure 6.14), which is regarded as an extension of an aggrega tion window . This improves 
the accuracy of the aggregation result. By extendin g an extra 15 seco nd (adjustable) ag¡
gregation window, window 1 is able to include event 2. and wind ow 3 is able to includ e 
event 5. 
The value set for the watermark depends on the busin ess requir ement. A long watermark 
could catch events that arrive very late, but it adds more latency to the sys tem. A short 
watermark means data is less accurate, but it adds less latency to the sys tem. 
17 6 I Chapter 6. Ad Click Event Aggregation 
d 


[Page 181]
90 1 ~0 ⌐ 150 « 110 Second 
I I 
ò I 
I I 
I I 
Processing Time ⌐: 
I 
5 I 
I 
I 
I 
Window 1 CD !0 1 
Window 2 « 
Window3 ⌐ ⌐ 
Figure 6.14: Watermark 
Notice that the watermark technique does not handle events that have long delays. We 
can argue that it is not worth the return on investment (ROI) to have a complicated 
design for low probability events. We can always correct the tiny bit of inaccuracy with 
end-of-day reconciliation (see "Reconciliation " section on page 189). One trade-off to 
consider is that using watermark improves data accuracy but increases overall latency , 
due to extended wait time. 
Aggregation window 
According to the "Designing data-intensive applications" book by Martin Kleppmann 
[16], there are four types of window functions: tumbling window (also called fixed win ¡
dow), hopping window, sliding window, and session window. We will discuss the tum ¡
bling window and sliding window as they are most relevant to our system. 
In the tumbling window (highlighted in Figure 6.15), time is partitioned into same-length, 
non-overlapping chunks. The tumbling window is a good fit for aggregating ad click 
events every minute (use case 1). 
Tumbling Window 
(1 minute window) 
1 
I 
Aggregate 
click count 
2 
I 
Aggregate 
click count 
3 
I 
Aggregate 
click count 
4 
I 
Figure 6.15: Tumbling window 
Aggregate 
click count 
5 
I 
Minute 
In the sliding window (highlighted in Figure 6.16), events are grouped within a window 
that slides across the data stream, according to a specified interval. A sliding window 
can be an overlapping one. This is a good strategy to satisfy our second use case; to get 
the top N most clicked ads during the last M minutes. 
Step 3 - Design Deep Dive I 177 


[Page 182]
Sliding window 
(3 minute window , 
Run every minut e) 
1 
I 
Delivery guarantees 
2 3 4 5 Minute 
I I I I 
Top ads from last 3 minute s 
Top ads from last 3 minute s 
Figure 6.16: Slidin g wind ow 
Since the aggregation r esult is utilized for billing, data acc uracy and co mpleteness are 
very imp ortant. The system needs to be able to a nswer ques tions such as: 
ò How to avoid processing duplicate events? 
ò How to ensure all events are processe d? 
Mess age queues such as Kafka usually provid e three deliver y sem antics: at-most once, 
at-least once, and exactly once. 
Which delivery method should we choose? 
In most circumstances , at-least once pro cessing is good enough if a s mall percentage of 
duplicates are acceptable. 
H owever , this is not the case for our system. Differe nces of a few percent in data points 
could result in discrepancies of millions of dollars. Therefore, w e recommend exaclly¡
once delivery for the system. If you are interested in learning more a bout a real-life ad 
aggregation system, take a look at how Yelp implements it [1 7]. 
Data deduplication 
One of the most common data quality issues is dupli cated data. Duplicated data can come 
from a wide range of sources and in this section, we discuss two common sources. 
ò Client-side. For example, a client might resend the s ame event multipl e times. Du¡
plicated events sent with malicious int ent are best handl ed b y a d fraud/risk control 
components. If this is of interest, please refer to the reference material [18). 
ò Server outage. If an aggregatio n service nod e goes down in the middl e of aggregation 
and the upstream service hasn 't yet received an acknowledgment, the same events 
might be sent and aggregated again. Let's take a closer look. 
Figure 6.17 shows how the aggregation service node (Aggrcgator) outage introdu ces du¡
plicate data. The Aggregator manages the status of data consumpti on by storing the 
offse t in upstream Kafka. 
178 I Chapter 6. Ad Click Event Aggregation 


[Page 183]
Upstream 
(Kafka ) 
,..... 
-. ~ 
-. ~ 
Aggregator 
' 1. Poll events ' ' 
2. Consume from 
Downstream 
(Kafka) 
offset 100 
~ 3. Aggregate events 
- from 100 to 110 ' ' I 
I 
' I 
I -
I 
~ I 
I 4. Send aggregated 
I 
I 
I 
result ' ~ ' -
6. Ack upstream 5. Ack back 
-with offset 110 , 
~ 
I 
I 
" ò 
I 
Data duplication 
if system failed at step 6 
and consume again from offset 100 
Figure 6.17: Duplicate data 
If step 6 fails, perhaps due to Aggregator outage, events from 100 to 110 are already sent 
to the downstream, but the new offset 11 O is not persisted in upstream Kafka. In this case, 
a new Aggregator would consume again from offset 100, even if those events are already 
processed, causing duplicat e data . 
' --
The most straightforward solution (Figure 6.18) is to use external file storage, such as 
HDFS or S3, to record the offset. However, this solution has issues as well. 
Step 3 - Design Deep Dive I 179 


[Page 184]



[Page 185]
Upstrea,.,, 
( Kaf\ca) ( Aggregator ) [ HDFS I SJ 
I 
' ' . 
' 
- : ' 1 Poll events ' ,_ . ' ' - ' 2 Consume from ' ' offset 100 ' - . . ' ' ~ ' /or1' ~ r.ffc,,at ' . 
3. Aggregate events 
from 100 to 110 
-
3 7. Save cffset -- .T 
Can cause potPn tl 
message loss ; 
' ' ' 4 . Send agg regated resu lt 
6. Ack upstream 5. Ack back 
with new offset 110 ~ 
' 
- ' 
Figure 6.18: Record the offset 
' ' 
: 
' 
' ' ' 
' ' ' 
' 
. 
' ' -~ 
╖-1 I 
' ' 
In step 3, the aggregator will process events from offset 100 to 110, only if the last offset 
stored in external storage is 100. If the offset stored in the storage is 110, the aggregator 
ignores events before offset 110. 
But this design has a major problem: the offset is saved to HDFS or S3 (step 3.2) before the 
aggregation result is sent downstream . If step 4 fails due to Aggreg ator outage, events 
from 100 to 110 will never be processed by a newly brought up aggregator node, since 
the offset stored in external storage is 110. 
To avoid data loss, we need to save the offset once we get an acknowledgment back from 
d owns tream. The updated design is shown in Figure 6.19. 
----- ------ -----
180 I Chapter 6. Ad Click Event Aggregation 


[Page 186]
Upstream 
(Kafka) 
1. Poll events 
2. Consume from 
offset 100 
6. Ack upstream 
Agg regato r [ HDFS / 53 J 
. 
3.1 Verify offset 
""U 
3. Aggregate events : 
i----fr_om 100 to 110 ! 
~ : 
~'~>---~--- : 
4. Send aggregated result 
5. Ack back 
1~ 
5 .1 Save offset . ' 
u 
_ with new offset 110 
' ' ' ' ' 
Figure 6.19: Save off set after receiving ack 
Downstream 
(Kafka) 
In this design, if the Aggregator is down before step 5.1 is executed, events from 100 
to 110 will be sent downstream again. To achieve exactly once processing , we need to 
put operations between step 4 to step 6 in one distributed transaction. A distributed 
transaction is a transaction that works across several nodes. If any of the operations 
fails, the whole transaction is rolled back. 
Step 3 - Design Deep Dive I 181 


[Page 187]
Upstream 
(Kafka) Aggregator 
L 
Downstream 
(Kafka) 
1. Poll events 
2. Consume from 
offset 100 
7. Ack upstream 
~ with new offset 110 
I 
I 
' I 
' I 
I 
I 
' I 
' I 
3.1 Veri fy orrscl : 
3 . Aggrcgot e event~! 
r---.:.:...fro:::.:.m l 00 to l1 O : 
I 
. 
4. Send 0991╖ gal J result 
5. Save offset 
LI 
I 
' 
6. Ack bock 
' ' ' ' ' I 
I 
I 
I 
I 
I 
.. - - .... - .... - ò t t 
' ' : .. ) . -- r.,.. 
' ' 
' 
' 
' ' I 
I 
I 
' ' 
I o 
,.,. ,..,.,.,. . ............ M òò- ╖ ~ ----òòòò-,.ò---~---ò-òò òò' : 
o I 
I I 
Figure 6.20: Distribut ed lrnnsnclion 
As you can see> it's not easy' to dedupe data in la rge~scR l e sys tems. I low Lo a chieve 
exac tly-once processing is an advanced topic. If you are int╖erested in lhc details, please 
refer to refer ence material [9]. 
Scale the system 
From the back-of-the-envelope estimation, we know the busin ess grow s 303 per year, 
which doubles traffic every 3 years. H ow d o we handle t his g row th? Lel's take a 
look. 
Our syst em consists of three independent components: messa ge que ue, aggrega tion ser¡
vice , and database . Since these components are decoupled, we can scale each one inde¡
pendently . 
Scale the message queue 
We have already discussed how to scale the message queue exten sively in the "Distributed 
Message Qyeue" chapter, so we'll only briefly touch on a few point s. 
Producers . We don't limit the number of produ cer inst ances, so the s calability of pro¡
ducers can be easily achieved. 
Consumers. Inside a consumer group, the rebalancin g mechanism h elps to scale the 
consumers by adding or removing nodes. As shown in Figure 6.2 1, by adding two more 
consume rs, each consumer only processes events from one partition. 
- -
182 I Chapter 6. Ad Click Event Aggregation 


[Page 188]
---------------- -------------- ---------~ I r------- --------------------------------~ 
Topic 
I 
Topic : 
I 
Partition 0 Partition 0 ~ I Consumer 0 I 
Partition 1 
Rebalance Partition 1 I Consumer 1 
Partition 2 Partition 2 I Consumer 2 I 
Partition 3 Partition 3 I Consumer 3 I 
I 
~---- ---------- - - - - ------ - - ------- - -----J ~---- --------- - ------ - -- - ---------------
Figure 6.21: Add consumers 
\Vhen there are hundred s of Kafka consumers in the system, consumer rebalance can be 
quite slow and could take a few minu tes or even m ore. Therefore, if more consum ers 
need to be added , try to do it durin g off-peak hours to minimize the imp act. 
Brokers 
ò Hashing key 
Using ad_id as hashing key for Kafka partition to store events from the same ad_i d 
in the same Kafka partition . In this case, an aggregation service can subscribe to all 
events of the same ad_id from one single partit ion. 
ò The number of partitions 
If the number of partitions chan ges, events of the same ad_ id might be mapped to a 
different partition. Ther efore , it's recommended to pre-allocate enough partiti ons in 
advance, to avoid dynamically incr easing the number of partitions in production. 
ò Topic physi cal sharding 
One single topic is usually not enough. We c an split the data by geog raphy 
(topic_north_ america , topic_europe , topic _asia , e tc.) or by business type 
(topic_web_ads,topic_mobile_ads , etc). 
o Pros: Slicing data to different topics can help increase the system throughput. 
With fewer consumers for a single topic, the time to rebalance consumer groups 
is reduced . 
o Cons: It introduces extra complexity and increases maintenance costs. 
Scale the aggregation service 
In the high-level design, we talked about the aggregation service being a map/reduce 
operation. Figure 6.22 shows how things are wired together. 
Step 3 - Design Deep Dive I 183 


[Page 189]
Map Calculation 
Aggregation Server 1 
Kafka Map process 
Aggregation Server 2 
( Kafka ( )1--_,.,~, Map process 
Aggregation Server 3 
Kafka Map process 
Map 
Output 
Reduce 
Input 
Figure 6.22: Aggregation service 
Redu ce 
Calculation 
Aggregation Server 1 
Aggregation Server 3 
Redu ce proces s 
Reduce 
Output 
D 
If you are interested in the details, please refer to reference mat erial [ 19]. Aggrega¡
tion service is horizontally scalable by adding or removing nodes. Here is an interesting 
question ; how do we increase the throughput of the aggregation servic e? There are two 
options. 
Option 1: Allocate events with different ad_ids to different threads , as s hown in Figure 
6.23. 
184 I Chapter 6. Ad Click Event Aggregation 


[Page 190]
All Events 
Kafka 
r-------- ----- ----------1 ----------- -
: Aggreg ation Service Node 
-- . 
' 
Events of ad id 
From 1to 3 
Threads 
thread_id = 2 
ad_id = 2 
, ______________ ______ _______________________________ : 
r---------------------------------- --------------- --
Events of ad_id 
From 4 to 6 
Aggregation Service Node 
thread_id = 2 
ad_id = 5 
Threads 
--------------------------------------------------
Figure 6.23: Multi-threadin g 
I 
Option 2: Deploy aggregation service nodes on resouxce providers like Apache Hadoop 
YARN (20]. You can think of this approach as utilizing multi-pro cessing. 
Option 1 is easier to imp lement and doesn 't depend on resource provid ers. In reality , 
however, option 2 is more widely used becaus e we can scale the system by adding more 
computing resources. 
Scale the database 
~assandra native ly supports horizontal scalin g, in a way similar to consistent hash¡
ing. 
-- - -- Step 3 - Design Deep Dive I 185 


[Page 191]
Node I Node 2 
.CD 
╖CQCD 
Node4 Node 5 
Node I Node 2 
Node 4 Node S 
Figure 6.24: Virtual nodes [21] 
N ode 3 
0 00 
Node 6 
Node 3 
00 
0(~} 
00 ╖GJGJ. 
Node 6 
Data is evenly distributed to every node with a proper replication factor. Each node saves 
its own part of the ring based on hashed value and also saves cop ies from other virtual 
n odes. 
If we add a new node to the cluster, it autom atically rebalances the vir tual nodes among 
all nodes. No manual resharding is required. See Cassa ndr a's officia l documentation for 
more details [21]. 
Hotspot issue 
A shard or service that receives much more data than the oth ers is cal led a hotspot. This 
occurs because major companies have advertising budgets in the milli ons of dollars and 
their ads are clicked more often. Since events are partiti oned by ad_i d. some aggregation 
servi ce nodes might receive many more ad click events than others, pote nt ially causing 
server over load. 
Th.is problem can be mitigated by allocating more aggregati on n odes to process popular 
ads. Let's take a look at an example as shown in Figure 6.25. Assume each aggregation 
node c an handl e only 100 events. 
1. Since there are 300 events in the aggregation n ode (beyond the capacity of a node 
can handle) , it applies for extra resources through the resource manager . 
2. The resour ce manager allocates more resources (for examp le, add l wo m ore aggre¡
gation nodes) so the original aggregation node isn't overloaded. 
186 I Chapter 6. Ad Click Event Aggregation 


[Page 192]
3. TI1c original aggregation node split events into ~{ gro ups and each aggregation n ode 
handles 100 events. 
4. 111e result is written back to the original aggregate node. 
Data 
Input 
Resource 
Manager 
' ' ' ' ' 
Extra 
-------« resource 
allocated 
' ' ' 
~ - - ---- -- ------------------- -- - - ------. I I 
I 
I 
I 
I 
I 
I 
I 
I _____ _ .., 
I 
I 
I 
I 
I 
I 
I 
I ,,, 
,' I 
, I 
100 events 
8-1 00~╖~ 
100 events 
f.\ Apply for 
\...!../ extra 
resources 
@Y- i 
Split events -- -- - - - - ;,.. - - - --- - - - - - - - - - - -- -- - - - - -- - _, , 
' ' ' ' ' ' ' 
' I 
' , 
I 
I 
, 
0 ' 
Reduced result 
Figure 6.25: Allocate more aggregation nodes 
Aggregated _. 
Output 
There are more sophisticated ways to handle this problem, such as Global-Local Aggre¡
gation or Split Distinct Aggregation. For more information , please refer to [22]. 
Fault tolerance 
Let's discuss the fault tolerance of the aggregation service. Since aggregation happens 
in memory, when an aggregation node goes down, the aggregated result is lost as well. 
We can rebuild the count by replaying events from upstream Kafka brokers. 
Replaying data from the beginning of Kafka is slow. A good practice is to save the "system 
status" like upstream offset to a snapshot and recover from the last saved status. In our 
design, the "system status" is more than just the upstream offset because we need to store 
data like top N most clicked ads in the past M minutes. 
Figure 6.26 shows a simple example of what the data looks like in a snapshot. 
Step 3 - Design Deep Dive I 187 


[Page 193]
Snapshot for top 3 mos t cl1ckP.d F1cls from l<1st 5 m1m1tP'\ 
Message 
Queue 
Data 
...___ 1 Aggregation 
Service 
r - -
ad1. 12 ò ad1 f 1 13 r? r 3 j .1] 
ad3: 5 - ò ad3. [ 1 [ 1 r 3 l 0 r 0 l 
ad2. 3--- ò ad2 ["o r2 f o I 1 IºJ 
' '--- ----- --- --------- - ---╖ -- ------╖- ..... 
Figure 6.26: Data in a s napshot 
I I I I I 
1 2 3 4 5 
With a snapshot, the failover process of the aggrega tio n service is q uit e simple. If one 
aggrega tion service node fails, we bring up a new node and r ecove r d ata from the lat╖ 
est snapshot (Figure 6.27). If there a re new events that arr ive a fter the last snapshot 
was taken, the new aggregation node will pull those data fro m the Kafka broker for re╖ 
play. 
, ' , 
x 
, , 
, 
' 
, 
External 
Nodes 
, , , , 
Primary _A New 
~a_g_g~-~g_d~_tio_n_, - - ln~~:;;~~I --l___J--- --- -- -------òL-a-gg-~-~-~a-et_io_n_, 
Snapshot 
Storage 
Figure 6.27: Aggregation n ode failover 
Data monitoring and correctness 
As menti oned earlier, aggregation results can be used for RTB and billing purp oses. It's 
criti cal to monitor the system's health and to ensur e cor rec tness. 
Continuous monitoring 
Here are some metrics we might want to monit or: 
ò Latency. Since latency can be introdu ced at each stage , it's invalu able to track times¡
tamp s as events flow through different parts of the sys tem. The differences between 
those timestamps can be exposed as latency metrics. 
ò Message queue size. If there is a sudden increase in queue size, we may need to add 
more aggregation nodes. Notice that Kafka is a message queue implemented as a 
distribut ed commit log, so we need to monitor the record s-lag metri cs instead. 
188 I Chapter 6. Ad Click Event Aggregation 


[Page 194]
ò System resources on aggrega tion nodes: CPU. disk, JVM, etc. 
Reconciliation 
Reconciliatio n means comparing different sets of data in order lo ensure data int egrity . 
Unlike reco nciliation in the bankin g industry , where you can compar e your records with 
the bank 's records , the result of ad click aggregation has no third -party result to reconcil e 
with . 
What we can do is to sort the ad click events by event time in every partition at the e nd 
of the day, by using a batch job and reconc iling with the real-Lime aggregation result. If 
we have higher accuracy requir ements , we can use a smaller aggrega tion window ; for 
example, one hour. Please note, no matt er which aggregatio n window is used, the result 
from the batch job might not match exact ly with the real-time aggregation result , since 
some events might arrive late (see "Time " section on page 175). 
Figure 6.28 shows the final design diagram with reconciliation support. 
Log Watcher Message 
Queue 
Alternative design 
Raw data 
database 
Ad oount 
Data (Aggregole oveiy min) 
Aggregation Message Database 
Queue t---- -+1 Writer 
Service - Top 100 moot dicked Ads - '------.- -....., 
Database 
Writer 
(llQgregote every min) 
Data Aggregation 
Service 
(Recalculation only) 
Reconciliation 
Figure 6.28: Final design 
Aggregation 
database 
Query 
Service 
(Dashboard) 
In a generalist system design interview , you are not expected to know the internals of dif¡
ferent pieces of specialized software used in a big data pipelin e. Explaining your thou ght 
process and discussing trade -offs is very imp ortant, which is why we propose a generi c 
solution. Another option is to store ad click data in Hive, with an ElasticSear ch layer built 
for faster queries . Aggregation is usually done in OLAP databases such as ClickHo use 
[23] or Druid [24]. Figure 6.29 shows the architectur e. 
Step 3 - Design Deep Dive I 189 


[Page 195]
ftfVP _ ] 
Cllckl louse 1 
Query aggregation results 
Merchant Facing 
Analytics 
Figure 6.29: Alternative design 
For more detail on this. please refer lo referen ce materi al (25). 
Step 4 - Wrap Up 
-
╖f F.l;i'ltir')A~fl'h 
r i 
Ou~ 
Data Sclenll~t 
Queries 
In this chapt er, we went through the pro cess of designing an ad click event aggregation 
system at the scale of Facebook or Google. We covered: 
ò Data model and API design. 
ò Use MapReduce paradigm to aggregate ad click events. 
ò Scale the message queue, aggregation service, and database. 
ò Mitigate hotspot issue. 
ò Monitor the system continuously. 
ò Use reconciliation to ensure correctness. 
ò Fault tolerance. 
The ad click event aggregation system is a typical big data pro cessing sys tem. It will be 
easier to understand and design if you have prior knowledge or expe rience with industry¡
standard solutions such as Apache Kafka, Apache Flink, or Apach e Spark. 
Congratulations on getting this fart Now give yourself a pat on the back. Good job! 
190 I Chapter 6. Ad Click Event Aggregation 


[Page 196]
Chapter Summary 
Ads Aggregation 
step 1 
step 2 
step 3 
aggrcgAte count 
functional req rel urn lop 100 
aggregation filtering 
correctness 
handle delayed evenls 
non -functional req 
robustness 
mim1tes laten cy 
1 billion ads click 
estimation SOK peak QPS 
daily storage req: 100GB 
query api design 
raw data 
aggregated data 
data model 
comparison 
choose database 
J_ async prncessin g 
high-level design ~ MapReduce 
suppor t 3 use cases 
stream ing vs batching 
time 
aggregation window 
delivery guarantees 
scale the system 
fault tolerance 
data monitoring and correctness 
alternative solution 
step 4 --wrap up 
Chapter Summary I 191 


[Page 197]
Reference Material 
[l] Clickt.hrough rate (CTR): Definition. https ://supp ort. goog lc.com/goog le-ads/answ 
er /26158 7 5 ?hl =en. 
[2] Conversion rate: Definition . https://support.googl e.co m/goog le-ads/answer/26B44 
89?hl=en. 
[3] OLAP functions. http s:/ /docs.oracle .com/da tabase /121/0LAX S/olap_fun ctions.h 
tm#OLAXS169. 
[ 4] Display Advertising with Real-Time Bidding (RTB) and Behavioural Targeting. ht 
tps:/ /arxiv.org/pdf/1610.03013.pdf. 
[5] LanguageManual ORC. https ://cwiki.apac he.org /confluence /display /hive/languag 
emanual+orc . 
[ 6] Parquet. https:/ /databrick s.com/glossary /what- is-parquet. 
[7] What is avro. http s:/ /www.ibm .com/topics/avro . 
[8] Big Data. https://www.datal,wery.com /techniques /big-data / . 
[9] An Overview of End-to-End Exactly-O nce Processin g in Apache Flink. https://llin 
k.apache.org /features /2018/03/01/end-t o-end-exactly-once-apache-flink.html. 
[10] DAG model. https://en.wikipedia.org /wiki/Directed_acyclic _grap h. 
[11] Understand star schema and the impor tance for Power BI. http s://docs.microsoft.c 
om.I en-us/power- bi/ guidance/ star-sc hema. 
[1.2] Martin Kleppmann . Designing Data-Intensive Applications. O'Reilly Media , 2017. 
[13] Apache Flink. http s://flink.apache.or g/. 
[ 14] Lambda architecture . http s:/ I databrick s.com/ glossary /lambd a-architecture . 
[15] Kappa architecture. https:/ /hazelcast.com/glossary /kappa -arc hitecture /. 
[16] Martin Kleppmann. Stream Processing. In Designing Data-Intensive Applications. 
O'Reilly Media, 2017. 
[17] End-to-end Exactly-once Aggregation Over Ad Streams . http s://www.youtube.co 
m/watch ?v=hzxytnPcAUM. 
[ 18] Ad traffic quality. http s://www.google .com/ads/ adtrafficq uali ty /. 
[19] Understandin g MapReduce in Hadoop. https ://www.section.io /engineering-educa 
tion /understandin g-map-reduce-in-hadoop /. 
[20] Flink on Apache Yarn. https ://ci.apache .org/projects /flink /flink -docs -release-1.13 
/docs/deployment/resource-providers/yarn/. 
192 I Chapter 6. Ad Click Event Aggregation 


[Page 198]
[21] How data is distributed across a cluster (using virtua l node s). http s://<lors datfls1 a 
x.com/en/cassandra-oss /3.0/ cassa ndra / architecture /arch Data Di c;t ri bu tr Di c;tri bu Ir 
.html. 
(22] Flink performance tuning . hllp s://night lies.apache .org/nink /nink -docs -master /d 
ocs/dev /table /tuning /. 
[23] ClickHouse . https ://c lickhou se.com /. 
[24) Druid. https ://druid .apac he.org/. 
[25] Real-Time Exactly-Once Ad Event Processing with Apache Flink, Kafka, and Pinot. 
https: //eng.uber.com /real -ti me-exact ly-once -ad-even t-processi ng/. 
Reference Material I 193 


[Page 199]
7 Hotel Reservation System 
In this chapter, we design a hotel reservation system for a hotel chain such as Marri ott 
International. The design and techniques used in this chapter are also appli cable to o th er 
popular booking-related interview topics: 
ò Design Airbnb 
ò Design a flight reservation system 
ò Design a movie ticket booking system 
Step 1 - Understand the Problem and Establish Design Scope 
The hotel reservation system is complicated and its components vary based on business 
use cases. Before divin g into the design, we should ask the interview er clarification ques¡
tions to narrow down the scope . 
Candidate: What is the scale of the system? 
Interviewer : Let's assume we are buildin g a website for a hotel chain that has 5,000 
hotels and 1 million rooms in total. 
Candidate: Do customers pay when they make reservations or when they arrive at the 
hotel? 
Interviewer: For simplicity , they pay in full when they make reservati ons . 
Candidate: Do customers book hotel rooms through the hotel's website only? Do we 
need to support other reservation opt ions such as phone calls? 
Interviewer: Let's assume people could book a hot el room through the hotel website 
or app. 
Candidate : Can customers cance l their reservations ? 
Interviewer: Yes. 
Candidate : Are there any other things we need to consider? 
Interviewer: Yes, we allow 103 overbookin g. In case you do not know, overbooking 
means the hotel will sell more rooms than they actually have. Hotels do this in anticipa ¡
tion that some custom ers will cance l their reservations. 
I 195 


[Page 200]
Candidate : Since we have limited lime, I assume lhe hotel room sear ch is not m scope 
W e focus on the following features. 
ò Show the hotel-related page. 
ò Show the hotel room-related detail page. 
ò Reserve a room. 
ò Admin pan el to add/remove/update hotel or roo m info . 
ò Suppor t the overbooking feature. 
Interviewer: Sounds good. 
Interviewer : One more thing, hotel prices change dyn amic ally. The price of a hotel 
room depends on how full the hotel is expect ed to be on a given day. For this interview, 
we can assume the price could be different each day. 
Can didate: I'll keep this in mind. 
Next , you might want to talk about the most important non -fun ctional r equire¡
ments. 
Non-functional requirements 
ò Support high concurren cy. During peak season or big events, some popular hotels 
may have a lot of customers trying to book the same room . 
ò Modera te latency. It's ideal to have a fast response tim e when a user makes the reser¡
vation, but it's acceptable if the system takes a few seconds to proce ss a reservation 
reque st. 
Back -of-the-envelope estimation 
ò 5,000 hotels and 1 million rooms in total. 
ò Assume 703 of the rooms are occupied and the average stay durati on is 3 days. 
ò Es timat ed daily reservations: 
rv 240,00Q) 
1 million x 0. 7 
3 233,333 (rounding up lo 
240 000 ò Reservations per second = 5 ' ="'-' 3. As we can see, the average 10 seconds in a day 
reservation transaction per second (TPS) is not high . 
Next , let 's do a rough calculation of the QPS of all pages in the system. There are three 
steps in a typical customer flow: 
1. View hotel/room detail page. Users browse this page (query) . 
2. View the booking page. Users can confirm the booking details , such as dates, number 
of guests, payment information before booking (query). 
3 . Reserve a room. Users click on the "book" button to book the room and the room is 
reserved (transaction). 
--- ----- -- ------
196 I Chapter 7. Hotel Reservation System 
I 
_ ....... 


[Page 201]
Let's assume aro und 103 of lhe users reach the next step and 903 of users dro p off 
the flow before reaching the final step . We can also assume that no p refctchin g fea ture 
(prefetching the content before the user reac hes the next step) is imp lemented. Figure 
7.1 shows a rough estimati on of what the QPS looks like for d ifferent steps. We know 
the final reservatio n TPS is 3 so we can work backward along the funn el. The QPS of lhe 
order confirmatio n page is 30 and the QPS for the detail page is 300. 
View hotel/room detail 
(QPS=300) 
Order book ing page 
(QPS= 30) 
Reserve rooms 
(QPS=3) 
Figur e 7.1: QPS distributi on 
Step 2 - Propose High-level Design and Get Buy-in 
In this section, we'll discuss : 
ò API design 
ò Data mode ls 
ò High-leve l design 
API design 
We explore the API design for the hotel reservatio n system. The most important APis 
are listed below using the RESTful conventions. 
Note that this chapter focuses on the design of a hotel reservation system . For a compl ete 
hotel website , the design needs to provide intuitive features for customer s to sear ch for 
rooms based on a large array of criteria. The APis for these search features, while impor¡
tant, are not technically challenging . They are out of scope for this chapter. 
Hotel-related APls 
Step 2 - Propose High-level Design and Get Buy-in I 197 


[Page 202]
-
-
API Detail 
,_ 
GET /v1 /hotels/ID Get detailed information about a hotel. -----
POST /v1/hotels Add a new hotel. This API is only available to 
hotel staff. --
PUT /v1/hotels/ID Update hotel information. 111is API is only avail-
able Lo hotel staff. 
DELETE /v1/hotels/ID Delete a hotel. 111is API is only avai lable to hotcl 
staff. 
Table 7.1: Hotel-related APis 
Room-related APls 
API Detail 
GET /v1/hotels/ID/rooms/ID Get detailed informati on about a roo m. 
POST /v1/hotels/ID/rooms Add a room. 111is API is only avai lable to hotel 
staff. 
PUT /v1/hotels/ID/rooms/ID Update room infor mati on. This API is only avail-
able to hotel staff. 
DELETE Delete a room . This API is only available to hotel 
/v1/hotels/I D/ rooms/ID staff. 
Table 7.2: Hotel -related APis 
Reservation related APls 
API Detail 
GET /v1/reservations Get the reservation history of the logged-in user. 
GET /v1/reservations/ID Get detailed inform ation about a reservation . 
POST /v1/reservations Make a new reservation. 
DELETE /v1/reservations/ID Cancel a reservation . 
Table 7.3: Reservation -related APis 
Making a new reservation is a very important feature . The reque st parameters of making 
a new reservation (POST /v1 I reservations) could look like this . 
{ 
} 
11 sta rtDate 
11
: 
11
2021 - 04 - 28
11
, 
11 endDate
11
: 
11
2021 - 04 - 30
11
, 
11 hotelID
11
: 
11
245
11
, 
11 roomID
11
: 
11
U123546 73389
11
, 
11 reservationID
11
:
11
13422445
11 
Please note reservationID is used as the idempote ncy key to prevent double booking. 
Double booking means multiple reservations are made for the same room on the same 
day. The details are explained in the "Concurr ency issue" sectio n on page 206. 
198 I Chapter 7. Hotel Reservation System 
-


[Page 203]
Data model 
Brfore we decide which database to use, lel's lake a close look al the data access palterns. 
For the hotel res ervation system, we need lo suppor l the following queries: 
Q!1ery 1: View detailed information aboul a hotel. 
Query 2: Find availabl e types of rooms given a dale range. 
Q.!1ery 3: Reco rd a reservation. 
Q.!1ery 4: Look up a reservation or past history of reservations. 
From the back -of-the -enve lope estimation , we know the scale of Lhe syslem is nol large 
but we need to prepare for traffic surges during big events. With these requirements in 
mind, we choose a relational database because : 
ò A relational database works well with read-heavy and write less frequently workflow. 
This is because the number of users who visit the hotel website/apps is a few orders 
of magnitude higher than those who actually make reservations. NoSQL databases 
are generally optimized for writes and the relational database works well enough for 
read-heavy workflow. 
ò A relational database provides ACID (atomicity, consistency, isolation, durabilit y) 
guarantees. ACID properties are important for a reservation system. With out tho se 
properties, it's not easy to prevent problems such as negative balance, double charge, 
double reservations, etc. ACID properties mal<:e application code a lot simpler and 
make the whole system easier to reason about. A relational database usually provides 
these guarantees. 
ò A relational database can easily model the data. The structure of the business data 
is very clear and the relationship between different entities (hotel, room, room_ type , 
etc) is stable. This kind of data model is easily modeled by a relational database. 
Now that we have chosen the relational database as our data store, let's explore the 
schema design. Figure 7.2 shows a straightforward schema design and it is the most 
natural way for many candidates to model the hotel reservation system. 
Step 2 - Propose High-level Design and Get Buy-in I 199 


[Page 204]
~--------------------
Hotel Service 
hotel _id 
name 
address 
location 
hotel 
room 
room _ id 
room_ type _id 
noor 
number 
hotel_id 
name 
is_ available 
PK 
PK 
--------------------
------------- ----- --! 
I 
Rate Service 
room_type _rate 
hotel_id 
date 
rate 
PK 
PK 
------ ----------- ---
Reservation Service 
reservation 
reservation _id PK 
hotel_id 
room_ld 
start_date 
end_date 
status 
guest_ id 
! 
I 
L-------------------~ 
Figure 7.2: Database schema 
Gues t Service 
guest 
guest _ id 
fir st n ame 
last_ name 
email 
PK 
I __ _____________ ____ } 
Most attributes are self-explanatory and we will only explain the status field in the reser¡
vation table. The status field can be in one of these states : pendin g, paid, refunded, 
canceled, rejected. The state machine is shown in Figure 7.3. 
Pending 
Canceled Paid Reje cted 
Refunded 
Figure 7.3: Reservation status 
This schema design has a major issue. This data model works for compa nies like Airbnb 
as room_id (might be called listing_id) is given when users make reservations. However, 
this isn't the case for hotels. A user actually reserves a type of room in a given hotel 
instead of a specific room. For instance, a room type can be a standard roo m, king-size 
room, queen-size room with two queen beds, etc. Room numb ers a re given when the 
guest checks in and not at the time of the reservation . We need to upd ate our data model 
to reflect this new requirement. See "Improved data mode l" in the deep dive section on 
200 I Chapter 7. Hotel Reservation System 


[Page 205]
page 203 for more details. 
High-level design 
We use the microservice architecture for this hotel reservation system. Over the past 
few year s. microservice architect ure has gained great popularity. Companie s thal use 
microse rvice include Amazon, Netflix, Uber, Airbnb, Twitter , etc. If you want to learn 
more about the benefits of a microservi ce architecture, you can check oul some goo d 
resources [ 1] (2] . 
Our design is mod eled with the microservice architecture and the high-level design dia¡
gram is shown in Figure 7.4. 
External CON 
Internal 
Hotel Service 
Hotel Cache Hotel DB 
Public Private 
User 
Rate DB Reservation DB 
Payment 
Service 
Payment DB 
Figure 7.4: High -level design 
ò Admin 
Internal API 
Hotel Management 
Service 
We will briefly go over each component of the system from top to bottom. 
ò User: a user books a hotel room on their mobile phone or computer. 
ò Admin (hotel staff): authorized hotel staff perform administrative operations such as 
refunding a customer , canceling a reservation, updating room information, etc. 
ò CDN (content delivery network): for better load time, CDN is used to cache all static 
assets , including javascript bundles , images , videos, HTML, etc. 
ò Public API Gateway: this is a fully managed service that supports rate limiting , au¡
thentication, etc. The API gateway is configured to direct requests to specific ser ¡
vices based on the endpoints. For example, requests to load the hotel homepage are 
directed to the hotel service and requests to book a hotel room are routed to the 
reservation service. 
ò Internal APis: those APis are only available for authorized hotel staff. They are 
accessible through internal software or websites. They are usually further protected 
Step 2 - Propose High-level Design and Get Buy -in I 201 


[Page 206]
by a VPN (virtual prival r netw ork) . 
ò Hotel Service: this providr s detailed information on hote ls nnd room c;. f lotd <1nri 
room data are genrra lly static, so ran hr eas ily cac hed . 
ò Rate ervice: this provides room rates for different futur e date s. An intrrrc;t 1 n~fart 
about the hotel industry is that the price of a room depends on how full thr hotel I\ 
expected lo be for a given day. 
ò Reserva tion Service: receives reservatio n reque sts and reserves th e hotel rooms. This 
service also lracks room inventory as roo ms a re rese rved or rese rvation s are can¡
celed . 
ò Payment Service: executes payment from a c ustomer and updat es th e reservation 
status to paid once a payment transaction succee ds, or rejected if the transaction 
fails . 
ò Hot el Management Service: only available to authorized hotel staff. Hotel staff are 
eligible to use the following features: view the record of an upcomi ng reservation, 
reserve a room for a customer, cance l a reservation , etc. 
For clarity , Figure 7.4 omits many arrows of interac tions betw een micro services. For 
example, as shown in Figure 7 .5, there should be a n arrow between Reservation service 
and Rate service. Reservation service queries Rate service for roo m rates. This is used to 
compute the total room charge for a reservation. Another examp le is that there should 
be many arrows conne cting the Hotel Manage ment Service with mos t of the other ser¡
vices. When an admin makes changes via Hotel Manage ment Service, the reque sts are 
forwar ded to the actual service owning the data, to handl e t he c hanges. 
Reservation 
Service 
Rate Service Hotel Service 
Figure 7.5: Connections between services 
For production systems , inter -service communi cation often employs a modern and high¡
performance remote procedure call (RPC) fram ework like gPRC. There are many benefits 
to usin g such frameworks. To learn more about gPRC in particular, check out [3]. 
Step 3 - Design Deep Dive 
Now we've talked about the high-level design, let's go deeper into the following. 
ò Improved data model 
ò Concurrency issues 
202 I Chapter 7. Hotel Reservation System 


[Page 207]
ò Scaling the syste m 
ò Resolving data inconsistency in the microservice archit ecture 
Improved data model 
As mentioned in the high-level design, when we reserve a ho lei room , wr net un lly reserve 
a type of room, as opposed to a specific room . What do we ne ed to change about the API 
and schema to accommodate thi s? 
For the reservation API, roomID is replaced by roomTypeID in the reque st param eter. 1hc 
APJ to make a reservation looks like this : 
POST /v1/r eservations 
Request parame ters: 
{ 
} 
"star tOate" ; 
11
2021 - 04 - 28
11
, 
11 endOate 11 :
11
2021 - 04 - 30
11
, 
"hote l IO" : 
11
245
11
, 
11 roo mTypeIO
11
: 
11
123546 73389
11
, 
11 reservation IO" :
11
13422445
11 
The updated sche ma is shown in Figure 7.6. 
,--------- ---- ---- ---. 
Hotel Service 
hotel_ld 
name 
address 
location 
hotel 
PK 
' 
Rate Service 
room_type _rate 
hotel _ id 
date 
rate 
PK 
PK 
--------- -----------
Guest Service 
guest 
guest _id 
first_ name 
last_ name 
email 
PK 
' ------------ ------ --~ 
Reservation Service 
room 
room_id PK 
room_type_ld 
floor 
number 
hotel_ld 
name 
is_avallable 
room_type_inventory 
hotel_id 
room _type_id 
date 
total_lnventory 
total_reserved 
- ---- ---- - --- ------~ 
Figure 7.6: Updated schema 
We'll briefly go over some of the most important tables. 
roo1: contains information regarding a room. 
reservation 
reservation _id PK 
hotel_id 
room_type_ld 
start_ date 
end_date 
status 
guest_id 
Step 3 - Design Deep Dive I 203 


[Page 208]
room_type_rate : stores price data for a specific room Lype, for futur e dates. 
reservation : records guest reservation data . 
roo11_ type _inventory: stores inventory data about hotel rooms . This tabl e is very impor¡
tant for the reservation system, so let's lake a close look at each column . 
ò hoteLid : ID of the hotel 
ò room_ type_ id: ID of a room type. 
ò date : a single date . 
ò totaLinventory: the total number of rooms minus tho se tha t are Lemporarily taken 
off the inventory . Some rooms might be taken off from Lhe mark et for maint enance. 
ò totaLreserved : the total number of rooms book ed for the specified hotel_id, 
room_ type_id, and date. 
There are othe r ways to design the room_ type _inventory table, but having one row per 
date makes managing reservations within a date range and queries easy. As shown in 
Figure 7.6, (hoteLid , room_type_id, date) is the comp osite primary key. The rows of the 
table are pre-populated by querying the inventory data across all future dates within 2 
years. We have a scheduled daily job that pre-populates inventory data when the dates 
advance further. 
Now that we've finalized the schema design , let's do som e estimation about the storage 
volume . As mentioned in the back-of-the -envelope estimation , we have 5,000 hotels. 
Assume each hotel has 20 types of rooms. That's (5,000 hotels x 20 types of rooms x2 
years x 365 days) = 73 million rows. 73 million is not a lot of data and a single database 
is enough to store the data. However, a single server mean s a single point of failure. To 
achieve high availability, we could set up database r eplications across multiple regions 
or availa bility zones. 
Table 7.4 shows the sample data of the room_type_inventory table. 
hotel_id room type id date total inventory total reserved 
211 1001 2021-06 -01 100 80 
211 1001 2021-06-02 100 82 
211 1001 2021-06-03 100 86 
211 1001 ... . .. 
211 1001 2023-05-31 100 0 
211 1002 2021-06-01 200 164 
2210 101 2021-06-01 30 23 
2210 101 2021-06 -02 30 25 
Table 7.4: Sample data of the room_ type_ inventory table 
The room_ type_inventory table is utilized to check if a cus tomer can reserve a specific 
type of room or not. The input and output for a reservation might look like this: 
204 I Chapter 7. Hotel Reservation System 
14' 


[Page 209]
ò Input : startDate (2021-07-01), endDate (2021-07-03), roomTypeid, hotelid, 
numberOfRoomsToReserve 
ò Output : True if th e spe cified typ e of room has inventory and users can book it. Oth ¡
erwi se, it returns False. 
From the SQL perspective, it contains the following two steps: 
1. Select rows within a date ran ge 
SELECT date , totaLinventory, total_ reserved 
FROM room_type _inv entory 
WHERE room_type _i d = ${roomTypeid} AND hotel _id = ${ 
hote lid} 
AND date between ${startDate} and ${endDate} 
This query returns data like this : 
date total _inventory total_reserved 
2021-07 -01 100 97 
2021-07-02 100 96 
2021-07-03 100 95 
Table 7.5: Hotel inventory 
2. For each entry, the application checks the condition below: 
if ((total_reserved + ${number0fRoomsToRese rve}) <= 
tot al_inventory) 
If the condition returns True for all entries , it means there are enough rooms for each 
date within the date range . 
One of the requirements is to support 103 overbooking. With the new schema , it is easy 
to impleme nt: 
if ((total_reserved + ${number0fRoomsToReserve}) <= 110% * 
to ta Li nventory) 
At this point , the interviewer might ask a follow-up question: "if the reservat ion data is 
too large for a single database, what would you do?" There are a few strategies: 
ò Store only current and futur e reservation data. Reservation history is not frequently 
accesse d.. So they can be archived and some can even be moved to cold storage . 
ò Database sharding. The most frequent queries include making a reservation or 
looking up a reservation by name. In both queries, we need t o c hoose the hot el 
first , meaning hoteLid is a good sharcling key. The data can be s hard ed b y 
hash(hotel_id) 3 number_of_server s. 
Step 3 - Design Deep Dive I 205 


[Page 210]
Concurrency issues 
An other 1mp o rtanl problem lo look a t is doublr bookin g. We n ee d to c;olv(ò two proh 
]ems: 
1. 1hc same use r clicks on the hook bu tt on multiple times 
2. M ult iplc user s l ry to hook t hr same ro om n l l he same ti m e. 
Le t 's take a look a l the first scenario. As show n in Figu re 7.7, lwo rcc;nvn tions are 
mad e. 
User's first click 
ò òò 
INSERT INTO RESERVATION ( 
121 . 
2, 
3, 
202 1-06-01 , 
202 1-06-0 4, 
pend1ng_pay, 
g uest1 
) 
User's seco nd click 
ò 
INSERT INTO RESERVATION ( 
121, 
2, 
3, 
2021-06-01 , 
2021-06-04, 
pending_pay, 
guest1 
) 
' ' 
i row 1: 121, 2, 3, 2021-06-01, 2021-06-04, pending_pay, guest1 i 
! row 2: 121, 2, 3, 2021-06-01, 2021-06-04, pending _pay, guest1 ! 
~---------- ---- ----- -- - -- ---- --- - ----- - -- - - --- ---- ---- - - - ---- ~ 
Figure 7.7: Two reservations are made 
There are two common approaches to solve this problem : 
res ervation Id 
holl'I od 
room typl' od 
start d:ite 
end date 
st atus 
guest od 
ò Client-si de implementation. A client can gray out, hid e or disable the " submit " button 
on ce a request is sent. This should prevent the doubl e-clicking issue most of the time. 
However , this approach is not very reliabl e. For examp le, users can disable javascript, 
th ereby bypassing the client check. 
ò Idempotent APis. Add an idempotency key in the reservation API reque st. An API 
call is idemp otent if it produces the same result no matt er how many times it is 
called. Figure 7.8 shows how to use the idemp otency key reservation_id to avoid 
the doubl e-reservation issue. The detailed steps are explained below. 
206 I Chapter 7. Hotel Reservation System 


[Page 211]
User 
ò ~ 
Reservation 
Service 
I 
I 
I 
I 
I 
I 
I 
I 
Generate reservation order ╖~ 
+ - - - « Show reservation page (reservatlon_ld) ╖ - -U 
1-----.3. Subm it reservation (reservation_id} -
Unique constraint is violated 
(reservation_id) 
Figure 7.8: Unique constrain t 
1. Generate a reservation order. After a customer enters detailed information about 
the reservation (room type , check-in date, check-out date, etc) and clicks the "continue " 
button, a reservation order is generated by the reservation service. 
2. The system generates a reservat ion order for the customer to review. The unique 
reservation _id is generated by a globally unique ID generator .and return ed as part of 
the API response . The UI of this step might look like this: 
Step 3 _ Design Deep Dive I 207 


[Page 212]
Booking.com <2) = 
rlnal Stop 
o~~~~~o~~~~-o 
Almost done, Alex! We just need a 
few more details to confirm your 
booking . 
Hotr.I òl <1ò 1 
Sim Fran cisc o Morriott Marqui s Union v 
Square 
Check╖ln Check-ou t 
Wed, Jul 7, 2021 Sat, Jul 10, 20 21 
3 nights , 1 room Chnngc dat<'s 
King Room No Vlow $508 
ld % TAX S.7112 
Tounsn1 loe $2 l!l 
2.?5 'lo City to' $1143 
Card Number ò 
~ No charge - only needed to hold your room 
Cardholder's name ò 
' - --------I Alex 
Expiration date ò ,----
MM{YY 
'-
Complete my booking > 
Figure 7.9: Confirmation page (Source: [ 4]) 
3a. Submit reser vation 1. The reservation_id is included as part of the req uest. It is the 
primary key of the reserva tion table (Figure 7.6). Please note that the idempotency key 
doesn 't have to be the reservation_id. We choose reservation_id because it already 
exists and works well for our design. 
3b. If a user clicks the "Complete my booking" butt on a seco nd time, reservation 2 is 
submitted. Because reservation_id is the prim ary key of the reservation table, we can 
rely on the unique constraint of the key to ensure no doubl e reservation happens . 
Figure 7.10 explains why double reservation can be avoided . 
208 I Chapter 7. Hotel Reservation System 
-


[Page 213]
User's first click 
ò 
INSERT INTO RESERVATION ( 
G]IJ╖ ---------------------
2. 
3, 
2021-06-01 , 
2021-06-04, 
pendlng_pay, 
guest1 
) 
User's second click 
ò 
INSERT INTO RESERVATION ( 
!ill] , __ 
2, -----. 3, ...... .._ 
2021-06-01, 
2021-06-04, 
pending_pay, 
guest1 
) 
~ x __________ i ___ ______________________________________ t ________ _ 
' ' 
: row 1: 121, 2, 3, 2021-06-01 , 2021-06-04, pending_pay, guest1 i 
I I 
~-- ------------------------------------------------------ - - --1 
Figure 7.10: Unique constraint violation 
Unique 
cons traint 
violat ion 
Scenario 2: what happens if multipl e users book the same type of room at the same 
time when there is only one room left? Let' s consider the scenario as shown in Figure 
7.11. 
Step 3 - Design Deep Dive I 209 


[Page 214]
TI me 
total Inventory = 100 
total_reserved = 99 
User 1 
CD ò 
"" Check room inventory 
":!..I 1 room left 
l 
fA\ Reserve room : 
~ total_reserved += 1 
total_inventory = 100 @ Commit 
total_ reserved = 100 
../ 
User 2 
~al inventory= 100 
L total reserved = 99 
« 
Check room inven tory 
1 room left 
« 
Reserve room : 
total _reserved += 1 
CZ) commit 
../ 
total _inventory = 100 
total _reserved = 100 
Figure 7.11 : Race condition 
1. Let's assume the database isolation level is not seriali zable (5]. User 1 and User 2 try 
to book the same type of room at the same time, but ther e is only 1 room left. Let's 
call User l's execution transaction 1 and User 2's execution transaction 2. At this 
time , there are 100 rooms in the hotel and 99 of them are reserved . 
2. Transaction 2 checks if there are enough rooms left by checkin g if (totaLreserved + 
rooms_to_book) :S totaLinventory. Since there is 1 more room left, it return s True. 
3. Transaction 1 checks if there are enough rooms by checking if (totaLreserved + 
rooms_to_book) :S totaLinventory . Since there is 1 more room l eft, it returns True 
as well. 
4. Transaction 1 reserves the room and updates the inventory: reserved_ room becomes 
100. 
5. Then transaction 2 reserves the room. The isolation property in ACID means 
database transactions must complete their tasks independently from other transac¡
tions. So data changes made by transaction 1 are not visible to transaction 2 until 
transactio n 1 is completed (committed). So transaction 2 still sees totaLreserved 
210 I Chapter 7. Hotel Reservation System 
_ .... _____ ... . A 


[Page 215]
as 99 and reserves the roo m b y upd ating the inventory: reserved_room beco mes 
100. 1l1is results in the sys tem allowin g both users to book a room, but there is only 
1 room left. 
6. Transaction 1 successfu lly commits the change. 
7. Tra nsactio n 2 success fully commit s the chan ge. 
Thr soluti on to this prob lem generally requires some form of locking mechani sm. We 
e>q)lorc the followi ng techniqu es: 
ò Pessimis tic locking 
ò Optimistic lockin g 
ò Database constrai nts 
Before jumpi ng into a fix, let' s take a look at the SQL pseudo-code utilized to reserve a 
room. TI1e SQL has two parts : 
ò Check roo m inventory 
ò Reserve a room 
# step 1: check room inventory 
SELECT date , total_inventory, total_reserved 
FROM room_type _inventory 
WHERE room_type _id = ${roomTypeld} AND hotel_id = ${hotelld} 
AND date between ${start0ate} and ${end0ate} 
# For every entry returned from step 1 
i f (( total_reserved + ${number0fRoomsToReserve}) > 110% * 
to t al_inventory) { 
Rollback 
} 
# step 2: reserve rooms 
UPDATE room_type_inventory 
SET total_reserved = total_reserved + ${numberOfRoomsToReserve} 
WHERE room_type_id = ${roomTypeld} 
ANO date betwee n ${start0ate} and ${end0ate} 
Commit 
Option 1: Pessimistic locking 
The pessimistic locking [ 6), also called pessimistic concurrency control , prevents simulta¡
neous updates by placing a lock on a record as soon as one user starts to update it. Other 
users who attempt to update the record have to wait until the first user has released the 
lock (committed the changes). 
For .MySQL, the "SELECT ò ò ò FOR UPDATE" stat ement works by locking the rows returned 
by a selection query. Let 's assume a transaction is started by "transaction 1 ". Other 
Step 3 - Design Deep Dive I 211 


[Page 216]
transac tions have to wait for transaction 1 lo finish before beginnin g anoth er trans action. 
A d etailed explanation is shown in Figure 7. 12. 
Time User 1 
ò 
------------- -~------- - ---- -' Transaction 1 
BEGIN TRANSACTION 
# check room inventory 
SELECT ... FOR UPDATE 
# reserve room 
UPDATE query 
I 
COMMIT TRANSACTION : 
I 
~--- --- -------- _________ _____ J 
T 
Transaction 2 
waits for 
Transaction 1 
to finish 
_! 
User 2 
ò 
------------- ~-------------¡' Transaction 2 : 
I 
I 
BEGIN TRANSACTION ] i 
# check room Inventory 
SELECT ... FOR UPDATE 
╖# reserve room 
Total reserved = 100, cannot 
reserve room 
I 
I 
I ROLLBACK TRANSACTION I i 
I 
╖--- ------- -- ---I-- --- ------ - --. 
Figure 7.12: Pessimistic locking 
In Figure 7.12, the "SELECT ò ò . FOR UPDATE" statement of tran saction 2 waits for trans¡
action 1 t o finish because trans action 1 locks the rows. After transaction 1 finishes, 
totaLreserved becomes 100, which means there is no room for user 2 to book. 
Pros: 
ò Prevents applications from updating data that is being or has been chan ged. 
ò It is easy to implement and it avoids conflict by serializing upda tes. Pess imistic lock¡
ing is useful when data contention is heavy. 
Cons: 
ò Deadlocks may occur when multiple resources are locked . Writin g deadlock-free 
appli cation code could be challenging . 
ò This approach is not scalable. lf a tran saction is locked for t oo long, other trans ac¡
tions cannot access the resource. This has a significant impac t on database perfor¡
mance , especially when transactions are long-lived or involv e a. lot of entitie s. 
Due to thes e limitations , we do not recommend pessimis tic locking for the reservation 
system. 
212 I Chapter 7. Hotel Rese rvation System 


[Page 217]
Option 2: Optimistic locking 
Optimistic locking [7], also referred to as optimistic concurrency control , allows multipl e 
concurr ent users to atte mpt to update the same resource . 
1here are two commo n ways to implement optimisti c locking: version numbe r and times ¡
tamp. Version number is generally considered lo be a better option b ecause lhe server 
clock can be inaccurate over time. We explain how optimistic locking works with version 
number. 
Figure 7.13 shows a successful case and a failure case. 
-- ------- -- - - - ------ ------ -----~ ------ - - ╖ 
Read v1 
: e / 
: .-~ 
: User 1 Write v2 
./ No conflict 
Read v2 
~. 
/. .. 
Write v3 User 2 
i --- ------- - --------- ╖~ - - - - - - - - ------------- - - - --~ 
I I 
I I 
I 
I 
I 
I 
I 
I 
Read v1 
e / 
.. ~ 
User 1 Write v2 
I 
I 
' 
, 
' 
Conflict 
' \ 
' ' ' ' 
X confllct 
Read v1 
---╖ .. 
User2 
/ 
Write v2 
~ - - - ----------------- - - - - --- ------ - - - -- - -- -- -- -- --
Figure 7.13: Optimistic locking 
1. A new column called version is added to the databas e table. 
2. Before a user modifies a database row, the application reads the version number of 
the row. 
3. When the user updates the row, the application increases the version number by 1 
and writes it back to the database. 
4. A database validation check is put in place; the next version number should exceed 
the current version number by 1. The transa ction aborts if the validation fails and 
the user tries again from step 2. 
Optimistic locking is usually faster than pessimistic locking because we do not lock the 
database. However, the performance of optimistic locking drops dramatically when con¡
currency is high. 
To understand why, consider the case when many clients try to reserve a hot el room at 
the same time. Because there is no limit on how many clients can read the available room 
Step 3 - Design Deep Dive I 213 


[Page 218]
count , aJl of them read back the same available room count and the current vers ion num¡
ber. When different c lients make rese rvations and write back the results lo the databa se, 
only one of them will succeed. and the rest of th e clients rece ive a version check failure 
message . These clients have lo retry. In the subsequent round of retries, there is only 
on e success ful client again, and lhe res t have to retry. Althou gh the e nd res ult is correct, 
repea ted retries cause a very unp leasa nt user exper ience. 
Pros: 
ò Jt preve nts applicat ions from editing stale da la. 
ò We don 't need to lock the database resource. There 's actually no locki ng from the 
databa se point of view. Il's entirely up Lo the application to handle the logic with the 
version number . 
ò Optimistic locking is generally used when the data con tenti on i s low. W hen con flicts 
are rare , transac tions can complete wi tho ut the expense of managing locks . 
Cons: 
ò Performance is poo r when data con tenti on is heavy. 
Optimis tic locking is a good opti on for a h otel reservation sys tem since the QPS for 
reserva tions is usually not high. 
Option 3: Database constraints 
This approac h i s very similar to opti mistic locking. Let's exp lore how it works. In the 
room_ type_inventory table, add the following constrain t: 
CONSTRAINT ' check_room_count' CHECK ((' tot al _in ventor y - t ot al _re served 
' >= 0) ) 
Using the same example as shown in Figm e 7.14, when u ser 2 tries to reserve a 
room , totaLreserved becomes 101, which violates the totaLinventory (100)¡
total_reserved (101) > 0 constraint. The tran saction is then rolled back. 
214 I Chapter 7. Hotel Reservation System 


[Page 219]
TI me 
Pros 
total_inventory = 100 
total_reserved = 99 
User 1 
CD ò 
@ Check room Inventory 
1 room left 
j 
@ Reserve room: 
òoòòUòòred +z 1 
@ commit 
../ 
User2 
total inventory = 1 00 
total reserved "" 99 
« 
Check room Inventory 
1 room left 
Reserve room: 
« total_reserved += 1 
/x 
totaUnventory - total_reserved >= 0 constraint is violated 
Figure 7 .14: Databas e constraint 
ò Easy to implement. 
ò It works well when data contention is minimal . 
Cons 
ò Similar to optimisti c locking , when data contention is heavy, it can result in a high 
volume of failures. Users could see there are rooms available, but when they try 
to book one , they get the "no rooms available" response. The experience can be 
frustra ting to users . 
ò The database constraints cannot be version-controlled easily like the application 
code. 
ò Not all databases support constraints. It might cause problems when we migrate 
from one database solution to another . 
Step 3 - Design Deep Dive I 215 


[Page 220]
<..incc this apprnach 1c; rac;v to 1mpltmrnl an<i fh<' cfata cnntrnt1nn for ~ hntel rr~trv~ 
twn 1c; uc;uallv not high (low QPS) . 11 1c; 'lnorhn goocl ophnn for the hntcl re~rrv.1hnn 
c;vc;lcm 
Scalability 
l c;uall\'. tht loaci nf lhl' holeò! rrc::rrvallon c;yc;trm 1c; not high J Jowt>vrr thr intt>rv1e Pr 
m11!ht have fl follow up q11<'c;t1nn ╖lrnt if tJw hold r< c;rrvat1on wc;tt'm ic; uvcJ not I"~' 
fnr a hotel chain hul for a popular lrnvc I c;ifcò c;urh ac; hooking C'om or rxprdia cnm >. Jn 
th1c; rAC:C'. thr QP~ Cf'IUld hr 1.000 I HTI('<; higher . 
\\ncn thr ~╖c:trm load 1c; high. wr nrrcl to unclcrstand what might herom" the hnttltnf'ck 
All 0ur c:cn1crc; arr c;tatclrc;s, so thry rnn he easily rxpandr d hy addin~ more c;erver~ Tht> 
clat0ba5e. however. contains all thr states <ind cann ot h<' scaled up by simply addin~ mort 
ciatahac:ec; f,<>t's explore how to c:ca]e the database. 
Database sharding 
One way to scale the database is to appl y data base c;hardin g The idea ic; to spl it the data 
mto multiple databases so that each of them only contams a p ortion of data. 
\\ nen we shard a database we need t o consid er h ow t o distribut e the data. As we can 
S<'C' from the data model section, most que ries need to filter by hoteL id. So a natural 
conclusio n is we s hard data by hotel_ id. In Figure 7.15. the load is spread among 16 
shards. Assume the QPS is 30.000. Afte r data base shardi ng, eac h shard handles 11Ji~ = 
l .x/ 0 QPS. which is "', thin a single MySQL serve r's load capacity. 
Figure 7.15: Database sharding 
Caching 
The hotel inventory data has an interesting characteristic; only current and future ho¡
tel inve nt ory data are meaningful beca use customers can only book rooms in the near 
216 Chapter 7. Hotel Reservation System 


[Page 221]
.---
future . 
o for the storage choice. ideall y we want to have a time-to-live (TTi j) mrchani~m to 
expire old data auto matically. Historica1 data can he queried on a different datahasc . 
Redis is a good choice becAusc TlL And Least Recently Used (Ll~U) rachc evictio n poli cy 
help us make optima l use of memory . 
IftJ1e loading speed and database scalab ility beco me an issue (for instan ce. we arc desig n¡
ing al booldng .com or Expedia's scale). we can add a cache layer on lop of the database 
and move the check room inventory and reserve roo m logic to the cache layer. as shown 
10 Figure 7.16. In this design , only a small percentage of the request s hit the inventory 
database as most ineligible requests are blocked by the inventory cache. One thin g wort h 
mentioning is that even when there is enough inventory shown in Redis, we still nee d to 
recheck the inventory at the database side as a precaution . The database is the source of 
truth for the inventory data . 
Reservation 
Service 
Query inventory Update Inventory 
/ ~ 
ò Async update cache r~~ J 
Inventory Cache Inventory DB 
Figure 7.16: Caching 
Let's first go over each component in this system. 
Reservation service : supports the following inventory management APis: 
ò ~ery the number of availab le rooms for a given hotel, room typ e, and date range . 
ò Reserve a roo m by executing totaLreserved + 1. 
ò Update inventory when a user cance ls a reservation . 
Inventory cache : all inventory management query operations are moved to the inven ¡
tory cache (Redis) and we need to pre-populate inventory data to the cache. The cache 
is a key-value store with the following structure: 
key : hotelID_r oomTypeID_{date } 
value : the number of available rooms for the given hotel ID, 
room t ype ID and date . 
For a hotel reservatio n sys tem, the volume of read operations (check room inventory) 
is an order of magnitude higher than writ e operations . Most of the read operations are 
Step 3 ╖Design Deep Dive I 217 
. ╖--- -


[Page 222]
-╖ 
anc;wcrcd h\╖ the rarhr 
Inve ntory DB <:force; inventor\' da111 ac; the c:ourcc of truth 
New challeng s posed by the cac he 
Addm~ 11 rArhr lswcr c;igmfira ntly mrr<'~q╖<; tlw <:\ 'tcm c;calat'l1htv and rhr011~hp11t h1111t 
Rl<:0 mtrnd11rrc; 11 nn ch11lkn~c╖ how In mainlam clllfll ronc:1c:trnrv hct~ r<'n the cfat:.lh::l~t 
smd I h( r11chc 
\\11rn A 11c;c1 honkc; a ro0m. two npt rnlinns arc rxcrntrd in the happv path. 
Qucn ╖ room m\'C╖ntnn╖ to find out 1f thrrr arr rnou~h room<: lefr The query rnnci on 
th( Jm╖cnton rachr 
2 Update im╖cnton╖ data lhr invrntorv DB 1c; updated firc;t The chan~e i~ thl"n prnp¡
Rf!Atcd t0 thr rachr ac;vnrhronously. This ac;vnchronous cachr up<lMe could be- in¡
\╖nltrd hy the appliratJOn codr which updates the inventory cache ttfter d::tta 1c; ~avt>d 
In thr databa~. It could also be propagated using chan~e data capture (CDC) [R]. 
CDC is a mechanism that reads data changes from the database and applies rhe 
chanf!eS to another data system. One common solution is Debt'zium [9]. Jt uses 
a source connector to read changes from a database and applies them to cac he solu¡
tions such a~ Red1s [ 10] 
l\erauc;e the inventory data is updated on the database first. there is a possibility that the 
cache does not reflect the lates t inventory data For example , the cache may rep ort there 
I'- stilJ an empty room when the database says there is no room left or ..,;ce versa. 
If you think care fully. you find that the inconsistency betwee n invent ory cac he and 
database actually does not m atter, as long as the database does the final inventory vali¡
dation check. 
Lct 's take a look at an example. Let's say the cache says the re is stiU an empty room. 
but the database says no. Jn thi s case, wh en th e use r queries th e roo m inve ntory , they 
find there is still roo m availa ble, so they try to reserve it. When the request reac hes the 
inventory database , the database does th e valid ation and find s that there is no roo m left. 
ln thi s case, the client receives an error, indi cating someone else just booked the last room 
bcforr them . When a use r refreshes th e website, they prob ably see th ere is no roo m left 
beca use the da tabase has sync hronized inventory data to th e cache, befo re t hey click the 
refresh button . 
Pros 
ò Reduced database load. Since read queries are answered by the cache layer, database 
load is signi fican tly reduced . 
ò High perfo rman ce. Read queries are very fast because resuJts are fet ched from mem ¡
ory. 
218 I Chapter 7. Hotel Reservation System 


[Page 223]
Cons 
ò Maintaining data consistency between the database and cache is hard. We need to 
think carefully a bout how this inconsistency affects user exper ience. 
Data consistency among services 
In a traditional monolithic architectur e [11], a shared relational database is used to ensure 
data consistency. In our microservice design, we chose a hybrid approac h b y having 
Reservation Service handle both r eservat ion and inventory APis so that the inventory 
and reservation d atabas e tables are stored in the same relational database. As explained 
in the "Concurrency issu es" section on page 206, this arran gement allows us to leverage 
the ACID prop erti es of the relational database to elegantly handl e many concurrency 
issues that arise during the reservation flow. 
However, if your interviewer is a microservice purist, they might challenge this hybrid 
approach. In their mind , for a microse rvice architectur e, each microservice has its own 
databases as shown on the right in Figure 7.17. 
Reservation 
Service 
Inventory 
Service 
Hotel OB 
Monoli thic Archit ecture 
Payment 
Service 
Reservation 
Service 
Reservation DB 
Inventory 
Service 
lnventOIY DB 
Mlcroservlce Architecture 
Figure 7 .17: Monolithic vs microservice 
Payment 
Service 
Payment DB 
This pure design introd uces many data consistency issues. Since this is the first time 
we cover microservi ces, let's explain how and why it happ ens. To make it easier to 
understand , only two services are used in this discussion. In the real world, ther e could 
be hundreds of microservices vvithin a compan y. In a monolithic archite cture , as shown 
in Figure 7.18, different operations can be wrapped in a single tran saction to ensure ACID 
properties. 
Step 3 ╖ Design Deep Dive I 219 


[Page 224]
User 
ò ... 
Databa se 
u 
I 
I 
I 
I 
I 
Manage room inventory -~ 
.- --- --- ---------- ---------- --- ---- ------- ---- ~ 
Single 
Transaction 
R~erve room n 
.- -------------------------------------------- U~~~ 
I 
I 
Figure 7.18: Monolithic archit ecture 
However, in a microservice architecture, each service has its own database . One logi¡
cally atomic operation can span multiple services. This means we cannot use a single 
transaction to ensure data consistency. As shown in Figure 7.19, if the update operation I 
fails in the reservation database, we need to roll back the reserved room count in the ò 
inventory database. Generally, there is only one happy path , but many failure cases that 
could cause data inconsistency. 
User 
ò ~ 
Inventory 
Service 
I 
Manage room inventory J ~ 
Single 
Transaclion 
----------------------------------
Reservation 
Service 
I 
Reserve room -~ 
Single 
- --- ----- - - ---- --- ----------- ------:-------- ----- ------- - - - ~~sactlon 
I 
I 
Figure 7 .19: Microservice architecture 
To address the data inconsistency, here is a high-level summary of industry -proven tech-
220 I Chapter 7. Hotel Reservation System 
-
I 


[Page 225]
niques. If you want to read the details, please refer to the reference materials . 
ò Two-phase commit (2PC) [12). 2PC is a database protocol used to guar antee atomic 
transaction commit across muJliple nodes , i.e., either all nodes succeeded or all nod es 
failed. Because 2PC is a blocking protocol, a single node failure blocks the progress 
until the node has recovered . It's not perfor mant. 
ò Saga. A Saga is a sequence of local transactions. Each transaction updates and pub ¡
lishes a message to trigger the next transaction step. If a step fails, the saga executes 
compensating transactions to undo the changes that were made by preceding trans ¡
actions [ 13]. 2PC works as a single commit to perform ACID transactions while Saga 
consists of multiple steps and relies on eventual consistency. 
It is worth noting that addressing data inconsistency between microservices requires 
some complicated mechanisms that great ly increase the complexity of the overall design. 
It is up to you as an architect to decide if the added complexity is worth it. For this prob¡
lem, we decided that it was not worth it and so went with the more pragmatic approach 
of storing reservation and inventory data under the same relational database . 
Step 4 - Wrap Up 
In this chapter , we presented a design for a hotel reservation system. We started by 
gathering requirements and calculating a back-of-the -envelope estimation to understand 
the scale. In the high-level design, we presented the API design, the first draft of the data 
model, and the system architecture diagram. In the deep dive, we explored alternative 
database schema design as we realized reservations should be made at the room type 
level, as opposed to specific rooms. We discussed race conditions in depth and proposed 
a few potential solutions: 
ò pessimistic locking 
ò optimistic locking 
ò database constraints 
We then discussed different approaches to scale the system, including database sharding 
and using Redis cache. Lastly, we went through data consistency issues in microservice 
architecture and briefly went through a few solutions. 
Congratulations on getting this far! Now give yourself a pat on the back. Good job! 
Step 4 - Wrap Up I 221 


[Page 226]
Chapter Summary 
step I 
step 2 
Hotel Reservation 
step 3 
__[__ reserve a room 
functional rcq ~ admin panel 
support ove rbook ing 
-
< 
support hi gh concurrency 
non-f unclional r eq 
moderate latency 
hotel-relat ed 
res ervation-relat ed 
view hotel detail 
find avajJable rooms 
data model 
m ake a reservation 
lookup a reservation 
high-lev el desig n 
improved data model --- use roomTyp eID 
pessimi stic locking 
database cons traint 
< 
database shardin g 
scaJabilily 
caching 
data consiste ncy among services 
step 4 --wrap up 
222 I Chapter 7. Hotel Reservation System 


[Page 227]
4 -
L 
Reference Material 
[1] What Are The Benefits of Microservices Architecture ? https://www.appdynam ics . 
com/topi cs/benefi ts-of- microse rvices. 
[2 J Microservices. https ://en. wikipedia .org/wiki /Microservices. 
[3) gRPC. hllps ://www .grpc.io /docs /what-is-grpc /introduction /. 
( 4] Booking.com iOS app. 
(5] Serializability. https: // en.wik ipedia.org/wik.i/Serializability . 
[6) Optimistic and pessimistic record locking. https ://ibm.co/3Eb2930. 
[ 7] Optimistic concurrency control. h ttps: // en.wik.ipedia.org /wiki /Op timis tic_ concurr 
ency _con trol. 
(8) Change data capture. http s://docs.oracl e.com/cd/B10500_01/server.920 /a96520 /cd 
c.htm. 
[9) Debizium . https: //debezium .io/. 
(10] Redis sink. https: //bit.ly /3r3AEUD . 
(11] Monolit hic Architecture . https: //microservices.io /patterns /monolithic .html. 
[12] Two-phase commit protocol. https: //en.wik.ipedia.org /wiki/Two-phase _commit_p 
rotoco l. 
[ 13] Saga. https: //microservices.io/pa tterns/ data/saga.html. 
Reference Material I 223 
-


[Page 228]
8 Distributed Email Service 
In this chapter. we design a large -scale email service, such as Gmail, Outlook , or Yahoo 
Mail. ll1e growth of the internet has led to an explosion in the volume of emails. In 2020, 
Gmail had over 1. billion active users and Outlook had over 400 million users worldwide 
[1] [2]. 
~ outlook.com Mgma ll.com yahoo.com 
Figure 8.1: Popular email providers 
Step 1 - Understand the Problem and Establish Design Scope 
Over the years , email services have changed significantly in complexity and scale. A 
modem email service is a complex system with many features. There is no way we 
call design a real-world system in 45 minutes . So before jumping into the design , we 
definitely want to ask clarifying questions to narrow down the scope. 
Candidate : How many peopl e use the product? 
Interviewer : One billion users. 
Candida te: I think the following features are important: 
ò Authentica tion. 
ò Send and receive emails . 
ò Fetch all emails . 
ò Filter emails by read and unread status. 
ò Search emails by subject, sender, and body. 
ò Anti-spam and anti-virus . 
Interviewer : That's a good list. We don't need to worry about authentication. Let's 
focus on the other features you mentioned. 
---- ---- --
I 22s 
- -


[Page 229]
Candidate : How do users conned with mail servers? 
Interviewer : Traditionally, users conne ct wit h mail servers throu gh native clients that 
usc SMTP, POP. IMAP , and vendor -sperifk proto cols. 'CT1ose prot oco ls MC' legacy lo some 
extent. yet still very popu lar. for this interview , Jet's assume I ITTP is used for client and 
server communication . 
Candidate : Can emails have allachmcnls? 
Interviewer : Yes. 
Non -functional requirements 
Next , let's go over the most important non-functional requir ements. 
Reli ability. We should not lose email data. 
Availability . Email and user data should be a utomatically replicated across multiple 
nodes to ensure availability . Besides, Lhc system should continu e Lo fun ction despite 
partial system failw╖es. 
Scalability. As the numbe r of users grows, the system should be able to handl e the in¡
creasing number of users and emails. The performan ce of the sys tem should not degrade 
with more users or emails. 
Flexibility and extensi bility. A flexible/ex tensible system allow s us to add new fea¡
tures or improve performan ce easily by addin g new components. Traditi onal email pro¡
toco ls such as POP and IMAP have very limited functionality (more on this in high- level 
desig n). Therefore, we may need custom prot ocols to satisfy the flexibility and extensi¡
bility requirements. 
Back-of-the-envelope estimation 
Let's do a back-of-the -envelope calculation Lo determine the scale and to discover some 
challen ges our solution will need to address. By design, emails are storage heavy appli¡
cations. 
ò 1 billion users. 
ò Assume the average numb er of emails a person sends per day is 10. QPS for sendin g 
109 x 10 emails= 105 = 100,000. 
ò Assume the average numbe r of emails a person receives in a day is 40 [3] and the 
average size of email metadata is 50 KB. Metadata refers to everything related to an 
email , excluding attachment files. 
ò Assume metadata is stored in a databas e. Storage requirement for maintaining meta¡
dala in 1 year: 1 billion user s x 40 emails / day x 365 days x 50 KB = 730 PB. 
ò Assume 203 of emails contain an attachment and the average attachment size is 500 
KB . 
ò Storage for attachments in 1 year is: 1 billion u sers x 40 emails/ day x 365 days x 
203 x 500 KB = 1,460 PB 
226 I Chapter 8. Distri buted Email Service 


[Page 230]
Prom this back -of-th e-e nvelope c<ilculalion , il's clear we wou ld deal wilh a lot of claln. 
So. it's likely that we need a distributed databa se solution. 
Step 2 - Propose High-level Design and Get Buy-in 
In this section, we first discuss some basics about email servers and how email servers 
evolve over time. Then we look at the high-level design of distributed email servers . The 
content is struc tured as follows: 
ò Email knowledge 101 
ò Trad itional mail servers 
ò Distributed mail servers 
Email knowledge 101 
There are various email protocols that are used to send and receive emails. Historically, 
most mail servers use email protoco ls such as POP, IMAP, and SMTP. 
Email protocols 
SMTP: Simple Mail Transfer Protoco l (SMTP) is the standard protocol for sending emails 
from one mail server to another. \ 
The most popular protocols for retrieving emails are known as Post Office Protocol 
(POP) and the Internet Mail Access Protocol (IMAP). 
POP is a standard mail protocol to receive and download emails from a remote mail 
server to a local email client. Once emails are downloaded to your computer or phone, 
they are deleted from the email server, which means you can only access emails on one 
computer or phone . The details of POP are covered in RFC 1939 [ 4]. POP requires mail 
clients to download the entire email. This can take a long time if an email contains a 
large attac hment. 
IMAP is also a standard mail protocol for receiving emails for a local email client. When 
you read an email, you are connected to an external mail server, and data is transferred 
to your local device. IMAP only downloads a message when you click it, and emai ls are 
not deleted from mail servers , meaning that you can access emails from multiple devices. 
IMAP is the most widely used protocol for individual email accounts. It works well when 
the connec tion is slow because only the email header information is downloaded until 
opened. 
HTTPS is not technically a mail protocol , but it can be used to access your mailbox , 
particularly for web-based email. For example, it's common for Microsoft Outlook to talk 
to mobile devices over HTTPS , on a custom-made protocol called ActiveSync (5). 
Domain name service (DNS) 
A DNS server is used to look up the mail exchanger record (MX record) for the recipient 's 
domain. If you run DNS lookup for gmail.com from the command line, you may get MX 
records as shown in Figure 8.2. 
Step 2 - Propose High-level Design and Get Buy-in I 227 


[Page 231]
mail e><changer 
mail exchanger 
mail exchanger 
mail exchanger 
mail exchanger 
r 
MX Priority 
Figure 8.2: MX records 
Mail servers 
TI1e priority numbers indicate preferences , where the mail serve r with a lower priority 
numbe r is more preferred . In Figure 8.2, gmail -smtp-in .1. google. com is used first (pri¡
ority 5). A sending mail server will attempt to connect and send messages to thfa mail 
server first. If the connection fails, the sending mail server will attempt to connect to the 
mail server with the next lowest priority , which is al t1. gmail-smtp-in .1. google. com 
(priority 10). 
Attachment 
An email attachment is sent along with an email message, commonly with Base64 encod¡
ing [ 6]. There is usually a size limit for an email attachment. For example, Outlook and 
Gmail limit the size of attachments to 20MB and 25MB respectively as ofJune 2021. Th.is 
number is highly configurable and varies from individual to corporate accounts . Multi¡
purpose Intern et Mail Extension (MIME) [7] is a specification that allows the attachment 
to be sent over the internet. 
Traditional mail servers 
Before we dive into distributed mail servers . let's dig a little bit through the history and 
see how traditional mail servers work, as doing so provides good lessons about how to 
scale an email server system. You can consider a traditional mail server as a system that 
works when there are limited email users , usuall y on a single server . 
Traditional ma il server architecture 
Figure 8.3 describes what happens when Alice sends an email to Bob, using traditional 
email serYers. 
. .. 
.. . .., 


[Page 232]
User Alice 
allce@outlook.com 
Outlook 
client 
ò 
CD Send 
,- ------------------- ---------
' I 
: IMAP/POP 
I 
I Server 
Fetch Store 
c&ora{.J 
outlook .com 
ò mail server , : __ ___ _________________________ ~ 
User Bob 
bob@gmall.com 
ò 
T 
~GmaJI 
ò1 client 
@ Get 
-------------------------------' 
' ' Send -l.+ SMTP 
Server 
@Store Fetch 
~Ora~ 
gmail.com 
I 
I 
' I 
: mail server : 
~ - - --- - ---------------- -- --- -- -~ 
Figure 8.3: Traditional mail servers 
The process consists of 4 steps : 
1. Alice logs in to her Outlook client, composes an email, and presses the "send" button. 
The email is sent to the Outlook mail server. The communication protocol between 
the Outlook client and the mail server is SMTP. 
2. Outlook mail server queries the DNS (not shown in the diagram) to find the address of 
the recipient 's SMTP server . In this case, it is Gmail's SMTP server. Next, it transfers 
the email to the Gmail mail server. The communication protocol between the mail 
servers is SMTP. 
3. The Gmail server stores the email and makes it available to Bob, the recipient. 
4. Gmail client fetch es new emails through the IMAP/POP server when Bob logs in to 
Gmail. 
Storage 
In a traditional mail server , emails were stored in local file directories and each email 
was stored in a separate file with a unique name. Each user maintained a user directory 
to store configuration data and mailboxes . Maildir was a popular way to store email 
messages on the mail server (Figure 8.4). 
Step 2 - Propose High-level Design and Get Buy-in I 229 


[Page 233]
Figure 8.4: Maildir 
File directories worked well when the user base was small, but it was challenging to 
retrieve and backup billions of emails. As the email volume grew and the file structure 
became more complex., disk 1/0 became a bottleneck. The local directories also don't 
satisfy our high availability and reliability requireme nts . The disk can be damaged and 
servers can go down. We need a more reliable distributed storage layer. 
Email functionality has come a long way since it was invented in the 1960s, from text¡
based format to rich features such as multimedia , threading [8], searc h, labels, and more. 
But email protocols (POP, IMAP, and SMTP) were invented a long time ago and they were 
not designed to support these new features, nor were they scalab le to support billions of 
users . 
Distributed mail servers 
Distributed mail servers are designed to support modem use cases and solve the prob¡
lems of scale and resiliency. This section covers email APis, distributed email server 
architecture, email sending, and email receiving flows. 
Email APls 
Email APis can mean very different things for different mail clients, or at different stages 
of an email's life cycle. For example; 
ò SMTP/POP/IMAP APis for native mobile clients. 
ò SMTP communications between sender and receiver mail servers. 
230 I Chapter 8. Distrib uted Email Service 
( 


[Page 234]
--
ò RESTful APT over HTTP for fuJJ-fealured and int erac tive web-based email appli ca¡
tions . 
Due to the length limitations of thi s book, we cover only some of Lhe mos t important 
APls for webmail. A common way for webm ail to communicat e is through th e HTTP 
protocol. 
1. Endpoint: POST /v1 /111essages 
Sends a message to the recip ients in the To, Cc, and Bee headers. 
2. Endpoint: GET /v1 /folders 
Returns all folders of an email acco unt. 
Response: 
[{id: string U nique folder identifier . 
nam e: stri ng Name of the folder . 
According to RFC6154 {9}, the default folders can be one of 
the following: 
All, Archive , Drafts , Flagged, Junk , Sent, and Trash. 
user_id: stri ng Reference to the account owner 
}] 
3. Endpoint: GET /v1 /folders/{ :folder _id}/111essages 
Returns all messages under a folder. Keep in mind this is a highly simplified APL In 
reality, this needs to support pagination. 
Response: 
List of message objects. 
4. Endpoint: GET /v1 /messages/{: message_id} 
Gets all information about a specific message . Messages are core building blo cks for an 
email application , containin g information about the sender, recipients , message subject , 
body, attachments, etc. 
Response: 
A message's object. 
{ 
user_ id: stri ng 
from: name : strin g, email: string 
to: [name: stri ng, email: string] 
subject: string 
body: string 
is read: boolean 
} 
II Reference to the account owner. 
II <nam e, email> pair of the sender. 
II A list of <name, email> paris 
II Subject of an email 
II Message body 
II Indicate if a message is read or not. 
Step 2 - Propose High-level Design and Get Buy-in I 231 


[Page 235]
Dist ributed mail server architecture 
While i l i s easy lo sel up an email server that handles a s mall numb er of u sers, it is 
difficult lo scale beyo nd one server. 1l1is is mainly beca use traditional email servers were 
designe d t o work with a s ingle server only. Synchroni zing data ac ross servers can be 
difficult, and keepin g emails from being misclassified as spam by recipients' mail servers 
is very c hall enging. In this section, we explore how to leverag e cloud technologies to 
mak e it easier. 1l1e high-level design is shown in Figure 8.5. 
Metadata DB 
https 
Webmail 
WebSocket 
Real-time 
Servers 
LJ LJ 
Attachment store Distributeq cache 
Storage Layer 
Figure 8.5: High-level design 
Let us take a close look at each component. 
Webmail . Users use web brow sers to receive and send emails. 
Search store 
Web servers. Web servers are public-facing request /response services , used to manage 
features such as login, signup , user profile , etc. In our design , all email API requests, such 
as sending an email, loading mail folders, loading all mails in a folder , etc ., go through 
web serv ers. 
Real-time servers. Real-time servers are responsible for pushin g new email updates 
to clients in real-tim e. Real-time servers are stateful serv ers because they need to main¡
tain persistent conne ctions. To support real-time communication, we have a few op¡
tions, such as long polling and WebSocket. WebSocket is a more elegant solution but one 
drawbac k of it is browser compatibility . A possible solution is to establish a WebSocket 
connection whenever possible and to use long -polling as a fallback. 
Here is an example of a real-world mail server (Apach e James [10]) that implements the 
]SON Meta Application Protocol (]MAP) subprotocol over WebSocket [11]. 
Metadata database. This databas e stores mail metadata including mail subject, body, 
232 I Chapter 8. Distributed Email Service 
' I 


[Page 236]
--
from user, to users , etc. We discuss the database choice in the deep dive seclion. 
Attachment store. We choose object stores such as Amazon Simple Storage Service (S3) 
as the attachme nt store. S3 is a scalable storage infrastructure that 's suitable for storin g 
large files such as images, videos , files, etc. Attachments can take up to 25 MB in size. 
NoSQL column-family databases like Cassandra might not be a good fit for the following 
two reasons: 
ò Even though Cassandra supports blob data type and its maximum theoretical size for 
a blob is 2GB, the practical limit is less than lMB [12]. 
ò Anot her problem with putting attachments in Cassandra is that we can' t use a row 
cache as attac hments tal<e too much memory space. 
Distributed cache. Since the most recent emails are repeatedly loaded by a client , 
caching recent emails in memory significantly improves the load time. We can use Redis 
here because it offers rich features such as lists and it is easy to scale. 
Search store . The search store is a distributed document store. It uses a data structure 
called inverted index [13] that supports very fast full-text searches. We will discuss this 
in more detail in the deep dive sectio n. 
Now that we have discussed some of the most important components to build distributed 
mail servers, let 's assemble together two main workflows. 
ò Email sending flow. 
ò Email receiving flow. 
Email sending flow 
The email sending flow is shown in Figure 8.6. 
Step 2 - Propose High-level Design and Get Buy- in I 233 


[Page 237]
Webmall 
Load balancer 
Check spam 
(~~~() 
Error queue 
' 
~ SMTPOutgolng 
I 
-╖ ' ' ' ' ' . 
' ' 
Outgoing queue : _____________________ : 
Metadata Search store Attachment Latest email 
L( LJ ~ ~. 
Database Database Object Store Cache 
Storage Layer 
Figure 8.6: Email sending flow 
1. A user writes an email on webmail and presses the send button. The request is sent 
to the load balancer . 
2. The load balancer makes sure it doesn 't exceed the rate limit and routes traffic to web 
servers . 
3. Web servers are responsible for: 
ò Basic email validation_ Each incoming email is checked agains t pre-defined rules 
such as email size limit. 
ò Checking if the domain of the recipient's email address is the same as the sender. 
If it is the same, the web server ensures the email data is spam and virus free. If 
so, email data is inserted into the sender 's "Sent Folder" and recipient's "Inbox 
Folder". The recipient can fetch the email directly via the RESTful APL There is 
no need to go to step 4. 
4. Message queues. 
4.1. If basic email validation succeeds, the email data is passed to the outgoing queue. 
If the attachment is too large to fit in the queue, we could store the attachment 
in the object store and save the object reference in the queued message. 
4.2. If basic email validation fails, the email is put in the error queue . 
5. SMTP outgoing workers pull messages from the outgoing queue and make sure 
emails are spam and virus free. 
234 I Chapter 8. Distributed Email Service 


[Page 238]
6. The outgoing email is stored in th e "Sent Folder" of the stora ge layer. 
7. SMTP outgoi ng work ers send the email t╖o the recipient mail server. 
Each message in the outgoing queu e contains all the metadata required to create an email. 
A distributed message queue is a critical component that allows asynchronous mail pro ¡
cessing. By decoup ling SMTP outgoing workers from the web servers, we can scale SMTP 
outgoing workers independently. 
We monitor the size of the outgoing queue very closely. If there are many emails stuck in 
the queue, we need to analy ze the cause of the issue. Here are some possibilities: 
ò 1he recipie nt's mail server is unavailable. In this case, we need to retry sending the 
email at a later time . Exponential backoff [14] might be a good retry strategy. 
ò Not enough consumers to send emails. In this case, we may need more consumers 
to reduce the pro cessing time. 
Email receiving flow 
The following diagram demonstrates the email receiving flow . 
.. ----------------....... . 
' ' Webma ll 
Check spam 
Ctlaek 
@ WebSocke1 @ Https 
Load balancer WebseNers 
Metada!a Se"""1 ston> Attacnnent lAtast email 
L( L] $J ~. 
Database Database ObJeci Store cache 
Storage Layer 
Figure 8.7: Email receiving flow 
1. Incoming emails arrive at the SMTP load balancer. 
2. The load balancer distributes traffic among SMTP servers. Email acceptance policy 
can be configured and applied at the SMTP-connection level. For example, invalid 
emails are bounc ed to avoid unnecessary email processing . 
3. If the attachment of an email is too large to put into the queue, we can put it into the 
attachment store (S3). 
4. Emails are put in the incoming email queue. The queue decouples mail processing 
Step 2 - Propose High-level Design and Get Buy-in I 235 


[Page 239]
workers from SMTP serve r<; so they ran be sen led independe ntl y. Moreover, thr 
queue serves as a buffer in rase the emai l volume surges . 
5. Mail process ing workers arc responsible for a lot of t asks, includ ing filtering out 
spam mails . s loppi ng virusrs, etc. 111e following steps assume an email pas<;ed the 
validation. 
6. The email is stored in the mail storage, cache, and object data store. 
7. If the receiver is curren tly onlin e, lhe e mail is pushed to real- tim e serve rs. 
8. ReaJ-lime serve rs are VvcbSockcl servers that allow clients to receive new emails In 
real-time. 
9. For offline users , emails are stored in th e storage laye r. When a user comes back 
onli ne, the webmai l client connects to web serve rs via RESTful APJ. 
10. Web servers pull new emails from the storage layer and return them to the client. 
Step 3 - Design Deep Dive 
Now lhat we have taJked about aJl the parts of the email server, let 's go deeper into some 
key components and examin e how to scale the system. 
ò Metadata database 
ò Search 
ò Deliverability 
ò Scalability 
Metadata database 
In this section, we discuss the characteristics of email meladata , choosing the right 
database , data model, and conversation threads (bonus point). 
Characte ristics of email metadata 
ò Email head ers are usually small and frequently accessed. 
ò Email body sizes can range from small to big but are infrequently accessed . You 
normally only read an email once. 
ò Most of the mail operations, such as fetching mails , marking an emai l as read, and 
search ing are isolated to an individual user. In other words, mails owned by a user 
are only accessible by that user and all the mai l operations are performed by the same 
user. 
ò Data recency impa cts data usage. Users usually only read the most recent emails. 
823 of read queries are for data younger than 16 days (15]. 
ò Data has high-reliability requirements. Data loss is not acceptab le. 
236 I Chapter 8. Distrib uted Email Service 
( 
1.\1 
' ò..f 
. ' 


[Page 240]
-
Choosing the right database 
At Gmail or Outlook scale , the database system is usually custom-made lo reduce in¡
put/output operations per second (IOPS) [ 16], as this can easily become a maj or con¡
straint in the system. Choosing the right database is not easy. It is helpful lo consider all 
the options we have on the table before deciding the most suitable one . 
ò Relational database. The main motivation behind this is to search through emails 
efficiently. We can build indexes for email header and body. With indexes , simple 
search queries are fast. However, relational databases are typically optimized for 
small chunks of data entries and are not ideal for large ones. A typical email is usu¡
ally larger than a few KB and can easily be over lOOKB when HTML is involved . You 
might argue that the BLOB data type is designed to support large data entries. How¡
ever, search queries over unstru cture d BLOB data type are not efficient. So relational 
databases such as MySQL or PostgreSQL are not good fits. 
ò Distributed object storage. Another potential solution is to store raw emails in cloud 
storage such as Amazon S3, which can be a good option for backup storage, but it's 
hard to efficiently support features such as marking emails as read, searching emails 
based on keywords, threading emails , etc. 
ò NoSQL databases. Google Bigtable is used by Gmail, so it's definitely a viable solu¡
tion. However , Bigtable is not open sourc ed and how email search is implemented 
remains a mystery. Cassandra might be a good option as well, but we haven 't seen 
any large email providers use it yet. 
Based on the above analysis , very few existing solutions seem to fit our needs perfectly . 
Large email service providers tend to build their own highly customized databases . How¡
ever, in an interview setting, we won't have time to design a new distributed database , 
though it's important to explain the following characteristi cs that the database should 
have. 
ò A single column can be a single-digit of MB. 
ò Strong data consistency . 
ò Designed to reduce disk 1/0. 
ò It should be highly available and fault -tolerant. 
ò It should be easy to create incr emental backups. 
Data model 
One way to sto re the data is to use user _id as a partition key so data for one user is stored 
on a single shard . One limitation of this data model is that messages are not shared among 
multiple users . Since this is not a requirement for us in this interview, it's not somethin g 
we need to worry about. 
Now let us define the tables . The primary key contains two components, the partition 
key, and the clustering key. 
Step 3 - Design Deep Dive I 237 


[Page 241]
ò Partition key: respnmib le for distributing cl ntA acrosc; nodes. l\s n gf'nrrtl l rul .. 'ò Wr w :rnt to spread the cl ala evenly. 
ò Clustering key : rrspo11sihlc for sor tin g data wi thi n A par t it ion. 
J\t a high k vd, an email service needs to supp ort Lhc following qu eries at the d l aa laye r: 
ò lhc first query is lo get aJl folders for a user. 
ò The second quer y is to display all emails for a specifi c folder. 
ò The Lhird query is lo crea le/dele le/ge l a specific email. 
ò 111c fourth query is lo fetch all read or unread emails. 
ò Bonus poin t: get conversa tion threa ds. 
Let 's lal<e a look al them one by one. 
Query 1: get all folders for a user. 
As shown in Table 8.1, user _id is th e partiti on k ey, so folders own ed by the s ame user 
are located in one partition. 
K Partition Key 
Cj Clustering Key (ascend¡
ing) 
G.!.tClusterlng Key (descend¡
~ing) 
folders _by_user 
user_id UUID K 
folder_id UUID 
folder name TEXT 
Table 8.1: Folder s by user 
Query 2: display all emails for a specific folder. 
When a user loads their inbox , emails are usually sorted by timestamp , showing the 
most rece nt ones at the top. In order to store all emails for the same folder in one parti¡
tion , composite partition key <user _id, folder _id> is used. Another column to note is 
email_id . Its data typ e is TIMEUUID [17], and it is the dustering key used to sort emails 
in chronolo gical order. 
238 I Chapt er 8. Distributed Email Service 
I 
I 
~ 
' , 
/ 
/ 


[Page 242]
╖-emalls _by_folder 
user_ld UUID K 
folder_id UUID K 
email_ id TIMEUUIDC ,t. 
from TEXT 
subject TEXT 
preview TEXT 
is_read BOOLEAN 
Table 8.2: Emails by folder 
Query 3: create/delete/get an email 
Due to space limitations , we only explain how to get detailed information about an email. 
The two tables in Table 8.3 are designed to support this query. The simple query looks 
like this: 
SELECT * FROM emails_by_user WHERE email_id c 123; 
An email can have multiple attachments, and these can be retrieved by the combination 
of emaiLid and filename fields. 
email s_by_user attachment s 
user_id UUID K email_id TIMEUUID c 
email_id TIMEUU ID C,t. filename TEXT K 
from TEXT url TEXT 
to UST<TEXT> 
subject TEXT 
body TEXT 
attachments LIST <filenamelsize> 
Table 8.3: Em.ails by user 
Query 4: fetc h all read or unread emails 
If our domain model was for a relational database , the query to fetch all read emails would 
look like this : 
SELECT * FROM emails_by_folder 
WHERE user _id = <user_id > and folder_id = <folder_id> and 
i s_read = true 
ORDER BY email _id; 
The query to fetch all unread emai ls would look very similar. We just need to change 
is_read = true to is_read = false in the above query. 
Step 3 - Design Deep Dive I 239 


[Page 243]
Our data model. however . is designed for NoSQL. A NoSQL database norma lly only sup¡
ports queries on parti tion and cluster keys. Since is_ read in the emails _by _ folcler table 
is neither of those. most NoSQL databases wi ll rrject thi s query . 
One way to gel around this limit ation is to fetc h the entire folder for a user and perform 
th e filtering in the application. This could w ork for a small email se rvice, but at our 
design scale. this does not work well. 
This problem is commonly solved with denormaliza tion in NoSQL. To supp ort the read¡
/unread queries, we denor mali ze the emails_by _folder data into two tables as shown in 
---
Table 8.4. r 
ò read_emails: it stores all emails that are in read status. 
ò unread_emails: it stores all emails that are in w1read status. 
To mark an UNREAD email as READ, the email is deleted from unread_emails and then in¡
serted to read_email s. 
To fetch all unread emails for a specific folder, we can rw1 a query like thi s: 
SEL ECT * FROM unread_email s 
WHERE user_id = <user_ id> and f older_i d = <folder _id> 
ORDER BY ema i l _id ; 
read_emails unread _ emails 
user id UUID K user_ld UUID 
folder_id UUID K folder_id UUID 
email_id TIMEUUID c ,i. email_id TIMEUUI D 
from TEXT from TEXT 
subject TEXT subject TEXT 
preview TEXT preview TEXT 
Table 8.4: Read and unread emai ls 
K 
K 
c.i. 
Denormalizat ion as shown above is a common practice . It makes the application code 
more compli cated and harde r to maintain , but it improve s the read performance of these 
queries at scale . 
Bonus point: conversation threads 
Threads are a feature supported by many e mail clients. It groups email replies with their 
original message [8]. This allows users to retri eve all emails associated with one conver¡
sation. Traditi onall y, a thread is implemented using algorithms such as JWZ algorithm 
[18]. We will not go into detail about the algorithm, but just explain the core idea behind 
it. An email header generally contains the following three fields: 
240 I Chapter 8. Distributed Email Service 
ò 
" 


[Page 244]
" header s " { 
} 
"Message - Id" : " <7BA 04 B2A- 00 C-4 012 - 8857 - 8621 G3 C34501 @gma.il. 
co m > 11 , 
11 In - Rep 1 y - To" : 
11 
< CAEWTXu Pf N::: L zEC j DJtgY 9 Vu 0 3 kgFv JnJ USHTt 6 
IW@gmail . com>" , 
"References" : [ 11 <7BA 04 B2A- 430 C- 4 012-8 B57- 862 10 3C3450 1@gmail 
. com>" ] 
Message-Id The value of a message ID. It is generated by a client while 
sendin g a message. 
In-Reply-To The parent Message-Id to which the message replies. 
References A list of message IDs related to a thread . 
Table 8.5: Email header 
With these fields. an email client can reconstruct mail conversations from messages , if 
all messages in the reply chain are preloaded. 
Consistency trade-off 
Distributed databases that rely on replication for high availability must make a funda¡
mental trade-off betwee n consisten cy and availability. Correctness is very important for 
email systems , so by design, we want to have a single primary for any given mailbox. In 
the event of a failover, the mailbox isn't accessible by clients, so their sync /update oper¡
ation is paused until failover ends. It trades availability in favor of consistency. 
Email deliverability 
It is easy to set╖ up a mail server and start sending emails. The hard part is to get emails 
actually delivered to a user 's inb ox. If an email ends up in the spam folder, it means there 
is a very high chance a recipient won 't read it. Email spam is a huge issue. According 
to research done by Statista [19], more than .503 of all emails sent are spam. If w e set 
up a new mail serve r, most likely our emails will end up in the spam folder because a 
new email serve r has no reputation. There are a couple of factors to consider to improve 
email deliverabi lity. 
Dedicated IPs . It is recommended to have dedicated IP addresses for sending emails. 
Email provide rs are less likely to accept emails from new IP addresses that h ave no his¡
tory. 
Classify emails . Send different categories of emails from different IP addresses. For 
example, you may want to avoid sending marketin g and other important emails from 
the same servers because it might make ISPs mark all emails as promotional. 
Email sender reputation. Warm up new email server IP addresses slowly to build a 
good reputation , so big providers such as Office365, Gmail, Yal100 Mail, etc. are less 
likely to put our emails in the spam folder. According to Amazon Simple Email Service 
[20], it takes about 2 to 6 weeks to warm up a new IP address. 
Step 3 - Design Deep Dive I 241 


[Page 245]
Ban spammers quickl y. Spammers shou ld he hr:innerl quickly before they havr a qjg. 
nificanl impact on Lhe server's repulat ion. 
Feedback proces sing. Jl's vrry impor tan t to set up feedback loops with ISPs so we can 
keep the comp laint rate low and ban spa m account s quickly . Jf an emai l failc; to deliver 
or a user complains, one of lhc following outcomes occurs: 
ò I lard bouncr . 111is means an cm<t il is rcjrc trd by ISP because the recipient 's email 
address is invalid. 
ò Soft bounce. A soft bounce indicat cs an emai l failed to deliver due to temporar y 
condi tions , such as ISPs being loo busy. 
ò Complaint. This means a recipient clicks the "report spam" button . 
Figure 8.8 shows the process of collectin g a nd processin g boun ces/co mplaints. We use 
separa te queu es for soft bounces, hard boun ces, and complaint s so they can be mana ged 
separa tely. 
(EJEJEJ() 
Soft boun ces 
r-::-1_ _. Bounces. and _ Feedback .__ _ _..,(EJ EJ EJ ( ) 
~ Complaints , processing . _ . 
'----- --.,----' Hard boun ces 
Com plaints 
Figure 8.8: Handl e feedback loop 
Email authentication. According to the 2018 data breach inve stigation report provided 
by Verizon, phishing and pretexting represent 933 of bre aches (21]. Some of the common 
techniques to combat phi shing are: Sender Policy Framework (SPF) (22], DomainKeys 
Identified Mail (DKIM) (23], and Domain -based Message Authentication , Reporting and 
Conformance (DMARC) (24]. 
Figure 8. 9 shows an example header of a Gmail message . As you can see, the sender 
@info6.ci ti. com is authenticated by SPF, DKIM, and DMARC. 
242 I Chapter 8. Distributed Email Service 


[Page 246]
Message ID ,,.-f'l1l "'╖1/1f /i1)~~f),{t)j(f"1/ -4; 11.11r4tf (1 )I '(i!tr ~ i 
Cree led at. Sun. May 2. 2021al6 41 PM (Delivered after 17 secondq) 
From : Citi Alerts <elerts@info6 .cltlcom> Using XyzMeiler 
To: @gmail com> 
Subject ╖ Your Citl« accoun t statement is ready 
SPF PASS wit h IP 63.239.204. 146 Lei:nn morr 
DKIM : 'PASS' with domain info6.citi com l.eom more 
DMARC . 'PAS S' l earn mo1 e 
Figure 8.9: An examp le of a Gmail header 
You don't need to remember all those terms. The imp ortan t thing to keep in mind is that 
getting emails to work as int ended is hard. It requires not only domain know ledge , but 
good relations hip s with ISPs. 
Search 
Basic mail search refers to searching for emails that contain any of the e ntered key¡
words in the subject or body. More advanced features include filtering by "From '', "Sub¡
ject'", "Unread", or other attributes . On one hand , whenever an email is sent , received, or 
deleted, we need to perform reindexing . On the other hand , a search query is only run 
when a user presses the search button . This means the search feature in email systems 
has a lot more writes than reads. By comparison with Google search , email search has 
quite different characteristics, as shown in Table 8.6. 
Scope Sorting Accu1╖acy 
Indexing generall y 
takes time , so some 
Google search The whole internet Sort by relevance items may not 
show in the search 
result immediately. 
Sort by attributes Indexing should be such as time, has 
Email search User's own email attachment , date near real-time, and 
box the result has to be within , is unread, accurate. etc. 
Table 8.6: Google search vs email search 
To support search functionality, we compare two approaches: Elasticsearch and native 
search embedded in the datastore . 
Step 3 - Design Deep Dive I 243 


[Page 247]
--
Option 1: Elasticsearch 
TI1e high -level design for emai l searc h using Elaslicsear ch is shown in Figure 8.10. Be¡
cause queries are mostly performed on the user's own <'mail serve r, we ca n gro up unc.ler╖ 
lying documents to the same node using user _id as I he partition key. 
Search Send email Receive email Delete email 
Async Async Async 
Sync Kafka 
RESTful API 
Elasticsearch Cluster 
Figure 8.10: Elasticsearch 
When a user clicks the search button , the user waits until the search response is received . 
A searc h request is synchronous . When events such as "send email'', "rece ive email" 
or "delete email " are triggered , nothing related to search needs to be returned to the 
client . Reindexing is needed and it can be done with offline jobs . Kafka is used in the 
desig n t o decouple services that trigger r eindexing, from services that actually perform 
re indexin g. 
Elasticsearch is the most popular search -engine database as of June 2021 [25] and it sup¡
ports full-tex t search of emails very well. One challenge of adding Elasticsearch is to 
keep our primary email store in sync with it. 
Option 2: Custom search solution 
Large-scale email providers usually develop their own custom search engines to meet 
their specific requirem ents. Designing an email search engine is a very complicated task 
and is out of the scope of this chapte r. Here we only briefly touch on the disk 1/0 bottle¡
neck, a primary challenge we will face for a custom search engine. 
As shown in the back-of-the -envelope calcu lation , the size of the metadata and attach¡
ments added daily is at the petabyte (PB) level. Meanwhile, an email account can easily 
have over half a million emails. The main bottleneck of the index server is usually disk 
I/O. 
244 I Chapter 8. Distributed Email Service 


[Page 248]
Since the process of building the ind ex is write-heavy. a good stra tegy might be to use 
Log-Structure d M erge-Tree (LSM) [26] to stru cture the index data on disk (Figure 8.11). 
111~ write path is optim.ized by only performing sequential writes. LSM trees are the core 
data structure behind databas es such as Bigtable , Cassa ndra, and RocksDB. When a new 
email arrives, it is first added to level 0 in-memory cache, and when data size in memo ry 
reaches the predefined threshold , data is merged to the next level. Another reason to use 
LSM is to separa te data that change frequently from those that don't. For example, email 
data usually does n't chang e, but folder information tends to change more often due to 
diff erenl' filter mles. In this case, we can separate them into two different section s, so 
that if a request is related to a folder change , we chang e only the folder and leave the 
email data a.lone. 
If you are interested in reading more about emai l searc h, it is highly recommended you 
take a look at how search works in Microsoft Exchange servers [27]. 
_ ................ -- .... -................. -........................ ╖--╖╖ .............. ---.......... --.......................................... -.. .. .. .. ............ -............ ---............ -......................... .. _.. : 
8 i 
nme 
Level4 
(disk) 
...... ------.. --...... ----.... -.. ----.. -...................... -----........ -.. -----........ ----....... --╖-..... ---..... _ ╖- ............. ----.. ..... .. -................ ---................. ......... ..... -.. ' 
------.................... -............................................................ ----.. --------.. ................ ----------.. ............... .. .. --..... .......... ---.. ----...... -------------...... , 
Level 3 
(disk) 
' ............ .. ------...... ------╖ .. .. --.. ----.. ...... -.. ----.... ---........ ------------------------.. .. --------........... --.. -.. -------------------.. -............ -. 
' 
----...... ---------....... - ---.......... ---........ --------.. ---..... ----- .... --- -------.............. ----.. -- .. ------.................. -----------------.... --
Level2 
(disk) gg 
' 
' 
' ' 
.......... ---------.... -------........ -----................ -----.. ------...... -.............. --.... ----......... -.. .. -----.. -..... ............. -------.... -............... .. ---------.. - -~ 
--.. --.. -------------------...... ---------------..... -- .. .. ,. ______ ----....... ----. ---.................. ---........ -------.... -----------------.. -.. --.. --... , 
uu uu 
Level 1 
ò (disk) 
' ........ ---.. .... ------........ ------.. --------... ------.. .. .. --.. .. ----------............................. .. ...... ----.. -................................. ---.. --.... ------....... ------
Figure 8.11: LSM tree 
' ' 
' 
Each approac h has pros and cons: 
Step 3 - Design Deep D ive I 245 


[Page 249]
1--F_e_a_tu_ r_e ______ --i __ E_l_a_s_ti_c_se_a_r_c_h ____ --=-~ Custom searc h eng~ 
Scalabi lity 
System complexity 
Data consistency 
Data loss possible 
Development effort 
Scalable lo some extent 
Need lo main tai-;-two -
different sys tems: datas ¡
lore and Elasticsearch 
Two copies of data. One 
in the metadata datas-
Easier to sca le as we can 
optimi ze the system for 
the email use case 
One system 
tore, and the other in A sing le copy of data in 
Elasticsearc h. Data con- the metada ta datasto re 
sistency is hard to main ¡
tain 
No. Can rebuild the 
Elasticsearch ind ex from 
the prim ary s torage, in 
case of failure 
Easy to integrate . To 
support large scale email 
search , a dedicated Elas¡
ticsearch team might be 
needed 
No 
Significant engineering 
effort is needed to de¡
velop a custom email 
search engine 
Table 8. 7: Elastic search vs custom search engine 
A general rule of thumb is that for a smaller scale email system, Elasticsearch is a good 
option as it's easy to integrate and doesn 't require significant engineering effort. For 
a larger scale, Elasticsearch might work , but we may need a dedicated team to develop 
and maintain the email search infrastructure . To support an email system at Gmail or 
Outlook scale, it might be a good idea to have a native search embedded in the database 
as opposed to the separate indexing approach . 
Scalability and availability 
Since data access patterns of individual users are independent of one another, we expect 
most components in the system are horizontally scalable. 
For better availability, data is replicated across multiple data centers. Users communica te 
with a mail server that is physically closer to them in the network topology . During a 
network partition, users can access messages from other data centers (Figure 8.12). 
246 I Chapter 8. Distributed Email Service 
-╖ ' ò' I 


[Page 250]
I 
I 
I 
r ----------------- - -----------------------------r------ -~------------ ---- -- ---- --1 
I 
Userfrom e 
United States i-. 
United States Data Center 
Servers Databases 
Replicatio n 
Servers Databases 
Europe Data Center 
' - --- - -- - ----------------------------------------------- --------------------------- ---- --~ 
r------------- --- -------- ------------------------------------------ - ----- - ----------- --- i 
I I 
Userfrom e 
United States ..a 
United States Data Cen ter 
Servers Databases 
Replication 
Servers Databases 
Europe Data Center 
' -- - ----------------- ~ ----- - - --- --------------- -------------- - ---------------------~-----
Figure 8.12: Multi-data center setup 
Step 4 - Wrap Up 
I 
In this chapter, we have presented a design for building large-s cale email servers. We 
started by gathering requirements and doing some back-of-the-envelope calculations to 
get a good idea of the scale. In the high-level design , we discussed how traditional email 
servers were designed and why they cannot satisfy modern use cases. We also discussed 
email APis and high-leve l designs for sending and receiving flows. Finally, we dived deep 
into metadata database design , email deliverability, search, and scalability . 
If there is extra time at the end of the interview. here are a few additional talking 
points: 
ò Fault tolerance . Many parts of the system can fail, and you can talk about how to 
handle node failures, network issues, event delays, etc. 
ò Compliance. Email service works all around the world and there are legal regulation s 
to comply with . For instance , we need to handl e and store personally identifiable 
information (PII) from Europ e in a way that complies with Genera l Data Protection 
Regulation (GDPR) [28]. Legal inter cept is another typical feature in this area [29]. 
ò Security. Email security is important because emails contain sensitive information . 
Step 4 - Wrap Up I 247 


[Page 251]
Gmail provides safety features such as phishing protections , safe browsing, proactive 
alert , account safety. confidential mode, and emai l encryp tion [30) . 
ò Optimizations. Sometimes, the same email is sent to multiple recipients , and the 
same email attachment is stored several times in the object store (S3) in the group 
emails . One optimiza tion we could do is to check the exis tence of the attac hm nt in 
storage. before performing the expensive save opera tion . 
C'ongra tuJations on gettin g this far! Now give yourself a pat on the back. Good job! 
248 I Chapter 8. Distributed Email Service 


[Page 252]
Chapter Summary 
step I 
step 2 
Ema.ii Servers 
step 3 
step 4 
funnlonAI req 
~(';\rch emails 
Anli-spam 
rl.'liability: we should not lose data 
exte nsibility 
non-functi onal rcq 
scalability 
storage heavy system POP 
emall protocols L IMAP 
~SMTP 
email knowledge IOI 
DNS --M.X record 
attachme nt --MIME 
email apis 
traditional mail. servers 
high-level design 
distributed mail servers 
email sending now 
email receiving now 
characte ristics 
choose the right databa se 
metadata databa se 
data model 
email dellverabllity consistency trade-off 
< 
elasUcsearch 
search 
custom search engine 
scala bility & availability 
f: ult t I node failure, netw ork issue, a oerance-- event delay 
Pll 
compliance< 
GDPR 
.t pWshing protection, safe brows-secun y-- . . . mg, email encryption . etc 
optimizatio ns __ the s_ame e~l was sent to 
multiple rec1p1ents 
Chapter Summary I 249 


[Page 253]
Reference Material 
[1] N umber of Active Gmail Users . hllp s://fi nanceso nlin e.com/ numb cr-of-ac live-grn 
aj]-users /. 
[2] Outl ook. https: //en.wikip edia.org /wiki /Outl ook.co m. 
[3] How Many Emails /\r e Sent Pe r Day in 2021? hllp s:// rcv icw42.co m/reso urccs/how 
-many -emails-arc -sent -per-day/. 
[ 4) RFC 1939 - Post Ofllce Pro toco l - Version 3. http ://www.faq s.org/rfc s/ rfcl 939.html. 
[ 5] Ac ti veSy nc. http s:/ /en. wikip cdia.org/wiki / Acliv eSync. 
[ 6] Email attachment. hllp s://en.wikipedia .org/wiki /Email _attachm ent. 
[7] MIME. http s://en.wikip edia.org/wiki / MIME. 
[8] Threading. http s://en.wikip edia.org/wik.i/Convers a tion _ threading. 
[9) IMAP LIST Extensi on for Special-Use Mailboxes . https ://datatracker.ietf.org /doc/h 
tml/rf c6154. 
[10] Apache James. https: //james .apache .org/. 
[11] A ]SON Meta Application Protoco l (]MAP) Subprotoco l for WebSocket. ht tps: //to 
ols.ietf.org /id/draft -ietf-jmap -webso cket-07.h tml#RFC7692. 
[ 12] Cassandra Limitations . https: //cwiki.apache .org / confl u en ce/ disp lay /CASS ANDR 
A2/CassandraLimitations . 
[ 13] Inverted index. https :// en.wikipedia.org /wiki/Inverted _index. 
[ 14] Exponential back off. https: // en. wik.ipedia .org/wiki /Expo n ential_backoff. 
[15] QQ Email System Optimization (in Chinese). https: //www.slideshare.net /areyo uo 
k/06-qq-5431919 . 
(16] IOPS . https ://en.wikiped.ia .org/wiki /IOPS. 
[17] UUID and timeuuid types . https: //docs .datastax.com /en/cql - oss/3.3/cql/c ql_refe r 
ence /uuid _type _r.html . 
[18] Message threading . https ://www.jwz.org/doc/ thread.ing .html . 
[19] Global spam volume . https ://www.s tat.ista.com/statistics /420391 /spam-email- traffi 
c-s hare /. 
[20] Warming up dedicated IP addresses . https ://docs.aws.amazon.com /ses/latest/ dg/de 
dicate d-ip-warming. html. 
[21] 2018 Data Breach Investiga tions Report. https: //enterprise .verizon.com / reso urces 
/reports/DBIR_2018_Report .pdf. 
250 I Chapter 8. Distributed Email Service 


[Page 254]
[22) SendC'r Policy Fram ework . hltp s://en .w ikipcdiA.org/wiki /Sr nder _Policy _Fra mewo 
rk. 
[23) DomainKeys Identifi ed Mail. https://en.w ikip edia .org/wiki/DomainK cys_lden tifi c 
d_Mail. 
(24) Domain-base d Message Authentication, Reportin g & Conform ance. http s://dmar c. 
org/. 
(25) DB-Engines Ranking of Search Engines. http s://db-engines.com/en/rankin g/sear 
ch+engine. 
[26] Log-stru ctured merge-tre e. http s:/ I en.wikipedia.org /wiki/Log-st ructured _merge- t 
ree. 
[27) Microsoft Exchange Confere nce 2014 Search in Exchange. https ://www.youtube.co 
m/watch ?v=SEXGCSzz Qak&t=2173s. 
[28) General Data Protectio n Regulation . https ://en.wikipedia .org/wiki /General_Dat 
a_Protectio n_Regulatio n. 
[ 29] Lawful interception. https: // en. wikipedia.org/wiki /Lawful_interception. 
[30) Email safety. http s://safety.google/ intl/en _us/gmail/. 
Reference Material I 251 


[Page 255]
9 53-like Object Storage 
In this chapter, we design an object storage service similar to Amazon Simple Storage 
Service (S3). S3 is a service offered by Amazon Web Services (AWS) that provides object 
storage thro ugh a RESTful API-basedint erface. Here are some facts about AWS 53: 
ò Launched in June 2006 . 
ò 53 added versionin g, bucket policy, and multipart upload support in 2010. 
ò S3 added server-side encryption , multi-object delete, and object expiration in 2011. 
ò Amazon reported 2 trillion obje cts stored in S3 by 2013. 
ò Life cycle policy, event notification , and cross-region replication support were intro¡
duced in 2014 and 2015. 
ò Amazo n r eported over 100 trillion objects stored in S3 by 2021. 
Before we dig into object storage, let's first review storage systems in general and define 
some terminologies . 
Storage System 101 
At a high-level, storage systems fall into three broad categories: 
ò Block storage 
ò File storage 
ò Object storage 
Block storage 
Block storage cam e first, in the 1960s. Common storage devices like hard disk dri ves 
(HDD) and solid-state drives (SSD) that are physically attached to serve rs are all consid¡
ered as block sto rage. 
Block storage presents the raw blocks to the server as a volume. This is the most flexible 
and versatile form of storage. The server can format the raw blocks and use them as a file 
system, or it can hand control of those blocks to an application. Some applications like 
I 253 


[Page 256]
-
a database or a virtua l machin e engi ne ma nage these blocks di rectly in order lo squeeze 
every drop of performa nce oul of them. 
Block storage is not limited to physica lly allached storage . Block storage could be con¡
nected lo a server over a high-spee d n r lwork or ove r indus try -stand<l rcl conn ectivity 
protoco ls like Pibrc Channel (FC) [ 1] and iSC'Sl [2]. Concep tua lly. thr netwo rk-attached 
block storage still present s row blocks. To the servers, it wo rks the sC1 mc as physically 
aliac hcd block storage. 
File storage 
File s torage is b uilt on t op of block storage. It pro vides a higher-level abstra ction to 
make it easier to handl e files and directori es. Data is s tored as files under a hierarchical 
direc tory s tru cture. File storage is the most comm on general -purp ose storage solution . 
File storage could be made access ible by a large number of servers using common file¡
level net work protocols like SMB/ClfS [3 J and NFS [ 4 J. The serv ers access ing file storag e 
do not n eed t o deal with the complexity of managing the blocks, form attin g volume, etc. 
TI1e simpli city o f file s tora ge makes iL a great solutio n for sharin g a large number of files 
and folders within an organi zation . 
Object storage 
Obje ct storage is new. It makes a very deliberate tradeoff to sacrifice performance for high 
dur ability, vast scale , and low cost. It targets relatively "cold" data and is mainly used for 
archival and backup . Object storage stores all data as objects in a flat structure. There is 
no hierarchical directory structure. Data access is normally provided via a RESTful APL 
It is relativ ely slow compared to other storage types. Most pub lic cloud serv ice providers 
have an object storage offering, such as AWS S3, Google object storage , and Azure blob 
storage . 
Comparison 
Block Storage 
r block ~ [block ~ r block ~ 
r block ~ [block ~ r block ~ 
[block ~ r block~ [block ~ 
File Storage 
Figure 9.1: Three different storage optio ns 
Table 9.1 compares block storage, file storage, and object storage. 
254 I Chapter 9. 53-like Object Storage 
Object Storage 


[Page 257]
- - ╖- --Block stora ge- -Fi le storage Object storage ╖-N (objccl vcrsioning 
Mutable y y is support ed, 
Content in-place upd ate is 
not) 
Cost High Medium to high Low 
Perfonnan ce Medium lo high , Medium to high Low to medium very high 
Consistency Strong consistency Strong consistency Strong consistency 
(5] 
Data access SAS [ 6 ]/iSCSI/FC Standard file access, RESTful API CIFS/SMB, and NFS 
Scalability Medium scalability High scalability Vast scalability 
Virtual machines 
(VM), General-purpose file Binary data , Good for high-performance 
applications like system access unstructured data 
database 
Table 9.1: Storage options 
Terminology 
To design S3-like object storage, we need to understand some core object storage concepts 
first. This section provides an overview of the terms that apply to object storage. 
Bucket . A logical containe r for objects . 1he bucket name is globally unique . To upload 
data to S3, we must first create a bucket. 
Object. An object is an individual piece of data we store in a bucket. It contains object 
data (also called payload) and metadata. Object data can be any sequence of bytes we 
want to store. The rnetadata is a set of name -value pairs that describe the object. 
Versioning. A feature that keeps multiple varian ts of an object in the same bucket. It is 
enabled at bucket-level. This feature enab les users to recover objects that are deleted or 
overwritten by accident. 
Unifo rm Resource Identifier (URI) . The object storag e provides RESTful APis to ac¡
cess its resourc es, namely, buckets and objects . Each resource is uniquely identified by 
its URL 
Service-level agreentent (SLA). A service- level agreement is a contra ct between a ser¡
vice provider and a client. For example , the Amazon S3 Standard -Infrequent Access stor¡
age class provides the following SLA [7]: 
ò Designed for durability of 99.9999999993 of objects across multiple Availability 
Zones. 
ò Data is resilient in the event of one entire Availability Zone destruction . 
Storage System 101 I 255 


[Page 258]
ò Designed for 99.03 availability. 
Step 1 - Understand the Problem and Establish Design Scope 
The following questions help to clarify the requirements and narrow down the 
scope. 
Can didate: Which features should be includ ed in the design? 
Interviewe r: We would like you lo design an S3-like object storage system with the 
following funclionali ties: ' 
ò Bucket creation. 1' 
ò Object uploading and downloading. 
ò Object versioning. 
ò Listing objects in a bucket. It's similai- to the aws S3 ls command [8]. 
Candidate : What is the typical data size? 
Interviewer : We need t o s tore both massive objects (a few GBs or more) and a large 
number of small objects (tens of KBs,) efficiently. 
Candidate : How much data do we need to store in one year? 
Interviewer : 100 petabytes (PB). 
. ~ 
Candidate : Can we assume data durnbility is 6 nines (99.99993) and service availability f 
is 4 nines (99.9 93)? 
Interviewer : Yes, that sound s reasonable . 
Non-functional requirements 
ò 1 OOPB of data 
ò Data durability is 6 nine s 
ò Service availability is 4 nines 
ò Storage efficiency. Reduce storage costs while maintaining a high degree of reliability 
and performance . 
Back-of-the -envelope estimation 
Object storage is likely to have bottlenecks in either disk capacity or disk IO per second 
(IOPS). Let's take a look. 
ò Disk capacity. Let's assume objects follow the distribution listed below: 
o 203 of all objects are small objects (less than lMB). 
o 603 of objects are medium-sized objects (1 MB rv 64MB). 
o 203 are large objects (larger than 64MB). 
ò IOPS. Let's assume one hard disk (SATA interface, 7200 rpm) is capable of doing 
256 I Chapter 9. 53-lfke Object Storage 


[Page 259]
100 ,...., 150 rand om seek s per seco nd (100 ,...., lSO TOPS). 
With those assumpti ons, we can estimat e the total numb er of objects the syste m can 
persist. To simplify th e calculati on, let's use the median size for each object type (0.5MB 
for small objects , 32.MB for medium objects, and 200MB for large objects). A 403 storag e 
usage ratio gives us: 
ò 100 PB = 100 x 1000 x 1000 x 1000 MB = 1011 MB 
1011 x 0.4 
ò (0.2 x 0.5 MB + 0.6 x 32 MB + 0.2 x 200 MB) = 0.68 billion objects . 
ò If we assume the metadata of an object is about IKB in size, we need 0.68TB space 
to store all metadata information. 
Even thou gh we may not use those numbers, it's good to have a general idea abo ut the 
scale and constraint of the system. 
Step 2 - Propose High-level Design and Get Buy-in 
Before diving into the design , lef s explore a few interesting properties of object storage, 
as they may influenc e it. 
Object immutability . One of the main differen ces between object storage and the other 
two types of stora ge sys tems is that the objects stored inside of object storage are im¡
mutable. We may delete them or replace them entirely with a new version, but we cannot 
make incremen tal chan ges. 
Key-value store . We could use object URI to retriev e object data (Listing 9.1). The object 
URI is the key and objec t data is the value. 
Request: 
GET /buck et 1 /o bj ec t1 . txt HTTP/ 1.1 
Response : 
HTTP /1 .1 200 OK 
Content- Length: 456 7 
[4567 bytes of object dat a] 
Listing 9.1: Use object URI to retrieve object data 
Write once , read many times . The data access pattern for object data is wri tten once 
and read many times. According to the research done by Linkedln, 953 of requests are 
read operations [9). 
Support both small and large objects . Object size may var y and we need to suppor t 
both. 
The design philosophy of object storage is very similar to that of the UNIX file system. 
In UNIX, when we save a file in the local file syste m, it does not save the filename and 
file data together. Instead, the filename is sto red in a data structure called ''inod e" [IO], 
Step 2 - Propo se High-level Design and Get Buy -in I 257 


[Page 260]
and the file data is stored in different disk locations. ╖n1c inode contains a list of file block 
pointers tha t point lo the disk locations of the f11e data. When we access a local file, we 
first fetch the metadatll in thr inodc. We then rellcl I hr file data by following the file block 
pointers to the actual clisk locations . 
TI1c object storage works sunilarly. The inodr becomes the metRclata store that stores all 
the object metadata . The hard disk becomes the data store that stores the object data. Jn 
the UNIX fiJe system, the inode uses the file block pointer lo record the location of data 
on Lhe hard disk. In object storage, the metada ta store uses the ID of the object to find 
the correspo nding objec t da ta in the data store, via a networ k request. Figure 9.2 shows 
the UNIX file syste m and the objec t storage. 
r----------------------------
1 
Unix File System : 
inode 
Fiie Name 
Owne r UID 
Group UID 
Mode 
Local Disk Access 
: Hard disk I 
I 
I 
I I , _ __________________ _ _ _______ ! 
,.. ------- ------- ----- ---- ---- -----, 
I I 
1 Obj ect Store System 
MetaStor e 
Object name-+-Object ID 
Object name-+-Object ID 
Object name -Obj ect ID 
Object name-Objec t ID 
Object name-Object ID 
I 
I 
Networ k Request 
DataStore 
--------------------------------
Figure 9.2: UNIX file system and object store 
Separating metada ta and object d ata s implifi es the design. The data s tore contains im¡
mut able data while the metadata store contain s mut able data. This separation enables us 
to impl ement and optimize these two components independently . Figure 9.3 shows what 
the bucket and object look like. 
258 I Chapter 9. S3-llke Object Storage 
1' 
r 


[Page 261]
Metedata 
ID 
Bucket Name 
Polley 1----
Ufe Cycle 
Bucket 
Dote 
0110101010110 
1010010101801 
9100180010100 
Metadeta 
ID 
Object Name 
Version ID 
Expiration 
Access Control 
Bucket 
Figure 9.3: Bucket & object 
High-level design 
Figure 9.4 shows the high-level design . 
ò 
r------------------------------~ 
I 
: Secondary I 
Data Store ~----1~ 
Service 
Storage Node 
Prima 
0 
Data Store ~--A 1 -----~ _ _ A_P_I _S~erv_ic_e_~-------'--+-..t Service LJ 
Storage Node Identity & Access 
Management 
r------------ ----------- -1 I 
I 
I 
I 
Metadata Service 1 
Metadata DB 
Metadata Store 
Seconda 
Data Store ~-¡
Service 
Slorage Node 
-------------------- - - -- - - - -- -Data Store 
Figure 9.4: High -level design 
Let's go over the compone nts one by one . 
Load balancer . Distributes RESTful API requ ests across a number of API servers. 
API service . Orchestrates remote pro cedure calls to the identity and access manage¡
ment service, metadata service, and storage stores . This service is statele ss so it can be 
horizontally scaled. 
Identity and access management (IAM ). The central place to hand le authentication , 
authorization, and access control. Authenti cation verifies who you are, and authorization 
validates what operations you could perform based on who you are. 
Step 2 - Propose High-level Design and Get Buy -in I 259 
l----


[Page 262]
Data to~ :10~ and retrienò the actuaJ data. All data-related operations an 
on ob_1ect ID l :-t 1D 
. letadata tore . ~tore: the metadata of the object . 
. "ote that the metadata and data. tore. are JU<\t logicaJ components. and there are dilrnmt 
wa~ _ to implement them. FN n.ample. m C'eph ╖ s Rado. Gatt wa\ [ 11 ). there is no 
alone metadata ~tore Enòn-thing. indudmg the object bucket. 1s persisted as one 
multiple Rado_ object 
:\ow we banò a ba 1c understanding of tJ1e lugh-le,╖el de 1gn. let╖ explore somr of the 
most important workflo w m ob1ect torage . 
ò Cploadmg an ob1ect. 
ò Download.mg an object. 
ò Ob1ect versiorung and h tmg object in a bucket They "ill be explained in the ╖de¡
sign deep din~ - section on page 263. 
Uploading an object 
ò ... 
Pl? CUT HTIP PUT: 
()Crea!a ~ @o-e&e olJied 
r------------ -- - --- - ---- -- ---~. 
« ~ 
ldEntly 
~end-' 
~ ~a:: 
' 
' 
~ ---~~.--~---' 
Identity & hx:ess 
Management 
r----------- -----------~ 
ò . 
l CJ 
I I s:,, 
- t 
Data 
Service 
~---- --- --------------------~ 
DataStore 
Figure 95: Uploading an object 
ò 
An object has to reside in a bucket In this example, we first create a bucket named 
bucket -to-share and then upload a file named script. txt to the buckeL Figure 9.5 ex¡
plains how this How works in 7 steps . 
L The client sends an HTTP PUT request to create a bucket named bucket - to-share. The 
----- - ---- - -
260 Chapter 9. 53- like Object Storage 
( 


[Page 263]
request is forwarded to the API service . 
2. The API service calls the IAM to ensure the user is authorized and has WRITE permi s¡
sion. 
3. The API service calls the meta.data store lo c reate an entry with the bucket in fo in 
the meta.data database . Once the entry is created , a success message is retur ned t o 
Lhe client. 
4. After the bucket is created , the client sends an HTTP PUT request to create an object 
named script. txt. 
5. The API servi ce verifies the user 's identity and ensures th e user has WRITE permiss ion 
on the bucket. 
6. Once validati on succee ds, the API service sends the object data in the HTTP PUT pay¡
load to the data s tore. 1he data store persists the payload as an object and r eturn s 
Lhe UUID of the object. 
7. The API service calls the meta.data store to create a new entry in the meta.data 
database. It contains important meta.data such as the obj ect_id (UUID), bucket _id 
(which bucket the object belongs to), obj ect _name, etc. A sample entry is shown in 
Table 9.2. 
object_name obj ect_id bucket _id 
script.txt 23905866-0052-00F6- 82AA182E-F599-4590-
014E-C914E61ED42B B5E4-1F51AAE5F7E4 
Table 9.2: Samp le entry 
The API to upload an object could look like this: 
PUT /bucket-to-sh are / script.txt HTTP/1.1 
Host: foo. s3example . org 
Oate: Sun , 12 Sept 202 1 1 7 : 51: 00 GMT 
Authorization: autho r ization st r ing 
Content-Type: t ext/ plain 
Content- Length : 456 7 
x - a rn z -met a -au tho 1╖ : A 1 ex 
[4567 bytes of object data ] 
Listing 9.2: Uploading an object 
Downloading an object 
A bucket has no directory hierar chy. However, we can create a logical hierarc hy by 
concatenating the bucket name and the object name to simulate a folder stru cture. For 
example, we name the object bucket-to-share/script. t xt instead of script. txt . To ge t 
an object, we specify the object name in the GET request. 1he API to download an objec t 
looks like this: 
Step 2 - Propose High-level Design and Get Buy -in I 261 


[Page 264]
G [ 1 I bur k P t. - Lo sh a r e I s c r╖ i pi . t. x l II 1 l P / 1 . 1 
ll0~l. foo.s3exnmple.or9 
Ont.e: Sun, 1Z Sept. ,()(1 18:30:!11 GMl 
J\ u t. ho n n~ ti on : au tho r i z a l. i n n s L r╖ i n fl 
Listing 9.3: Dow nloading an objecl 
HTIP GET: 
CD/bucket-to-share/ 
script.txt 
« 
ò ... 
@ Download object 
@ 
Get 
~ -------- ------ ------ - - -- ------ -
' I I I 
' Seco ndary i 
Storage 
Service i----.LJ 
'------' 
Storage Node 
Prima 
0 
Identity 
- validation and 
authorization 
API Service - object by __.___.__, 
~-~f,_-----' UUID 
Storage 
Service 
Identity & Access 
Managemen t 
Query DB to get 
@ object location 
(UUID) 
------------- ------------╖ I 
' ' Metadata Servic e 
LJ 
Metadata DB 
Metadata store 
Figure 9.6: Downloading an object 
Storage 
Service 
Storage Node 
Second a 
Storage Node 
Data Store 
---
As menti oned ear lier, the data s tore does not store the name of the o bject and it only 
suppor ts o bject opera tions via obj ect_id (UUID). In order t o downlo ad the object, we 
first map the object name to the UUID. The workflow of downl oading an object is shown 
below: 
1. The client sends an HTTP GET request to the load balancer : GET /bucket-to-s hare / sc 
ript . txt 
2. The API service queries the IAM to verify that the user has READ access to the bucket. 
3. Once validated, the API service fetches the correspondin g object's UUID from the 
met adata store. 
4. Next, the API service fetches the objec t data from the data store by its UUID. 
5. The API service r eturn s the object data to the client in HTTP GET response. 
262 I Chapter 9. 53-like Object Storage 


[Page 265]
Step 3 - Design Deep Dive 
In this section, we dive deep into a few areas: 
ò Data store 
ò Metadata data model 
ò Listing objects in a bucket 
ò Object versioning 
ò Optimizing up]oads of large files 
ò Garbage collection 
Data store 
Let's take a closer look at the desig n of the data store . As discussed previou sly, the API 
service handles external reques ts from users and calls different internal services to fulfill 
those requests . To persist or retrieve an object, the API service calls the data store . Figure 
9. 7 shows the int eractions between the API service and the data store for uploading and 
down1oad.ing an object. 
Upload Object 
- - - - Request: Upload 
I 
A~I (-.---- Payload: file_content -----_.A 
_ Service j---_ ~ 
. DataStore 
Response: Ob1ectlD=30a3e98e-55d9-11ec-bf63-0242ac130002 
Download Object 
Request: Download 
IAPll----- Object lD: 30a3e98e-55d9-11ec-bf63-02~2ac130002..... --. 
~----------- . DataStore Response: data = ftle_content 
Figure 9.7: Upload and download an object 
High-level design for the data store 
The data store has thr ee main components as shown in Figure 9.8. 
Step 3 - Design Deep Dive I 263 


[Page 266]
Data Node 
[⌐] Primary 
Data traffic / I \ 
~ Heartbeat Data rephcatlon 
i 
Placement H b ~ Data 1
- ----
1 
Service ò - eart eat t3J repllcatlon 
~---~ Data N~d; 
Data routin g service 
Secondary 
Heartbeat 
[⌐] Secondary 
Data Node 
Figure 9.8: Data store compon ents 
1h e data routing service provides RESTful or gRPC [12] APis to access the data node 
cluster. It is a stateless service that can scale by adding more servers . This service has 
the following responsibili ties: 1~ 
ò Qy.ery the placement service to get the best data node to store data. 
ò Read data from data nodes and return it to the API service. 
ò Write data to data nodes. 
Placement service 
Th.e place ment service determine s which data nodes (primar y and replicas) should be 
chosen to store an object. It maintains a virtual cluster map, which provides the physical 
topology of the cluster. The virtual cluster map contains location information for each 
data node which the placement service uses to mal{e sure the replicas are physically 
separated. 1his separation is key to high durability. See the "Durability" section on 
page 270 for details. An example of the virtual cluster map is shown in Figure 9.9. 
Root Default 
Figure 9.9: Virtual cluster map 
264 I Chapter 9. 53-like Object Storage 
~ 


[Page 267]
The placement service continuous ly monit ors all data nodes through hcarth eals . If a 
data node doesn 't send a heartbeat within a configurable 15-sccond grace period, Lhc 
placement service marks the nod e as "down " in the virtu al cluster map. 
This is a critical service , so we suggest buildin g a cluster of 5 or 7 placement servi ce 
nodes with Paxos [13] or Raft [14] consensus proto col. The consensus proto col ensures 
that as long as more than half of the nodes are healthy, the service as a who le continue s 
to work. For example , if the plac ement service cluster has 7 nodes, it can tolerate a 3 
node failure. To learn more abo ut consensus protocols , refer to the reference materials 
[13] [14]. 
Data node 
1he data node stores the actual object data. It ensures reliability and durability by repli¡
cating data to multiple data nodes , also called a replication group . 
Each data node has a data service daemon running on it. The data service daemon con¡
tinuously sends hear tbeats to the placement service. The heartbeat message includes the 
follO\ving essential information: 
ò How many disk drives (HDD or SSD) does the data node manage? 
ò How much data is stored on each drive? 
When the placement service receives the heartbeat for the first time, it assig ns an ID 
for this data node, adds it to the virtual cluster map, and returns the following informa¡
tion: 
ò a unique ID of the data node 
ò the virtual cluster map 
ò where to replicate data 
Data persistence flow 
I ,._ 
Step 3 - Design Deep Dive I 265 


[Page 268]
Data Store Data Node 
@Send data to primary node 
/~Pnma~ 
@ 
Heartbeat @ Data 
rep II cation 
Data Routing 
Service 
~Write data 
~~Reply with ~ ObJld -r--'-- -----1 
Choose 
primary by 
consulting 
placement 
service 
Placement 
Service Heartbeat 
Heartbeat 
Figure 9.10: Data persistence flow 
Now let 's take a look at how data is persiste d in the data node. 
1. The API service forwards the object data to the data store. 
i 
Data 
replical!on 
Data Nod; J Seconda/ 
[0] Secondary 
Data Node 
2. The data routing service generates a UUID for this object and queri es the placement 
service for the data node to store this object. The placement service checks the virtual 
cluster map and returns the primary dat a node. 
3. The data routing service sends data directly to the primar y data node, together with 
its UUID. 
4. The primary data node saves the data locally and replicates it to two secondary data 
nodes . The primary node responds to the data routin g service when data is success¡
fully replicated to all secondary nodes. 
s. The UUID of the object (Objld) is returned to the API service. 
In step 2, given a UUID for the object as an input , the placement service returns the 
replication group for the object. How does the placement service do this? Keep in mind 
that this lookup needs to be deterministic , and it must survive the addition or removal 
of replication groups. Consistent hashin g is a common implement ation of such a lookup 
function . Refer to [15] for more information . 
the rimary data node replicates data to all secondary nodes before it returns 
In step 4, P ╖ all d d Thi ╖ t 1his makes data strongly consistent among ata no es. s consis ency 
a response. ╖ ╖1 h 1 li fin' h p╖ . h 1 t y costs because we have to wait unh t es owest rep ca is es. ig-mes wit a enc co h the trade-offs between consistency and laten cy. ure 9.11 s ows 
266 9 53-like Object Storage Chapter ╖ 
! 
I 
I 
l 
I 
I 


[Page 269]
-
--- API service wait time J 
Data routing service 
Primary data node 
Secondary data node 1 
Secondary data node 2 
Data routing service 
Primary data node 
Secondary data node 1 
Secondary data node 2 
Data routing service 
Primary data node 
Secondary data node 1 
Secondary data node 2 
Flrst option: 
Best consistency 
Highest latency 
Second option: 
Medium consistency 
Medium latency 
Third option: 
Worst consistency 
Lowest latency 
Figure 9 .11: Trade-off between consistency and latency 
1. Data is considered as successfu lly saved after all three nodes store the data . This 
approac h has the best consistency but the highest latency. 
2. Data is considered as successfully saved after the primary and one of the secondaries 
store the data. This approach has a medium consistency and medium latency . 
3. Data is considered as successfully saved after the primary persists the data. This 
approach has the worst consistency but the lowest latency. 
Both 2 and 3 are forms of eventual consis tency. 
How data is organized 
Now let's take a look at how each data node manages the data. A simple solution is to 
store each object in a stand-alone file. This works, but the performance suffers when 
there are many small files. Two issues arise when having too many small files on a file 
system. First, it wastes many data blocks. A file system stores files in discrete disk blocks. 
Disk blocks have the same size, and the size is fixed when the volume is initialized. The 
typical block size is around 4KB. For a file smaller than 4KB, it would still consume the 
entire disk block. If the file system holds a lot of small files, it wastes a lot of disk blocks. 
wilh each one only lightly filled with a small file. 
Second, it could exceed the system 's inode capacity. The file system stores the location 
and other information about a file in a special type of block called inode. For most file 
systems, the number of inodes is fixed when the disk is initialized. With millions of 
small files, it runs the risk of consumin g all inodes. Also, the operating system does not 
handle a large number of inodes very well, even with aggressive caching of file syst em 
Step 3 - Design Deep Dive I 267 
-----


[Page 270]
meladala. For these reasons, storing small objr r ts <1s individua l tllc><; <lore; not work w~n 
in prnclice. 
To address these issues, we ra n mrrgr many small ohjcclc; int o a l<1rgrr file. Jt work<; 
conceptu ally like a write-ahrad log (WAL). W hr n we save an ohjrrt, it is apprn ded to an 
existing read-write file. When. lhr rr~d -writr filr rrac hrs its capacity threshold (usually 
sel to a few GRs). the read-wnt c file is marked as read-only a nd a new read-write file ic; 
created lo receive new objects. Once a file is markr d as read-only, it can only serve read 
requ ests. Figure 9.12 e, plains how this process works. 
API Service 
Read-only File Read-only Fiie Read-write File object4 
object 1 
object 2 
object 3 
object 4 
Empty spaces 
Local File System 
Figure 9.12: Store multiple s mall objects in one big file 
Note that write access to the read-write file must be serialized. As shown in Figure 9.12, 
objects are stored in order, one after the other, in the read-wri te file. To maintain this on¡
disk layout , multiple cores processing incoming write requests in parallel must take their 
turns to write to the read-write file. For a modern server with a large number of cores 
processing many incoming requests in parallel, this seriously restri cts write throughput. 
To fix this, we could provide dedicated read -write files, one for each core pro cessing 
incoming requests. 
Object lookup 
With each data file holding many small objects, how does the data nod e locate an object 
by UUID? The data node needs the following information: 
ò The data file that contain s the object 
ò The startin g offset of the object in the data file 
ò The size of the object 
268 I Chapter 9. 53-like Object Storage 


[Page 271]
TI1e database schema lo support this lookup is shown in Table 9.3. 
Field 
object_id 
f ile_name 
start _offset 
object_size 
object _ mapping 
object_ Id 
file_name 
start_ offset 
object_ size 
Table 9.3: Object_mapping table 
Description 
UU1D of the object 
The name of the file that contains the object 
Beginning address of the object in the file 
The numb er of bytes in the object 
Table 9.4: Object_mapping fields 
\Ve considered two option s for storing this mapping: a file-based key-value store such as 
RocksDB [16] or a relational database . RocksDB is based on SSTable [17], and it is fast 
for writes but slower for reads. A relational database usually uses a B+ tree [18] based 
storage engine, and it is fast for reads but slower for writes. As mentioned earlier, the 
data access pattern is write once and read multiple times. Since a relational database 
provides better read performance, it is a better choice than RocksDB. 
How should we deploy this relational database ? At our scale, the data volume for the 
mapping table is massive. Deploying a single large cluster to support all data nodes could 
work, but is difficult to mana ge. Note that this mapping data is isolated within each data 
node. There is no need to share this across data nodes. To take advantage of this property , 
we could simply deploy a simple relational database on each data node. SQLite [19] is a 
good choice here. It is a file-based relational databas e with a solid reputation. 
Updated data persistence flow 
Since we have made quit e a few changes to the data node, let's revisit how to save a new 
object in the data node (Figure 9.13). 
1. The API service sends a request to save a new object named object 4. 
2. The data node service appends the object named object 4 at the end of the read-writ e 
file named I data/ c. 
3. A new record of object 4 is inserted into the object_mapping table. 
4. The data node service returns the UUID to the API service. 
Step 3 - Design Deep Dive I 269 


[Page 272]
Local MnchlMC! 
/\Pl SM'lce 
\ 
j~ 
[ 
Data Node> 1 
Sf'l'VICI) 
RMd -only Fiio 
/da ta/a 
Road-only Fll!I 
/d818f!J_ 
R1>ad-wrlte Fiie 
/data/c I ' ... ' 
object 1 
object 2 file name 
obj Id 
- -':._ 
object 3 òò start offset - - ╖ 
-----╖---------╖ 
object 6 
' , object 4 : 
.. - --- ... - .... ---- - - - I 
objeci _slze ò 
Empty spaces 
Local Fiie System 
object mapping table 
file _name offset 
. 
- --.. 
-/data/c OX23283 
. 
Object Mapping 
Database 
-
obi . size 
512 
- - - --- -------╖ ------------- - ----- ---- ------------------ --------- -- ------- ------ -- -- - ------ ------ -- ---- ----- - ------ -- -------------╖ 
Figure 9.13: Updated data persistence flow 
Durability 
Data reliability is extremely important for data storage s ystems. How can we create a 
storage system that offers six nines of durability ? Each failure case has to be carefully 
considered and data needs to be properly replicated . 
Hardware failure and failure domain 
Hard drive failure s are inevitable no matter which media we use. Some storage media 
m ay have better durability than others , but we cannot rely on a single hard drive to 
achieve our durability objective. A proven way to increase durability is to replicate data 
to multipl e hard drives, so a single disk failure does not impact the data availability, as a 
wh ole. In our design , we replicate data three times. 
Let's assume the spinning hard drive has an annual failure rate of 0.813 [20]. This 
numb er highly depends on the model and make. Making 3 copies of data gives us 
1 - 0.00813 =,....., 0.999999 reliability. This is a very rough estimate. For more sophisti¡
cated calculations , please read. [20]. 
For a complete durability evaluation, we also need to consider the impacts of different 
failure domains . A failure domain is a physical or logical section of the environment that 
is negat ively affected when a critical service experiences problems. In a modern data cen¡
ter, a server is usually put into a rack [21], and the racks are grouped into rows/floors /¡
rooms. Since each rack shares network switches and power , all the servers in a rack 
are in a rack-level failure domain. A modern server shares components like the mother¡
board , processors, power supply, HDD drives, etc. The components in a server are in a 
node-level failure domain. 
Here is a good example of a large-scale failure domain isolation. Typically, data cen-
270 I Chapter 9. 53-like Object Storage 
' 


[Page 273]
r---
trrs diVJdc infrnstruc tu rc tlrnt slrnres nothin g into different /\vRilahi hty Zo nes (/\Zs) . We 
replicate our data to diff cren t J\Zs lo minimi ze the failur e imp act (Fi[!;ure 9. 14). Not e 
thAI the choice of failure domain leve l doesn 't directly increase the durability of da ta, 
bu1 it will result in bett er r eliability in extreme cases, suc h as large -scale powe r o uta ges, 
cooling syste m failure s, naturaJ disast er s, etc. 
AZ 1 
(Independent power and networking) 
Rack 1 Rack 2 
I Node 1 I I Node 1 I 
I Node 2 I I Node 2 I 
Replicate Replicate 
AZ3 AZ2 
(Independent power and networking) (Independent power and networking) 
Rack 1 
I Node 1 I 
I Node 2 I 
Erasure coding 
Rack 2 Rack 1 
I Node 1 I 
Replicate 
I Node 1 j 
I Node 2 I I Node 2 I 
Figure 9.14: Multi -Datacenter replication 
Rack2 
I Node 1 I 
j Node 2 j 
Ma.king three full copies of data gives us roughly 6 nines of data durability. Are there 
other options to further increase durability? Yes, erasure coding is one option. Era ¡
sure coding (22] deal s with data durability differently. It chunks data into smaller pieces 
(placed on different servers) and creates parities for redw1dancy. In the event of fai lures, 
we can use chunk data and parities to reconstruct the data. Let's take a look at a concrete 
example (4 + 2 erasure coding) as shown in Figure 9.15. 
Step 3 - Design Deep Dive I 271 


[Page 274]
<D 
Sphl into 
equal-sized 
data chun ks 
« 
Calculate 
pari ties 
(3) 
Data loss due 
lo node crash 
Figure 9.15: Erasure coding 
Data 
recons truction 
1. Data is broken up into four even-sized data chunk s dl, d2, d3, and d4. 
2. The mathematical formula [23] is used to calculate the parities pl and p2. To give a 
much simplifi ed example , pl= dl +2 x d2 - d3 +4 x d4 and p2 = -dl +5xd2 + d3 
-3 xd4 [24]. 
3. Data d3 and d4 are lost due to node crashes. 
4. The mathematical formula is used to reconstruct lost data d3 and d4, using the known 
val ues of dl , d2, pl , and p2. 
Let 's take a look at another examp le as shown in Figure 9.16 to helter understand how 
erasure coding works with failure domains. An (8+4) erasure coding setup breaks up the 
original data evenly into 8 chunk s and calculates 4 parities. All 12 pieces of data have the 
same size. All 12 chunk s of data are distributed across 12 different failure domains. The 
mathematic s behind erasure coding ensures that the original data can be reconstructed 
when at most 4 nodes are down. 
272 I Chapter 9. 53-like Object Storage 


[Page 275]
-
o1J ooo 
DODOO 
DODOO 
DODOO 
00000 
00000 
00 
0 
ODDO 
DODOO 
Failure Domain 
00000000 
Math Calculation 
a 
0 DODOO 
Failure Domain Failure Domain Failure Domain 
Figure 9.16: (8 + 4) erasure coding 
Compared to replication where the data router only needs to read data for an object 
from one healthy node, in erasure coding the data router has to read data from at least 
healthy nodes . This is an architectural design tradeoff. We use a more comp lex solution 
with a slower access speed, in exchange for high er durability and lower storage cost. For 
object storage where the main cost is storage, this tradeoff might be worth it. 
How much extra space does erasure coding need? For every two chunk s of data , we 
need one parity block, so the storage overhead is 503 (Figure 9.17). While in 3-copy 
replication, the storage overhead is 2003 (Figure 9.17). 
Step 3 - Design D eep Dive I 273 


[Page 276]
3 copy r1>plK'~t 1on 
DAta 1~ c11$lnhuted Ar.ro~ 3 nod~ 
~ 
1GB 
0 25 0 25 0 '~ 0 25 0.25 0 25 
G6 Gil GB GS G8 00 
f 
Data is distr ibuted across 6 nodes 
Erasure coding (4+2) 
-╖ 
Figure 9.17: Extra space for replication and erasu re coding 
Docs erasure coding increase data durability? Let's assume a node has a 0. 13 annual 
failure rate . According to the calculation done by Backblaze [20], erasu re coding can 
achieve 11 nines durabiLity. The calculation requires complicat ed math . If you 're inter¡
este d, refer to [20) for details. 
Table 9.5 compares the pros and cons of replication and erasure coding . 
Replication Erasure coding 
6 nines of durability (data 11 nines of durability (8 + 4 
Durability erasure coding). Erasure copied 3 times) coding wins. 
Storage 2003 storage overhead. 503 storage overhead. Erasure 
efficiency coding wins. 
Comp ute No computa tion. Replication Higher usage of computa tion 
resource wins . resources to calcula te parities . 
Write Replicating data to multiple Increased write latency because 
performance nodes. No calculation is needed. we need to calculate parities 
Replication wins. before data is written to disk. 
In normal operatio n, reads are In normal operation, every read 
served from the same replica. has to come from multipl e 
Read Reads under a failure mode are nod.es in the cluster. Reads 
performance not impacted because reads can under a failure mode are slower 
be served from a non-fault because the missing data must 
replica. Replication wins. be reconstructed first. 
Table 9.5: Replication vs erasure coding 
In summary, replication is widely adopted in latency-sensitive applications while erasure 
coding is often used to minimize storage cost. Erasure coding is a ttractive for its cost 
274 I Chapter 9. 53-like Object Storage 


[Page 277]
rffir1rncv And ch1rnhilil y. h11I ii p.rrn tl rompll cnl<'ll llw d11ln 11 nd1ò dtòsign. 'lll,╖1<'11111╖. 1111 
this drsi,rn . wr motnl ' fnn1s nn rrpltrnlinn. 
Correctness verification 
Ernsuf'(' codmg incrrascs dAln durnhilil y nl cornpnrnhlc╖ storngt' c:oslN. Now we' < 1111 1111w1╖ 
on to solve nnothcr lrnrd clrnllcn╡c: dRln corrnpt lnn. 
If a disk fails completely And the fnihm.ò cnn ll<' dC' lrclrd, It cnn be lrcnt<òd ns n clntn nodeò 
fndure. In this case, we can reconstruct dAIR using rrnsurc coding. I lowC'VN , In rttt.╖mory 
dalR corrup tion is a reguJer occurrence in lnrgcò-srnlc RyRlcms. 
This problem can be addressed by verifying checksums [25] between proccAs bnunclnrlrR. 
A checksum is a small-sized block of data that i.s used lo dclecl dolR crror11. Figureò 9.18 
11lustratcs how the checksum is generated. 
Data 
Checksum 
011e1e101a110 Checksum I F6 l 18HlG1G1G1GG1 
~ 
algorithm I F7 33 51 1 B 90 
010G1GGGHl1GG 
Figur e 9.18: Generate checksum 
If we know the checksum of the original data, we can comput e the checksum of the data 
after transm ission: 
ò lf they are different, data is corrupt ed. 
ò lf they are the same, there is a very high prob ability the data is not corrupt ed. Th e 
probability is not 1003, but in prac tice, we could assume they are the sa me. 
Check.sum or Checksum ol the 
the original data received data 
F7 33 51 1 8 90 f6 I-Compare -+j F7 33 51 18 90 F6 I 
Figur e 9.19: Compare checksums 
There are many checksum algorithms, such as MDS [26), SHAl [27], HMAC [28], etc. A 
good checksum algorithm usually output s a significantl y different value even for a small 
change made to the input. For this chapt er, we choose a simple checksum algorithm suc h 
asMD S. 
In our design, we append the checksum at the end of each object. Before a file is marked 
as read-only, we add a c hecksum of the e ntir e file at the e nd . Figure 9.20 shows th e 
layout. 
Step 3 - Design Deep Dive I 275 


[Page 278]
Read-only File Read-only Filo Read-write File 
object 1 Checksum 
object 2 Checksum 
object 3 Checksum 
object 4 Checksum 
objec t 5 Checksum 
Empty spaces 
-
......_ 
Checksum Checksum 
Local Fiie System 
Figure 9.20: Add checksum to data node 
With ( + 4) erasure coding and checksum verification , this is what happens when we 
read data : 
1. Fetch the object data and the checksum. 
2. Comput e the checksum against the data received. 
(a) If the lwo checksums match , the data is error-free. 
(b) If the ch ecksums are different, the data is corrup ted. We will try to recover by 
readin g the data from other failure domains . 
3. Repea t steps 1 and 2 until all pieces of data are returned . We then reconstruct the 
data and send it back to the client. 
Metadata data model 
In this section , we first discuss the database schema and then dive into scaling the 
database . 
Schema 
The database schema needs to support the following 3 queries: 
Qyery 1: Find the object ID by object name. 
Qyery 2: Insert and delete an object based on the object name. 
Qyery 3: List objects in a bucket sharing the same prefix. 
276 I Chapter 9. 53-like Object Storage 


[Page 279]
Figure 9.2 1 shows the schema desig n. We need two d<lt <\base tab les: bucket ~111d 
object. 
bucket 
bucket_ name 
bucket_ Id 
owner_ld 
enable_ versionlng 
object 
bucket _ name 
object_name 
object_ version 
object_ Id 
Figure 9.21: Database tables 
Scale the bucket table 
Since tJ1ere is usually a limit on the number of buckets a user can create, the size of the 
bucket table is small Let's assume we have 1 million customers, each customer owns 10 
buckets and each record takes lKB. That means we need lOGB (1 million x 10 x lKB) 
of storag e space. lhe whole table can easily fit in a modern database server. However , a 
single database server might not have enough CPU or network bandwidth to handl e all 
read requests . If so, we can spread the read load among multiple database replicas. 
Scale the object table 
The object table holds the object metadata . 1he dataset at our design scale will W<ely not 
fit in a single databa se instance. We can scale the object table by shard!ing. 
One optio n is to shard by the bucket_id so all the objects under the same bucket are 
stored in one shard . 1his doesn' t work because it causes hotspot shards as a bucket 
might contain billions of objects. 
Another option is to shard by obj ect_id. The benefit of this sharding scheme is that 
it evenly distributes the load. But we will not be able to execute query 1 and query 2 
efficiently because those two queries are based on the URI. 
We choose to shard by a combination of bucket_name and object_name. This is becaus e 
most of the metadata operations are based on the object URI, for example, findin g the 
object ID by URI or uploading an object via URI. To evenly distribute the data, we can 
use the hash of the <bucket_name, obj ect_name> as the sharding key. 
With this sharding scheme , it is straightforward to support the first two queries , but the 
last query is less obvious. Let's take a look . 
Listing objects in a bucket 
The object store arranges files in a flat structure instead of a hierarchy , like in a file system . 
An object can be accessed using a path in this fonnat, s3: //bucket-name/ object-name. 
For example, s3: //mybucket/abc/d/e/f /file. txt contains: 
ò Bucket name : mybucket 
ò Object name : abc/ d/ e/f /file. txt 
Step 3 - Design Deep Dive I 277 


[Page 280]
-
To help users organize Lhcir objec ts in a bucket , S3 introdu ces a concept called ' prefixes '. 
A prefix is a s tring al the beginnin g of th e objec t n ame. S3 uses prefixes lo organize the 
drila in a way similar to directo ries. 1 Iowevc r, prefixes arc not di rec tories. Listing a bucket 
by prefix limit s the results lo only tho se object name s that begin with the prefix . 
In th e exa mple a bove wilh the palh s3: //mybucket/abc/d/e/f /file . txt , the prefix is 
abc/d/e/f/. 
The /\WS 53 listin g command has 3 typical uses : 
1. List all buckets owned by a user . 'lhe comma nd looks like this: 
8ws ,~ list - buckets 
2. List all objects in a bucke t thal are a t the same leve l as the specifie d prefix. The 
co mmand looks like this: 
aws $ ls s~ ://my b ucket/abc/ 
In this mode , objects with more slashes in the name after the prefix are rolled up into 
a common prefix. For examp le, with these objects in the bucket: 
CA/cities/ l osangele s.tx t 
CA/cities/s anf ranci so. t xt 
NY/cit i es/ ny . t xt 
fede ral .tx t 
Listin g th e bucket with the 
11 
/
11 
prefix would return these resu lts, with everythin g 
und er CA/ and NY/ rolled up into them: 
CA/ 
NY I 
federal . txt 
3. Recurs ively list all objects in a b ucket that shares the same prefix . The command 
looks like this: 
aws s3 l s s3 : //m ybucket/a bc/ -- recursi ve 
Using the same example as above, listing the bucket with the CA/ prefix would return 
these res ults: 
CA/ci t i es / l osange le s.tx t 
CA/citi es/s anf ranci so. t xt 
Single database 
Let's first explore how we would supp ort the listin g command with a single database. To 
list all buckets owned by a user, we run th e following query: 
SELECl * FROM bucket WHERE owner_id={id } 
To list all objects in a bucket that share the s ame prefix, we run a quer y like this . 
SELECT * FROM object 
WHE RE bucket _id = 
11
123
11 
ANO object _name LIKE ' abc/%' 
278 I Chapter 9. 53-like Object Storage 
' . 


[Page 281]
-
ln thjs example. we find all objer ls with bucket _id equal s to 123 that share thr prefix 
abc/. Any objects with more slashes in their names after the specified prefix arc rolled 
up in the applicati on code as sta led eRrlier in use case 2. 
Tue same query would suppor t the recursive listing mode, as stated in use case 3 pre ¡
viously. Tiw application code would list every object sharing the same prefix, without 
performing any rollups. 
Distributed databases 
When the metadata table is sharded, it's difficult to implement the listing fun ction be¡
cause we don't know which shards contain the data . 1l1e most obvious solution is to run 
a search query on all shard s and then aggregate the results . To achieve this, we can do 
tl1e following: 
1. The metadata service queries ever y shard by running the foll.owing query : 
SELECT * FROM object 
WHERE bucket_id = 
11
123" AN O object _name LIK E 'a /b/tli ' 
2. The metadata service aggregates all objects returned from each shard and returns the 
result to the caller. 
Th.is solution works , but implementin g pagination for this is a bit complicated. Before we 
explain why, let's review how pagination works for a simple case with a single database. 
To return pages of listing with 10 objects for each page, the SELECT query would start 
with this: 
SELECT * FROM object 
WHERE bucket_id = 
11
123" ANO object_name LIKE 'a/b/%' 
ORDER BY object_name OFFSET 0 LIMI T 10 
The OFFSET and LIMIT would restri ct the results to the first 10 objects. In the next call, 
the user sends the request with a hint to the server, so it know s to construct the quer y 
for the second page \vith an OFFSET of 10. 1his hint is usually done with a curso r that 
the server returns with each page to the client. The offset information is encoded in the 
cursor. The client would includ e the cursor in the request for the next page. The server 
decodes the curs or and uses the offset information embedded in it to construct the query 
for the next page. To continu e with the example above, the query for the second page 
looks like this: 
SELECT * FROM metadata 
WHERE bucket_id = 
11
123
11 
ANO object_name LIKE 'a/ b/%' 
ORDER BY object _name OFFSET 10 LIMIT 10 
This client-server request loop conti nues until the server returns a special cursor that 
marks the end of the entire listing. 
Now, let's explore why it's complicated to supp ort pagination for sharded databases. 
Since the objects are distributed across shard s, the shards would likely return a varyin g 
number of results. Some shards would contain a full page of 10 objects, whil e o thers 
Step 3 - Design Deep Dive I 279 


[Page 282]
wou]d be partial or empty. lhe application code would receive resu lts fro m every shard, 
aggrega te and sort them, and return only a page of 1 O in our exam ple. The o bjec ts that 
don 't get includ ed in the curren t round must be conside red agai n for the next round, 
TIUs means that each shard would likely have a d ifferent offset. The serve r must track 
the offsets for all the shards and associate those o/Tsets with the cursor. If there are 
hundred s of shards , ther e wiJJ be hundreds of offsets to track. 
We have a solution that can solve the problem, but there are so me tradcoffs. Since object 
storage is tuned for vast scale and high durability, objec t listing performance is rarely a 
priority. In fact, a11 commercial objec t storage supp orts o bject listin g with sub-optimal 
performance . To Lake advantage of this, we could denor malize the listin g data into a sepa¡
rate table sharded by bucket ID. This table is only used for listin g objects. With this setup, 
eve n bucke ts with billions of objects would offer accep table performance. This isolates 
the listing query to a single database which greatly simplifi es the imp lementation. 
Object versioning 
Versioning is a feature that keeps multiple versions of an object in a bucket. With ver¡
sioning, we can restore objects that are accidentally deleted or overwritten . For example, 
we may modify a document and save it under t he same name, inside the same bucket. 
With out versioning, the old version of the document metadata is replaced by the new 
ve rsion in the metadata stor e. The old version of the document is marked as deleted, so 
its storage space will be reclaimed by the garba ge collecto r. With vers ioning, the object 
storage keeps all previous versions of the document in the metadata s tore, and the old 
versions of the docwnent are never marked as deleted in the object store. 
Figure 9.22 explains how to upload a versioned object. For this to work, we first need to 
enab le versioning on the bucket. 
280 I Chapter 9. 53-like Object Storage 


[Page 283]
----
ò ,. 
CD HlTP PUT object 
@ 
a 
Identity 
- validation and 
authorization 
API Service Upload 
object 
Identity Service Check: 
@ 1. Object exists? 
2. Versloning enabled? 
@Create object 
metadata 
r' - - - - - - - - - - - - - - - - - - - - - - - - - -, 
I I 
' ' Metadata Service : 
I 
' ' I 
' I 
' I 
' I 
' Metadata DB : 
~-- ---- - - ------- ------------' Metadata Store 
~------- - - - ---- - - --- --- ------ - - -
' ' ' 
' Secondary ' ' ' Storage ;LJ ' ' Service ' ' ' ' Storage Node ' ' 
Primary 
Storage ;LJ - Service 
Storage Node 
' I 
' ' Secondary ' ' I 
LJ 
' Storage ' I 
Service I 
I 
I 
Storage Node I 
' ' '-------------------------------Data Store 
Figure 9.22: Object versioning 
1. The client sends an HTTP PUT request to upload an object named script. txt. 
2. The API service verifies the user's identity and ensures that the user has WRITE per¡
mission on the bucket. 
3. Once verified, the API service uploads the data to the data store. The data store 
persists the data as a new object and returns a new UUID to the API service. 
4. The API service calls the metadata s tore to store the metadata information of this 
object. 
5. To support vers ioning , the object table for the metadata store has a column called 
object_ version that is only used if versioning is enabled. Instead of overwriting the 
existing record, a new record is inserted with the same bucket_id and object_name 
as the old record , but with a new object_id and object_version . The object_id is 
the UUID for the new object returned in step 3. The object_version is a TIMEUUID 
[29] genera ted when the new row is inserted. No matter which database we choose 
for the metadata store, it should be efficient to look up the current version of an 
object. The current version has the largest TIMEUUID of all the entries with the same 
object_name. See Figure 9.23 for an illustr ation of how we store versioned metadata. 
Step 3 - Design Deep Dive I 281 


[Page 284]
Current version 
Metadata Store 
Previous 
current 
version ' , 
' ' 
'~ 
jobject version= fas3 f--f-+ 
' --' --... 
object _ version = bn31- i--
object _verslon = 1ag1- f-+ 
object name=script.txt 
objec t id=DxM13n 
obiec t_name=scnp t.txt 
ob1ect_id=Ox12Ha 
object _name=scripl.tx t 
objecUd=Ox91 b4 
Data Store 
object ld==OxM13n 
- ----- ╖ò object_ld=Ox12Ha 
- - - ò - - -ò objecUd=Ox9 1 b4 
Figure 9.23: Vers ione d metadata 
In additio n to uploading a versioned objecl, it can also be deleted. Let's take a look. 
-╖ 
When we delete an object, all versions remain in the bucket and we ins ert a delete marker, 
as shown in Figure 9.24. 
Current version 
Metadata Store 
Previous 
current 
version ---
J object_ version = kk1 h :f--- 1 object_name=script. txt 
Delete Marker 
-.... 
object_version = fas3- -+-- object_name=script.txt 
objecUd =OxM13n 
object_version = bn31 -~ object_name=script.txt 
objecUd=Ox 12Ha 
object_ version= 1ag1 -r---. object_name=script.tx t 
object_ld=Ox91 b4 
Data Store 
object_id=OxM13n 
object _ld=Ox12Ha 
object_id=Ox91 b4 
Figure 9.24: Delete object by inserting a delete mark er 
A delete marker is a new version of th e objec t, and it becomes the current version of the 
object once inserted. Performing a GET request when the current version of the object is 
a delete mark er return s a 404 Object Not Found error. 
Optimizing uploads of large flies 
In the back-of-the-envelope estimation, we estimated that 203 of the o bjects a re large . 
Some might be larger than a few GBs. It is possible to upload such a large object file 
dir ectly, but it could take a long time. If the network conne ction fails in the middle of 
the upload, we have to start over. A better solution is to slice a large object into smaller 
282 I Chapter 9. 53-like Object Storage 
). 
\ 
' 


[Page 285]
parts a nd upl oad th em indepe'nd enll y. Af1er all the part s a re uploade d, Lhe object store 
re-asse mbl es the objec t from the part s. 1his p rocess is called mull ipart up load. 
figu re 9.25 illu strates how mullip art upload w ork s: 
ò I Data Store I ... 
. -
I 
I 
Initiation : I 
I 
. -
I 
Multlpart ; 
Upload 
I 
-
--
Completion 
-
------------ ---------------- ------------------- I 
CD-Multlpart upload initiation - I 
I 
I 
I 
« uploadlD 
I 
.. I __ , 
::::: : ::::: ::::::::::: :::::::::::::::::::: : ::: :. --. 
-@-- D Part 1 . 
[ ] upload ID 
- 4 ETag 1 
D Part 2 
[ ] upload ID 
Efag 2 
' I 
' ...... I 
I 
D Part 8 
I 
I 
I 
[ ] uploadlD 
I 
I 
I 
I 
I 
ETag 8 I 
I 
------------------------------------------------ --
----------------------------------------------- --╖ I 
I 
I 
upload ID I 
I 
I 
Multipart Part 1-ETag 1 I 
I 
@ upload Part 2- ETag 2 
I 
' I 
completion I 
........ I 
I 
Part a-ETag 8 
I 
I 
I 
I 
.. @Success 
I 
I 
I 
------------------------------------------------,, 
Figure 9.25: Multipart upload 
1. The client calls the o bject storage to initiat e a multipart upload. 
2. The data store returns an uploadIO, which uniqu ely identifie s the upload. 
3. The client splits the large file into s mall objects and starts uploading. Let's assu me 
the size of the file is l.6GB and the client split s it into 8 parts, so each part is 200MB 
in size. The client uploads the first part to the data store together with the uploadID 
it receive d in step 2. 
4. Whe n a part is upload ed, the data store return s an ET ag, which is essentiall y t he mdS 
checksum of that part. It is used t o verify multipart uploads. 
5. After all parts are uploaded, the c lient sends a complete mul tipart upl oad r equest , 
which .inclu des the upl oadIO, part numb er s, and Hag s. 
6. The data store reasse mbles the object from its parts based on the part numb er. Since 
Step 3 - Design Deep Dive I 283 


[Page 286]
the object is really large, this process may take a few minutes. After r easse mbly is 
complete , it returns a success message to the client. 
One potential problem wilh this approach is t.h;::i t. old parts are no longer u seful after 
the object has been reassembled from them. To solve this problem, we can intr oduce a 
garbage collection service responsible for freeing up space from parts th at are no longer 
needed . 
Garbage collection 
Garbage collection i s the process of automa tically reclaiming storage space that is no 
longer used. 1here are a few ways tha ~ dat a migh t become gar bage: 
ò Lazy object deletion. An object is mar ked as deleted at dele te time without actually 
being deleted, 
ò Orphan data. For example, half uploaded data or abandoned multi par t u ploads. 
ò Corrupted data . Data that failed the checkswn verification. 
The garbage collector does not remove objects from the data store, righ t away. Deleted 
objects will be periodically cleaned up with a compact ion mechanism. 
The garbage collector is also responsible for reclaiming unused space in replicas. For 
replication, we delete the object from both prima ry and backup nodes. For erasure cod¡
ing, if we use (8 + 4) setup, we delete the object from all 12 nodes. 
Figure 9.26 shows an example of how compaction works. 
1. The garbage collector copies objects from /data/b to a new file named /da t a/d. Note 
the garbage collector skips "Object 2" and "Object 5" because the delete flag is set to 
tru e for both of them. 
2. After all objects are copied, the garbage collector updates the obj ect_ mappi ng ta¡
ble. For example, the obj _id and object_size fields of "Object 3" remain the same, 
but fil e_name and start _offset are upd ated to reflect its new location . To ensure 
data consistency, it's a good idea to wrap the update operations to file_name and 
start _off set in a database transaction. 
284 I Chapter 9. 53-like Object Storage 
. , 


[Page 287]
object _mapping table object _mapping table 
Id obj_ file_name offset obi_ size obj_id file_name offset ob]_ size 
'-"" 
~ 
J.--
----object 3 /data/b Ox23283 object 3 /data/d Ox10013 
\ ' 
~ 
\ ' 
' ' ' 
\ 
' \ 
' -
\ 
' ' 
\ 
' \ ' w \ 
' ' \ \ 
' 
\ 
' 
\ \ 
' ' 
\ \ \ 
~ 
\ 
~ ' ' 
I 
' /data/b 
I 
/data/d I I 
I I 
I I 
I I 
I I 
----- - -----------╖ ' ----r------- ' ' ' ' IM'. ' ' Obiect 3 ' ___________ .. x Object 2 
I , 
--<D--, 
lJil ------
Oblect 3 --- ---
---
___________ _,. 
------------ -- -
-
__ .,. -----x Object 5 -------- ___ .,. ----- --- Read-only File -- ---- ---- ---- - --- -----------------
Read-only File 
Before Compaction After Compaction 
Figure 9.26: Compaction 
ru we can see from Figure 9 .26, the size of the new file after compaction is smaller than 
the old file. To avoid creating a lot of small files, the garbage collector usually waits 
until there are a larg e number of read-only files to compact, and the compaction process 
appends objects from many read-only files into a few large new files. 
Step 4 - Wrap Up 
In this chapter, we described the high-level design for S3-like object storage. We com¡
pared the differences between block storage, file storage, and object storage. 
The focus of this interview is on the design of object storage, so we listed how the up¡
loading, downloading, listing objects in a bucket, and versioning of objects are typically 
done in object storage. 
Then we dived deeper into the design. Object storage is composed of a data store and a 
metadata store . We explained how the data is persisted into the data store and discussed 
tvvo methods for increasing reliability and durability: replication and erasure coding. For 
the metadata store, we explained how the multipart upload is executed and how to design 
the database schema to support typical use cases. Lastly, we explained how to shard the 
Step 4 - Wrap Up I 285 


[Page 288]
-
Reference Material 
[ l] Fibre channel. http s://en.wikipedia.org /wiki/Fibre_ Chann el. 
[2) i C I. https: //en.wikipedia.org/wiki /ISCSI. 
[3] erver Message Block. https ://en.wikipedia.or g/wiki/Server _Message _Block. 
[ 4) Network File System . https ://en.wikipedia .org/wiki/Network _File_System . 
[5] Amazon S3 Strong Consis tency. http s://aws.amazon.com/s3/consistency/. 
[ 6) S erial Attached SCSI. https :// en. wikipedia.org /wiki/Serial _Attached _ SCSI. 
[7] AWS CLI ls command . http s://docs.aws.amazon .com/cli/latest/reference/s3/ ls.html . 
[8] Amazon S3 Service Level Agre ement. http s://aws. amazon .com/s3/sla/. 
[9] Ambry. Linkedin ' sScalableGeo- DistributedObjectStore :https ://ass ured -cloud -co 
mputing.illinois .ed u/files/2014/03/ Ambry -Linkedlns -Scalable-GeoDistributed -Ob j 
ect-Store.pdf. 
[ 1 O] inode. https ://en. wikipedia.o rg/wiki/Inode. 
[ 11] Ceph' s Rados Gateway. http s://docs.ceph.com/en/pacific/radosgw /index.html . 
[12] grpc. http s://grpc .io/. 
[13] Paxos. https ://en.wikip edia.org/wiki/Paxos_(computer _science). 
[14] Raft. https: //raft.github.io /. 
[ 15] Consistent hashing. http s://www .toptal .com/big-data /consistent-hashing. 
[16] RocksDB. http s://g ithub .com/facebook /rocksdb. 
[17] SSTable. http s://www.igvita.com /2012/02/06/sstable-and-log-structured-storage-l 
eveldb/. 
[18] B+ tree. http s://e n.wikip edia.org /wiki /B32B_tree. 
[19] SQLite. https ://www.sqlite.org /ind ex.html . 
[20] Data Durability Calculation . https ://www. backblaze.com/ blog/cloud -stora ge- dur 
ability/. 
[21] Rack. http s://en.wikip edia .org/wiki /19-in ch_rack. 
[22] Erasure Coding . https ://e n.wikipedia.org/wiki/Erasure_code. 
[ 23] Reed-Solomon error correction . http s:// en. wiki pedia.org/wiki/Reed 3 E23 80393So l 
omon_ erro r_ correc tion. 
[24] Erasure Coding Demystified. https ://www .youtub e.com/watch?v=Q5kVuM7zEUI. 
[25] Checksum . http s://en.wikipedi a.org/wiki/Checks um. 
Reference M aterial I 287 


[Page 289]
(26] MdS. https: //en.wikipedia.org /wiki/MDS. 
(27) Shat. htt:ps://en.wikipedia .org /wi ki/SHA-1. 
(28] Hmac . https: //en.wikipedia.org /wiki/HMAC. 
(29] TIMEUUID . https ://docs.dataslax.com/en/cql-oss/3.3/cql/cql_reference/tim euuid_f 
unclions _r .html. 
288 I Chapter 9. 53-like Object Storage 


[Page 290]
y-
10 Real-time Gaming Leaderboard 
In this chapter , we are going to walk through the challenge of designing a leaderboard 
for an online mobile game. 
What is a leaderboard ? Leaderboards are commo n in gaming and elsewhere to show who 
is leading a partic ular tournament or competition. Users are assigned points for complet¡
ing tasks or challen ges, and whoever has the most point s is at the top of the leaderboard . 
Figure 10.1 shows an examp le of a mobile game leaderboard. The leaderboard shows the 
ranking of the leading competi tors and also displays the position of the user on it. 
I 
Rank Player Points I 
(* 
1 Aquaboys 976 ) 
(* 2 Steam 956 ) 
(* 3 Berlin's Angels 890 ) 
(* 
4 GrendelTeam 878 ) 
Figure 10.1: Leaderboard 
Step 1 -Understand the Problem and Establish Design Scope 
Leaderboar ds can be pretty straightforward, but ther e are a number of different matters 
that can add complexity . We should clarify the requir ements. 
Candi date: How is the score calculated for the leaderboard ? 
Interview er: The user gets a point when they win a match . We can go with a simple 
point system in which each user has a score associat ed with them . Each time the user 
wins a match , we should add a point to their total score. 
Candidate: Ar.e all players includ ed in the leaderboard ? 
Intervi ewer : Yes. 
I 289 


[Page 291]
Candidate: ls there a time segme nt associa ted with the leadcrboard ? 
Interviewer : Each month , a new tourna ment kicks off which starts a new lcadcrboard. 
Candidate : Can we assume wr only care about the top 10 users ? 
Interviewer : We want to display the top 10 users as well as the position of a s pecific 
user on the leaderboard . If lime allows, let's also discuss how to return users who are 
four places above and below a specific user. 
Candidate : How many users are in a tourn ament? 
Interviewer : Average of [) million daily active users (DAU) and 25 million m onthly 
active users (MAU). 
Candidate : How many matches are played on average durin g a tournament ? 
Interviewer : Each player plays 10 match es per day on average. 
Candidate : How do we determine the rank if two players have th e same score? 
Interviewer : In this case, their ranks are the same. If time allows , we can talk about 
ways to break ties. 
Candidate : Does the leaderboard need to be real-time? 
Interviewer : Yes, we want to present real -time results, or as close as possible. It is not 
okay to present a batched history of results. 
Now that we'v e gathered all the requirements , let's list the function al require¡
ments . 
ò Displa y top 10 players on the leaderboard . 
ò Show a user 's specific rank. 
ò Displa y players who are four places above and below the desired user (bonus) . 
Other than clarifying functional requir ements, it's impo rtant to understand non¡
functional requirement s. 
Non -functional requirem ents 
ò Real-time update on scores . 
ò Score update is reflected on the leaderboard in real-time . 
ò General scalability , availability, and reliability r equirement s. 
Back-of-the-envelope estimation 
Let's take a look at some back-of-the-envelope calculations to determine the potential 
scale and challenges our solution will need to address . 
With 5 million DAU, if the game had an even distribution of players during a 24-hour 
period, we would have an average of 50 users per second ( 5╖m╖~,?~u =,.._, 50). How¡
ever, we know that usages most likely aren 't evenly distribut ed, and potentially there 
are peaks during evenings when many people across different time zones have time to 
play. To account for this, we could assume that peak load would be 5 times the average. 
290 I Chapter 10. Real-time Gaming Leaderboard 


[Page 292]
1llcrefore we'd wan t to allow for a peak load of 250 users per second. 
QP for users scoring a poinl: if a user plays ] O games per d ay on ave rage. the QPS for 
users scoring a point is: 50 x 10 =i"'.J 500. Peak QPS is 5x of the ave rage : 500 x !) = 
2,500. 
QPS for fetchin g the top l 0 leaderboar d: assume a user opens the game once a day and 
the top 10 leaderboard is loaded only when a user firsl ope ns the game. The QPS for thi s 
is around 50. 
Step 2 - Propose High-level Design and Get Buy-in 
In this section, we wilJ discuss API design, high-level architecture , and data mod ¡
els. 
API design 
At a high level, we need the following three APl s: 
POST /v1/scores 
Update a user's position on the leade rboar d when a user wins a game . The request param¡
eters are listed below. This should be an internal API that can only be called by the game 
servers. The client should not be able to update the leaderbo ard score directly . 
Field Description 
user_i d The user who wins a game. 
point s The number of point s a user gained by winnin g a game . 
Table 10.1: Request param eters 
Response: 
Name Description 
200 OK Successfully updated a u ser's score. 
400 Bad Request Failed to upd ate a user's score. 
Table 10.2: Response 
GET /v1 /scores 
Fetch the top 10 player s from the leaderboard. 
Sample response: 
St ep 2 - Propose High-level Design and Get Buy-in I 291 
-


[Page 293]
{ 
} 
" data" : [ 
{ 
}, 
{ 
} 
], 
"user _id" : 11 user _id 111 , 
11
user _name 11 : 11 alice 11 , 
11
rank
11
: 1, 
"score" : 976 
"user _id
11
: 
11
user _id 2" , 
" user _ name 
11 
: 
11 
bob 11 , 
11
rank
11
: 2, 
11
score
11
: 965 
"total" : 10 
GET /vl/ scores/{:u ser_id} 
Fetch the rank of a specific user. 
Field Descripti on 
user _id The ID of the user whose rank we would like to fetch . 
Table 10.3: Request parameters 
Sample respons e: 
{ 
} 
"user _info 11 : { 
} 
II use r - id II : II use r 5 II , 
"score" : 940 , 
11
rank
11
: 6, 
High-level architecture 
The high-leve l d esign diagram is shown in Figure 10.2. There are two services in this 
design . The game service allows users to play the game and the leaderboar d service 
creates and displays a leaderboard. 
292 l Chapter 10. Real-tim e Gaming Leaderboard 


[Page 294]
G) w in agame 
Game 
service 
fA\ a. Get leaderboard 
~ b. Get player _rank 
Leaderb oarcl 
service 
Leaderboard 
Store 
Figure 10.2: High-level design 
1. When a player wins a game, the client sends a request to the game service . 
2. The game service ensures the win is valid and calls the leaderboard service to update 
the score. 
3. The leaderboard service updates the usee s score in the leaderboard store. 
4. A player makes a call to the leaderboard service directly to fetch leaderboard data, 
including: 
(a) top 10 leaderb oard. 
(b) the rank of the player on the leade rboard. 
Before settling on this design, we considered a few alternatives and decided against them . 
It might be helpful to go thro ugh the thought process of this and to compare different 
options. 
Should the client talk to the leaderboard service directly? 
Step 2 - Propose High-level Design and Get Buy-in I 293 
.. 


[Page 295]
~ -- -- Current Option -- - -╖ 
I 
:.o 
I G) Win a game 
Game 
service 
« Update score 
Leaderboard 
service 
~ - - - -- -Alternative Option - - - -- ; 
I I 
« Update score 
Leaderboard 
service 
I 
CD 
Set score 
Figure 10.3: Who sets the leaderb oard score 
ln the alternative design, the score is set by the client. This option is not secure because it 
is subject to man-in-th e-middle attack [1], where players can put in a proxy and change 
scores at will. TI1erefore, we need the score to be set on the server-side. 
Note that for server authorit ative games such as online poker, the client may not need 
to call the game server explicitly to set scores. The game server handles all game logic, 
and it knows when the game finishes and could set the score without any client inter¡
vention . 
Do we need a message queue between the game service and the leaderboard ser¡
vice? 
The answer to this question highly depends on how the game scores are used. If the data 
is used in other places or supports multiple functionalities , then it might make sense to 
put data in Kafka as shown in Figure 10.4. This way, the same data can be consumed 
by multiple consumers, such as leaderboard service, analytics service , push notification 
service , etc. This is especially true when the game is a turn -based or multi -player game 
in which we need to notify other players about the score update. As this is not an explicit 
requirement based on the conversation with the interview er, we do not use a message 
queue in our design. 
294 I Chapter 10. Real-time Gaming Leaderboard 


[Page 296]
Data models 
Game 
service Kafka 
Leaderboard 
service 
Analytic 
service 
Push Notifi cation 
service 
Figure 10.4: Game scores are used by multipl e servic es 
One of the key compon ents in the syste m is the leaderboard store. We will discuss three 
potential solutions: relational database, Redis, and NoSQL (NoSQL solution is explain ed 
in deep ilive section on page 309). 
Relational database solution 
First, let's take a step back and start with the simplest solution . What if the scale doesn ' t 
matter and we have only a few users ? 
We would most likely opt to have a s imple leaderboard solution using a relational 
database system (RDS). Each monthly leaderboard could be represented as a database 
table containing user id and score column s. When the user wins a match , either award 
the user 1 point if they are new, or increase their existing score by 1 point. To determine 
a user╖s ranking on the leaderboar d, we would sort the table by the score in descending 
order. The details are explained below. 
Leaderboard DB table: 
leaderboard 
user_id 
score 
varchar 
int 
Figure 10.5: Leaderboard table 
In reality, the leaderboard table has additi onal information, such as a game_id, a times¡
tamp, etc. However, the und erlying logic of h ow to query and update the leaderboard 
remains the same . For simplicity, we assume only the current month 's leaderboard data 
is stored in the leaderboard table. 
A user wins a point : 
'--Le_a_d_er_b_o_ar_d~f---- Insert or update DB ~ service ~ 
Figure 10.6: A user wins a point 
Step 2 - Propose High-level Design and Get Buy-in I 295 


[Page 297]
-~ 
ssume every score update would be an increment of 1. If a user d oesn't yet have an 
en try in the leaderboard for the month , the first insert would be: 
11'1\(Rl 1NTO leaderboard (user _id, score) VALUES (' mary1934 ', 1) 
An update to the user's score would be: 
urOATF leaderboard set score=score + 1 whe1e use r _i d= 'mar y19 34 ' ; 
Find a user's leaderboard position: 
Leaderboard 
service Fetch fmm DB, sorted by rank -LJ 
Figure 10.7: Find a user's leaderboard position 
To fetch the user rank , we would sort the leaderboard table and rank by the score: 
SELECT (@rownum : = @rownum + 1) AS rank, user _id, score 
FROM 1 ea de rboa rd 
ORDER BY score DESC ; 
The result of the SQL query looks like this: 
rank user_id score 
1 happ y _tomato 987 
2 mallow 902 
3 smith 870 
4 mary1934 850 
Table 10.4: Result sorted by score 
1his solution works when the data set is small, but the query becomes very slow when 
ther e are millions of rows. Let's take a look at why. 
To figure out the rank of a user, we need to sort every single player into their correct spot 
on the leaderboard so we can determine exactly what the correct rank is. Remember that 
there can be duplicate scores as well, so the rank isn't just the position of the user in the 
list. 
SQL databases are not performant when we have to process large amounts of continu¡
ously changing information . Attempting to do a rank operation over millions of rows is 
going to take 10s of seconds, which is not acceptable for the desired real-time approach. 
Since the data is constantly changing, it is also not feasible to consider a cache. 
A relational database is not designed to handle the high load of read queries this imple¡
mentation would require. An RDS could be used successfully if done as a batch operation, 
but that would not align with the requirement to return a real-time position for the user 
296 I Chapter 10. Real-time Gaming Leaderboard 


[Page 298]
-
on the leaderboard . 
One optimization we can do is to add an index and limit the numb er of pages lo sc<tn 
wilh the LIMIT clause . 1he query looks like thi s: 
SELFCT ( @rownum := @rownum + 1) AS rank, user_id, score 
FROM leade rboa rd 
ORDrn BY score DC SC 
LIMIT 10 
However, this approac h doesn't scale well. First, finding a user 's rank is not performant 
because it essentially requires a table scan lo determine the rank. Second , this approach 
doesn't provide a straig htforward solution for determini ng the rank of a user who is not 
at the lop of the leaderboard . 
Redis solution 
We want to find a solutio n that gives us predictab le performance even for millions of users 
and allows us lo have easy access to common leaderboard operations , without needing 
to fall back on complex DB queries . 
Redis provides a potential solution to our problem. Redis is an in-memory data store 
supporting key-value pairs. Since it works in memory, it allows for fast reads and writes. 
Redis has a specific data type called sorted sets that are ideal for solving leaderboard 
system design problems. 
What are sorted sets? 
A sorted set is a data type similar to a set. Each member of a sorted set is associated with 
a score. The members of a set must be unique , but scores may repeat . The score is used 
to rank the sorted set in asce ndin g order. 
Our leaderboard use case map s perfec tly to sorted sets. Internally, a sorted set is imple ¡
mented by two data struct ures: a hash table and a skip list [2]. The hash table map s users 
to scores and the skip list maps scores to users. In sorted sets, users are sorted by sco res. 
A good way to understand a sorted set is to picture it as a table with score and member 
columns as shown in Figure 10.8. The table is sorted by score in descending order. 
Step 2 - Propose High-level Design and Get Buy-In I 297 
-


[Page 299]
-
score member 
-
fl!) user10 
97 user20 
-
f)ll user105 
fl2 user45 
E derboard _feb_2021 j----- 90 user? 
86 user101 
83 user9 
82 user302 
79 user200 
72 user309 
Figure 10.8: February leader board is represented by the sorted set 
In this chapter , we don 't go into the full detail of the sorted set implementation, but we 
do go over the high -level ideas . 
A skip list is a list structure that allows for fast search. It consists of a base sorted linked 
list and multi -level indexes. Let's take a look at an example. In Figure 10.9, the base 
list is a sorted singly-linked list. The time complexity of insertion , removal , and search 
operations is O(n). 
How can we make those operations faster ? One idea is to get to the middle quickly, as 
the binary search algorithm does. To achieve that , we add a level 1 index that skips every 
other node , and then a level 2 index that skips every other node of the level 1 indexes. 
We keep introducing additional levels, with each new level skipping every other nodes 
of the previous level. We stop this addition when the distan ce between nodes is ~ - 1, 
where n is the total number of nodes. As shown in Figure 10.9, searching for number 45 
is a lot faster when we have multi-level indexes . 
298 I Chapter 10. Real-time Gaming Leaderboard 


[Page 300]
-
~ ------ ------------- - -- --------- - -- - - - ------- - -- - -- - -- - -- - - - - -- - -- ------ -- - -- -- : 
I I 
Basellst ~~~~1451 ╖~ @ 
! _ _ _ _ _ _____________ _ __ _ _ _ __ _____ __ _ _ __________ _ _ _ __ ______ ________ ___ _ _ _________ _ 
D 
--------- ------------------------------------------- --------- --------- ------ ---, 
Levell index 
I 
I 
I 
I 
' I 
I 
I 
I 
I 
I 
I 
' I 
I 
I 
' : ________ ________ _____ __ _______ ____ ______ ____ ___ _____________ _______ __ ______ ____ . 
D 
r--- --- -- ----- ------ - ------ ------------ -- ------------- -- ---------- ------- -- ----1 
Level 2 index 
Levell index 
I 
I 
~--- ------ - ----- - ----- - ---- --- --------- ------- - ------- --- - - --- - ----- ---- ------ --
Figure 10.9: Skip list 
When the data set is small , the speed improvement using the skip list isn't obvious. Figure 
10.10 shows an example of a skip list with 5 levels of indexes. In the base linked list , it 
needs to travel 62 nodes to reach the correct node. In the skip list, it only needs to traverse 
11 nodes [3). 
----
1 0 
I 
0 0 0 0 0 6- -
1 (' 0 0 0 0 0 0 0 0 0 0 0 
1 . 0 c 0 
" 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
c 0'" ('.' 0 0 (' 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 c 0 0 (' 0 0 0 6 .. 0 0 
Figure 10.10: Skip list with 5 levels of indexes 
Sorted sets are more performant than a relational database because each element is auto ¡
matically positioned in the right order during insert or update , as well as the fact that the 
complexity of an add or find operation in a sorted set is logarithmic : O(log (n)). 
In contrast , to calculate the rank of a specific user in a relational databas e, we need to 
run nested queri es: 
Step 2 - Propose High-level Design and Get Buy-in I 299 


[Page 301]
S!Llrl *,( SELFC1 COUN1 (*) rROM leader boar d l b2 
WHLR[ lb2 . score >= lb1. score) RANK 
FROM leaderboard lb1 
~IHCRE lb1 .user_id = {:user_id}; 
Implementation using Redis sorted sets 
Now that we know sorted sets are fast, let's take a look at the Redis operations we will 
use to build our leaderboard [4] (SJ [6] [7]: 
ò ZADD: insert the user into the set if they don't yet exist. Otherwise, upd ate the score 
for the user. It takes O(log( n)) to execute. 
ò ZINCRBY: increme nt the score of the user b y the specified increment. If the user 
does n't exist in the set, then it assumes the score s tart s at 0. It takes O(log( n)) 
to execute. 
ò ZRANGE/ZREVRANGE: fetch a range of users sort ed by the score. We can specify the order 
(range vs. revran ge), the numb er of entries , and the positio n to start from. This takes 
O(log( n) +m) to execute, where m is the number of entries to fetch (which is usually 
small in our case), and n is the number of entries in the sorted set. 
ò ZRANK/ZREVRANK: fetch the position of any user sorti ng in ascending /descending order 
in logarithmic time. 
Workflow with sorted sets 
1. A user scores a point 
Leaderboard 
service 1----- ZINCRBY ----ò ò 
red1s 
Figure 10.11: A user scores a point 
Every month we create a new leaderboard sorted set and the previous ones are moved to 
historical data storage. When a user wins a match, they score 1 point; so we call ZINCRBY 
to increment the user's score by 1 in that month 's leaderboard, or add the user to the 
leaderboard set if they weren 't already ther e. The syntax for ZINCRBY is: 
ZINCRBY <key > <increment > <user > 
The following command adds a point to user ma ry1934 after they win a match. 
ZINCRBY leaderboard_feb _2021 1 'mary1934' 
2. A user fetches the top 10 global leaderboard 
300 I Chapter 10. Real-time Gaming Leaderboard 
~I 


[Page 302]
-
Leaderboard ò 
service 1----- ZREVERANGE ---- d' 
'-------.J re 1s 
Figure 10.12: Fetch top 10 global leaderboard 
We will call ZREVRANGE to obtain the members in desce nding order because w e want the 
highest scores, and pass the WITHSCORES attribute to ensure that it also return s the to tal 
score for each user, as well as the set of users with the highest scores. The foll owin g 
command fetches the top 10 players on the Feb-2021 leaderboard. 
ZREVRANGE leaderboard _ fe b_202 1 0 9 WIT HSCORES 
1his returns a list like this: 
[(user2, score2), (user1, score 1), (user5, score5) .. . ] 
3. A user wants to fetch their leaderboard position 
Leaderboard 
service 
1----- ZREVERANK ---- .. 
red1s 
Figure 10.13: Fetch a user 's leade rboar d position 
To fetch the position of a user in the leader board, we will call ZREVRANK to retrieve their 
rank on the leaderboard. Again , we call the rev version of the command because we want 
to rank scores from high to low. 
ZREVRANK leade rboa rd _ feb _2021 'mary1934 
1 
4. Fetch the relative position in the leaderboard for a user . An example is shown in Figu re 
10.14. 
Step 2 - Propose H igh-level Design and Get Buy-in I 301 


[Page 303]
I Rank Player Points I 
( 267 Aquaboy s 876 ) 
( 258 B team 845 ) 
( 259 Berlin's Angels 832 ) 
( 360 GrendelTeam 799 ) 
( 361 Mallow007 785 ) 
( 362 Woo78 743 ) 
( 363 milan- 114 732 ) 
( 364 G3" M\/\ 2 726 ) 
( 365 Mailso _91_ 712 ) 
Figure 10.14: Fetch 4 player s above and below 
Whil e not an explicit requir ement , we can easily fetch the relative position for a user by 
leverag ing ZREVRANGE with the number of results above and below the desired player. For 
example, if user Mallow007's rank is 361 and we want to fetch 4 players above and below 
them, we would run the following command. 
ZREVRANGE leaderboard_feb_2021 357 365 
Storage requirement 
At a minimum , we need to store the user id and score. The worst-case scenario is that 
all 25 million monthly active users have won at least one game, and they all have entries 
in the leaderboard for the month . Assuming the id is a 24-character string and the score 
is a 16-bit integer (or 2 bytes), we need 26 bytes of storage per leaderboard entry. Given 
the worst -case scenario of one leaderboard entry per MAU, we would need 26 bytes x 25 
million= 650 million bytes or rv 650MB for leaderboard storage in the Red.is cache. Even 
if we double the memory usage to account for the overhead of the skip list and the hash 
for the sorted set, one modem Redis server is more than enough to hold the data. 
Another related factor to consider is CPU and I/0 usage. Our peak QPS from the back¡
of-the-envelope estimation is 2500 updates /sec. This is well within the performance en¡
velope of a single Redis serveL 
One concern about the Redis cache is persistence, as a Redis node might fail. Luckily, 
Redis does support persistence , but restarting a large Redis instance from disk is slow. 
Usually, Redis is configured with a read replica, and when the main instance fails, the 
read replica is promoted , and a new read replica is attached . 
302 I Chapter 10. Real-time Gaming Leaderboard 


[Page 304]
-
I t'Sh.i~t. we need lo have 2 supporting tables (user and point) in a relational database lik e 
\h, L. TI1e user table would store the user ID and user's display name (in a real-world 
l\pplirrttion, this would contain a lot m ore data). The point table would con tain the user 
id. score, and timestarnp when they won a game . This can be leveraged for other game 
functions such as play histor y, and can also be used to recreate the Re dis leaderboar d in 
the event of an infrastructure failure. 
As a small performance optimiza tion, it may make sense to create an additional cac h e of 
the user details. potentially for the top 10 players since they are retrieved most frequently. 
However, this doesn 't amount to a large amount of data. 
Step 3 - Design Deep Dive 
Now that we've discussed the high -leve l design, let's dive into the following: 
ò Whether or not to use a cloud provider 
o Manage our own services 
o Leverage cloud service provid ers like Amazon Web Services (AWS) 
ò Scaling Redis 
ò Alternative solution : NoSQL 
ò Other considerations 
To use a cloud provider or not 
Depending on the existing infrastructure, we generally have two options for dep loying 
our solution . Let's take a look at each of them. 
Manage our own services 
ln this approach, we will create a leade rboard sorted set each month to store the leader¡
board data for that period . The sor ted set store s member and score information . The rest 
of the details about t he user, such as their name and profile image, are stored in MySQL 
databases. When fetc hing the leaderboard , besides the leaderboard data, API servers als o 
query the data base to fetch corresponding users ' names and profile images to display on 
the leaderboard . If this becomes too inefficient in the long term, we can levera ge a user 
profile cache to sto re users' details for the top 10 players. Tue design is shown in Figure 
10.15. 
Step 3 - Design Deep Dive I 303 
╖-


[Page 305]
Leaderboa rd - - ò 
Sorted set redis 
..:..o 
User profile 
+ - -User Points Mys~ ,__ _ _ 6 ~ 6 .._____, 
Load balancer '-~--' 
User profile cache ò 
(for lop 10) -
red is 
Figure 10.15: Mana ge our own services 
Build on the cloud 
The second approac h is to leverage cloud infr astr uctures. In this section, we assume our 
existing infrastrncture is built on AWS and that it's a natural fit to build the leaderboard 
on the cloud. We will use two major .AWS technologies in this design: Amazon API 
Gateway and AWS Lambda function [8]. The Amazon API gateway provides a way to 
define the HTTP endpoints of a RESTful A.PI and connect it to any backend services. We 
use it to connect to our AWS lambda functions . The mapping between Restful APis and 
Lambda functions is shown in Table 10.5. 
APis Lambda function 
GET /v1/scores LeaderboardFetchTop10 
GET /v1/scores/{:user_id} LeaderboardFetchPlayerRank 
POST /v1/scores LeaderboardUpdateScore 
Table 10.5: Lambda functions 
AWS Lambda is one of the most popular serverless computing platforms. It allows us 
to run code without having to provision or manage the servers ourselves. It runs only 
when needed and will scale automatically based on traffic. Serverless is one of the hottest 
topics in cloud services and is supported by all major cloud service providers . For exam¡
ple, Google Cloud has Google Cloud Functions [9] and Microsoft has named its offering 
Microsoft Azure Functions [10]. 
At a high level, our game calls the Amazon API Gateway, which in turn invokes the 
appropriate lambda functions. We will use AWS Lambda functions to invoke the appro¡
priate commands on the storage layer (both Redis and MySQL), return the results back 
to the API Gateway , and then to the application. 
We can leverage Lambda functions to perform the queries we need without having to 
spin up a server instance. AWS provides support for Redis clients that can be called from 
the Lambda functions. This also allows for auto-scaling as needed with DAU growth. 
Design diagrams for a user scoring a point and retrieving the leaderboard are shown 
below: 
304 I Chapter 10. Real-time Gaming Leaderboard 


[Page 306]
I 
U case 1: scoring a point 
Leaderboard 
service Win game 
ò _...-"" red1s 
Leaderboard 
Call ZINCRBY 
---~:::: 
AWS 
API Gateway 
AWS 
Lambda 
Insert point 
Figure 10.16: Score a point 
~ Point table 
MySQL 
Use case 2: retrie ving leaderboard 
ò Leaderboard 
___.....-red is 
CD Call ZREVRANGE 
Leaderboard 
service 
_ Get -
leaderboard .._ _ __..&::::FeWh 
AWS 
API Gateway 
AWS user details ...____ 
Lambda -- \'\ 
MySQC Point table 
Figure 10.17: Retrieve leaderboard 
Lambdas are grea t b ecause they are a serverless approach , and the infrastructure will 
take care of auto -scaling the function as needed . This means we don't need to manage 
the scaling and enviro nment setup and maintenan ce. Given this, we recommend going 
with a serve rle ss approach if we build the game from the ground up. 
Scaling Redis 
With 5 million DAU, we can get away with one Redis cache from both a storage and 
QPS perspective. However , let's imagine we hav e 500 million DAU, which is 100 times 
our original scale. Now our worst-case scenario for the size of the leaderboard goes up 
lo 65GB (650MB x 100), and our QPS goes up to 250,000 (2,500 x 100) queries per 
second. This calls for a sharding solution. 
Data shard ing 
We consider sharcling in one of the following two ways: fixed or hash partitions . 
Fixed partition 
One way to understand fixed partiti ons is to look at the overall range of points on the 
leaderboard. Let's say that the number of points won in one month ranges from 1to1000, 
and we break up the data by range. For example, we couJd have 10 shards and each shard 
would have a range of 100 scores (For examp le, 1 ""' 100, 101 ,...., 200, 201 ""' 300, ... ) as 
shown in Figure 10.18. 
Step 3 - Design Deep Dive I 305 


[Page 307]
[1. 100] 
Sort ed set 
[101, 200] [201, 300] 
Sorted set Sorted set 
Figure 10.18: Fixed partition 
(901, 1000) 
Sorted set 
For this lo work, we want to e nsure t╖here is an even distribution of scores across the 
leaderboa.rd. Otherwise, we need to adjus t lhc score range in each shard to make sure 
of a relatively e ven dislributio n. In this approach, we shard lhe data ourse lves in the 
application code. 
When w e are inserting or updating Lhe score for a user, we need to know which shard 
they are in. We could do thi s by caJculatin g lhe user's current score from the MySQL 
databa se. 11tis can work , but a more performant option is lo crea te a secondary cache to 
store the mapping from user ID to score. We need to be carefu l when a user increases 
their score and moves between shards. In this case, we need to remove the user from 
their current shard and move them to the new shard. 
To fetch the top 10 players in lhe leaderbo a.rd, we would fetch the top 10 players from 
the shard (sorted set) with the highest scores. In Figure 10.18, the last shard with scores 
[901. 1000] contain s the top 10 players . 
To fetch the rank of a user, we would need to calculate the rank within their current 
shard (local rank), as well as the total numb er of players with higher scores in all of the 
shards . Note that the total number of players in a shard can be retrieved by running the 
info keyspace comman d in 0 (1) [11]. 
Hash partition 
A second approach is to use the Redis cluster , which is desira ble if the sco res are very 
clustered or clumped . Redis cluster provid es a way to shard data autom atically across 
multiple Redis nodes. IL doesn't use consistent hashing but a different form of shar di.ng, 
where every key is part of a hash slot. There are 16384 hash slots [12] and we can 
comput e the hash slot of a given key by doing CRC16 (key) 3 16384 [13]. 11tis allows us to 
add and remove nodes in the cluster easily without redistributin g all the keys. In Figure 
10.19, we have 3 nodes, where : 
ò The first node contai ns hash slots (0, 5500]. 
ò The second node contains hash slots [5501, 11000]. 
ò 111e third node contains hash slots (1 1001, 16383]. 
306 I Chapter 10. Real-time Gaming Leaderboard 


[Page 308]
Slot [O, 5500) 
I 
r------------'---------, 
\ Primary. 
: I \ 
' ' I 
I 
I 
I 
ò ò Replica Replica 
Shard 1 
Slot [O, 5500) 
I I 
, ______________________ _ 
Client 
Proxy Slot "' CRC16(key) % 16384 
Slot: (5501, 11000) Slot: [11001, 16383] 
r-----------------------
! ò : ' ' ! Primary : 
I I \ 
òò Replica Replica 
Shard 2 
ò Slot (5501, 11000] : 
╖-----------------------╖ 
Redis Cluster 
Figure 10.19: Hash partition 
\ 
r-------\ ______ ________ _ 
' 
\ Primary. 
I I \ 
ò ò : Replica Replica 
I 
I 
: Shard 2 
: Slot [11001, 16383] 
I 
I 
I 
I 
' - - --- ------------------╖ 
An update would simply c hange the score of the user in the corresponding shard (de¡
termined by CRC16(key) 3 16384). Retrieving the top 10 players on the leaderboard is 
more complicated. We need to gather the top 10 players from each shard and have the 
application sort the data.. A concrete example is shown in Figw-e 10.20. Those queries 
can be parallelized to reduce latency. 
Step 3 ò Design Deep Dive I 307 


[Page 309]
shard 0 (top 10) 
score member 
!l!I user10 
90 user? 
~fi user101 
70 user109 
... ... top 10 
score member 
99 user10 
shard 1 (top 10) !)7 user20 
score member 94 user105 
97 user20 scatter-gather user45 92 
83 user9 .. 
90 user? 
79 user200 
86 user101 
72 user309 83 user9 
... ... 82 user302 
79 user200 
shard 2 (top 10) 72 user309 
score member 
911 user105 
02 user45 
82 user302 
71 users 
... ... 
Figure 10.20: Scatter-gather 
This approach has a few limitations: 
ò When we need to return top k results (where k is a very large numb er) on the leader¡
board , the latency is high because a lot of entries are returned from each shard and 
need to be sorted. 
ò Latency is high if we have lots of partitions because the query has to wait for the 
slowest partition. 
ò Anoth er issue with this approach is that it doesn't provide a straightforward solution 
for determining the rank of a specific user. 
1herefore, we lean towards the first propo sal: fixed partition. 
Sizing a Redis node 
There are multiple thin gs to consider when sizing the Red.is nodes (14]. Writ e-heavy 
applications requir e much m ore available memory, since \Ve need to be able to accom¡
modate all of the write s to create the snaps hot in case of a failure. To be safe, allocate 
twice the amount of memory for write-heavy applications . 
Redis provides a tool called Reclis-benchmark that allows us to benchmark the perfor-
308 I Chapter 10. Real-ti me Gaming Leaderboar d 


[Page 310]
, _ 
mancc of the Red is setup, by simulatin g multiple clients excculin g multip le queries and 
returning the numb er of requests per second for Lhe given hardwar e. To learn more aboul 
Red1s-benchmark, see [ 15]. 
Alternative solution: NoSQL 
An alternative soluti on lo consider is NoSQL databases. Whal kind of NoSQL should we 
use? Ideally, we want to choose a NoSQL that has the followin g prop erties: 
ò Optimized for writ es. 
ò Efficiently sort items within the same partition by score. 
NoSQL databases such as Amazon's DynamoDB [16], Cassandra, or MongoDB can be 
a good fit. ln this c hapt er, we use DynamoDB as an example . DynamoDB is a fully 
managed NoSQL database that offers reliable performance and great scalability. To allow 
efficient access to data with attrib utes other than the primary key, we can levera ge global 
secondary indexes [17] in DynamoDB. A g lobal secondary index contain s a selection of 
attributes from lhe parent table, but they are organized using a different primar y key. 
Let's take a look at an example. 
The updated system diagram is shown in Figure 10.21. Redis and MySQL are repla ced 
with DynamoDB. 
Leaderboard 
service - lfu-
AWS 
API Gateway 
AWS 
Lambda 
Figure 10.21: Dynam oDB solution 
AWS 
Dynamo DB 
Assume we design the leaderboard for a chess game and our initial table is s hown in 
Figure 10.22. It is a denormalized view of the leaderboard and user tables and contain s 
everything needed to render a leaderb oarcl 
Primary key Attributes 
user_id score email profile_pic leaderboard _name 
lovelove 309 love@ test.com https ://cdn .example l3.png chess#20 20-02 
i_love _tofu 209 test@test.co m https ://cdn .exampl e/p. png chess#2020-02 
golden_gate 103 gold@test.com http s:/lcdn .example l2.png chess#2020 -03 
pizza or bread 203 piz@test.com https :l/cdn .example /31 .png chess#2021 -05 
ocean 10 oce@ test.com https ://cdn .example /32.png chess#2020-02 
. . . .. . .. ~ .... ... 
Figure 10.22: Denormalized view of the leaderboard and user tables 
This table scheme works, but it doesn't scale well. As more rows are added , we have to 
scan the entir e table to find the top scores. 
Step 3 - Design Deep D ive I 309 
L 


[Page 311]
wr nerd lo add inclrxrs Our first ~ ll empt is lo ' linear c;ran. . use 
year-month} ac; the parl1!1on key and the score as the sort key, as 
rurr JO 21. 
-- - -Attribute s -ondary Index 
y ~sortt user_ld email profile _pi e -
c 
e 
key 
(score) 
__.;- -=o2 30!l roverove love@ test.com https ://cdn.example /3.png 
.02 :.?09 ;_rove_tofu test@test.com hl1ps://cdn .example /p png 
__.J 
03 I 103 golden_gale gold@test.com https://cdn.example /2.png 
--l pizza_ or_ bread p1z@test.com https ://cdn.example /31.png )2 I 203 
)2 ! 10 ocean oce@test.com https://cdn .example /32.png 
I .. ... ... . . . 
Figure 10.23: Partition key and sort key 
l runs into issues al a high load. Dynam oDB splits data across multiple 
:;istent hashing. Each item lives in a corresponding node base d on its 
'e want to structure the data so that data is evenly distribu ted across 
r table design (Figure 10.23), all the data for the most recent month 
n one partition and that partiti on becomes a hot par tition. How can we 
n? 
.ta into 11 partitions and append a partition numb er (user _id 3 
.ions) to the partition key. This pattern is called write sharding. Writ e 
111plexity for both read and write operations , so we sh ould consider the 
y. 
ion we need lo answer is, how many partit ions should we have? It 
"rite volume or DAU. The important thin g to remember is that t here is 
:n load on partitions and read complexity. Becau se data for t he s ame 
.renly across multiple partition s, the load for a single partition is much 
to read items for a given month, we have to query all the partiti ons 
.ilts, which adds read complexity. 
>oks something like this: game_namett{ yea r- month}#p{part i tion_nu mber }. 
the updated schema table. 
11-time Gaming Leaderboard 
dar}' 1nde>< 
I secon 
GIO~ pt<) sort 
itioO keY ( keY 
rll1 (score ) 
309 
Figu1 
dary index us i1bal secon 
~╖~ and the score as tl ) l!lke\' :> ╖.lh;,, their own par1 '(1t0 \\') IJ' 
, der to fetch the top 10 -╖nor 
╖'. nu╖oned earlier. We JI me . . ~ ╖scatter" portion), anc .,Juie 
:~: .ill the partitions (this is 
>-
j 
iop 10 trom partition 0 (scattt 
~n key (PK) Sort use1 
key 
(score) 
~tJ20-02#pO 309 lovelc 
I 
bp 10 from partition 1 (scatter) 
~key{PK) Sort 
key 
(score) 
~20-02#p1 209 
~'i20-02#pl 203 
user_fc 
i_love_tc 
Pizza or - . 
~ IO from partiUon 2 ( ~ scatter) 
key (PK) Sort 
key user_\d 
(score) 
\Q 


[Page 312]
- -- - - - - - --- - --- -
Global Secondary Index Attributes -
Partition key (PK) Sort user_ld email proflle _plc 
key 
(sco re) 
chess#2020-02# p0 :mo love love love@test.com https ://cdn.example/3 .png 
chess#2020-02 #p1 20!) 1_love_ tofu test@test.com https://cdn.example/p .png 
chess#2020-03 #p2 103 golden_gate gold@test.com https://cdn.example/2 .png 
chess#2020-02#p1 203 pizza_ or_ bread plz@test.com https://cdn.example/31 .png 
chess#2020 -02#p2 10 ocean oce@test.com https://cdn .example/32 .png 
... ... ... . .. . .. 
Figure 10.24: Updated partition key 
1he global secondary index uses game_nameU{ year-month}#p{parti t ion_number} as the 
partition key and the score as the sort key. What we end up with are n partitions that are 
all sorted within their own partition (locally sorted). If we assume we had 3 partition s, 
then in order to fetch the top 10 leaderboard , we would use the approach called "scatter ¡
gather" mentioned earlier. We would fetch the top 10 results in each of the partitions 
(this is the "scatter" portion) , and then we would allow the application to sort the results 
among all the partitio ns (this is the "gather " portion) . An examp le is shown in Figure 
10.25. 
top 10 from partition 0 (scatter) 
Partition key (PK) Sort 
key 
(score) 
user_id 
chess#2020-02#p0 309 lovelove 
top 10 from partition 1 (scatter) 
Partition key (PK) Sort user _Id 
key 
(score) 
chess#2020-02#p1 209 i_love_tofu 
chess#2020-02#p1 203 pizza_or_bread 
top 10 from partition 2 (scatter) 
Partition key (PK) Sort user _id 
key 
(score) 
chess#2020-02#p2 10 ocean 
a th er 
gather 
Figure 10.25: Scatter -gather 
Top 10 leaderboard 
score user_ld 
309 love love 
209 i_love_tofu 
203 pizza_ or_ bread 
200 Apple 
199 Orange 
197 peach 
196 data 
180 Bird 
179 cc 
177 too_much 
Step 3 - Design Deep Dive I 311 


[Page 313]
l lnw du\\ c drcidc 011 the mun brr of pRrl i\ ions? 'Jhis might require some careful hench ¡
mC1rk1ng. More partiti ons dccrertsc the load on each partition hul add complexity , as 
\\'(' nrcd to sm iter fl('J"()SS more partitions lo bui.ld the nnrtl leaderboard. By employing 
hcnchmarking. we can sec the trade -off more clea rly. 
Howc,╖er. similar to the Redis partit ion soluti on mentioned earlie r, thi s approac h doesn 't 
provide a straig htforward solution for del crmining the relative rank of a user. But it is 
possible lo ge t the percentile of a user's positio n, w hich cou ld be goo d enough. 1n real 
life. telling a player that they are ln the top 10 ,...., 203 migh t be better than showing 
the exact rank at eg. L200,001. Therefore , if the scale is large enough that we needed 
lo shard, '"e could assume th at th e score distributi ons are roughly the same across all 
shards . If this assumpt ion is tru e, we could have a cron job that analyzes the distributi on 
of the score for each shard, and caches tha t result. 
The resul t would look something like this : 
10th perce ntil e= score < 100 
20th percen tile = score < 500 
90th percentile = score < 6500 
1h en we could quick ly return a user 's relative ranking (say 90th perce ntil e). 
Step 4 - W rap Up 
In this chapter, we have created a solution for buildin g a real-time game leaderboard with 
the scale of millions of DAU. We explore d the straig htforurar d soluti on of using a MySQL 
database and rejecte d that approach beca use it does no t scale to millions of u sers. We 
then designed the leaderboard usi ng Redis sorted sets. We also looked into scaling the 
solution to 500 million D AU, by leverag ing sharding across different Redis cach es. We 
als o propose d an alterna tive NoSQL solution. 
In the event you h ave some extra time at the end of the inten riew, you can cover a few 
more topics : 
Faster retrieval and breaking tie 
A Redis Has h provi des a map betwee n stri ng fields and values. We could leverage a hash 
for 2 use cases : 
1. To store a map of the use r id to the user object that we can display on the leaderboard. 
TI1is allows for faster r etriev al than h aving to go to the database to fetch the user 
object. 
2. ln the case of two playe rs having the same scores, \.Ve could rank th e users based on 
who received that sco re first. When w e increment the scor e of the user, we can also 
store a m ap of the user id to the t imestamp of the most recentl y won game . In the 
case of a tie, the user with the older timestamp ran ks higher. 
312 I Chapter 10. Real-time Gaming Leaderboard 
! 
I 
t 
╖5╖ 
,... 


[Page 314]
System failure recovery 
TI1c Redis cluster can potentially experie nce a large -scale failur e. Given the design above. 
we could create a script that leverages the fact lhal the MySQL dalab <1sc reco rds an ent ry 
with a timestamp each tim e a user won a game. We could iterate throu gh all of the entri es 
for each user, and call ZINCRBY once per entry, per user. This would allow us lo recreate 
the lcaderboard offline if necessary, in case of a large-scale outage. 
Congra tulations on getting this far! Now give yourse lf a pat on the back. Good job! 
Chapter Summary 
step 1 
display top 10 
fou r places above and 
below the desired user 
< 
real-time update 
non-functional req 
scalab le 
< 
5 million DAU 
estimation 
upd ate score qps: 2.Sk 
_ú__ score point 
api design ~ get leaderboard 
get player rank 
high-level design 
< 
relational database solution 
data mod el 
redis soluti on 
_ú__build on the cloud or not 
step 3 ~ scale Redis 
alternative solution : NoSQL 
< 
faster retrieval and breaking tie 
step 4 
syste m failur e recovery 
Chapte r Summary I 313 


[Page 315]
Reference Material 
[I ) Man-in-the-middle attack. hltps://en.wikipedia.org/wiki/Man-in-Lhe-middlc_allac 
k. 
[2] R edis Sorted Sel source code. htlp s://github .com/redis/redis/blob /un stable/src/t_z 
sct.c. 
r3J Geekbang. http s://staticOO 1 .geekban g.org/resource /image /46/a9/46d283cd82c987 
153b3fe0c76dfba8a9.jpg. 
[4] Building real-time Leaderboard wilh Redis. http s://medium .com/@sandeep4 .verm 
a/buildin g-real-lime-leaderboard -wit'h-redis-82c98aa 4 7b9f. 
(5] Build a real-tim e gaming leaderb oard with Amazon ElastiCache for Redis. hllps: 
11 aws.a mazon.com/blogs/ databa se/building-a-rea l-time- gaming-leaderboard -with 
-amazo n-elastic.ache-fo r-redis. 
[6] How we created a real-time Leaderboard for a million Users. http s://levelup. gilcon 
nected.com/how-we-c reated-a-real- Lime-lea derboard -for-a- million-users -SSSaaa 
3ccf7b. 
[7] Leaderboards. htlp s://redislabs.co m/ solutions/use-cases / lead er boards /. 
[8] Lambda . http s://aws.amazon.com/lambda/. 
[9] Google Cloud Functions. http s://cloud.google.com/funclio ns. 
[ 10] Azure Functions. http s:/ /azure .microsoft. com/ en-us/services/fun ction s/. 
[11] Info command. https://redi s.io/co mmand s/INFO. 
[12] Why redis cluster only have 16384 slots . http s://stackover flow.com/questions /3620 
3532/why-reclis-cluster-only-have -16384-slots. 
[ 13] Cyclic redundancy check. http s:// en. wikipedia.org /wild /Cyclic _redundancy _ che 
ck. 
(14) Choos ing your node size. http s://docs.aws.a mazon.comJAmazonElastiCa che/latest 
/red-ug/nodes-se lect-s ize.html. 
(15) How fasl is Redis? http s://redis.io/topics/benchmarks. 
(16] Using Global Secondary Indexes in DynamoDB . htt:ps://docs.aws.a mazon.com/am 
azond ynamod b/latesV developerguid e/ GSI .ht ml. 
[l 7] Leaderboard & Write Shardin g. htlps ://www.dynamodbguide .com/ leaderboard-wr 
i te-shard ing/. 
314 I Chapter 10. Real-time Gaming Leaderboa rd 


[Page 316]
11 Payment System 
ln this chapter, we design a payment syste m. E-commer ce has exploded in popularlty 
across the world in recent years. What make s ever y tran sactio n p ossible is a payment 
system running behind the scenes. A r eliable , scalable, and flexible payment sys lem is 
essential . 
What is a paymen t syste m? According to Wikip edia, "a payment sys tem is any system 
used to settle finan cial trans actions through the transfer of monetar y value. lhis includ es 
the institutions , instrum ents, peop le, rules, procedures, stand ards, and technologies that 
make its exchange possible" [1). 
A payment system is easy to under stand on the surface but is also intimid ating for many 
developers to work on. A small slip could potentially cause significant revenue loss and 
destroy credibilit y among users. But fear not! In this chapter, we demy stify payment 
systems . 
Step 1 - Understand the Problem and Establish Design Scope 
A payme nt syste m can mean very differen t thin gs to different people. Some may think 
it's a digi tal wallet like Apple Pay or Goog le Pay. Others may think it's a backend sys tem 
that handles payments such as PayPal or Strip e. It is very important to determine the 
exact requirem ents at the beginning of the inter view. These are some questions you can 
ask the interviewer: 
Candidate: What kind of payment system are we building? 
Interviewer : Ass ume you are building a payment backend for an e-comme rce applica¡
tion like Amazon.com. When a customer places an order on Amazon.com. the payment 
system handl es every thin g related to money movement. 
Candidate : What payment options are supported? Credit cards, PayPal , bank cards, 
etc? 
Interviewer: The payment system shou ld supp ort all of these options in real life. How¡
ever, in this interview, we can use credit card p ayment as an example. 
Candidate : Do we handle credit card payment processing ourselves? 
I 315 


[Page 317]
-
Interviewer : No, vve use Lhfrd-party p<i.ymcnl processors, such as Stripe, BrainLree 
I 
Squnrc. etc. 
Candidate : Do we store credit card data in our system? 
Interviewer : Due to extremely high security and compliance requirem ents, we do not 
store card number s directly in our system. We rely on third -party payme nt processors 
to handle sensitive credit card data . 
Candidate : Is the application global? Do we need to suppo rt different currencies and 
int ernational paym ents? 
Interviewer : Great question . Yes, the appli cation would be global but we assume only 
one currency is used in this interview. 
Candid ate: How many payment transa ctions per day? 
Interviewer : 1 million transactions per day. 
Candida t e: Do we need to support the pay-out flow, which an e-commerce site like 
Amazon uses to pay sellers every month ? 
Interviewer : Yes, we need to support that. 
Candida te: I think I have gathered all the requirements . Is there anything else I should 
pay atte ntion to? 
Interviewer : Yes. A payment sys tem interacts with a lot of internal services (account¡
ing, analyti cs, etc.) and external services (payment service providers). When a service 
fails, we may see inconsistent states among services. Therefore , we need to perform 
reconciliation and fix any inconsistencies. This is also a reqwrement. 
With the se questions, we get a clear pictur e of both the functional and non-functional 
requirements. In this interview , we focus on designing a paymen t system that supports 
the following. 
Functional requirements 
ò Pay- in flow: payment system receives money from customer s on behalf of sellers. 
ò Pay-out flow: payment system sends money to sellers around the world . 
Non-functional requirements 
ò Reliability and fault toleran ce. Failed payments need to be carefully handled. 
ò A reconciliation process behveen internal services (payment systems. accountin g 
syste ms) and external serv ices (payme nt service providers) is required . The process 
asynchronously verifies that the payment information across these sys tems is con¡
sist ent. 
Back-of-the-envelope estimation 
The syste m needs to proc ess 1 million transa ctions per day, which is 1.000,000 transac¡
tio ns / 105 seconds = 10 tran sactions per second (TPS). 10 TPS is not a big number for 
a typi cal database , which means the focus of this system design interview is on how to 
316 I Chapter 11. Payment System 
I ;r 
~╖ 
. .. 
' 


[Page 318]
correctly handle paym ent tran sactions. rath er than aimin g for high tluough put. 
Step 2 - Propose High-level Design and Get Buy-in 
Al a high level, the payment flow is broken down into l wo steps lo reflect ho\ò 
flows: 
ò Pay-in flow 
ò Pay-oul flow 
Take the e-commerce site, Amazon , as an example. After a buyer places a 
money flows into Amazon's bank account, which is the pay-in flow. Althoug, 
is in Amazon's bank account, Amazon does not own all of the money. Tut 
a substantial part of it and Amazon only works as the money custodian f0> 
when the products are delivered and money is released, the balance after fo 
from Amazon's bank account to the seller's bank account. This is the pay╖ 
simplified pay-in and pay-out flows are shown in Figure 11.1. 
Pay-in flow 
Buyer 
ò ò I 
I 
I 
I 
E-commerce 
Website 
)t{ ò,ò 
I 
I 
I 
~ _J~[ __ ~Pay-in~Pay-out 
Seller 
ò ò 
Bank 
Account 
Figure 11.1: Simplified pay-in and pay-out flow 
lhe high-level design diagram for the pay-in flow is shown in Figure 11.2. Let's take a 
look at each component of the sys tem. 
- -- -- - -~- Step 2 - Propose High-level Design and Get Buy-in I 317 
-


[Page 319]
ò ~ 
G)Payment event 
Payment service 
Pay Pal 
3 Payment - ò Payment 
Order Executor ~ 
I 
stripe 
adyl!n ' I 
' I 
I 
I 
Payment System : 
I 
I 
I 
I 
' ' 
Payment Service 
Provide rs (PSP) 
Internal : External 
' 
Figure 11.2: Pay- in flow 
VISA 
ò ╖ Card Schemes 
The payme nt service accepts payment events fro m u sers a nd coor dinates the payme nt 
process. The firs t thing it u sually does is a risk check, assess ing for complian ce with 
regu lations such as AML/CIT [2], and for evidence of criminal activity such as money 
law1der ing or financ ing of ter rorism. TI1e payment service only pro cesses payments that 
pass this risk check. Usually, the risk check service uses a thir d-party provide r because 
it is very compli cate d and highly specialize d. 
Payment executor 
Th e paymen t executor executes a single paymenl order via a Payme nt Service Provider 
(PSP). A payme nt evenl may contain seve ral payment orders. 
Payment Service Provider (PSP) 
A PSP moves money from acco unt A to account B. In this simplified exam ple, the PSP 
moves the money out of the buyer's credit card account. 
Card schemes 
Card schemes are the o rganiza tions t hat process credit card opera tions. Well known 
ca.rd schemes are Visa, MasterCard, Discovery, etc. The card scheme ecosys tem is very 
complex [3]. 
Ledger 
Th e ledger keeps a fin ancial record of the payment transaction. For example, when a user 
pays the seller $1, we reco rd it as debit $1 from t he user and credit $1 to the seller. The 
ledger system i s very importan t in post-p ayment analysis, such as calculating the total 
revenue of the e-co mmerce website or forecasting futur e revenue. 
318 I Chapt er 11. Payment System 


[Page 320]
Wallet 
1lie wallet keeps the account balance of the mer chant. It may also record how much a 
given user has paid in total . 
As sho'\\rn in Figure 11.2, a typical pay-in flow works like this: 
1. When a user clicks the "place order" button , a payment event is generated and sent 
10 the payment service. 
2. The payment service stores the payment event in the database. 
3. Sometimes, a single payment event may contain several payment orders. For exam¡
ple, you may select products from multiple sellers in a single checkout process. If the 
e-conunerce website splits the checkout into multiple payment orders, the payment 
service calls the payme nt executor for each payment order. 
4. TI1e payment executor stores the payment order in the database. 
5. The payment executor calls an external PSP to process the credit card payment. 
6. After the payment executor has successfully processed the payment, the payment 
service updates the wallet to record how much money a given seller has . 
7. The wallet server stores the updated balance information in the database. 
8. After the wallet service has successfully updated the seller 's balance information, the 
payment service calls the ledger to update it. 
9. TI1e ledger service appends the new ledger information to the database. 
APls for payment service 
We use the RESTful API design convention for the payment service. 
POST /v1/payò ents 
This endpoint executes a payment event. As mentioned above, a single payment event 
may contain multiple payment orders. The reque st parameters are listed below: 
Field Description Type 
buyer_info The information of the buyer json 
checkout_ id A globally unique ID for this checkout string 
This could be encryp ted credit card informa -
credit_card_i nfo tion or a payment token . The value is PSP- json 
specific. 
payment_orders A list of the payment orders list 
Table 11.1: API request paramet ers (execute a payme nt event) 
The payment_orders look like this: 
Step 2 - Propose High-level Design and Get Buy-in I 319 


[Page 321]
- - - - -Field Descrip tio n Ty pe 
I -- Which seller will receive lhe - - ---- ╖-seller _account strin g 
L money 
The transaction amount for the 
amount order strin g 
L_ 
I currency TI1e currency for the orde r string (ISO 4217(4]) 
A globally unique TD for Lhis 
paymeni_order_id payment string 
Table 11.2: paym ent_orders 
Note that the payment_order _id is globally unique. When Lhe payme nt execu tor sends 
a payment request to a tl1ird-part y PSP. the payment_order _id is used by the PSP as the 
deduplication TD, also called Lhe idempo ten cy key. 
You may have noticed that Lhe data type of the "amoun t" field is "string~ rather than 
"double ". Double is not a good choice because: 
1. Different protoco ls, software, and hardware may suppo rt different numeric preci¡
sions in serialization and dese rialization. 1his difference might cause unint ended 
rounding errors . 
2. The number could be extremely big (for examp le, Japan 's GDP is around 5 x 1Ql4 
yen for the calendar year 2020), or extremely small (for examp le, a satoshi of Bilcoin 
is io- 8). 
It is reconune nded to keep numbers in string forma l dming transmission and storage. 
They are only parsed to numbers when use d for display or calculatio n. 
GET /v1/payments/{:id} 
111is endpoin t r eturns the execution status o f a sin gle payment order b ased on 
payment_order_id. 
The payment API mentioned above is simil ar to t he API of some well-kn own PSPs. If 
you are interes ted in a mor e comprehensive view of paym ent APis, check out Strip e's 
API doc wnentation [5]. 
The data model for payment service 
We need two tables for the payme nt service: payme nt eve nl and payment orde r. When 
we selec t a sto rage soluti on for a payme nt sys tem, perfonnan ce is usually not the most 
importan t factor. Instead, we foc us on the foll owing: 
1. Proven stability. Whether the s torage syste m h as been u sed by o ther big financia l 
firms for many years (for example more than 5 years) with positive feed back. 
2. The richness of supportin g tools, such as monit oring and inves tigation t ools. 
3. Maturi ty of the database admini strator (DBA) job mark et. Whether we can recruit 
experienced DBAs is a very importan t factor to consider. 
320 I Chapter 11. Payment System 
~1, pre! 
,1,,.sG 
,r111I t'' 
, .. 
'( 
╖.1nitnl 
~;~e: 
~(01 
~I 
... 
-,l 
'╖ 
~I 
~I 
- -


[Page 322]
Usually. we prefer a lradiliona l rela tiona l datab<lsc with ACID transac tion supp ort over 
No QL/NcwSQL. 
Tue paymen t eve nt table contains detailed payment eve nt inform ation. This is what il 
looks like: 
Nan\e Type 
checkout _id slring PK 
buyer _info strin g 
seller _info strin g 
credit_card_info depends on the card provider 
is_payment_done boole an 
Table 11.3: Payment event 
The payme nt order table stores the exec ution status of each payment orde r. Th.is is what 
it looks like: 
Name Type 
payment_order_id Strin g PK 
buyer_account string 
amount strin g 
currency suin g 
checkout_id strin g FK 
payment_order _statu s string 
ledger_updated boolean 
wallet_ updated boolean 
Table 11.4: Payment order 
Before we dive into the tabl es, let's take a look at some back ground information . 
ò The checko ut_id is the foreign key. A single checkout crea tes a payment event that 
may contain several payment orders . 
ò When we call a third-party PSP to deduct money from the buyer 's credit card , the 
money is not directly tran sfer red to th e seller . Instead, the money is tran sfer red to 
the e-co mmerce website's bank acco unt This process is called pay-in. When the pay¡
out condition is satisfied , such as wh en the produ cts are delivered, the seller initiate s 
a pay-o ut. Only then is the money transferr ed from the e-com merce website 's bank 
accoun t to the seller's bank account. Therefore , durin g the pay-in flow, we only need 
the buye r's card information , not the seller 's bank accou nt information. 
In the paymen t order table (Table 11.4), payment_ord er _status is an enumerated typ e 
(enum) that keeps the execut ion status of the paym ent order. Execution statu s incl udes 
NOT_STARTEO, EXECUTING, SUCCESS, FAILED. The updat e logic is: 
1. The initial status of payment_order _status is NOT_STARTEO. 
Step 2 - Propose High-level Design and Get Buy-In I 321 


[Page 323]
- ╖ 
\\ lH n I h( pa\ me nl c;rrnrr c;rnclc: thr pavmrn t orckr In I he pin mrnt rxrrntor. the 
n~yr.i0nt _order _status 1c. EXECUTING. 
-., 'lht pi!,╖mcnl ½;<Tvicr upda tes thr payment_o rder _status lo SUCCESS o r F AI LEO de¡
pC'ndm!! on the rrspnnc;e nf the- paymPnl executor . 
nn, l the pay111eni order _status is SUCCESS. the pa}'1nr nt service calls the wallet service 
11 1 update the sdler halance anrl update the wallel_updated field to TRUE. Here we simplify 
thl' d e c;1~n b~ assuming walle t upda tes always succeed. 
Oner it ic; done. the next step for the paymen t se rvice is to call the ledger se rvice to update 
the ledger database by updatmg the ledger _updated field to TRUE. 
\\hen all payment orders unde r th e sa me checkout_ id are processed successfu lly. the 
pavment service updates the i s_payment_done lo TRUE in Lhe payment event table. A 
"chcduJed JOb Ullually run s at a fixed interval to monitor the s tatu s of the in -flight pay¡
ment orde rs. It sends an alert when a paymen t order does n ol fin ish within a thresh old 
.,o that enginee rs can inves tiga te ii. 
Double-entry ledger system 
There is a very importan t d esign princi ple in the ledger syste m : the double-e ntry princi¡
ple (also called double -entry accounling /b ookkeeping [6]). Double -en try system is fun¡
damen tal to any paymen t system and is key lo accurate bookkeepi n g. It records every 
payment transa ction into lwo separa te ledger accou nts w ith t h e same amount. One ac¡
count is debited and the other is cred ited w ith the same amount (Table 11.5). 
Acco unt Debit Credit 
' 
buyer $1 
seller $1 
Table 11.5: Double-en try sys tem 
The double-entry sys tem stales that the sum of all the transac tion entri es must be 0. 
One cent lost means someone e lse gains a cent. It provides end-to-e nd tracea bili ty and 
ensures consistency thro ughout the payment cycle. To find out more about impl ementin g 
the double -entry system, see Square's engineering blog ab out immu table doubl e-e ntry 
accou ntin g database service [7]. 
Hosted payment page 
Most companies pref er not to store credit caJ:d information internall y because if they do, 
they have to deaJ with comp lex regu latio ns su ch as Payment Card Indu stry Data Securit y 
Standar d (PCI DSS) [8] in the Unit ed States. To avo id handlin g c redit card inform ation , 
companies use hosted credit card pages prov ided b y PSPs. For w ebsites, it is a widget 
or an ifrarne , w hile for mobile a ppli cations, it may be a pre-built page from Ll1e paym ent 
SOK Figure 11.3 illustra tes an example o f the checkout experien ce with PayPal int egra¡
tion. The key point h ere is that the PSP provides a hosted paym en t page that captur es the 
customer card informat ion directly, rather than relying o n our paymen t service. 
322 I Chapter 11. Payment System 


[Page 324]
-
Pay Pal 
Pay with PayPal 
W11t1 a rayPal accou'11 you'11 Pli[l lhle for flC'e 1Pt11rn ~,111ppt11a 
P11r. 111'ò' Pr otf' 1.;l1un. ;mrJ 11101 cò 
Em<11I or╖ mobile numl)er 
I P~ssword 
Stay logged in for faster purchases 0) 
Login 
Having trouble logging in? 
or 
Pay with Debit or Credit Card 
Figure 11.3: Hosted pay with PayPal page 
Pay-out flow 
The components of the pay-o ut flow are very similar to the pay-in flow. One difference is 
that instead of using PSP to move money from the buyer 's credit card to the e-commerce 
website's bank account , the pay-out flow uses a third -party pay-out provider to move 
money from the e-comme rce website's bank account lo the seller' s bank account. 
Usually, the payment sys tem uses third -party account payab le provider s like Tipalti (9] 
to handle pay-ou ts. There are a lot of bookkeeping and regulatory requirements with 
pay-outs as well. 
Step 3 - Design Deep Dive 
In this section, we focus on makin g the system faster. more robust, and secure. In a 
distributed system, errors and failures are not only inevitable but common. For exam¡
ple, what happens if a customer pressed the "pay" button multiple times? Will the y be 
charged multiple times ? How do we handl e payment failures caused by poor network 
connections? In this section , we dive deep into several key topics. 
ò PSP integration 
ò Reconciliation 
ò Handling payme nt processing delays 
Step 3 - Design Deep Dive I 323 


[Page 325]
---- ╖╖╖ 
ò C'nmmuni calilm ::imong inl ernal services 
ò 1-fa ndlin g fajled payment s 
ò Exac t-once delivery 
ò Consistency 
ò Security 
PSP integration 
If the payment system can directly connect to banks or card schemes such as Visa or Mas¡
terCard , payment can be made without a PSP. 11.1ese direcl connections are uncommon 
and highly speciali zed. They are usually reserved for really large companies that can 
justify such an inves tment. For most companie s, the paym ent system integrates with a 
PSP instead , in one of two ways: 
l . If a company can safely store sensitiv e payment information and chooses to do so, 
PSP can be integrated using APL The company is responsible for developing the 
payment web pages, collecting and storing sensitiv e payment informati on. PSP is 
responsible for com1ecting to bank s or card schemes. 
2. If a company chooses not to store sensitive payment inform ation due to complex reg¡
ulations and security concerns , PSP provid es a hosted payme nt page to collect card 
payment details and securely store them in PSP. This is the approach most companies 
take . 
\}le use Figure 11.4 to explain how the hoste d payment page works in detail . 
f=1---@ Store 
L__J token 
Checkout 
Page 
LJ 
1 
Checkout 
@ 
Display 
PS P's 
Payment 
page 
with token 
Client Browser 
Payment 
@ Start 
payment 
Create payment 
--- with nonce ---~ 
9 Webhook with 
completion result 
Figure 11.4: Hosted payment flow 
324 I Chapter 11. Payment System 
/JO 
,...01 
~'! 
-(0 
~11 
t:,, 
~'!!╖ 
r~' 
~11 
11~1. 
JI 
~~ 
~~ 
}, 
fJI' 
⌐.'f 
~b( 
ò _,. 
~[if 
~I 
~ ,, 
~ 
ii n 
re 
0 
\d\.: 
l 
fu 
re 
~I 


[Page 326]
We omitted the pay ment executor, ledger, and wallet in Figure 11.4 for simplicity. 1hc 
payment service orchestrates the whole payme nt process. 
1. The user clicks the "checkout" button in the client brow ser. 1he client calls the pay¡
ment senrice with the payment order inform ation. 
2. After receiving the payment order information . the payment service sends a paym ent 
registration request to the PSP. ╖nus registration request contain s payment informa¡
tion, such as the amou nt, currency, expiration date of the payment request , and the 
redirect URL. Because a payment order should be registered only once, there is a 
UU1D field to ensure the exactly-once registration . This UUID is also called nonce 
(10]. Usually, this UUID is the ID of the paym ent order. 
3. 1he PSP returns a token back to the payment service. A token is a UUID on the PSP 
side that uniquel y identifies the payment registration. We can examine the payment 
registration and the payment execution stat us late r using this token . 
4. The payment service stores the token in the database before calling the PSP-hosted 
payment page. 
5. Once the token is persisted , the client displays a PSP-hosted payment page. Mobile 
applications usually use the PSP"s SDK integration for this fun ctionality. Here we 
use Stripe's web integration as an example (Figure 11.5). Strip e provides a JavaScript 
library that displays the payment Ul, collects sensitive payment information, and 
calls the PSP directly to complete the payment. Sensitive payment informatio n is 
collected by Stripe. It never reaches our payment system . The hosted payme nt page 
usually needs two pieces of inform ation: 
(a) The token we received in step 4.. The PSP' s javascript code uses the token to 
retrieve detailed information about the payment request from the PSP's backend . 
One important piece of information is how much money to collect. 
(b) Another import ant piece of informati on is the redirect URL. This is the web page 
URL that is called when the paym ent is complete. Whe n the PSP's JavaScript 
finishes the paym ent, it redir ects the browser lo the redirec t URL. Usually, the 
redirect URL is an e-commer ce web page that shows the sta tus of the checkout. 
Note that the redirect URL is different from the webhook (1 1] URL in step 9. 
Step 3 - Design Deep Dive I 325 


[Page 327]
$129 .00 
Purt-ut 
I 
l'urn 910,. crtonm 
1 
~tnl" r i "' 
SG'iOO 
$64 00 
ti Pay 
Frrnil 
C.Hd lntorm.ittOl'I 
... '' ╖' .. 
{ .. 
United Sl~lc< 
Figuse 11.5: Hosted payment page by Stripe 
0 
6. The user fills in the payme nt details on the PSP' s web page , such as the credit card 
number , holder 's name, expiration date , etc, then clicks the pay butt on. The PSP 
starts lhe payment processing . 
7. The PSP return s the payment status. 
8. TI1e web page is now redirec ted to the redirect URL. The payment status that is re¡
ceived in step 7 is typically appended to the URL. For examp le, the full redirect URL 
could be [12): https: //your - company. com/?tokenID=JIOUIQ123NSF&payResul t=X32 
4FSa 
9. Async hrono usly, the PSP calls the payment service with the payment status via a 
webhook. TI1e webhook is an URL on the payment system side that was registe red 
with the PSP during the initial setup with the PSP. When the payment sys tem re¡
ceives payment events through the webhook, it extracts the paym ent status and up¡
dates the payment_o rder _status field in the Paym ent Order database table. 
So far, we exp laine d the happy path of the hosted payment page. In realit y, the network 
connection could be unreliable and all 9 step s above could fail. Is ther e any syste matic 
way to handl e failure cases? The answer is reconciliation. 
Reconciliation 
When sys tem components comm unicate asynchronously , there is no guarantee that a 
'fl: 
message will be delivered, or a response will be return ed. This is very common in the ╖ò 
payment business , which ofte n u ses asynchron ous communi cation to increase system ~ 
performance. Externa l sys tems, such as PSPs or bank s, prefer asy nchron ous communi- ~ 
326 I Chapter 11. Payment System 
---


[Page 328]
cation as well. So how can we ensure correc tness in this case? 
1l1c answer is reconciliation . This is a p ractice that periodical ly compares the stales 
among related servi ces in order to verify that Chey are in agreemenl. It ls usually the lasl 
line of defense in the payme nt sys tem. 
Every night the PSP or banks send a settlemen t file to their clien ts. The settle ment file 
contains the balance of the bank account, toget her with all the transaclio ns that took 
place on this bank acco unt durin g the day. 1he reconciliatio n sys tem parses the set¡
tlement file and compares the details with the ledger system. Figure 11 .6 below shows 
where the reconciliation process fits in the system. 
ò ~ 
' Payment event 
Payment System 
I 
I 
Internal : External 
Payment Service 
Providers PSP 
Pay Pol 
illlyen 
Settlement file 
Card Schemes 
VISA 
Figure 11.6: Reconciliation 
Reconciliation is also used to verify that the payment system is internally consistent. 
For example, the states in the ledger and wallet might diverge and we could use the 
reconciliation system to detect any discrepancy . 
To fix mismatches found during reconciliati on, we usually rely on the finance team to 
perform manual adjustments. The mismatch es and adjustments are usually classified into 
three categorie s: 
1. The mismatch is classifiable and the adjustment can be automated. In this case, we 
know the cause of the mismatch , how lo fix it, and it is cost-effective to write a 
program to automate the adjustment. Engineers can automate both the mismatch 
classification and adjustment. 
2. The mismatch is classifiable, but we are unable to automate the adjustment In this 
case, we know the cause of the mismat ch and how to fix it, but lhe cost of wrilmg an 
auto adjustment program is too high . The mismatch is pul into a job queue and Lhe 
finance team fixes the mismatch manually . 
Step 3 - Design Deep Dive I 327 


[Page 329]
.\. lhe m1snrn1ch is u nclassifia ble. Jn thi s case, we do not know how the mismatch 
happen s. 111e mismatch is pul in to a sp eci al job queue. The finance tea m inves tigates 
il manually. 
Handling payment processing delays 
As disc ussed prev iously, an end -to-e nd payment request flows through man y compo¡
nent s and invo lves both internal and external parties. While in most case s a p ayment 
request wou ld complete in seco nd s, there are situa tions w here a p aymen t request would 
stall and so metimes take hours or days befo re it is completed or rejec ted. Here are some 
examp les whe re a payment request could take longer than usual : 
ò The PSP deems a paymen t reques t high risk and require s a huma n to review it. 
ò A cre dit card r equires extra protec tion like 3D Secure Au thenticatio n [13] which 
requires extra details from a card holder to verify a purchase. 
'TI1e payment service must be able lo handle these paym en t requests that take a long 
time to p rocess. If the buy page is hosted by an external PSP, w hich is quite common 
these days, the PSP would hand le these long-runn ing paym ent reques ts in the following 
ways: 
ò The PSP w ould return a pend ing status to our clienl Our clien t would display that to 
the user. Ow╖ client would also provi de a page for the custo mer t o check the current 
paym ent status. 
ò Tue PSP tracks the pending payment on our behalf, and noti fies the payment service 
of any s tatus update via Lhe webhook the payment service reg istered with the PSP. 
When the payme nt request i s finall y c ompleted, the PSP calls the registere d webhook 
mentioned abov e. The payme nl service updates its internal sys tem and completes the 
shipm en t to the customer. 
Alternativ ely, instead of updati ng the payme nt service via a webh ook, some PSP would 
pu l the burde n on U1e payment servi ce to p oll the PSP for status updates on any pending 
paymen t requests. 
Communication among internal services 
There are two type s o f comm unicatio n patte rns t hat internal servi ces use to communi ¡
cate: synchron ous vs async hronous. Both are explained below. 
Synchronous communication 
Synchro nous communi cation like HTTP works well for small-scale systems, but its short¡
comings b ecome obvio us as the scale increas es. It creates a long request and r esponse 
cycle that d epends o n m any services. The drawbacks of this approach are : 
ò Low perfor mance . If any o ne of the services in the chain d oesn 't perform well, the 
whole system is impac ted. 
328 I Chapter 11. Payment System 
\~1╖ 
.. 


[Page 330]
╖~ .. 
\ 
I ò 
ò Poor failure isolation . If PSPs or any other services fail, the client will no longe r 
receive a respo nse . 
ò Tight couplin g. The request sender needs to know lhc recipient. 
Hard to scale. Without using a queue to act as a buffer, it's not easy to scale the 
system to supp ort a sudden increase in traffic . 
Asynchronous communication 
Asynchronous communicati on can be divided into two categories: 
ò Single receiver: each requ est (message) is processed by one receiver or service. It's 
usually implemented via a shared message queu e. The message que ue can have mul¡
tiple subscribers, but once a message is processed, it gets removed from the queu e. 
Let's take a look at a concrete example. In Figure 11.7, service A and service B both 
subscribe to a shared message queue. When ml and m2 are consumed by service A 
and servi ce B respe ctively, both messages are removed from the queue as shown in 
Figure 11.8. 
Service A 
L::'.J El El El 
m4 m3 m2 m1 
Service B 
Figure 11.7: Message queue 
Service A 
El El 
m4 m3 
Service B 
Figure 11.8: Single receive r for each message 
ò Multiple receivers: each request (message) is processed by multipl e receive rs or ser¡
vices. Kafka works well here . When consumers receive messages, they are not re~ 
moved from Kafka. The same message can be pro cessed by different service s. This 
model maps well to the payment syst em, as the same request might tJ:igger multiple 
side effects such as sendin g push notificati ons, updatin g financial reportin g, ana-
Step 3 - Design Deep Dive I 329 


[Page 331]
Jytics. etc. An example is illustrnted in Fi~re l J.9. P::-iymrnl events RT<' published 
to Kafka and consumed by different services such as thr payment system, analytics 
service, and billing service. 
El El EJ El 
m4 m3 m2 m1 
Payment 
System 
Analytics 
Billing 
Figure 11.9: Multiple receivers for the same message 
Generally speaking, synchronous communication is simpler in design, but it doesn't al¡
low services to be autonomous. As the depend ency graph grows, the overall performance 
suffers. Asynchronous communication trad es design simplicity and consistency for scal¡
ability and failure resilience. For a large-scale payment system with complex business 
logic and a large number of third-party dependenci es, asynchronous communication is 
a better choice. 
Handling failed payments 
Every payment system has to handle failed transactions. Reliability and fault toler¡
ance are key requirements . We review some of the techniques for tackling those chal¡
lenges. 
Tracking payment state 
Having a definitive payment state at any stage of the payment cycle is crucial. Whenever 
a failure happens , we can determine the current state of a payment transa ction and decide 
whethe r a retry or refund is needed. The payment state can be persisted in an append¡
only database table. 
Retry queue and dead letter queue 
To gracef ully handle failures, we utilize the retry queue and dead letter queue , as shown 
in Figure 11.10. 
ò Retry queue: retryable errors such as transient errors are routed to a retry queue. 
ò Dead letter queue [14): if a message fails repeatedly, it eventually lands in the dead 
letter queue. A dead letter queue is useful for debugging and isolating problematic 
messages for inspection to determine why they were not processed successfully. 
330 I Chapter 11. Payment System 
~r 
i 1 
!IS 


[Page 332]
Payment 1-- -i 
S tern 
Retryable? 
Retry Queue 
L 
Fanure 
Retryable? 
Dead Letter Queue 
Database 
Figure 11.10: Handle failed payments 
1. Check whether the failure is retryable. 
(a) Retryable failures are routed to a retry queue. 
(b) For non-retryable failures such as invalid input, errors are stored in a database . 
2. The payment system consumes events from the ret-ry queue and retries failed pay¡
ment transactions. 
3. If the payment transaction fails again: 
(a) If the retry count doesn 't exceed the threshold , the event is routed to the retry 
queue. 
(b) If the retry count exceeds the threshold, the event is put in the dead letter queue . 
Those failed even ts might need to be investigated. 
If you are interested in a real-world example of using those queues, take a look at Uber's 
payment system that utilizes Kafka to meet the reliability and fault-tolerance require ¡
ments [15]. 
Exactly-once delivery 
One of the most serious problems a payment system can have is to double charge a cus¡
tomer. It is important to guarantee in our design that the payment system executes a 
payment order exactly-once [16]. 
At first glance , exactly-once delivery seems very hard to tackle, but if we divide the prob¡
lem into two parts , it is much easier to solve. Mathematically, an operation is executed 
exactly-once if: 
1. It is executed at-least-onc e. 
2. At the same time, it is executed at-most-once. 
We will explain how to implement at-least-once using retry, and at-most-once using 
idempotency check. 
Step 3 - Design Deep Dive I 331 


[Page 333]
Retry 
Occasionally , we need lo retry a payment tran sac tion du e to ne twor k errors or tim eout. 
Retry provides the at-least-once guarantee. For ex;:implc, as sh own in Fip;urc 11 .11 , w her e 
th e client tries to make a $10 payment, but the payment requ es t ke ep s failing due to a 
poor network conne cl1on. In thi s example, th e netw ork evc ntu " lly recove red and th e 
request succeeded at the fourth al1 empl. 
I Client I 
-4 
R etry 
R etry 
-
R etry 
Pa $10 y 
╖X 
Pa $10 y 
x 
Pa y$ 
x 
Pa y $ 
./ 
10 
10 
I Payment I 
System 
Pay ment failed 
-
Pay ment failed 
Pay ment failed 
-
Pay ment succeeded 
Figure 11.11: Retry 
Deciding the appropriate time intervals between retri es is important. Here are a few 
common retry strategies. 
ò Inunedi ate retry : client immediately resends a request. 
ò Fixed intervals: wait a fixed amow1t of time between the time of the failed payment 
and a new retry attempt. 
ò Incremental intervals: client waits for a short time for the first retry , and then incre¡
mentally increases the time for subsequent retries. 
ò Exponential backoff [17): double the waiting time between retri es after each failed 
retry. For example, when a request fails for the first time, we retry after 1 second; if 
it fails a second time, we wait 2 seconds before the next retry; if it fails a third time, 
we wait 4 seconds before another retry. 
ò Cancel: the client can cancel the request. This is a common practice when the failure 
is permanent or repeated requests are unlikely to be successful . 
Detenninin g the appropriate retry strategy is difficult. There is no "one size fits all" solu¡
tion. As a general guideline, use exponential backoff if the network issue is unlike ly to be 
resolved in a short amount of time. Overly aggressive retry strategies waste computing 
332 I Chapter 11. Payment System 


[Page 334]
rM(IUr~s nnd cAJ1 csrnse service ove rloa d. A good prnclirr is to prnv1dr an rrro r codr 
\lllh n Retry-Afte r heAdcr. 
pctt<'nllnl proh lem of retryin~ is douhlr pRymrnl s. Lei us take a look at two scr nar-
1 " 
ò ren rio 1 Tur payment system in tegrates with PSP using a hosted payment page. and 
the d 1t"nt rhcks the pey butt on twire . 
ò cenarlo 2: The pavm ent is successfulJy process ed by the PSP, but the response fails to 
n-11rh our payme nt sys tem due to netw ork errors . 1he user clicks the "pay" butt on again 
or the chent retries the payment. 
In order to avoid double payment. th e payment has to be executed at-most-once. This 
at-most-once guara ntee is also called idempolency. 
ldempotency 
Id~mpot ency is key to e nsuring the a t-most-once guarantee . Accordi ng to Wikip edia, 
'"1dempotence is the property of cert ain operati ons in mathematics and computer scie nce 
\\-hereby they can be applied multiple times without changing the result beyo nd the ini ¡
hal applica tion'" [18]. From an API standpoin t, idempote ncy means clients can make the 
same call repeatedly and pro duce th e same result. 
For communi catio n betwee n clients (web and mobile applications) and servers, an idem¡
polency key is usually a u niqu e val ue that is generated by the c lient and expires after 
a certai n p eriod of time. A UUID is commonly used as an idempotency key and it is 
recommended by many tech companies such as Strip e [19] and PayPal [20]. To per¡
form an idempoten t p ayme nt request, an idem potency key is added to the HTTP header: 
<idempotency-key: key_value>. 
Now that we unde rstan d the basi cs of idempotency, let's t ake a look at h ow it h elps to 
solve the double payment issues mentioned above . 
Scenario 1: what if a customer clicks the 
11
pay" button quickly twice? 
In Figure 11.12, when a user clicks "pay;" an id.empo tency key is sent to the payment 
system as par t of Lhe HTTP request . In an e-co mmerce website, the idempotency k ey is 
usually the ID of th e s hoppi ng cart right befor e the checkout. 
For the second request, it's treated as a retry because the payment syste m h as already 
seen the idempote ncy k ey. W hen we include a previo usly speci fied idempotency key 
m the reques t h eader, the payment sys tem r eturn s the latest status of the previous r e¡
quest. 
Step 3 - Design Deep Dive I 333 


[Page 335]
POST (idempotency-key: UUID} 
r-=1 ,------ _____n- Payment l 
L "''' t System J 
First request -------
Charge succeeded 
~-------- - ------ - ------------
-- ------------------- ----- ------- - - --- ------------- --------- ----, 
POST {ldempotency-key: UUID) 
~ 
Retry 
Return previous message 
Payment 
System 
Servor has 
already seen the 
ldemp otency key. 
Do not process 
the request again 
---------------------------------------------- ----------- ------- -----
Figure 11.12: Idempotency 
I 
I 
I 
I 
I 
I 
If multiple concurrent requests a re detected with the same idempotency key, only one 
request is processe d and the others receive the 429 Too Many Request s sta tus code. 
To supp ort idempotency , we can use the database's unique key constraint. For example, 
the primar y key of the database table is served as the idempotency key. Here is how it 
works: 
1. When the payment system r eceives a p ayment, it tries to insert a row into the 
database table. 
2. A successful inser tion means we have not seen thi s payment request before. 
3. If the inserti on fails because the same prim ar y key already exists, it means we have 
seen this payment request before. The second request will not be processe d. 
Scenar io 2: The payment is successfully processed by the PSP, but the response 
fails to reach our payment system due to network errors. Then the user clicks the 
"pay" button again. 
As shown in Figure 11.4 (step 2 and step 3), the payment service sends the PSP a nonce 
and the PSP retur ns a correspondin g token . The nonce uniqu ely represents the payment 
order, and the token uniquel y maps to the nonce. Therefore, the token uniqu ely maps to 
the payment order. 
When the user clicks the "pay" button again, the payment order is the same, so the token 
sent to the PSP is the same. Because the token is used as the idempo tency key on the 
PSP side, it is able to identify the double payment and return the status of the previous 
execution . 
Consistency 
Several stateful services are called in a paym ent execution: 
334 I Chapter 11. Payment System 


[Page 336]
-
-
1. The pstymcn t service kee ps pay mr nl -rclri tcd dalri such i:is non ce, token, pnymcnt or-
der. execu tion status, etc. 
2. The ledger keeps all acco untin g data. 
3. The WAilet keeps the acco unt bala11cc of the merclrnnl. 
4 1l1e PSP keeps the payment execution status. 
s. Data might be replicated among different database replicas to increase reliability. 
Jn R dlstTibuted environment, the communication between any two services can fail, caus ¡
ing: data inconsistency. Let's take a look at some techniques to resolve data inconsistency 
10 a payme nt system. 
To maintain data consistency betw een internal services, ensuring exactly-once proc ess¡
ing is very ilnp ortant. 
To maintain data consistency between the internal service and external service (PSP), we 
usually rely on idempotency and reconciliation. If the external service supports idempo¡
tency, we should use the same idempotency key for payment retry operations. Even if 
an external service supports idempotent APJs, reconciliation is still needed because we 
shouldn't assume the external system is always right. 
If data is replicated, replication lag could cause inconsistent data between the primary 
database and the replica s. There are generally two options to solve this: 
1. Serve both reads and writes from the primary database only. This approach is easy 
to set up, but the obvious drawback is scalability. Replicas are used to ensure data 
reliability, but they don 't serve any traffic, which wastes resources. 
2. Ensure all replicas are always in-sync. We could use consensus algorithms such 
as Paxes [21] and Raft [22], or use consensus -based distributed databases such as 
YugabyteDB [23] or CockroachDB (24). 
Payment security 
Payment security is very important. In the final part of this system design, we briefly 
cover a few techniques for combating cyberatt acks and card thefts. 
Step 3 - Design Deep Dive I 335 


[Page 337]
--
- Probl em Solution 
Request/response eavesdropping Use HTTPS 
Data tampering Enforce encryp tion and integrity-
monitoring 
Man-in-the-middle attack Use SSL wilh certificate pinn ing 
Database replication across mult i-
Data loss pie regio ns a nd take s napshots o f 
dala 
Distributed denial-of-service <1 ttack Rate Jimiling and firewall [25] (DDoS) 
Tokenization. Instead of using real 
Card theft card n umbers, tokens are s tored 
and used for payment 
PCT DSS is an inform ation secu-
PCI compliance rity standard for organizations that 
handle branded credit cards 
Address verifica tion, card verifica-
Fraud tion value (CVV), user b ehavior 
analysis, etc. [26] [27] 
Table 11.6: Payment security 
Step 4 - Wrap Up 
In this chapter , we inves tigated the pay-in flow and pay-out flow. We went into great 
depth about retry, idempotency, and consisten cy. Payment error handlin g and security 
are also covered at the end of the chapter . 
A p ayment system is extremely complex. Even thou gh w e have covered many topics, 
there are still more worth mentionin g. The following is a repres entative but not an ex¡
haustiv e list of relevant topics. 
ò Monitorin g. Monitorin g key metrics is a c ritical part of any mod ern application. 
With extensiv e monitoring, we can answer questions like "What is the average accep¡
tance rate for a specific payment method?", "What is the CPU usage of our servers?", 
etc. We can create and display those metrics on a dashboard. 
ò Alertin g. When somethin g abnormal occurs, it is important to alert on-call develop¡
ers so they respond promptl y. 
ò Debugging tools. "Why does a payment fail?" is a common question. To make 
debugging easier for engineers and customer support, it is important to develop 
tools that allow staff to review the transaction statu s, processing server history, PSP 
records, etc. of a payment trans action. 
ò Currency exchange. Currency exchange is an important considerati on when design- j 
ing a payment system for an internati onal user base. . 
ò Geography. Different region s might have completely different sets of payment meth- j 
336 I Chapter 11. Payment System 


[Page 338]
ode; 
ò < n h pa 'lTient. Cas h paymen t is very commo n in IndiR, Brn1.il. nml some other <'<> llll 
ln<' . tTher [28] and Airbnb [29) wrnl<' dct Aileci engineering biogs nhn11l how they 
handled cas h-based payment. 
ò '░ogle App le pay integration . Please read [30] if interested . 
t \░lO!!JlltuJati ons on getting this far! Now give yourse lf a pat on the back. Good job! 
Step 4 - Wrap Up I 337 


[Page 339]
Chapter Summary 
step l 
step 2 
Payme nt Service 
step 3 
< 
pay 111 Jlow 
functional rcq 
pay-out flow 
< 
reliability: handl e failed payment s 
non-functiona l req 
reco nciliation 
estimation -- 10 TPS 
paym ent service 
payment exec utor 
payment service provider 
pay-in flow 
card scheme 
ledger 
wallet 
pay-out flow -- third -party service 
PSP inte gra tion 
reconciliation 
handlin g paymen t processing delays 
communi cation among internal services 
< 
keep paym ent safe 
handl e failed payments 
retr y queue and dead letter queue 
<
retry 
exactly-once delivery 
idempotency 
consistency 
payment security 
step 4 --wrap up 
338 I Chapter 11. Payment System 


[Page 340]
Reference Material 
{1] PRymenl system. ht tps://en.wikip edia.org/wiki/Paymcnl_systcm. 
f 2] AML/CFT. ht tps://cn.wikip edia.org/wiki/Moncy _laundering. 
f3l Card scheme. http s://en.wik.ipedia.org/wiki/Card_scheme. 
[4] ISO 4217 . https: //e n.wikip edia.org/wiki/IS0 _ 4217. 
[S) tripe API Reference. https ://stripe. com/docs/api. 
[ 6] Double-e ntry bookkeeping. https: / /en. wikip edia.org/wiki/Double-entry _ boo kkec 
ping. 
(7] Books, an immut able double-entry accounting database service. http s://developer . 
square up.com/blog/books-an-immutable- double-entry -accounting-database -serv 
ice/. 
[8] Payment Card Industry Data Security Standard. https ://en.wikipedia .org/wiki /Pa 
yment_ Card_Industry _Data_Security _Standard. 
[9] Tipalti . https: //tipalti .com/. 
[ l O] Nonce. http s:// en. wikipedia . org/wiki/Cryptographic_nonce. 
[11) Webhooks . https: //stripe .com/docs /webhooks. 
[12] Customize your succes s page . https ://stripe.com /docs/payments /checkout /custom 
-success-page. 
[13) 3D Secure . https ://en.wikipedia.org /wiki/3-D_Secure. 
[14) Kafka Connect Deep Dive - Error Handling and Dead Letter Qyeues . https ://www . 
confluent.io /blog /kafka-connect-deep- dive-error-handling -dead-letter-queues /. 
[15] Reliable Processing in a Streaming Payment System. https:/ /www.y outube. com/w a 
tch?v=STD8m7wlxEO&list=PLLEUtp5eGr7D z3fWGUpiSiG3d_ WgJe-KJ. 
[16] Chain Services with Exactly-Once Guarantees . https: //www .confluent.i o/blog/ch 
ain-servi ces-exactly-guarantees /. 
[ 17] E:Kponential backoff. https: // en.wikipedia.org /wiki/Exponential _backoff. 
[ 18) Idempotence. https: //en.wikipedia.org /wiki/Idempotence. 
[19) Stripe idempotent requests. https ://stripe. com/docs/api/idempotent _requests. 
[ 20] Idempotency . https: // developer. paypal .corn/ docs/platform s/ develop/idempotency I╖ 
[21] Paxos. https: //en.wikipedia .org/wiki/Paxos_(computer_science). 
[22] Raft. https :/ /raft.github.io /. 
[23] YogabyteDB. https: //www.yugabyte.com/ . 
Reference Material I 339 


[Page 341]
[24] Cockroachdb . htlp s://www.cockroach labs.com/. 
[25] What is DDoS attack. hltps://www .cloud Oare.com/learn ing/ddo s/what-is-a- ddos¡
at lack/. 
[26) H ow Payment Gateways Can Detect and Prevent Online Fraud. htt ps://www.c har 
gebee.com/blog/optimize-onli ne-billin g-s lop-onlin e-fraud/. 
[27) Advan ced Techn ologies for Detecting and Preventin g Fraud a t Uber. http s://eng.ub 
er.com/advanced- lechno logies-detecling-prevenlin g-fraud-uber/. 
[28) R e-Architecting Cash and Digital Wallet Payments for Indi a with Uber Engineering. 
hltps:// eng. uber.com/india-pay ments/. 
(29] Scali ng A irbnb's Payment Platform . http s://medium.com/a.irbnb-engineering/scal 
ing- a.irbnbs-payment-platform-43ebfc99b324. 
[30] Paym en ts In tegration at Uber: A Case Study - Gergely Oro sz. http s://www .youtub 
e.com/watc h ?v=yooCES BOSRA. 
340 I Chapter 11. Payment System 
òò 


[Page 342]
12 Digital Wallet 
P'arnlent platfurm.s usually pro'ide a digital wallet sen;ce to clients. so they can store 
~- in the wallet and spend it later. For example. you can add money to >our digital 
nllet from your bank card and when you buy products online. you are gh'en the option 
t(I pay usmg the money in your wallet. Figure 12.l shows this process. 
~'╖ $ ~---+-.'l! 
I I ò ò 
~-a'!let 
Pa)\ie.t $}!Stein 
Figure 12..1: Digital wallet 
Spending money is not the only feature that the digital wallet provides. For a payment 
platform like PayPal we can directly transfer money to somebody else's wallet on the 
same payment platform.. Compared "ith the bank-to-bank transfer , direct transfer be¡
tv.cen digital wallets is faster. and most importantly , it usually does not charge an extra 
fee.. figure 122 shows a cross -"\\-allet balance transfer operation. 
Digital wallet 
Figure 122: Cross-wallet balance transfer 
Suppose we are asked to design the back.end of a digital wallet application that supports 
the cross-wallet balance transfer operation. At the beginning of the interview , we will 
2sk clarification questions to nail down the requirements. 
Step 1- Understand the Problem and Establish Design Scope 
I 341 
-


[Page 343]
--
Candidate : Should wr only focus on lrnlancc transfer opcr<1linn'> hr twrr n two digital 
wa llrl <>? Do wr need to worry about other real urcs? 
Interviewer : Let's focus on br1 lanec transfer opcra lions only. 
Candidate : II ow many l ransacl ions per seco nd (TPS) docs the system need to support? 
Interviewer : Lei's assume 1,000 ,000 TPS. 
Candidate : A digital wallet h as slricl requir ement s for correctness. Can we assume 
transac tional guarant ees [1] are sufficient? 
Int erviewer : 11rnt sound s good . 
Candidate : Do we need to prov e correc tness? 
Interviewer : This is a good question. Corr ectness is usually only verifiable after a trans¡
act ion is complete. One way to verify is lo compare our int ernal records with state ments 
from bank s. The limitation of recon ciliation is that it only shows discrepancies and can¡
not tell how a differen ce was genera ted. Therefore, we would like to design a sys tem with 
reprodu cibility , meaning we cou ld always reconstruc t hist orical balance by replaying the 
data from the very beginning . 
Can didate : Can we assu me the avai lability requirement is 99.99 3 
Interviewer: Sounds goo d. 
Can didate : Do we need to tal<e foreign exchange into considera tion? 
Interviewer : No, it's out of scope . 
In summary , our digital wallet n eeds to support the following: 
ò Support balan ce transf er opera tion between two digital wallets. 
ò Support 1,000,000 TPS. 
ò Reliability is at least 99.993 . 
ò Support transactions . 
ò Support reprodu cibility. 
Back-of-the-envelope estimation 
When we talk abou t TPS, we imply a tran sactional databa se will be used. Today, a rela¡
tional database running on a typical data center nod e can support a few thousand trans¡
actions per second. For example, reference [2] cont ains the performance benchmark 
of some of the pop ular transactional database servers . Let's assume a database node can 
supp ort 1,000 TPS. In order to reach 1 million TPS, we need 1,000 database nodes. 
However , this calculation is slightly inaccurat e. Each tran sfer command requires two 
opera tions: deducting money from one account and depositing money to the other ac¡
count. To support 1 million tran sfers per second, the system actually needs to handle up 
to 2 million TPS, which mean s we need 2,000 nodes. 
Table 12.1 shows the total numb er of nodes required when the "per-node TPS" (the TPS 
a s ingle node can handl e) changes. Assuming hardwar e remain s the same, the more 
342 I Chapter 12. Digital Wallet 


[Page 344]
-
transnclions a single node can handl e per seco nd. the lowe r the total numb er of nodes 
required , indicati ng lower hardwl'\re cost. So one of our design goals is to increase the 
number of transactions a single node can handl e. 
Per-node TPS Node Number 
100 20,000 
1,000 2,000 
10.000 200 
Table 12.1: Mappin g between pre -node TPS and nod e number 
Step 2 - Propose High-level Design and Get Buy-in 
In this section. we will discuss the following: 
ò API design 
ò Three high-level designs 
1. Simple in-memory solution 
2. Database-based distributed transaction solution 
3. Event sow╖cing solutio n with reproducibility 
API design 
We will use the RESTful API convention. For this interview , we only need to support one 
API: 
API Detail 
POST /v1/wallet/balance_transfer Transfer balan ce from one wallet to an¡
other 
Request paramet ers are: 
Field Descdption Type 
f rom_account 1he debit account string 
to_account The credit account string 
amount The amount of money string 
currency The currency type string (ISO 4217 [3]) 
transaction_id ID used for deduplication uuid 
Sample response body: 
{ 
11 Stat us
11
: 
11
success
11 
11 Transaction_id
11
: 
11
01589980 - 2664- 11 ec - 9621 - 0242ac130002
11 
t 
One thing worth mentioning is that the data type of the "amount " field is "strin g;' 
Step 2 - Propose High-level Design and Get Buy-in I 343 


[Page 345]
ralh er Lhan "double". We explained Lhe reason ing in Chapler 11 Payment System on 
page 320. 
In practice , many people still choose float or doub le repre sentation of numbers because it 
is suppo rted by almost every programming language and database. It is a proper choice 
as long as we w1derstand lhe potential risk of losing precision . 
In-memory sharding solution 
The wallet applicatio n main tains an accow1t balan ce for every user accow1l. A good data 
stru cture to represent this <user , balance> rela tionship i s a map, whic h i s aJso called a 
hash table (map) or key-value store. 
For in-memory stores, one popular choice is Redis. One Redis node is not enough to 
handle 1 million TPS. We need to set up a cluster of Redis nodes and evenly distri bute 
user acco wits among them . This pro cess is called pai-titioni ng or sharding. 
To distrib ute the key-value data among n partitions, we could calculate the hash value 
of the key and divide it by n. The remainder is the destination of the partition. 111e 
pseudocode below shows the sharding process: 
Str ing accountID = 
11
A
11
; 
Int partitionNumber = 7; 
Int myPartition = account ID.h ashCode() % parti tio nNumber; 
The number of parti tions a nd a ddresses of all Redis nodes can be stored in a central¡
ized place. We could use ZooKeeper [ 4) as a highly-av ailable configurati on storage solu¡
tion . 
The final component of thi s solutio n is a service that handles the tran sfer commands . We 
call it the wallet service and it has several key responsibilities. 
1. Receives the transfer command 
2. Validates the tran sfer command 
3. If the command is valid, it upda tes the accowit balances for the two users involved 
in the transfe r. In a cluster, the account balan ces are likely to be in different Red.is 
nodes 
The wall et service is stateless. It is easy to scale horizontall y. Figure 12.3 shows the 
in-memory solution. 
344 I Chapt er 12. Digital Wallet 


[Page 346]
Transfer Command Transfer Command 
A- $1 ~s 
{ A: balance } { B: balance } { C: balance } 
Red is Red is Red is 
Figure 12.3: In-memory solution 
Partition 
Info 
Zoo keeper 
In this exam ple, we have 3 Redis nodes . Ther e are three clients, A, B, and C. Their account 
balances are evenly spread across these three Redis nodes. 1here are two wallet service 
nodes in this example that handle the balance transfer requests. When one of the wallet 
service nodes receives the transfer command which is to move $1 from client A to client 
B, it issues two commands to two Redis nodes. For the Redis node that contains client A's 
account, the wallet service deducts $1 from the account. For client B, the wallet serv ice 
adds $1 to the account. 
Candidate : In this design, account balances are spread across multiple Redis nodes. 
ZooKeeper is used to maintain the sharding information . The stateless wallet servic e 
uses the sharding information to locat e the Redis nodes for the clients and updat es the 
account balan ces accordingly. 
Interviewer : 1his design works , but it does not meet our correctness requir ement. The 
wallet servi ce updates two Redis nodes for each tran sfer. There is no guarant ee that 
both updates w ould succeed. If, for example , the wallet service node crashes after the 
first update has g one through but before the second update is done, it would result in an 
incomplete tran sfer . The two updates need to be in a single atomic tran saction. 
Distributed transactions 
Database sharding 
How do we make the updates to two different storage nodes atomic? The first step is to 
replace each Redi s node with a transactional relational database node . Figure 12.4 shows 
the architecture. Titis time , clients A, B, and C are partiti oned into 3 relational data bases, 
rather than in 3 Redis nodes . 
Step 2 - Propose High-level Design and Get Buy-in I 34 5 


[Page 347]
Transfer Command 
OQ] l Balance I 
Wallet 
Service 
0QJ l Balance 
Transfer Command 
Wallet 
Service 
[K).._I __ ~ 00.._I __ ~ 
OQ] I Balanc e 
@J .._I - '---....J 
Partition 
Info 
Zoo keeper 
Relational Database Relational Database Relatlonal Database 
Figure 12.4: Relational database 
Using tran sac tional databases only solves part of the problem . As mentioned in the last 
sec tion, it is very ill<ely that one transfer command will need to updat e two accounts 
in two different databases. There is no guarantee that two update operations will be '.d'l0 
handled at exactly the same time. If the wallet service restarted right after it update d 
the first account balance , how can we make sure the second account will be updated as 
well ? "$NJ 
Distributed transaction: Two-phase commit 
In a distributed system, a transaction may involve multiple processes on multip le nodes. 
To make a transaction atomic, the distributed trans action might be the answer. There are 
two ways to implement a distribut ed transaction: a low-level soluti on and a high-leve l 
solution . We will examine each of them . 
The low-level solution relies on the database itself. The most common ly used algorithm 
is called two-phase commit (2PC). As the name implies, it has two phases , as in Figure 
12.5. 
Prepare Commit 
, time 
Coordinator -!-r;..:...:..:..:.:..-==-::.::(}.-()--__.:._-<n-o-----c>----o--;-c>-----u--u- -:--¡
(Wa11e1 Servlco ) 
Database C -!------1"H--<i ╖-...;.....--o--o----;.--()---O-t--r, --.. 
I 
lockC 
I 
unloc:kC : 
Figure 12.5: Two-phase commit (source [5]) 
346 I Chapter 12.. Digital Wallet 


[Page 348]
I. The coordinator . which in our case is the wallet service . performs read and writ e 
operations on multiple databases as normal. As shown in Figure I 2.5, both databa ses 
A and C are locked . 
2. When the appli cation is about to commit the transactio n, the coord inator asks all 
databases to prepare the transaction . 
3. In the second phas e, the coordinato r collects replies from all databases and performs 
the following: 
(a) If all databases reply with a yes, the coordinator asks all databases to commit the 
t ra.nsaction they have received. 
(b) lf any database replies with a no, the coordinat or asks all databases to abort the 
transaction. 
)I is a low-level solution because the prepare step requires a special modification to the 
database transaction. For examp le, there is an X/Open XA [6] standard that coordinates 
heterogeneous databases to achieve 2PC. The bigges t prob lem with 2PC is that it's not 
performa.nt, as locks can be held for a very long time while waiting for a message from 
the other nodes . Another issu e with 2PC is that the coordinator can be a single point of 
failure, as shown in Figure 12.6. 
Coordinator 
(Wallet Service) 
Prepare 
Crashed X X 
! ~ 
Figure 12.6: Coordinat or crashe s 
time 
Distributed transaction : Try-Confirm / Cancel (TC/C) 
TC!C is a type of compensating tran sactio n [7] that has two steps: 
1. ln the first phase, the coordinator asks all databases to reserve resources for the 
transactio n . 
2. In the seco nd phase, the coordinator collects replies from all databases: 
(a) If all databases reply with yes, the coordinato r asks all databases to confirm the 
operation , which is the Try-Confirm process . 
(b) If any database replies with no, the coordin ator asks all databases to cancel the 
operation , which is the Try-Cancel process . 
It's importan t to note that the two phases in 2PC are wrapped in the same transaction , 
but in TC!C each phase is a separate trans actio n. 
Step 2 - Propose High-level Design and Get Buy -in I 34 7 
-


[Page 349]
TC/ C example 
It would be much easier to explain how TC/C work s wit h a real-world examp le. Suppose 
we want to trnnsfer $1 from account A to account C. Table 12.2 gives a sum mary of how 
TCIC is executed in each pha se. 
Phase Operation A c 
1 Try Balance change: - $1 Do nothin g 
2 Confirm Do nothing Balance change: +$1 
Cancel Balance change: + $1 Do Nothin g 
Table 12.2: TC/C example 
Let's assume the wallet service is the coor dinator of the TC/C. At the beginning of the 
distributed transaction , accoun t A has $1 in its balan ce, and account C has $0. 
First phase: Try In the Try phase , the wallet service , which acts as the coordin ator, 
sends two transaction command s to two databases: 
1. For the databas e that contains account A, the coordinato r starts a local transaction 
that redu ces the balan ce of A by $1. 
2. For the database that contains account C, the coordinator gives it a NOP (no operation). 
To make the example adaptable for othe r scenarios , let's assume the coordinator 
sends to this database a NOP command. The database does nothing for NOP commands 
and always replies to the coordinator with a suc cess message. 
The Try phase is shown in Figure 12.7. The thick line indicates that a lock is held by the 
tran sactio n. 
Coordinator 
(Wallet Service) 
First Phase 
lJPDATE balance 
SET amount=amount-1 
WHERE account='A' 
NOP lock A unlock A ./ Done 
Database C --'-----1.'b,....---NOP----~ò 6....-----ò C'40 C40 
Figure 12.7: Try phase 
Second phase: Confirm If both databases reply yes, the wallet service starts the next 
Confirm phase . 
Account A's balance has already been updated in the first phase. The wallet service does 
not need to chang e its balance here. However, account Chas not yet received its $1 from 
account A in the first phase. In the Confirm phase, the wallet service has to add $1 to 
account C's balance. 
348 I Chapter 12. Digital Wallet 
!I 
Jt 
l~ 


[Page 350]
1l1e Confirm process is shown in Figure 12.8. 
First Phase Second Phase: Confirm 
Coordinator ~c >--------------~ 
(Wallet Service) UPDATE balance 
SEl amountòamount╖ l 
WHERE accountò'A' 
I 
NOP lock A unlock A ./ Done : Confmn: C+$1 ./ Dono 
Database C ~----;'bl----NOP-----ò }----'----<'\-J.. ------ +-\ ~-..._. 
Cz$0 O C-$1 
Figure 12.8: Confirm phas e 
lock C unlock A 
UPDATE balance 
SET amountòamount+l 
WHERE accountò'(' 
Second phase: Cancel What if the first Try phase fails? In the example above we have 
assumed the NOP operation on acco unt C always succeeds, although in practice it may fail. 
For example. acco unt C might be an illegal account, and the regulator has mandated that 
no money can flow into or out of this account. In this case, the distributed transaction 
must be cance led and we have to clean up. 
Because the balance of account A has already been updated in the transaction in the Try 
phase, it is impossible for the wallet service to cance l a completed transaction. What it 
can do is to start another transaction that reverts the effect of the transaction in the Try 
phase, which is to add $1 back to account A. 
Because account C was not updated in the Try phase , the wallet service just needs to 
send a NOP operation to account C's database . 
The Cancel process is shown in Figure 12.9. 
Coordinator 
(Walet SeMce) 
First Phase 
UPDATE balance 
SET amountòamount╖ l 
WHERE accountò'A' 
Second Phase: Cancel 
UPDATE balance 
NOP lock A unlock A X r "''"cl lock C unlock A ./ Done 
Database C ~----<\'---NOP'----òò J)-__ __._ __ '----NOP'----4~~.,_ __ ..___.. 
C.$0 C:SO ~ 
Figure 12.9: Cance l phase 
Comparison between 2PC and TC/C 
Table 12.3 shows that there are many similarities between 2PC and TC/C, but there are 
also differences. In 2PC , all local transactions are not done (still locked) when the second 
phase starts, while in TC/C, all local transa ctions are done (unlo cked) when the second 
phase starts. In other words, the second phase of 2PC is about completin g an unfini shed 
Step 2 - Propose High-level Design and Get Buy-in I 349 


[Page 351]
- --- -.A 
trans action, such as an abo rt or commit, while in TC/C. the seco nd pha se is about using 
a reverse operation to off set Lhe previous transaction result when an error occurs. Tue 
following table summari zes their differences. 
First Pha se Second Phase: success Second Phase: fail 
2PC Local transac tions are Commit aJl locaJ Can cel all local 
not done yet transact ions transa ctions 
All local trans actions Execute new local Reverse the side effect of 
TC/C are co mpleted. eilhcr tran sactions if the already committed 
committ ed or needed lransac tion, or called 
canceled " undo " 
Table 12.3: 2PC v.s. TC/C 
TC/C is also called a rustributed tran saction by compen sation. It is a high-level solution 
because the compensation , also called the "und o," is implemented in the business logic. 
The advantage of this approach is that it is datab ase-ag nostic . As long as a database 
suppor ts transactions , TC/C will work. The disadvantage is that we have to manage the 
details and handl e the complexity of the distributed transactions in the business logic at 
the app licatio n layer. 
Phase status table 
We still have not yet answered the question asked earlier ; what if the wallet service 
.; 
restarts in the middle ofTC /C? When it restarts , all previous operation history might be ~ 
lost , and the system may not know how to recover . tJ 
The solution is simple. We can store the progress of a TC/C as phase status in a transac- _, 
tional database. The phase status includes at least the following information. f
1 
ò The ID and content of a distributed transaction . 
ò The status of the Try phase for each database. The status could be not sent yet, has 
been sent, and response received. 
ò The name of the second phase . It could be Confirm or Cancel. It could be calculated 
using the result of the Try phase . 
ò The status of the second phase . 
ò An out-of-order flag (e:>q)lained soon in the section "out-of-order Execution"). 
Where should we put the phase status tab les? Usually, we store the phase status in the 
database that contains the wallet account from which money is deducted . The updated 
architecture diagram is shown in Figure 12.10. 
350 I Chapter 12. Digital Wallet 


[Page 352]
Transfer Command Ttansfer Command 
Figure 12.10: Phase status table 
Unbalanced state 
Partition 
Info 
Zookeeper 
Have you noticed that by the end of the Try phase , $1 is missing (Figure 12.11)? 
Assuming everythin g goes well , by the end of the Try phase, $1 is deducted from account 
A and account C remains unchanged . The sum of account balances in A and C will be 
, O. which i s less than at the beginning of the TC/C. It violates a fundamental rule of 
accounting that the swn should remain the same after a transaction. 
The good news is that the transactional guarantee is still maintained by TC/C. TC/C com¡
prises several independent local transactions. Because TC/C is driven by application, the 
application itself is able to see the intermediate result between these local transactions . 
On the other hand , the database transaction or 2PC version of the distributed transaction 
was maintained by databases that are invisible to high-level applications. 
There are always data discrepancies during the execution of distributed transactions . The 
discrepancies might be transparent to us because lower-level systems such as databases 
already fixed the discrepancies. If not, we have to handle it ourselves (for example , 
TC/C). 
The unbalanced state is shown in Figure 12.11. 
Step 2 - Propose High-level Design and Get Buy- in I 35 1 


[Page 353]
First Phase Second Phase: Confirm 
Coordinator -l-l>-------------{')--<}-}-D---------1Y------o~ 
(Walle! &rvlce) UPDATE balanc~ 
SET a1T1ount~amoun""l ò l 
NOP-{ >----1--+, -+-
' I 
NOP lock A unlock A Done Confirm C+$1 ./ Done i 
Database C _._ __ """""~f-0 --NOP----~╖c~f-0 --~-c~i---....\---+~-4c~>--1 _ _._J .... 
lock C unlock A 1 
UPDATE balance I 
SET amounlòamount+ l 
WHERE accountò 'C' 
Before TCC start : A+C= S 1 Attor second phase: A.+ c,, $1 
/ 
Money recovery : $1 ~ Money loss: $1 Unbalonced stnte 
Figure 12.11: Unbalanced state 
Valid operation orders 
There are three choices for the Try phase: 
Try phase choices Accoun t A Account C 
Choice 1 -$1 NOP 
Choice 2 NOP +$1 
Choice 3 -$1 +$1 
Table 12.4: Try phase choices 
All three choices look plausible, but some are not valid. 
For choice 2, if the Try phase on account C is successful, but has failed on account A (NOP), 
the wallet service needs to enter the Cancel phase. There is a chance that somebody else 
may jump in and move the $1 away from account C. Later when the wallet service tries 
to deduct $1 from account C, it finds nothing is left, which violates the transactional 
guarantee of a distribut ed transaction. 
For choice 3, if $1 is deducted from account A and added to account C concurrently, it 
introdu ces lots of complications. For example, $1 is added to account C, but it fails to 
deduct the money from account A. What should we do in this case? 
Therefore , choice 2 and choice 3 are flawed choices and only choice 1 is valid. 
Out-of-order execution 
One side effect of TC/C is the out-of-order execution . It will be much easier to explain 
using an example. 
We reuse the above example which transfers $1 from account A to account C. As Figure 
12.12 shows, in the Try phase , the operation against account A fails and it returns a failure 
to the wallet service, which then enters the Cancel phase and sends the cancel operation 
to both account A and account C. 
Let's assume that the database that handles account Chas some network issues and it 
352 I Chapter 12. Digital Wallet 
f 
I 
I 
I 
.# 


[Page 354]
receives the Cancel instru ction before the Try instruction. In this case, there is nothing 
10 cancel. 
lhe out-of-order execution is show n in Figure 12.12. 
First Phase Second Phase: Cancel 
Coordinator -+1~ l:::="------~")--1--<n---------r-¡
C\'lallot SOrvlce) 
. . . 
' . 
Out-<>f-order: Con~cl operation arrived before r òY operation 
Figure 12.12: Out-of-order execution 
To handle out-of-order operations, each node is allowed to Cance l a TC/C without receiv ¡
ing a Try instruction , by enhanci ng the existing logic with the following updates: 
ò The out-of-or der Cancel operatio n leaves a flag in the database indicating that it has 
seen a Cancel operation, but it has not seen a Try operation yet. 
ò The Try operation is enhanced so it always checks whether there is an out-of-order 
flag, and it returns a failure if there is. 
This is why we added an out -of-ord er flag to the phase status table in the "Phase Status 
Table" section. 
Distributed transaction: Saga 
Linear order execution 
There is another popular distributed transaction solution called Saga [8]. Saga is the 
de-facto standard in a microservice archit ecture. The idea of Saga is simple: 
1. All opera tions are ordered in a sequence. Each opera tion is an independ ent tran sac¡
tion on its own databas e. 
2. Operations are executed from the first to the last. When one operation has finished , 
the next operation is triggered . 
3. When an operation has failed , the entir e process starts to roll back from the current 
operation to the first operation in reverse order, using compensating transac tions . 
So if a distributed transa ction has n opera tions, we need to prepare 2n operatio ns: 
n operations for the normal case and anoth er n for the compensating transaction 
during rollback. 
It is easier to und erstand this by usin g an example. Figure 12.13 shows the Saga workflow 
to transfer $1 from account A to account C. 111e top horizontal line shows the normal 
Step 2 - Propo se High-level Design and Get Buy-i n I 353 


[Page 355]
order of execu tion. 111e two ver tical lin es show whf\ t the sys tem sh ould do w hen there 
is an error . When it encou nt ers f\n error, th e transfe r operatio ns arc rolled back and the 
client receives an erro r message . J\s wc men I ion eel in th e "Valid operrllion orders" sec tion 
on page 352, we have to put the clcdu clion operati on b efo re the additi on operation. 
Start Gr--~~c_+..,..$_1~╖-----0 Success 
Error Error 
A+$1 C-$1 
A+$1 
Error 
Error 
Figure 12.13: Saga workflow 
How do we coordina te the operations? There are two ways to do it: 
1. Choreogra phy. In a microservice architecture, all the services involved in the Saga 
distributed transaction do their jobs by subscribing to other services' events. So it is 
fully decentralized coordinati on. 
2. Orchestration. A single coordinator instructs all services to do their jobs in the cor¡
rect order. 
The choice of which coordination model to use is determined by the business needs and 
goals. The challen ge of the choreography solution is that services communicate in a fully 
async hronous way, so each service has to maintain an inter nal state machine in order to 
understand what to do when other services emit an event. It can become hard to manage 
when there are many services. The orchestration solution handles complexity well, so it 
is usually the preferred solution in a digital wallet system. 
Comparison between TC/C and Saga 
TC/C and Saga are both application -level distrib uted transactions . Table 12.5 summarizes 
their similarities and differences. 
354 I Chapter 12. Digital Wallet 


[Page 356]
----TC/C Saga 
Compensating action In Cancel phase In rollback phase 
Central coordi nati on Yes Yes (orchestration mode) - -Operation execution any linear order 
Parallel execution Yes No (linear execut ion) possibility 
Could see the partial 
inconsistent status Yes Yes 
Application or database Application Application logic 
Table 12.5: TC/C vs Saga 
Whjch one should we use in practice ? The answer depends on the latency requirement. 
As Table 12.5 shows , operations in Saga have to be executed in linear order, but it is pos¡
sible to execute them in parallel in TC/C. So the decision depends on a few factors: 
1. If there is no latency requirement , or there are very few services, such as our money 
tr an sf er example, we can choose either of them. If we want to go with the trend in 
microservice architecture, choose Saga. 
2. If the system is latency-sensitive and contains many services/operations, TC/C might 
be a better option . 
Candidate : To make the balance transfer transactional , we replace Redis with a rela¡
tional database, and use TC/C or Saga to implement distributed transactions . 
Interviewer : Great work! The distributed transaction solution works , but there might 
be cases where it doesn 't work well. For example, users might enter the wrong operations 
al the application level. In this case, the money we specified might be incorrect. We need 
a way to trace back the root cause of the issue and audit all account operations. How can 
we do this? 
Event sourcing 
Background 
ln real life, a digital wallet provider may be audited. These external auditors might ask 
some challenging questions, for examp le: 
1. Do we know the account balance at any given time? 
2. How do we know the historical and current account balances are correct ? 
3. How do we prove that the system logic is correct after a code change? 
One design philosophy that systemat ically answers those questions is event sourcing, 
which is a technique developed in Domain-Driven Design (DDD) (9). 
Step 2 - Propo se High-level Design and Get Buy-in I 355 
-


[Page 357]
Definition 
TI1ere are four imp orl anl lerms in event sourcing. 
1. Command 
2. Event 
3. Stale 
4. State machine 
Command 
A command is the intended act ion from the outsid e world. For examp le, if we want lo 
transfer $1 from clien t A to client C, this money transfer request is a comma nd. 
In event sourcing, it is very imp01tant that everything has an order . So comma nds are 
usually put into a FIFO (first in, first out) queue . 
Event 
Command is an intention and not a fact because some comman ds may be invalid and 
cannot be fulfilled. For example, the tran sfer opera tion will fail if the acco unt balance 
becomes negative after the transfer . 
A command must be validate d before we do anything about it. Once the command passes 
the validation, it is valid and must be fulfilled. The result of the fulfillm ent is called an 
event. 
There are two major differen ces between command and event. 
1. Events must be exec uted because they represent a validated fact. In practice , we 
usually use the past tense for an event. If the command is "transfer $1 from A to C", 
the corresponding event would be "transferred $1 from A to C". 
2. Commands may contain randomness or 1/0 , but events must be deterministic . Events 
repres ent historical facts. 
There are two import ant properties of the event generation process. 
1. One command may generate any number of events. It could generate zero or more 
events. 
2. Event generation may contain randomn ess, meaning it is not guaranteed that a com¡
mand always generates the same event(s). The event generation may contain external 
1/0 or random numbers . We will revisit this property in more detail near the end of 
the chapter. 
The order of events must follow the order of commands. So events are stored in a FIFO 
queue, as well. 
------- ------ --- -- ---- - - -- - - -
356 I Chapter 12. Digital Wallet 
-


[Page 358]
State 
. tate i what will be changed when an event i applit"d. In thC' ' \\r t systr m. stntr is th l' 
balances of all client accounts. which can be rcprt'. ented with n mnp dntn struct ltl' <'. 'lh c 
ke\ i the account name or ID. and the value i the account balance. Key-vnlue storr s nrC' 
usuallv used to store the map data tructure . The relational dntabase can also b vit'w cd 
a 3 key-value tore . where keys are primary ke. nnd alues are tnble rows. 
State machine 
A state machine drh"es the event ourcing proce . It ha two major functions. 
Validate commands and generate even ts. 
2 Apply e\-ent to update state. 
úyent ourcing requires the behavior of the state machine to be deterministic. Therefore, 
the tate machine itself should never contain any randomness . For example , it should 
nt'\╖er read anything random from the outsid e using 1/0 , or use any random numbers. 
\\'hen it applies an event to a state, it should always generate the same result. 
figure 12.14 shows the static view of event sour cing architecture. The state machine is 
responsible for converting the command to an event and for applying the event. Because 
state machine has two primary functi ons, we usuall y draw two state machines, one for 
,-aJ.idating comman ds and the other for applying events . 
Command 
State 
Machine 
Va!'idate Event 
Figure 12.14 : Static view of event sourcing 
State 
Machine 
If we add the time dimension, Figure 12.15 shows the dynamic view of event sourcing. 
The system keeps receiving commands and processing them, one by one. 
Step 2 - Propose High-level Design and Get Buy-in I 357 
-


[Page 359]
Figure 12.15: Dynamic view of event sourcing 
Wallet service example 
State 
Time 
For the wallet service, the commands are balance tran sfer requests . These commands are 
put into a FIFO queue . One popu lar choice for the command queue is Kafka [10). The 
command queue is shown in Figure 12.16. 
I A -$1╖ c~ in - I A -$1- cJ j A -$1- sJ B-out --o 
Command Queue 
Kafka 
Figure 12.16 : Command queue 
Let us assume the state (the account balance) is stored in a relational database. The state 
machine examines each command one by one in FIFO order. For each command, it checks 
whether the account has a sufficient balance. If yes, the state machine generates an event 
for each account. For example, if the command is "A -+ $1 -+ C", the state machine 
generates two events : "A:-$ 1" and "C:+$1". 
Figure 12.17 shows how the state machine works in 5 steps . 
1. Read commands from the command queue. 
2. Read balance state from the database. 
3. Validate the command. If it is valid, generate two events for each of the accounts. 
4. Read the next event. 
5. Apply the event by updating the balance in the database. 
358 I Chapter 12. Digital Wallet 
~I 
.!fr\ 


[Page 360]
Command Queue 
Client - --1 ... ~1 A -$1ò er in-+ I A ~~1╖ cl I A -~~╖ al A -$1ò D 
Valldote 
Commend s 
I I 
I I 
I I I 
' 
I I I 
' 
I I I 
' 
I I I 
I I I I 
' 
I I I 
I I I I 
Event Queue 
Figure 12.17: How state machine works 
@ Update 
⌐Rea~ 
Apply 
- - - -events 
State 
Machine 
Reproducibility 
The most important advantage that event sourcing has over other architectures is repro¡
ducibility. 
Jn the distributed transaction solutions mention ed earlier, a wallet service saves the up¡
dated account balance (the state) into the databa se. It is difficult to know why the account 
balance was change d. Meanwhil e, historical balance information is lost during the up¡
date operation. In the event sourcing design, all changes are saved first as immutable 
history. The database is only used as an updated view of what balance looks like at any 
given point in time . 
We could always reconstruct historical balance states by replaying the events from the 
very beginnin g. Because the event list is immutable and the state machine logic is de¡
terministic, it is guaran teed that the historical states generated from each replay are the 
same. 
-
Figure 12.18 shows how to reproduce the states of the wallet service by replaying the 
events. 
Step 2 - Propose High-level Design and Get Buy-in I 359 


[Page 361]
Command Queue 
Event Queue 
A: 
B: $4 
C: $3 
D: $2 
I 
I 
I 
I 
B 
I 
I I 
I 
I I 
I I 
I 
I 
I 
I 
I 
8 
I I 
I I 
I I 
I I 
I I 
I I 
I I 
I I 
I I 
8 
I 
I \ 
I \ 
I 
I 
I 
I 
I 
I 
B: $5 
C: $4 
D: $2 
\ 
\ 
\ 
\ 
\ 
\ 
\ 
Historical State Historical State Historical State 
Figure 12.18: Repro duce states 
Reproducibility helps us answe r the difficult questions that the auditors ask at the begin¡
ning of the section. We repeat the questions here. 
1. Do we know the account balance at any given time? 
2. How do we know the historical and current account balan ces are correct? 
3. How do we prove the system logic is corr ect after a code change? 
For the first question, we could answer it by replaying events from the start , up to the 
point in time where we would like to know the account balance. 
For the second question, we could verify the correctness of the account balance by recal¡
culati ng it from the event list. 
For the thir d question, we can run different versions of the code against the events and 
verify that their results are identical. 
Because of the audit capability, event sourcing is often chosen as the de facto solution for 
the wallet service. 
Command-query responsibility segregation (CQRS) 
So far, we have designed the wallet service to move money from one account to another 
efficiently. However, the client still does n ot know what the account balan ce is. There 
needs to be a way to publish stat e (balance information) so the client, which is outside 
of the event sourcing fram ework, can know what the stat e is. 
Intui tively, we can create a read-only copy of the database (historical state) and share 
360 I Chapter 12. Digital W allet 
. .... 


[Page 362]
---╖╖ ╖╖╖╖-╖-----. ....,.. 
it with the outside world . Event sourcing answers t.his question in A slightly different 
\\'I)' 
Rnthrr than publishing the slate (balance informati on), event sourcing publish es all lh e 
m-nt3 . The externa l world could rebuild any customized sltllc itself. This design phil os-
ophy is called CQRS [ 11]. 
In cQRS. there is one slate machine respo nsible for the write part of the state, but ther e 
('l.O be many read -only s tate machines, which are responsible for building views of the 
states. '!hose views could be used for queries . 
These read-only sta te machines can derive different state representati ons from the event 
queue. For exampl e, clients may want to know their balances and a read-only state ma¡
dune could save state in a database to serve the balance query. Another state machine 
could build state for a specific time period to help investigate issues like possible double 
charges. The state information is an audit trail that could help to reconcile the financial 
records. 
The read-only state machines lag behind to some extent, but will always catch up. The 
architecture design is eve ntuall y consistent. 
figure 12.19 shows a classic CQRS architecture. 
Client 
Write Path 
Command Queue 
in--+ I A ~~1╖ cl \A -~~╖ el ~-__, 
I 
I I 
I I 
' ' ' 
I 
' 
I 
I 
I 
I 
' 
query 
I ò I 
' ' 
I 
I I 
' ò I I 
I I 
I I 
I I 
Even t Queue 
Read Path 
Query 
Service 
Figure 12.19: CQRS architectu r e 
State 
A; SS 
B: S4 
C: $3 
O: $2 
t 
@Upd ate 
jJ 
@ Read 
Publish Events 
9 
Rebuild 
State 
t 
A: SS 
B: ╡ 
C; S3 
0 : S2 
Historical State 
Step 2 - Propose High-level Design and Get Buy-in I 361 
-


[Page 363]
Ca ndidate : In thi s design. we use eve nt sourcing architc ctur r lo make lh r w hulr sys tem 
rcprod11 c1blc. All valid busi ness reco rd s arc save d in an immut ahlr eve nt qu eue which 
could be used for corre ct ncss verifica tion . 
Interviewer : 111at 's greal. Bui the event sourcing architecture you prop osed only han¡
dks one event at a time and it needs to communi cate with several external sys tems. Can 
we make it faster ? 
Step 3 - Design Deep Dive 
In this section, we dive deep int o techniqu es for achieving high p erforma nce, reliability, 
and scala bility. 
High-performance event sourcing 
In the earlier example, we used Kafka as the command and event store, and the databas e 
as a state sto re. Let's explore some optimizations. 
-
File-based command and event list 
The first optimization is to save command s a nd even ts to a local disk, rather than to 
a remote store ill<e Kafka. This avoids transit time across the network. The event list 
uses an append-only data structure. Appending is a seque ntial write operation, which is 
generally very fast. It works well even for magnetic hard drives because the operating 
system is heavily optimized for sequential reads and writes. According to this article [12], 
sequential disk access can be faster than random memory access in some cases. 
The second optimi zation is to cache recent commands and events in memory. As we 
explained before, we process commands and events right after they are persisted. We may 
cache them in memory to save the time of loading them back from the lo cal disk. 
We are going to explore some implementation details. A techniqu e called mmap [13] is 
great for implementing the optimiza tions mentioned previously. Mmap can write to a 
local disk and cache recent conte nt in m emory at the same time. It maps a disk file to 
memory as an array. The operat ing system caches certain sections of the file in memory 
to accelerate the read and write operations. For append-only file operations, it is almost 
guaran teed that all data are saved in memory, which is very fast. 
Figure 12.20 shows the file-based command and event storage. 
362 I Chapter 12. Digital Wallet 
'╖ 
:ro 


[Page 364]
' 
' ' 
. . . 
mE'mOC) I 
Event List 
. . 
mmap mmap 
. 
' 
. 
' ' 
. . . . 
' ' 
DD 
Command Event 
File File 
disk 
Figure 12.20: File-based command and event storage 
File-based state 
In the previous design, state (balance information) is stored in a relational database . In a 
production environment, a database usually runs in a stand-alo ne server that can only be 
accessed through networks. Similar to the optimizations we did for command and event, 
slate information can be saved to the local disk, as well. 
More specifically, we can use SQLite (14], which is a file-based local relatio nal database 
or use RocksD B [ 15], which is a local file-based key-value store. 
RocksDB is chosen because it uses a log-structure d merge-tree (LSM), which is optimized 
for write operations. To improve read performance, the most recent data is cached. 
figure 12.21 shows the file-based solution for command , event, and state. 
Step 3 ╖ Design Deep Dive I 363 


[Page 365]
memory 
Command List 
0- I 
Event List 
ò 
Rocks DB 
Stale In memory 
cache 
mmap mmap 
I 
I 
I 
I I 
D D D 
Command Rocks DB Event 
File File File 
disk 
Figure 12.21: File-based solution for command , event, and state 
Snapshot 
Once everything is file-based, let us consider how to accelerate the reproducibility pro¡
cess. When we first introdu ced reproducibility , the state machine had to process events 
from the very beginning, every time. What we could optimize is to periodically stop the 
state machine and save the current state into a file. This is called a snapshot. 
A snapshot is an immutable view of a historical state. Once a snapsho t is saved, the state 
machin e does not have to restart from the very beginning anymore. It can read data from 
a snapshot, verify where it left off, and resume processing from the re. 
For financial applications such as wallet service , the finance team often requires a snap¡
shot to be taken at 00:00 so they can verify all transactions that happened during that 
day. When we first introduced CQRS of event sourcing, the solution was to set up a read¡
only state machine that reads from the beginning until the specified time is met. With 
snapshots , a read-only state machine only needs to load one snapsho t that contains the 
data. 
A snapshot is a giant binary file and a common solution is to save it in an object storage 
-
I 
solution, such as HDFS (16]. ╖i~ 
Figure 12.22 shows the file-based event sourcing architecture. When everyth ing is file-
based, the system can fully utilize the maximum I/O throughput of the comput er hard-
ware. 
364 I Chapter 12. Digital Wallet 


[Page 366]
╖---
.. ' 
-
' .. I 
\\òòI I"' 
J 
l\\\\\t4~ 
... ~ l ""''U) \)0 bot~ 
~-. l l\\."\)1\.\ (\I tol<'4~ 
Candidate : \\╖e could refa :tor the de~crn f e\ nt , 'u.rdng so t hl' command list. eve nt 
hsl state. and snapsh t an- all '~ in file╖ Ev-ent soutting architecture processes the 
e\e.Dt list in a linear manner. which fits well int the desi_.~11 of hnrd disks and operati ng 
system cache. 
interviewer: The performance of the local file-based solution is better than the sys tem 
that requires accessing data from remote "aft.a and data.bases. However. there is another 
problem: because data is saved on a local disk a sen-er is now stateful and becomes a 
single point of failure . How do we impro'-e the reliability of the system? 
Reliable high-performance event sourcing 
Before we explain the solution. let's examine the parts of the system that need the relia¡
bility guarantee. 
Reliability analysis 
Conceptually, e\-erythin g a node does is around two concepts; data and computation. As 
long as data is durabl e.. it╖ s easy to recm-er the comp utational result by runnin g the same 
c.ode on another node. This means we only need to worry about the reliability of data 
because if data is lost, it is lost foreYer. The reliability of the system is mostl y about the 
reliability of the data. 
There are four types of data in our system. 
1. File-based command 
2. File-based event 
3. File-based state 
4. State snapsho t 
Let us take a close look at how to ensure the reliability of each type of data. 
Step 3 - Design Deep Dive I 365 


[Page 367]
Lale and snaps hot can always he regenera ted by replaying thr event list. To improve 
the reliability of state and s napshot, we just nrc<l to ensure the event l ist has s trong 
re liability. 
Now Jet us examine command. On thr face o[ it , event is ge ncrnlcd from command. We 
might think prov iding a s t rnng reliabilit y guaran tee for command should be sufficient. 
111is see ms to be cor rect <l t 11rsl glance, bul it misses somclhing important. Event gener¡
alion is not guaranleed to be determin istic, and also il may contain ra ndom factors such 
as rand om numb ers, externa l 1/0, clc. So command cannot guara ntee reproducibility of 
event s. 
Now it 's time lo lake a close look at event. Even t represents historical facts that int roduce 
changes lo the s tate (account balance). Eve nt is immutable a nd can b e used t o rebuild 
the slate. 
From this anal ysis, we conclude that event data is the o nl y o ne Lh al r equir es a high¡
reliabilily guarantee . We will exp lain h ow to achieve this in the next section. 
Consensus 
To provide high r eliability, we need to replicate the event list acros s multiple nodes. Dur ¡
ing the replica tion pro cess, we have to guara ntee the following pro perties. 
1. No data loss. 
2. The relative order of data with.in a log file remains the same across nodes. 
To achieve thos e g uaran tees, consensus-based r eplication is a good fit. The consensu s 
algori thm makes sure that multiple nodes reach a consensus on what the e vent list i s. 
Let's use the Raft [17] consensus algorithm as an exam ple. 
The Raft algo rithm guaran tees th at as long as more than half of the nodes are on line, the 
append-only lists on them h ave the same data. For example, if we h ave 5 nod es and use 
the Raft algorithm to s ynchronize their data, as long as at leas t 3 (more than ! ) of the 
nodes are up as Figure 12.23 shows, the sys tem can still work properly as a wh ole: 
0 0 0 0 0 
Up Up Up Down Down 
Figure 12.23: Raft 
A n ode can have three different roles in the Raft algorithm. 
1. Leader 
2. Candidate 
3. Follower 
We can find the implementation of the Raft algorithm in the Raft paper. We will only 
cover the high l evel concepts here and not go into detail. In Raft, at m ost one node is 
the leader of the cluster and the remainin g nod es are followers. The leader is respon-
366 I Chapter 12. Digital Wallet 


[Page 368]
sible for receivinp; external co mmands and replicating doll\ rrliRhl ' 1wrnss node's in 1 lw 
cluster. 
With the Raft algorithm , the system is reliable as long ns tlw majorit y of lhr nnclcs l\l'tò 
operational . For example. if there are 3 nodes in the cluster. it could tolrrntc tlw fnilme 
of l node. and if there are 5 nodes. it can tolerate the failure of 2 nodes . 
Reliable solution 
With replication. there won 't be a sing le point of failure in our file-based event sourcing 
architrc ture. Let's take a look at the implementation details. Figure 12.24 shows thr 
event sourcing architecture with the reliability guarantee . 
Follower 
ò --1-+ -.i Commands 
-
Follower 
I 
I 
I Events ~╖ l !_.er t . - -! ~ ' ""' I 
Raft > , - - - - - - -- - - - - - - - - - : 
I 
I 
I 
I 
_j_D-LJ.-auery-ò 
' ╖, , I 
I 
--- _,- I 
Raft : 
f : 
Even~- to:9J _[ 
Raft Node Group -------------
------ - ----Write ---------....:...0--- Read---: 
I 
Figure 12.24: Raft node group 
ln Figure 12.24, we set up 3 event sourcing nodes . These nodes use the Raft algorithm to 
synchronize the event list reliably. 
The leader takes incoming command requests from external users , converts them into 
events, and appends events into the local event list. The Raft algorithm replicates newly 
added events to the followers. 
All nodes, including the followers, process the event list and update the state . The Raft al¡
gorithm ensures the lead er and followers have the same event lists, while even t sourcing 
guarantees all states are the same , as long as the event lists are the same. 
A reliable system needs to handle failures gracefully, so let's explore how node crashes 
are handled. 
If the leader crashes, the Raft algorithm automatically selects a new leader from the 
remaining healthy nodes. This newly elected leader takes responsibility for accepting 
Step 3 - Design Deep Dive I 367 


[Page 369]
comma nds from extC'rnal user s. It is grnmrntC'ed that the clus ter as a whole can provide 
con tinu ed service when a node goes down . 
When the lrader cras hes, it is possib le that the cras h h appe ns befo re the command list 
is converted lo even ts. In this case, the client would notice the issue eith er by a timeout 
or by receiving an error response. 1l1c cli<:'nt needs lo resend Lhe same command to the 
newly elected leader. 
In cont ras t, follower crashes arc much easier to handl e. If a follower crns hcs, reques ts 
sent to it will fail. Raft hand les failure s by retrying indefinitely unti l the crash ed node is 
restar ted or a new one replaces il. 
Candidate : In this design, we use the Raft consensus algorithm lo replicate the event 
list across multipl e nodes. 1l1e leader r eceives command s and repli cates eve nts to other 
nodes . 
Interviewer : Yes, the sys tem is more reliable and fault -tolerant. However, in order to 
handl e 1 million TPS, one server is not eno ugh. How can we make the system more 
scalab le? 
Distributed event sourcing 
In the previous section , we explained how to implement a reliabl e high -performance 
event sourcing architecture. It solves the reliability issue , but it has two limita¡
tions . 
1. When a djgital wallet is updated , we want to receive the updated result immediate ly. 
But in the CQRS design , the request/response flow can be slow. This is because a 
client doesn 't know exactly when a digital wallet is updated and the client may need 
to rely on periodic polling. 
2. The capacity of a single Raft group is limited . At a certain scale , we need to shard 
the data and implement distributed transactions. 
Let's take a look at how those two problems are solved. 
Pull vs push 
In the pull model , an external user periodically polls execution stat us from the read -only 
stat e machine. This model is not real-time and may overload the wallet service if the 
polling frequency is set too hlgh . Figure 12.25 shows the pulling model. 
368 I Chapter 12. Digital Wallet 
-
I 
I 
I 
I 
, ~' 


[Page 370]
----- Perrodically query for the latest stAtus 
Follower 
I Evt.~.l. 1╖.0-LJ 
Raft - -- -- --- -- - --- : 
I 
I 
!.cru 
_. I 
'-------------'F---"'-----~-~ : 
------ I 
R~ : 
Ev!nt:. ~J.-~.cru 
< ... - ' 
Raft Node Group╖--------------
Follower 
f'4----------- Wrlte ----------1~-Read--+: 
I 
Figure 12.25: Periodical pulling 
The naive pull model can be improved by adding a reverse proxy [18] between the ex¡
ternal user and the event sourcing node. In this design, the external user sends a com¡
mand to the reverse proxy, which forwards the command to event sourcing nodes and 
periodically polls the execution status. This design simplifies the client logic, but the 
communication is still not real-time. 
Figure 12.26 shows the pull model with a reverse proxy added. 
Step 3 - Design Deep Dive I 369 
╖-


[Page 371]
ò ....... 
' 
, 
' ' ' ' Command ò 
Reverse 
Proxy 
Periodically query for the latest status 
.----------- ------ - --
Follower Even ls 
Rafi 
........ _______ _ 
' 
i.O I Commands I 
Rall 
Follower 
t : 
E""'.'., ~J _l.()-LJ 
< 
Raft Node Group ........ ___ .. _____ .... -
' - --------- Write-------- - - Read----..! 
Figure 12.26: Pull model with reverse proxy 
' ' 
Once we have the reverse proxy , we could make the respon se faster by modifying the 
read-only state machin e. As we mentioned earlier, the read-only s tate machine could 
have its own behavior. For example, one behavior could be that the read-on ly state ma¡
chine pushes execu tion status back to the reverse proxy, as soon as it receives the event. 
This will give the user a feeling of real-tim e response. 
Figure 12.27 shows the push-based mod el. 
370 I Chapter 12. Digital Wallet 


[Page 372]
Push the 181est status to reve~e proxy In reet-tlme 
' 
Follower j,.()-LJ 
.~ ,_.,.-!-~Commands i "-u-~ .~-~ ' 
: ' 
' ' ' Command : 
' Reverse 
Pro>cy Follower 
I I 
I 
I 
I 
Raft : 
.L ~J-~ .cru 
' < ;_> : 
Raft Node Group╖------- --- ---
' I 
I 
I 
I 
I 
' I 
I 
I 
I 
I 
I 
1'4----------- Write ------ ---..-- Read --l 
Figure 12.27: Push model 
Distributed transaction 
Once synchronous executio n is adopted for every event sourcing node group , we can 
reuse the distribu ted transaction solution, TC/C or Saga. Assume we partition the data 
by dividing the hash value of keys by 2. 
Figure 12.28 shows the updat ed design . 
Step 3 - Design Deep Dive I 371 


[Page 373]
... 
.-ii 
Reverc;e 
Proxy 
Response 
" 
:\ t : ' o-: 
;╖ 
Push the tot1>crt qfot u!I to mv1>rs1> proxy 1n rf':ll trmf' 
Follower 
0 _i] 
-╖╖ Raft 
rr;mmoodò I Q I + .. ~I 
Raft 
I ò I ~E_v_en~ts_, òò f--0 ..... f .0--LJ 
-╖╖ 
Follower 
Command ; Raft Node Group ' - - - - -- ╖ ╖ - ò 
TCC/Saga 
Coordinator 
Reverse 
Proxy 
- --------- Write -------- -..-- Read 
'╖ -ò - -.ò.ò -- ò -- . -. --- - --- ---- -. - ---. ~~~l?.!1_ ~ _(~~~?-~~t-~! - .. --.. ---. ------. -... ----. ----.. -. 
Partition 2 (account C) 
...-------------- ----- -, ' 
Follower 
' ' ' 
E}-0--El L J . .o--u 
R!tt . ---------╖ --. -╖╖ - i 
' ' 
_)D-
'----------'1~-"'---=--_-_-_-_-_-_~-=' : 
Raft : 
f I 
.,.,., ~o--uJ -~ .o--u 
Raft Node Grou~------ -- --------╖ : 
Follower 
' ' 
: .. 1----- ----W rrte ---------~Read___.; 
' : 
~------Push the latest status to reverse proxy in real-time ------' 
~---------- -- ---------------- -- -------- - --------------- -- -------------------- -- ----- -----
Figure 12.28: Final design 
Let's take a look at how the money tran sfer works in the final distribut ed event sourcing 
architec ture. To make it easier t o understand, we use the Saga distribut ed tran saction 
model and only explain the happy path with out any rollback. 
The money transfer operation contains 2 distribut ed operations: A:-$1 and C:+$ 1. The 
Saga coordinator coordinates the execution as shown in Figure 12.29: 
372 I Chapter 12. Digital Wallet 
.1--


[Page 374]
..... 
l. User A sends a distributed lran sac t.ion lo th e Saga coo rdin ator. It conta ins lwo op¡
erations: A:- $1 a nd C:+$ 1. 
z. Saga coordina tor crea tes a record in the phase status table to trace the sta tus of a 
transact ion. 
3. Saga coordinator exami nes the order of opera tion s and determines that it needs to 
handle A:- $1 first. The coord inator sends A:-$ 1 as a command to Partition 1, which 
contains account A's information . 
4. Partition l 's Raft leader receives the A- $1 command and stores it in the command 
list. It then validates the co mmand. If it is valid , it is converted into an event. The 
Raft consensus algorithm is used to synchronize data across different nodes. The 
event (deducting $1 from A's account balan ce) is executed after synchronization is 
complete. 
s. After the event is synchronized, the event sourcing framework of Partition 1 syn¡
cluonizes the data to the read path usin g CQRS. The read path reconstructs the state 
and the status of executio n. 
6. 1he read path of Partition 1 pushes the status back to the caller of the event sourcing 
framework, which is the Saga coordinator . 
7. Saga coordinator receives the success status from Partition 1. 
8. The Saga coor dinator creates a record, indicating the operation in Partition 1 is suc¡
cessful, in the phase status table . 
9. Because the first operation succeeds, the Saga coordinator executes the second op¡
eration, which is C:+$ 1. The coordinator sends C:+$1 as a command to Partition 2 
which contains account C's information . 
10. Partition 2's Raft leader receives the C:+$1 command and saves it to the command 
list. If it is valid, it is convert ed into an event. The Raft consensu s algorithm is used to 
synchronize data across different nodes. The even t (add $1 to C's account) is exec uted 
after synchronization is complete. 
11. After the event is synchroni zed, the event sourcing framework of Partit ion 2 syn¡
chronizes the data to the read path using CQRS. The read path recons tructs the state 
and the status of exec ution . 
12. The read path of Partition 2 pushes the stat us back to the caller of the event sourcing 
framework, which is the Saga coo rdin ator. 
13. The Saga coordinator recei ves the success status from Partition 2. 
14. The Saga coordinator creates a record , indicating the operation in Partition 2 is suc¡
cessful in the phase status table. 
15. At this time, all operations succeed and the distribut ed transacti on is completed. The 
Saga coordinator respond s to its caller with the result. 
Step 3 - Design Deep Dive I 373 


[Page 375]
( o) Pu~11 the latPst stntus to reverso proxy In real-time 
Reverse 
r 
Proxy Follower 
' ' 
; 1) 4 
I 
[ Commands] 
0 
Response 
o i ,+._to-L? J_ :.o╖u ò 
@ Raft « 
f : 
j0-{:J 
' 
I Events╖ ~-0-__ J 
(4) Raft . - ò -. 
Follower 
I'""" f--~J ~ .o-u ':3"' ' ., , ' ~) .. -" I 
Command : Raft Node Group 
i I :::,: ' ' ' 
TCC/Saga 
Coordinator 
, ' 
Reverse 
Proxy 
,- --------- Write -------- _____.,; .. - Read - ò ! 
' ' 
: ____ -- --------- ------------------- - ~~-~l ~i?_n_ ~ -(~99_0_~~~~! - --------------------------------__ : 
------------------------------------- -----------------------------------¡r------------- ---' ' Partition 2 (account C) 
Follower 
I Commands ~a-.s--o--u _ 
@) Raft - -@ - - -
Follower I E,!,., .f---0-uJ l.0-LJ 
----Raft Node Group ╖-
' 
- ----- ---- Write ----------ti~-Read- ! 
' 
~------1 12 Push the latest status to reverse proxy in real-time --- ----' 
' ' ~ -- - -- --- -- - - - - - - ----------- - - - ---- - ---- -- - ---- - - - -~- --- - --- - -- - - -- - -- - --- - -- - --- --- - -- - -! 
Figure 12.29: Final design in a numbered sequence 
Step 4 - Wrap Up 
In this chapter , we designed a wallet service that is capable of processing over 1 million 
payment commands per second. After a back-of-the-envelope estimation , we concluded 
that a few thousand nodes are required to support such a load. 
In the first design, a solution using in-memory key-value stores like Redis is proposed. 
The problem with this design is that data isn't durab le. 
374 I Chapter 12. Digital Wallet 
f' 


[Page 376]
Jn the second design. the in-memory rar hr is rcpli:H'<'d hy trnn sar lio nal <IAtahase<1 fn 
support multiple nodes. different trnn sactional protocols s uch as 2PC. TC !C , ancl <\aRa 
arf' propose d. 111c ma.in issue with transa ction hC\scci solut ions is th at w e ca nn ot ron<lurt 
A delA nudit easily. 
rxt. event sourcing is introduced. We first implemented event sourcing usin g an cxter¡
nRI datRhftse and queu e. but it's no t pcrfor manl. We improved performan ce by stori ng 
command. event. and state in a local node. 
A single node means a single point of failure. To increase the system reliabilit y, we use 
the Raft consensus algo rithm to replicate the event list onto multiple nodes. 
The last enhan cement we made was to adopt the CQRS feature of event sourcin g. We 
added a reverse proxy to change the asynchronous event sour cing framework lo a syn ¡
chronous one for external users. The TC/C or Saga protocol is used to coordinate Com¡
mand executions across multipl e node groups. 
Congratulations on getting this far! Now give yourself a pat on the back . Good job! 
Step 4 - Wrap Up I 375 


[Page 377]
Chapter Summary 
step I 
functional req __ money transfer b e¡
twee n t wo acco unts 
l million TPS 
reliability 99.993 
non-[un clion al req 
supp ort transactions 
supp ort reproducibility 
api design - - wallet/ba lance_tran sfer 
in-memory s hardin g solution 
database shardi.ng 
try-co nfirm cancel 
out-o f-order exec uti on 
event sourcing 
high-pe rformance eve nt sourcing 
step 3 reliable event ourcing 
< 
pull vs push 
distri buted even t sourcmg 
d1slrtbut ed tran sac tion 
step 4 -- wrap up 
37 6 I Chapter 12. Digital Wallet 
l. 


[Page 378]
-
Reference Material 
I l ] Tra nsRct1onal ~uarnntcrs. htt ps://dors.orncl <' .com/r d/E 17275 01 lht ml/pro~rnmm<" 
r refr r<'ncr/rcp tran s.html. 
12) TPC-E Top Prk r /PcrfomlRnc e Results . http: //tpc .orp;/tpcc/ resultct /tpce_pri ce _pe r 
f_ resu ltsS.asp ?rrsulttyp e= all. 
('] r O 4217 CURRENCY CODES. http s://cn.wikipcdia .org/ wiki/ISO _ 4217. 
1-t] Apache Zoo Keeper. https ://zookeepc r.apache .org/. 
f5] Martin Kleppmann . Designing Data-Intensive Applications. O'Reilly Media , 2017. 
[ti] X Open XA. https ://en.wikipedia.org /wiki/X /Open_XA. 
[-] Compen sating transaction . https ://en.wikipedia.org/wiki/Compensating_transacti 
on. 
[8) AGAS. HectorGarcia-Mo lina . http s://www.cs.cornell.edu /andru /cs711 /2002fa /re 
ading/sagas.pdf. 
(9) Eric Evans. Domain-Driven Design: Tackling Complexity in the Heart of Software. 
Addison-Wesley Professional, 2003. 
(IO] Apache Kafka. http s://kafka.apache .org/. 
( 11] CQRS. https: //martinfowler.com/bliki /CQRS.html. 
[12) Comparing Random and Sequential Access in Disk and Memory . https ://delivery 
images.acm.org/10.l 145/1570000/1563874/jacobs3.jpg. 
(13) mmap. https: //man 7 .org/linux /man-page s/man2 /rnmap.2.html . 
(14] SQLite. https: //www.sqlite.org /index.html. 
[ 15) RocksDB. http s:/ /rocksdb .org/. 
[16) Apache Hadoop . https: //hadoop. apache.org/ . 
[ 17) Raft. https ://raft.github.io /. 
[ 18] Reverse proxy. https: // en. wikipedia. org/wiki /Reverse _proxy. 
Reference Material I 377 


[Page 379]



[Page 380]
13 Stock Exchange 
In this chapter. we design an electronic stock exchange system. 
The basic function of an exchange is to facilitate the matching of buyers and sellers ef¡
ficiently. 1h is fundamental functi on h as not changed over time. Before the rise of com¡
puting, people exchan ged tangible goods by bartering and shoutin g at each other to get 
matched. Today, orders are processed silently by supercomputers, and people trad e not 
only for the exchange of prod ucts, but also for speculation and arbitr age. Technol ogy 
has greatly changed the landscape of trading and exponentially boosted electroni c mar¡
ket trading volume. 
When it comes to stock exchanges, most people think about major market players like 
The New York Stock exchange (NYSE) or Nasdaq, which have existed for over fifty years . 
Jn fact, there are many other types of exchan ge. Some focus on vertical segmentation 
of the financial industry and place special focus on technology [1 ], while others have an 
emphasis on fairness [2]. Before diving into the design, it is importan t to check with the 
interviewer about the scale and the important characteristics of the exchange in q ues-
tion. 
Just to get a taste of the kind of problem we are dealing with; NYSE is tradin g billions of 
matches per day [3], and HKEX about 200 billion shares per day (4]. Figure 13.1 shows 
the big exchanges in the "trillion-dollar club" by market capitalization. 
I 379 


[Page 381]
ò
òò ~ ... ,/\l,,ò4'11 
-
"1-.,11 ......... 
,.,..,..,.~ . 
'""'~""" .. 
I ...... M. y ........ 
tj C .. 
-~~--~-╖- - .......... ,,_ ~ .... " (. l'-"W' 
, ..... r ... rru. . ..,r;. .. .,. 
ò 9 , ............. ._ ..... ,~ .. .,. 
,,.., 
" 1 
'" Hl 
òòò ,,., . 
l1mifllll'f 
lwf'h.#1("' 
,, ,.,.., . 
Figure 13.1: Largest stock exchanges (Source : [5]) 
Step 1 - Understand the Problem and Establish Design Scope 
A modern exchange is a complicated syst em with stringent requirem ents o n laten cy, 
Lhroughput , and robustness. Before we start , let's ask the interviewer a few questions to 
clarify the requirements. 
Candidate: Which securitie s are we going to trade ? Stocks, options , or futures ? 
Interviewer : For simpli city, only stocks. 
Candi date : Which types of order opera tions are supported : placing a new order, can¡
celing an order, or r eplacing an order ? Do we need to support limit order, market order, 
or conditional order ? 
Interviewer : We need to support the following: placin g a new order and canceling an 
order. For the order typ e, we only need to consider the limit order. 
Candidate : Does the system need to supp ort after-hours tradin g? 
Interviewer : No, we just need to support the normal trading hours . 
Candidate : Could you describe the basic functions of the exchange? And the scale of 
the exchange, such as how many users , how many symbols, and how many orders? 
Interviewer : A client can place new limit orders or cancel them, and receive matched 
trades in real-time. A client can view the real-time order book (the list of buy and sell 
orde rs). The exchan ge needs to support at least tens of thou sands of users tracling at 
the same time, and it needs to support at least 100 symbols. For the trading volume, we 
should support billions of orders per day. Also, the exchange is a regulated facility, so 
we need to make sure it runs risk checks. 
Candidate: Could you please elaborate on risk checks? 
Interviewer : Let's just do simple risk checks. For example, a user can only trade a 
maximum of 1 million shares of Apple stock in one day. 
380 I Chapter 13. Stock Exchange 
-


[Page 382]
Candidate : I noticed you didn 't mention user wallet mana gement. ls it somethin g w e 
"d ? also need to cons1 er . 
Interviewer : Good catch! We need lo make sure users have sufficient funds when th ey 
place orders. If an order is waiting in the order book to be filled, the funds required for 
the order need to be w1lhheld to prev ent overspending . 
Non-functional requireme nts 
AAer checking with the interviewer for lhe functional requirements , we should deter¡
mine Lhe non-functional requiremenls . In fact, requirements like "at least 100 symbols " 
and òtens of thousands of users" tell us that the intervi ewer wants us to design a small-to ¡
medium scale exchange. On top of this, we should make sure the design can be extended 
10 support more symbols and users . Many interviewer s focus on extensibility as an area 
for follow-up questions . 
Here is a list of non-functional requirements: 
ò Availability. At least 99.99 3. Availability is crucial for exchanges. Downtime, even 
seconds, can harm reputation . 
ò fault tolerance. Fault tolerance and a fast recovery mechanism are needed to limit 
the impact of a production incident. 
ò Latency. The round-trip latency should be at the millisecond level, with a particular 
focus on the 99th percentile latency. The round trip latency is measure d from the 
moment a market order enters the exchange to the point where the market order 
returns as a filled execution . A persistently high 99th percentile latency causes a 
terrible user experience for a small number of users . ╖ 
ò Security. The exchange should have an account management system. For legal and 
compliance, the exchange performs a KYC (Know Your Client) check to verify a user 's 
identity before a new account is opened . For public resources, such as web page s 
containing market data, we should prevent distributed denial-of-service (DDoS) [6) 
attacks. 
Back-of-the-envelope estimation 
Let's do some simple back-of-the-envelope calculations to understand the scale of the 
system: 
ò 100 symbols 
ò 1 billion orders per day 
ò NYSE Stock exchange is open Monday through Friday from 9:30 am to 4:00 pm East¡
ern Time. That's 6.5 hours in total . 
1 billion ò QPS: = ,.,_,43,000 6.5 x 3,600 
ò Peak QPS: 5 x QPS = 215,000. The trading volume is significantly higher when the 
market first opens in the morning and before it closes in the afternoon. 
Step 1 - Understand the Problem and Establish Design Scope I 381 
-


[Page 383]
Step 2 - Propose High-Level Design and Get Buy-In 
Before we dive inlo the high-level design , let's briefly discuss some bas ic concepts and 
terminology lhat arC' helpful for designi ng an exchange . 
Business Knowledge 101 
Broker 
Most retail clien ts trade with an exchange via a bro ker. Some brokers w hom you might 
be familiar with include Charles Schwab, Robinhood, E*Tra de, Fidelity, etc. These bro¡
kers provide a friend ly user i nterface for retail users to place trades and view mark et 
data. 
Institutional client 
Institutiona l clien ts trade in large volum es using specialized trading software . Different 
institutional clients operate with different requirem ents. For examp le, pensio n funds aim 
for a stab le income. TI1ey trade infrequently, but when they do trade, the volwn e is large. 
They need features like order splitting to minimize the market impact [7] of their sizable 
orders. Some hedge funds specialize in m arket mald.ng and earn income via commi ssion 
rebates. They need low latency trading abiliti es, so obviously t hey cannot simply view 
market data on a web page or a mobile app, as retail clients do. 
Limit order 
A limit order is a buy or sell order with a fixed price. It might not find a m atch immedi ¡
ately, or it might just be partiall y matched. 
Market order 
A mark et orde r d oesn 't specify a pri ce. It is e xecuted at the prevailin g mark et price 
immediate ly. A market ord er sacrifices cost in ord er to guarantee executi on. It is useful 
in certain fast-moving market condi tions. 
Market data levels 
The US stock m arket h as three tiers of price quotes: Ll (level 1), L2, and L3. Ll market 
data contains the best bid pri ce, ask price, and quantitie s (Figure 13.2). Bid price refers 
to the highest price a buyer i s willin g to pay for a stock. Ask pri ce refers to the lowest 
price a seller is willing to sell the stock. 
APPLE stock 
Price Quantity 
bestask 100.10 ~ 
best bid 100. 08 I 2000 I 
Figure 13.2: Level 1 data 
L2 includes more price levels than Ll (Figure 13.3). 
382 I Chapter 13. Stock Exchange 


[Page 384]
""" \' \1\\11\ 
t.atò ' 
~~ ~~-s price levels and thC' qu<'U<'i qmmtity nt wh pd~ ' l '\''t'\ (Ftgnt't' 1:\.11). 
APPLE stock 
Pri<::e nttt)i . 
, ... ╖╖╖╖╖╖╖ò╖╖ò╖ ., 
I 
I 
I 
: depth of nsk 100. h 100 00 prlc I IJ(ll!' i . ,__ ____ --4 
Sell book : ,00. t2 600 900 
t---------
I 
I 
I 
I 
. 
100. ll 900 700 '466 I 
!--------------. 
I 
I 
best ask 100. 16 26& òoo 1\6& 10& ò 
'---------------------------------╖-╖-----------╖╖╖╖- ' 
~----------------------- - - ---------- - --- -- -- - ------- ~ 
: Price Quantity : 
I I 
I best bid 100 .. 68 : see 600 9&& I 
I 
Buy book : 100.97 
100.96 
100 ;oo 
Jae I 2ea I 
Ccndlestick chart 
I 
I 
I 
: depth of bid tee.es 
' 
1100 499 
see 199 
'----------------------------------------------------╖ 
Figure 13.4: Level 3 data 
___ .:andlestick chart repre sents the stock price for a certain period of time. A typical 
~ilestick looks like this (Figure 13.5). A candlestick shows the mark et's open , close, 
-.: ' and low price for a time interval. The common time intervals are one-minute , five¡
==zite, one-hour, one-day, one-week. and one-month . 
Step 2 - Propose High-Level Design and Get Buy In I 383 


[Page 385]
-
High ..-
Upper Sl1adow 
Open 
ReAI Body 
Close 
} owec Shadow 
Low 
Figure I 3.5: A single candlestick chart 
FIX 
FIX prot ocol (8], which stand s for Pinan cial Information exchang e protocol, was created 
in 1991. It is a vendor-neutral communi cations protocol for exchanging securiti es tran s¡
action informa tion. See below for an example of a securiti es transaction encoded in FIX 
(8). 
8=FIX.4. 2 I 9=176 I 35=8 I 49=PHLX I 56=PERS I 
52=200 71 123 - 05: 30: 00.000 I 11=ATOMNOCCC9990900 I 20=3 I 150=E I 39=E 
I 55= MSFT I 167=CS I 54 =1 I 38=15 I 40=2 I 44=15 I 58=PHLX EQUITY 
TESTING I 59=0 I 47=C I 32=0 I 31 =0 I 151=15 I 14=0 I 6=0 I 10=128 I 
High-level design 
Now that we have some basi c und erstandin g of the key concepts, let's take a look at the 
high-lev el design, as shown in Figure 13.6. 
' ' ' 
<º- - - --~.+ 
I ' 
I : 
I ' 
I 
I 
I 
I 
I 
I 
I 
I 
I 
Broker 
Roblnhood , 
Goldman 
Sachs , etc 
---0-- Critica l Path 
- @ ò Market Data Flow 
- -@-<> Reporting Flow 
D t Market Data 
Se~~e +- - - - - - -@ candlestick chart, order book - - - - - - Publisher 
Client 
Gateway 
Order Manager 
I wCRet I 
orders , executions 
Sequencer 
' I 
I 
I 
e 
Matching Engine 
~ 
Stock Exchange 
╖--- -- ----... ----.. .. ----.. ----------.. .. --.. -.. --...... --- ---.. -- . . .. - -.. ----- ... ò 
Figure 13.6: High-level design 
384 I Chapter 13. Stock Exchange 


[Page 386]
l.c:'t's trace the life of an order through various components in the diagram lo sec how 
the pieces fit toge ther. 
First, we follow th e order through the trading flow . ll1is is the critical path with stric t 
Jntrncy requirements . Everything has to happen fast in the flow: 
ò tep 1: A client pla ces an order via the broker 's web or mobile app. 
Step 2: 111e broker sends the order to the exchang e. 
Step 3: The order enters the exchange through the client gateway. The client gateway 
perfonns basic gateke eping functions such as input validation, rate limiting , authentica ¡
twn, normalization , etc. The client gateway then forwards the order to the order man ¡
ager. 
tep 4 ,...., 5: The order manager performs risk checks based on rules set by the risk man¡
ager. 
tep 6: After passing risk checks, the order manager verifies there are sufficient funds in 
the wallet for the order . 
Step 7"" 9: The order is sent to the matching engine . When a match is found, the match¡
ing engine emits two executions (also called fills), with one each for the buy and sell 
sides. To guarantee that matching results are deterministic when replayed, both orders 
and executions are sequenced in the sequencer (more on the sequencer later). 
Step 10 rv 14: The executions are returned to the client. 
Next, we follow the market data flow and trace the order executions from the matching 
engine to the broker via the data service. 
Step Ml : The matching engine generates a stream of executions (fills) as matches are 
made. The stre am is sent to the market data publisher. 
Step M2: The market data publisher constructs the candlestick charts and the order books 
as market data from the stream of executions and orders. It then sends market data to 
the data service. 
Step M3: The market data is saved to specialized storage for real-time analytics. Broker s 
connect to the data service to obtain timely market data. Brokers relay market data to 
their clients. 
Lastly, we examine the reporting flow . 
Step Rl,....,R2 (repo rting flow): The reporter collects all the necessary reportin g fields (e.g. 
client_id , price , quantity , order _type , filled_quantity, remaining_quantity ) from or¡
ders and executions, and writes the consolida ted records to the database. 
Note that the tracling flow (steps 1 to 14) is on the critical path, while the market data 
flow and reporting flow are not. They have different latency requirements. 
Now let's examine each of the three flows in more detail. 
Step 2 - Propose High-Level Design and Get Buy-In I 385 
-


[Page 387]
Trading flow 
111c trading flow is on the critical palh of th e exc hange. Everything must happen fast. 
ll1c heart of the trading flow is th e mat chin g engine. Let's go ove r tha t first. 
M atching engine 
1111.'' matching cngi ne is also called I he cross engine. Here are the primary responsibilities 
of the matching engine: 
1. Maintain the order book for each sym bol. An order book is a list of buy and sell 
orders for a symbol. We explain lhe constru ction of an order book in the Data models 
section later . 
2. Match buy and sell orders. A match resu lts in two executions (one from the buy side 
and the other from the sell side). 111e matching function must be fast and accurate. 
3. Distribute the executio n stream as mark et data . 
A highly availab le matchin g e ngin e implementation must be able to produ ce matches 
in a deterministic order. 111at is, given a known sequence of orders as an input, the 
matching engine mu.st produce the same seque nce of executions (fills) as an output when 
the sequenc e is replayed . This determinis m is a foundation of high availability which we 
will discuss at length in the deep dive section. 
Sequencer 
The sequencer is the key component that makes the matching engine deterministic . It 
stamps every incoming order with a sequence ID before it is processed by the match¡
ing engine. It also stamps every pair of executions (fills) completed by the matching 
engine with sequence IDs. In other words, the sequencer has an inbound and an out¡
bound instance, with each maintaining its own sequences. The sequence generated by 
each sequencer must be sequential numb ers, so that any missing numbers can be easily 
detected. See Figure 13.7 for details. 
Order Manager Match Engine 
Outbound Sequencer 
Figure 13.7: Inbound and outbound sequencers 
The incoming orders and outgoing executions are stamped with sequence IDs for these 
reasons: 
1. Timeliness and fairness 
2. Fast recovery I replay 
3. Exactly-once gu~antee 
386 J Chapter 13. Stock Exchange 
╖' 


[Page 388]
I 
' 
I 
ò. -
ut-nc.""t' r dor. not only p:cnerate seque nce IDs. It also fu nctions as a message queu e 
a c. ne- t0 send mrssngcs (incomi ng orders) to the matching engine. and ano ther one 
~~grs (ext.'cutions) back to the order manager. It is also an event store for th e 
~d <'Xecuti ons. It is similar to having two Kafka event stream s connec ted to th e 
,iun, t'J\e:tnc. one for incoming orders and the other for outgoing executions. In fact, 
M ,,'\UM ha\-e used KRf'ka if its latency was lower and more predictable . We discuss how 
~umc-er is implemented in a low-latency exchange environment in the deep dive 
-km. 
Order manager 
1ht ('rJe r manager receives orders on one end and receives executions on the other. It 
g~ the orders ╖ sta tes. Let's look at it closely. 
~ order manager receives inbou nd orders from the client gateway and performs the 
╖:&",ng: 
ò It sends the order for risk checks. Our requirements for risk checking are simpl e. For 
~pie, we verify that a user's trade volume is below $1M a day. 
ò It checks the order agai nst the user's wallet and verifies that there are sufficient funds 
to cover the trade. The wallet was discussed at length in the "Digital Wallet " chapter 
on page 341. Refer to that cl1apter for an implementation that would work in the 
exchange. 
ò It sends the order to the sequencer where the order is stamped with a sequence ID. 
The sequenced order is then processed by the matching engine. There are many 
attributes in a new order, but there is no need to send all the attributes to the matching 
engine. To reduce the size of the message in data transmission, the o rder manage r 
only sends the necessary attri bute s. 
On the other end , the order manager receives executions from the matching engine via 
the sequencer. The order manager returns t he executions for the filled order s to the 
brokers via the client gateway. 
The order manager sho uld be fast, efficient, and accurate. It maintains the current states 
for the orders. In fact , the challe nge of managing the various state transiti ons is the 
major source of comp lexity for the order manager. There can be ten s of thousand s of 
cases involved in a real exchange syste m. Event sourcing [9] is perfe ct for the design of 
an order manager . We discuss an event sourcing design in the deep dive section . 
Client gateway 
The client gateway is the gatekeepe r for the exchange. It receives orders placed by clients 
and routes them to the order man ager. The gateway provides the followin g functi ons as 
shown in Figure 13.8. 
Step 2 - Propose High-Level Design and Get Buy-In I 387 


[Page 389]
r - .. - ... - .. -- - , 
I 
' Gateway 
I 
: I Auth 11 Validation 
I 
! ~, - Ra_t_e _Li_m-it- j j Normali zation J 
I 
! ,~Fl_XT_S-up_p_o-rt-
' '---------------------------------
Figure 13.8: Client gateway components 
The client gateway is o n the critical path and is latency -sensitive. It should stay 
lightweight. It passes orders to the correct destinations as quickly as possible. The 
func tions above, while critical, must be completed as quickly as poss ible. It is a design 
trade-off to decide what f╖unctionalil y to put in the client gateway, and what to leave out. 
As a general guideline, we should leave complicated funct ions to the matching engine 
and risk check. 
There are different types of client gateways for retail and institutional clien ts. The main 
considerations are latency, transaction volume, and security requirem ents . For instance, 
institutions W<e the market makers provide a large portion of liquidi ty for the exchange. 
They require very low latency. Figure 13. 9 shows different client gateway connections 
to an exchange . An extreme example is the colocation (co lo) engine. It is the trading 
engine software running on some servers rented by the broker in the exchange's data 
center. The latency is literally the time it takes for light to travel from the colocated 
server to the exchange server [ 10]. 
Exchange 
Website /App 
Other API 
Users 
Market data flow 
App/Web 
Gateway 
Colo Engine 
Exchange 
Figure 13.9: Client gateway 
Sharded 
Services 
The market data publisher (MDP) receives executions from the matching engine and 
builds the order books and candlestick charts from the stream of executions. The or¡
der books and candlestick charts , which we discuss in the Data Models section later, are 
collectively called market data The market data is sent to the data service where they 
are made available to subscribers. Figure 13.10 shows an implem entation of MDP and 
how it fits with the other components in the market data flow. 
388 I Chapter 13. Stock Exchange 
I 
'1 
; i╖ 'I 


[Page 390]
f 
l 
t 
! 
╖╖-
MOP 
fQ,d;l f();d;l fQ,d;l 
~~~ 
[ ~:~~ ~ Orders. matched results Candlestick 
Charts 
Persistence 
Data Service 
Figure 13.10: Market Data Publisher 
Reporting flow 
One essential part of the exchange is reportin g. The report er is not on the trading critical 
path. but it is a critical part of the system. It provides trading history , tax reporting , 
compliance reporting, sett lements, etc. Efficiency and latency are critical for the trading 
flow. but the reporter is less sensitiv e to latency. Accuracy and compliance are key factors 
for the reporte r. 
It ts common practice to piece attribut es together from both incoming orders and outgo¡
ing executions. An incoming new order contain s order details, and outgoing execution 
usually only contains order ID, price, quantity , and execution status. The reporter merges 
the attributes from both sources for the reports. Figure 13.11 shows how the components 
m the reporting flow fit toge ther. 
Step 2 - Propose High-Level Design and Get Buy-In I 389 


[Page 391]
Order 
Manager 
Reporter 
orders -
fills/rejects 
, - ╖- - - òI 
! NewDOrderReq i ! NewDOrderAck DFill j 
I I I I 
I I I I 
I I I I 
I I I I 
I I I I 
: I : I 
: ___ Reque_s_l 137R".sp~nse ______ : 
Execution Report 
Settlement & 
Clearing 
Reporting 
Books & 
Records 
Figure 13.11: Reporter 
1- Matching J 
Manager ... -
A sharp reader might noti ce that the section order of "Step 2 - Propose High -Level Design 
and Get Buy-In" looks a little different than other chapters . In this chapter, the API design 
and data models sections come after the high-l evel design. The sections are arranged this 
way because these other sections requir e some concepts that were introduced in the 
high-level design . 
API Design 
Now that we und erstan d the high-level design, let's take a look at the API design. 
Clients inter act with the stock exchange via the brokers to place orders, view executions, 
view market data, download histori cal data for analysis, etc. We use the RESTful con¡
ventions for the API below to specify the interface between the brokers and the client 
gateway. Refer to the "Data models" section on page 393 for the resources mentioned 
below. 
Note that the RESTful API might not satisfy the latency requirements of institutional 
clients like hedge funds. The specialized software built for these institutions likely uses 
a different protocol, but no matter what it is, the basic functionality mentioned below 
390 I Chapter 13. Stock Exchange 
I 


[Page 392]
..... 
needs to be supported. 
order 
POST /v1 /order 
This endpoint places an ord er. It requir es authentication. 
Parameters 
symbol: the stock symbol. ~t nng 
side: buy or sell. ~I n ng 
price: the pric e of the limit order. Long 
orderType: limit or market (note we only support limit orders in our design). String 
quantity : the quantity o f the order. I ong 
Response 
Body: 
id: the ID of the o rder. Long 
creation Time: the system creatio n time of the order. Long 
fill edQuanti ty: the quantit y that has been successfu lly executed. Long 
remai ni ngQuanti t y: the quan tity still to be executed. Long 
status : new/cance l ed/fill ed. St1ing 
rest of the att ributes are the same as the input parameters 
Code: 
200: successful 
40x: param eter error /access denied/unauthorized 
500: serve r error 
Execution 
GET /v1/ executi on?symbol={:s ymbol }&orderld={:orderld}&start Time={:startTime}& 
endTime={: endTime} 
This endpoint queries exec ution info. It requir es auth entication. 
Parameters 
symbol: the stock symbol. String 
order Id: the ID of the order. Optio nal. String 
startTime: query star t time in epoc h [11]. Long 
endTime: query end time in epo ch. Long 
Response 
Body: 
Step 2 - Propose High-Level Design and Get Buy-In I 391 


[Page 393]
cxrru trnm rirnw with rach <' '<<'< utinn in sropr (c;rr nttrib 11tr'\ hr low) . \1 t.1\ 
id╖ the TD of the rxrcnl1nn . 
orderid the ID of the nnlt>r. 11 11ò 
symbol lh(' stoc k s\mhnl . t11rH1 
side hm nrsrll 1111 
pri ce. the prnc of the r\.t'rt1lio11 l 0111 
orderType: 1111111 nr markr l 11.~ 
quantity. lhr filled qua nltt\ . l.1111g 
( ndr: 
200: successfu l 
40x: pRrameler error /n ol found /access de nied/unau thorized 
500: server error 
Order book 
GET /v1 /marketdata/orderBook/L2?symbol={:symbol}&depth={:depth} 
Tius endpoi nt queries L2 o rder book information for a symb ol with designated 
depth . 
Parameters 
symbol: the stock sym bol. ~Lnnf! 
depth: order book depth per side. Tnl 
sta rt Time: query start lime in epoch . Long 
endT ime: query end tim e in epoch. Long 
Respo nse 
Body : 
bids: array with pri ce and size. Array 
asks: array with price and size.Array 
Code: 
200: successful 
40x: parameter error /not found/access denied/unauthorized 
500: ser ver error 
Historical prices (candlestick charts) 
GET /v1/ marketdat a/candles?symbol={:symbol}&resolution={:resolution}&startTime 
{:startTime}&endTime={:endTime} 
Th.is endpoint que ries candlestick chart data (see candl estick chart in data models sectio n) 
for a symbol given a time range and resoluti on. 
Paramete rs 
392 I Chapter 13. Stock Exchange 
I 
,: 
╖~ 
I I 
.-


[Page 394]
symbol : t..he stock symbol. St nng 
resoluti on: window length of the candlestick chart in seconds. l .nng 
startT ime: star t time of the window in epoch. Long 
endTime: end time of the window in epoch. Long 
Re ponse 
Body: 
candles: array with each candlestick data (attribut es listed below). Array 
open: open price of each candlestick. Double 
close : close price of each candlestick. Double 
hig h: high price of each candlestick. Double 
low: low price of each candlestick. Double 
Code: 
200: successful 
40x: parameter error/not found /access denied/unauthori zed 
500: server error 
Data models 
There are three main types of data in the stock exchange. Let's explore them one by 
one . 
ò Product, order, and execution 
ò Order book 
ò Candlestick chart 
Product, order, execution 
A product descri bes the attributes of a traded symbol , like product type , trading symbol , 
UT display symbo l, settlement curren cy, lot size, tick size, etc. 1his data doesn 't change 
frequently. It is p rimaril y used for UI display . The data can be stored in any database and 
1s highly cacheable. 
An order represents the inb ound instruction for a buy or sell order. An execution repre ¡
sents the outb ound mat ched result. An execution is also called a fill . Not every order has 
an execution . The o utput of the matching engine contains two executions , representin g 
the buy and sell side s of a matched order. 
See Figure 13.12 for the logical model diagram that shows the relation ships betwee n the 
three entities . N ote it is not a databa se schema. 
Step 2 - Propose High-Level Design and Get Buy-In I 393 


[Page 395]
Order 
-
+ orderlO╖ UUID 
+ productlD: int 
+ price.╖ long 
+ quantity: long 
+side ╖ Side 
+ orderStatus. OrderStatus 
+ orderType: OrderType 
+ timelnForce : TimelnForce 
+ symbol. long 
+ userlD╖ long 
+ clientOrderlD : string 
+ broker: string 
+ accountlD: long 
+ entryTime: long 
+ transaclionTime: long 
Product 
+ productlD: int 
+ symbol: type 
+ lotSize: int 
+ tickSize: decimal 
+ quoteCurrency: Currency 
+ settleCurrency: Currency 
+ description: string 
+ field: type 
0 n 
Execution 
+ execlD UUID 
-1 orderlD : UUID 
-1 price long 
+quantity . long 
+side ╖ Side 
+ orderStalus : OrderS tatus 
+ orderType : OrderType 
+ symbo l: long 
+ userlD. long 
+ feeCurren cy: Currency 
+ feeRate: long 
+ feeAmount: long 
+ accountlD : long 
+ execSta tus: ExecS tatus 
+ transactionTime: long 
Figure 13.12: Product , order, execution 
Orders and executions are the most important data in the exchange . We encounter them 
in all three flows mentioned in the high-level design , in slightly different forms. 
ò In the critical trading path, orders and executions are not stored in a database. To 
achieve high performance , this path executes trades in memory and leverages hard 
disk or shared memory to persist and share orders and executions. Specifically, or¡
ders and executions are stored in the sequencer for fast recovery , and data is archived 
after the market closes. We discuss an efficient implementation of the sequencer in 
the deep dive section. 
ò The reporter writes orders and executions to the database for reporting use cases like 
reconciliation and tax reporting. 
394 I Chapter 13. Stock Exchange 


[Page 396]
ò Executions are forwarded to the marke t data pro cessor lo reconstruct the order boo k 
and candlestick chart data. We discuss these data types next. 
Order book 
An order book is a list of buy and sell orders for a specific security or financial instrum en t, 
organized by price level [12] [13]. It is a key data stru cture in the matching e ngine for 
fast order matching. An efficient data structure for an order book must satisfy th ese 
requirements: 
ò Constant lookup lime. Operation includ es: getting volume at a price level or betwee n 
price levels . 
ò Fast add/cancel/exec ute operations, preferabl y 0(1) time complexity. Operati ons 
include: placing a new order, cance ling an order, and matching an order . 
ò Fast update . Operatio n: rep lacing an order . 
ò QJ!ery best bid/ask. 
ò Iterate through price levels. 
Let's walk through an examp le order execution against an order book , as illustrated in 
Figure 13.13. 
APPLE stock 
i -- -- - ---- - --- - --------- - -------------- ------- -- -- ---
1 Price Quantity , 
: depth of ask 1ea.13 1 ea 209 -price levels : I 
Sell book 100.12 600 909 
100.11 
best ask 100.1G 
╖------------------------
Price 
: best bid 100.G8 
Buy book l 106.07 
1G0.G6 2G9 
I 
: depth of bid 
I 
Figure 13.13: Limit order book illustrated 
In the examp le above, there is a large market buy order for 2,700 shares of Apple. TI1e 
buy order matches all the sell orders in the best ask queue and the first sell order in the 
100.11 price queue. After fulfilling this large order, the bid/ask spread widens, and the 
price increases by one level (best ask is 100.11 now). 
The following code snippet shows an implementat ion of the order book. 
Step 2 - Propo se High-Level Design and Get Buy- In I 395 
-


[Page 397]
C]aSS r1irtlPVf'J { 
} 
p1 hate Price limitPrice; 
p1 ivalr 101 o totalVol ume; 
p1 i V<lle List <Order> orders; 
class Bo ~ < ~1 Ir > { 
privat" Side sid e ; 
} 
p,.ivritr Map <Price, r1cPIPvrl > limitMap; 
class 01 dcrRook { 
} 
private Book <B uy > buyBook; 
rrivate Book <Sell > sellBook; 
private Pr1rclrvr] bestBid; 
p 1╖ 1 v a t e P 1 j t e L e v e l best 0 ff e r ; 
fHi vale Map<OrderID, Orde1 > or de r╖ Map ; 
Does the code meet all the design requirements stated above? For example, when 
adding /canceling a limit order, is the time complexity 0(1)? The answer is no since we 
are using a plain list here (private List <Order> order s). To have a mor e efficient order 
book , change the data sh╖ucture of "orders" to a doubly-linked list so that the deletion 
type of operat ion (cancel and match) is also 0 (1). Let's review how we achieve 0 (1) 
time complexity for these operations: 
1. Placing a new order means adding a new Order to the tail of the Pricelevel. This is 
0 (1) time complexity for a doubly -linked list. 
2. Matching an order means deleting an Order from the head of the PriceLevel. This is 
0 ( 1) time complexity for a doubly-linked list. 
3. Canceling an order means deleting an Order from the OrderBook. We leverage the 
helper data structure Map<OrderID, Order> orderMap in the OrderBook to find the 
Order to cancel in 0 (1) time. Once the order is found, if the "orders " list was a 
singly-linked list, the code would have to traverse the entire list to locate the previous 
pointer in order to delete the order. That would have tal<en 0 ( n) time. Since the list is 
now doubly-linked , the order itself has a pointer to the previous order , which allows 
the code to delete the order without traversing the entire order list. 
Figure 13.14 explains how these three operations work. 
396 I Chapter 13. Stock Exchange 


[Page 398]
befOtO ò n~I 
11111111 
\ kov ò 100 00 
vt1lue 
before .. 
aner 
!. 
before " null 
81181 
Order 
qu11111ltyc 500 
, Buy ordOf Is matchod nnd 
ò removod from tho f>rlaeLe\181 
' prlee . 100 08 
: qu111n11ty ò 500 
I 
bofore 
af1or 
Ordor 
quanllt yò 600 
« : 
l 
betoro 
afte<" nutl 
Orde< 
quan11ty = 900 
-.. -------.. -----------------. ---. ---. ---------------------------------------╖: 
Doubhllnktdll st <Ordtr> orders ' ' 
before before ' ,.-------------. -----
before = null ' : Placing a new buy ord 
after= null ' alter after ' ' ' I 
\ kl!)' = 100 07 Ordl!f Order Order __ J ___ .. ~ prlce = 100.07 
1 : : quan11ty = 200 VlllU9 quant ity = 100 quantity = 700 quanli1y=200 
Q); 
' : ,_ --╖----------------' ~- - - --- -- - - ------ - - -- -- - ---- - --╖- - - - ----╖-- ---- -- - - -- --------- -╖- --------- - ---
befOl1! .. ,. 
before= null ~foref before befor e 
after 
alter .,.,.. after after = null 
key= 100.06 Order 
~ 
Order Order 
value quantity= 1100 quantity = 300 quantity= 200 
"" ' 
St~p2 
r -- .......... -ò -- -- -.. -- .... -.. - --- .. - ---- .. --- -.. -- .. -- .. - --- --
l Cancel an order @ 
hsh"òp<DnlerIO, Or der> orderlhp l price= 100.06 
╖ Step 1 -~quantity= 400 
~~~~~~~~~~~ I 
: Step 1. Find lhe Order In orderM ap via OrderlD 
! S1ep 2. Remove lhe Order element from the Pricelevel 
-...... ----------.. -------............. -----╖----------------
Figure 13.14: Place , match , and cancel an order in 0 ( 1) 
See the reference material for mor e details [14]. 
It is worth noting that the order book data structure is also heavily used in the mark et 
data processor to reconstruct the Ll , 12, and L3 data from the streams of executi ons 
generated by the matching engine. 
Candlestick chart 
Candlestick chart is another key data structure (alongside order book) in the market data 
processor to prod uce mark et data. 
We model this with a Candlestick class and a CandlestickChart class. When the inter¡
val for the candlestick has elapsed, a new Candlesti ck class is instanti ated for the next 
interval and added to the link ed list in the CandleStickChart instance. 
cl as s Candlestick { 
private long openPrice; 
pri vate long cl ose Pri ce; 
private long highPrice; 
private long lowPrice; 
private long volume; 
private long timestamp; 
Step 2 - Propose High-Level Design and Get Buy-In I 397 


[Page 399]
pr╖ i ~ ,l\ r i 11 L in i er v a 1 ; 
} 
class C;rnrJlestickChrir l. { 
private Linkedlist<Candlesiirk ò slicks ; 
} 
Trac king price history in candlestick charts for many symbols at many time in tervals 
consumes a lot of memory. How can we op timize it? !Jere are two ways: 
1. Use pre-allocated ring buffers to hold slicks to reduce the number of new object 
allocations. 
z. Limit the numb er of sticks in the memory and persist th e rest Lo disk. 
We will examin e the optimi zation s in the "Mark et data publisher" section in deep dive 
on page 409. 
The masket data is usual ly persisted in an in-memory colum nar d atabase (for example, 
KDB [1 5)) for r eal-time analyti cs. After the market is closed, data is persisted in a his¡
torical database. 
Step 3 - Design Deep Dive 
Now that we understand how an exchange works at a high level, let's investigate how a 
modem exchange has evolved to become what it is today. What does a modern exchang e 
look like? The answer might surprise a lot of readers. Some large exchange s run almost 
everything on a single gigantic server . Whil e it might sound extreme , we can learn many 
good lessons from it. 
Let's dive in. 
Performance 
As discussed in the non-functional requirements , laten cy is very important for an 
exchange. Not only does the average latency need to be low, but the overall latency 
must also be stable. A good measure for the level of stability is the 99th percentile 
latency. 
Latency can be broken down into its components as shown in the formula below: 
Latency = 2":= executionTimeAlongCriticalPath 
There are two ways to reduce latency: 
1. Decrease the number of tasks on the critical path. 
2. Shorten the time spent on each task: 
a By reducing or eliminating network and disk usage 
b. By reducing execution time for each task 
398 I Chapter 13. Stock Exchange 


[Page 400]
Let's review the first point. As shown in thr high-level des ign, Lhr criti ca l lrndin p; pnth 
includes the followi ng: 
ga teway -t order mana ger -t sequencer -t matching engine 
1llc critical path only contains the nece ssary components. even logging is removed fro m 
the critical patJ1 to achieve low l<ltency. 
Now let's look at the seco nd point . In the high-level design , the components on lhe crit¡
ical path run on individual servers conn ected over the net work. The round trip netw ork 
latency is about 500 micro seco nds. When there are multip le components all communi ¡
cating over the network on the c riti cal path , th e total network latency adds up to singl e¡
digil milliseconds. In additi on, the sequenc er is an event store that persists events to 
rusk. Even assurrting an efficient design that leverages the performance advantag e of se¡
quential writ es. the latency of disk access still measures in tens of milliseconds . To learn 
more about network and disk access latency , see "Latency Numbers Every Programmer 
Should Know " [16]. 
Accounting for both network and disk access latency, the total end-to-end latency adds 
up to tens of millisec onds . While this number was respectab le in the early days of the 
exchange, it is no longer sufficient as exchanges compete for ultra-low latency. 
To stay ahead of the competition , exchanges over time evolve their design to reduce the 
end-to-end latency on the critical path to tens of microseconds , primarily by explo ring 
options to reduce or eliminate network and disk access latency. A time-tested design 
elimin ates the network hops by putting everything on the same server. When all com¡
ponents a.re on the same server, they can communicate via mrnap [ 17] as an event store 
(more on this later) . 
Figure 13.15 shows a low-latency design with all the components on a single 
server: 
-
r--- ---- --- ----- --- --- ---- ------ ----- --- -------------- ---- ------- --1 
Order Manager 
111111 ... I 
Appli cation Loop 
╖ ~ 
~ 
ò 
Reporter 
II 
One Single Server : I 
Matching Engine Market Data 
Publisher 
111111 . .. I 111111 . .. I 
Application Loop Application Loop 
mmap 
~ L ~ 
~ 
Logging 
II 
Aggregated 11 Position 
Risk Check Keeper I I 
I 
I 
------------------------------------------------------------------' 
Figure 13.15: A low laten cy single server exchan ge design 
Step 3 - Design Deep Dive I 399 


[Page 401]
╖n1ere a re a few interesting design derisions that are worth a closer look at. 
Let's first focus on the application loops in the diagra m ahove An app lication loop is 
an inlerest111g con cept. It keeps polling for task s to execute in a while loop and is the 
primary task execu tion mechani sm. To m eet the strict latency budget , only the mos t 
mi ssion -cri tical lasks shou ld be pro cesse d by the applica tion loop. lls goa l is to reduce 
th e execu tion time for eac h componen t and lo guaran tee a highly predic tab le execu tion 
t1111e (i.e .. a low !10th percentile laten cy). Each box in the diagra m rep rese nts a component. 
A component is a pro cess on the server. To max imize CPU efficie ncy, eac h appli cation 
loop (think of it as the main processi ng loop ) is single-thr eaded, and the thread is pinned 
lo a fixed CPU core . Using the order manager as an example, il looks like the following 
diagram (Figure 13.16). 
orders 
Order Manager 
Input Thread/Netloop 
dispatch 
r---------.. -- ----
' I 
: i Order State 
i Application :__update-I I 
: Loop : 
I I 
, Thread }---._ 
J pin to CPU 1 
~------------ - ----' 
dispatch 
3 4 
Output Thread/Netloop 
orders 
i 
Figure 13.16: Application loop thread in Order Manager 
ln this diagram , the application loop for the order manager is pinned to CPU 1. The 
benefits of pinning the applicatio n loop to the CPU are substantial : 
l. No context switch [18]. CPU 1 is fully allocated to the order manager's application 
loop. 
2. No locks and therefore no lock contention, since there is only one thread that updates 
states . 
Both of these contribute to a low 99th percentile latency. 
The tradeoff of CPU pinnin g is that it makes coding more complicated. Engineers need 
to carefully analyze the time each task takes to keep it from occupying the application 
loop thread for too long, as it can potentially block subsequent tasks. 
Next, let's focus our attention on the long rectangle labeled "mmap " at the center of 
400 I Chapter 13. Stock Exchange 


[Page 402]
-
figure 13.15. "mmap" refers to a POSIX-compliant UNIX system call nam ed mmap(2) lha l 
maps a file int o the memory o f a process. 
mmap(2) provi des a mechani sm for high-performan ce sharin g of memory between pro¡
cesses. 1he perfo rmance advant age is compound ed when the backing file is in I dev / shm. 
/dev/shm is a memory-backed file system. When mmap(2) is done over a file in /dev/shm, 
the access to the shared memory does nol result in any disk access at all. 
Modem exchanges take a dvantage of this to eliminat e as much disk a ccess from the 
critical path as p ossible. mmap (2) is used in the server to implement a message bus over 
which the comp onents on the critical path communicate . The communication pathway 
has no network or disk access, and sending a message on this mmap message bus takes 
sub-microsecond. By leveraging mmap to build an event store , coupled with the event 
sourcing design p aradigm which we will discuss next, modern exchan ges can build low ¡
\atency microse rvices inside a server. 
Event sourcing 
We discussed event sourcing in the "Digital Wallet" chapter on page 341. Please refer to 
that chapter for an in-depth review of event sourcing. 
The concept of event sourcing is not hard to understand . In a traditi onal application, 
states are persisted in a database . When something goes wrong, it is hard to trace the 
source of the issu e. The database only keeps the current states, and there are no records 
of the events that have led to the current states. 
ln event sourcing, instead of storing the current states , it keeps an immutable log of all 
state-changing events. These events are the golden source of truth. See Figure 13.17 for 
a comparison. 
OrderFllledE vent 
Order Event 
Version OrderStatu s Event Sequence Event Type 
V1 New 100 NewOrderEvent 
V2 Filled 101 OrderFllledEvent 
Non Event Sourcing Event Sourcing 
Figure 13.17: Non-event sourcing vs event sourcing 
On the left is a classic databa se schema. It keeps track of the order status for an order, but 
it does not contain any information about how an order arrives at the current state. On 
the right is the event sourcin g counterpart. It tracks all the events that change the order 
stales, and it can recover order states by replaying all the events in sequence. 
Figure 13.18 shows an event sourcing design using the mmap event store as a message 
bus. This looks very much like the Pub-Sub model in Kafka. In fact, if there is no slricl 
Step 3 - Design Deep Dive I 401 


[Page 403]
lat r ncy rrqu iremenl , Kafka could be used. 
External l Trading 
Domain : Domain 
(FIX) (SSE) 
- FIX 
' 
Gateway 
Event Store 
Client 
NewOrt!erEvent 
: Sequence 
I 
: Event type 
I 
I 
I SBE 
Matching Engine 
r---------. 
Order Manager 
Order Stale 
Send lo 
Matching 
Core 
Validate, matching 
upd~ 
~ 
Pull events 
OrderFilledEvent 
Event Store (mmap) 
Market Data 
Publisher 
Events 
I E~::i:nt~ Eòlents 
: Trading Domain (SBE) 
~ - --- ------ - - - --- - - ---- - ------- - ----- - ---- --- -- - - - ---------------------------------
Reporting Domain 
Reporter (Your choice) 
Order 
Manager 
Figure 13.18: An event sourcing design 
In the diagram , the exter nal domain communi cates with the trading domain using FIX 
that we introd uced in the Business Knowledge 101 section on page 382. 
ò The gateway transforms FIX to "FIX over Simple Binary Encoding" (SBE) for fast 
and compact encoding and sends each order as a NewOrderEvent via the Event Store 
Client in a pre-defined format (see event store entry in the diagram) . 
ò 1he order manage r (embedded in the matching engine) receives the NewOrderEvent 
from the event store, validates it, and adds it to its internal orde r sta tes. The order is 
then sent to the matching core . 
ò If the o rder gets matched , an OrderFilledEvent is generated and sent lo the evenl 
store. 
402 I Chapter 13. Stock Exchange 


[Page 404]
ò Oth<'t c11mpt111t╖111, '"' h n' th r m.11 \,.,I 11 \I ò\ l'H'' ''"'"'' 111111 1111ò "'I''''"'' """'" 111
1
1ò 111 
th<' c\'rrll -.11" t' md I'' '1't' '" th1 ,. ,,, "' 1\1 ~ '''"">th 
11w: d<' 1~n fnlh'"., tlw hi~h k' I 1tr, ",,,,,,t'h. h\ll lhr1,, 111 ò 11111111' 1111111 111111.-111111 1111111\111 
11 wi."'lrk mnrc tòflktt╖nth m ttw ''' ''"' '''"' '\I~ l'ò\1 1 \1h~n1 
The fir t di0t'1'\'l 'h'< 1., ttw ''''"'' m .m ,,,1 th ,,,, "'' 1\\1\\li ,, , l1r1111111
1
ò 11 I t
1
11
1
u1hl1
1 
llh1 111 \ 
thnt t. <'mht'<idt'ti m 1htlt'~l\I '"'"'l'''" nt~ It m1\kt' 1o1'' ll't' h\I lhl t1 1liò1tlt\ll 111'1 11111111 I ht 
c;tnl<". of thtò f"òt'\it"L t'C' "''I, 1t nt h,1 l\\\\h1pl,, '"'"'P''"t'nl~ " '' òII\}\ 11 1╖r 11l nillt iòd 1" d t'I 
mnn ~f╖r fr,r ,,tht't '"'"'I''"""' h "l ,l , 1 ~ ,,1 \l""'' tlw ,,, lc-1 1111\lt'!I " 1111hl 11111 I 1111 1
1
111 \', 
t'SJ'<'C't Jty lf th'' ╖ r '"'"'l ''""Ht. t'C' t\\'t ''" tht' l'\\t\\'OI I\ \1tl\\~ p 11lh . 11!1 Ill 1111' 1ò11111' 1111 I 111
1 
rep rh'r m th<' dt ònm 1th1'\~h t il ╖h \'I mr1,1wnt mn~nh11n~ t hr 111 hò1 !II 11 1t╖~ hv 11 IH' I I. 
\\'llh rv nt . "ur\~1\'1. tht' . t \h', rt' "' mml t h \ \' H\rnth't\I mi ' 'pl1\\'1\l
1
lt'. 
AnothC'r key di ff n" t. t h;1t th : ~u "\\\ r \,' "'''d\t"I t ' l St't' I\. \ V\rnl I 111ppt' I wd I u 
ii 'l 
\\'1th the <'' nt . nn: il\Q: :It'.~'╖ , " h , ' \'\\\t' ò h~l t'\ ' '\\t st rt' fo1╖ 1\tl l\\t' SSl\1'(t'S, Nul <' 
that thC' e' nt . tntò <'nt " ntain . ò 1 u ò tlòlt. 1hi: tlt'M is it\it'tk d hv llw S(' 
quencer . 
There i. onh- ne ò uen :'t"r fi: r n ti , nt ~ti: re. It L╖ \ hnd pm 'tkt' t h tWl' l\\Hlt iplc 
equencer . a th y " ill ~ght fi: r th" ~~ht t " Titt' tt: th ' ╖nt ~tore. In n t usy s 1slt'm like 
an exchange. a I t f tim " uld b " , ted ml ~k nt nti n. 11w~forr, thr s<'qurncrr 
is a ingle writ r which .equenre th e' nl e re , ending them the event store. 
Unlike the equenc-er in the high-le ,-el i s4-llll which al fun 'ti n ~ a a mess~ge store. 
the equencer here only d . e simpl thing nnd i u er fat. Figure 13.19 shows a 
de ign for the sequencer in a mem I')'-map (rrunap) environment. 
The equencer pull events from the ring buffer that i l al to each omponent. For each 
event. it tamp a equen ID on the en~nt and sends it t the eYent store . Vie can have 
bad-up equencers fur high aYa.ilahility in the primary equencer goes down. 
Step 3 - Design Deep Dive I 403 


[Page 405]
High availability 
l 
Gatewa l [ Matching 
Engine 
~ Wnte to ring buffei . 
.. '\ 
Sequencer pulls dat a ~ 
from nng buffe r 
Sequencer 
3 Sequencer writes to Event Store 
Event Store (mmap) 
Figure 13.19: ample design of Sequencer 
For high a,╖ailabilit y. our design aims for 4 nin es (99.993 ). This means the exchange can 
only hare J .6-1 econds of downtime per day. It requires almost immediate recovery if a 
en;ce goe down. 
To achieYe high availability , consi der the following: 
ò First, identify single-point-of-fa ilures in the exchange architecture. For example, the 
failure of the matching engine could be a disaster for the exchange. Therefore, we 
set up redundant instan ces alongside the primary instance . 
ò econd, detection of failure and the decisi on to failover to the backup instance should 
be fast 
For stateless services such as the client gateway , they could easily be horizontally scaled 
by adding more serve rs. For stateful components, such as the order manager and match¡
ing engine, we need to be able to copy state data across replicas. 
Figure 13.20 shows an example of how to copy data . The hot matching engine works as 
the primary instanc e, and the warm engine receives and processes the exact same events 
but does not send any event out onto the event store . When the primary goes down, the 
warm instance can immediately take over as the primary and send out events. When the 
warm secondary instance goes down , upon restart , it can always recover all the states 
from the event store. Event sourcing is a great fit for the exchange architecture. The 
inherent determinism makes state recovery easy and accurate. 
--- -----
404 I Chapter 13. Stock Exchange 


[Page 406]
Matching Engine 
(Hot) 
NewOrde rEvent 
OrderFllledEvent 
Matching Engine 
(Warm) 
NewOrderEvent 
Event Store (mmap) 
Figure 13.20: Hot -warm matching engine 
We need to desig n a mechanism to detect potential problems in the primary . Besides 
normal monitoring of hardwar e and processes , we can also send heartbeats from the 
matching engi ne. If a heartb eat is not received in time, the matching engine might be 
e ╖periencing problems. 
The problem with this hot-warm design is that it only works within the boundary of a 
single server. To achieve high availability , we have to extend this concept across multiple 
machines or eve n a cross data cent ers. In this setting, an entire server is either hot or 
warm, and the entire event store is replicated from the hot server to all warm replicas. 
Replicating the entire event store across machines takes time. We could use reliable UDP 
[19] to efficiently broad cast the event messages to all warm servers. Refer to the design 
of Aeron [20] for an example . 
ln the next section , we discuss an improvement to the hot-warm design to achieve high 
availability. 
Fault tolerance 
The hot-warm design above is relatively simple . It works reasonably well, but what hap¡
pens if the warm instances go down as well? 1his is a low probability but catastrophi c 
event, so we should prepare for it. 
This is a problem large tech companies face. They tackle it by replicating core data to data 
centers in multiple cities. It mitigates the risk of a natural disaster such as an earthqu ake 
or a large-scale power outage . To make the system fault-tolerant , we have to answer 
many questions: 
1. If the primary instance goes down , how and when do we decide to failover to the 
backup instance ? 
2. How do we choose the leader among backup instances ? 
3. What is the recovery time needed (RTO - Recovery Time Objective)? 
4. What functionalities need to be recovered (RPO - Recovery Point Objective)? Can 
our system operate under degraded conditions ? 
Let's answer these questions one by one. 
First, we have to understand what "down " really means. 1his is not as straightforward 
as it seems. Consider these situations. 
Step 3 - Design Deep Dive I 405 


[Page 407]
I lw svs l e 111 might se nd nut raise alarms , which cause unn rcC'ssary foilovcrs. 
:.! 1'111 s in the code might m use th e prim<lry instance to go dow n. 1hC' same hug could 
lmn g elm n the hnckup instance after the failove r. When all ba ckup instan ces arr 
knn r kcd out by th r bug, the sys tem is no longe r avai lable. 
' llH' Sl' nrc tough problem s to solve. 1 lcrc arc some sugges tions . W hen we flrs l relea se a 
new sys tem , we migh t need to perform failovers manua lly. Only when we ga th er enough 
si╡ nals nnd oprrntional experien ce and gai n more confidence in the sys tem do we au lo╖ 
mntc the failure detection pro cess. haos engineering [21] i s a good prac tice lo su rface 
t:dgc nscs and gain opera tional experie nce fas ter. 
( nee the drcision to fail over is correct ly made, how do we decide w hich server takes 
('l\'cr . For tun ately, lhi is a well-unders tood pro blem. TI1ere are man y battl e- tes ted 
k:~dt>r-ck lion algorit h ms. \Ve use Raft [22] as an example. 
Figure 13.21 hows a Raft cluster with 5 servers w ith their o wn event stores. The curr ent ' kadcr sends data to all the o ther instances (followers) . The minim um number of votes 
required to perfor m an opera tion in Raft is ~ + 1, wh ere n is the number of members in 
the lu ter. In this examp le, the minimum is ~ + 1 = 3. 
Th fi llowing diagra m (Figure 13.21) shows the followers receiv ing new even ts fro m the 
leader over RPC. Th e eve nts are saved to the follower's own mmap even t store. 
11111111111111111 
Appen dEntries RPCs 
Matching Engine 
(Hot) 
! 
NewOrderEvent 
OrderFilledEvent 
Matching Engine 
(Warm) 
i 
NewOrderEvent 
Event Store (mmap) 
Event Store (mmap) 
,-11 11~1111 1~111 11~11~~Eve-nt S-tore-(mm-ap) ~---, 
Event Store (mmap) 
Event Store (mmap) 
Figure 13.21: Event replic ation in Raft clu ster 
Let 's briefly examine the leader election pro cess. The leader sends heartbeat messages 
(AppendEnties with no content as shown in Figure 13.21) to its follow ers. If a follower 
has not receive d h eartbeat messages for a p eriod of time, it trig gers an election timeout 
that initiates a new election. The first follower that reaches electi on timeout becomes a 
406 I Chapter 13. Stock Exchange 


[Page 408]
I ...1 te and it asks the rest of the followers to vote (Request Vote). If the first follower -ant 1uR ò 
lò ò a maJ╖ority of votes it becomes the new leader If the first follower has a lower (t":'t' tVt'S ò ' 
nn value than the new node. it cannot b e the leader. If multipl e followers beco me 
1_r didates al thr same time, it is called a "split vote". In thi s case, the election times out, l"n . f " ,, T ' . 
.J n new election is initia ted. See Figure 13.22 for the explanation o term . 1me 1s 
llllll d 1 . 
1 ╖...1rd into arbitrary intervals in Raft lo represent normal operat ion an e ectlon. 111\1U 
time-
Elections Normal Operation Split Vote 
Figure 13.22: Raft terms (Source: [23]) 
'\ext. let's take a look at recovery time. Recovery Time Objective (RTO) refers to the 
amount of time an app licatio n can be down without causing significant damage to the 
tiii. iness. For a stock exchange, we need to achieve a second-leve l RTO, which definitely 
requires automatic failover of services. To do this , we categorize services based on pri¡
ority and define a degradation strategy to maintain a minimum service level. 
finally. we need to figure out the tolerance for data loss. Recovery Point Objective (RPO) 
refers to the amount of data that can be lost before significant harm is done to the busi¡
ness. i.e. the loss tolerance. In practice , this means backing up data frequently. For a 
stock exchange, data loss is not acceptable , so RPO is near zero. With Raft, we have many 
copies of the data . it guarantees that state consensus is achieved among cluster nodes . If 
the current leade r crashes , the new leader should be able to function immediately . 
Matching algorithms 
Let's take a slight detour and dive into the matching algorithms. The pseudo-code below 
e>..-plains how matching works at a high level. 
Context handl eO rder (OrderBook orderBook, OrderEvent orderEvent) { 
if (or derEvent.getSequenceid() != nextSequence) { 
return Error(OUT_OF_ORDER, nextSequence); 
} 
if (!va lidateOrder(symbol, price, quantity)) { 
return ERROR(INVALID_ORDER, orde rEvent) ; 
} 
Order order = createOrderFromEvent(orderEvent); 
switc h (msgType) : 
case NEW: 
retur n handleNew(orderBook, order); 
case CANCEL: 
re turn handleCancel(orderBook, order); 
def ault : 
re turn ERROR(INVALID_MSG_TYPE, msgType); 
Step 3 - Design Deep Dive I 407 


[Page 409]
} 
Context I a id 1 I~, (OrderBook orde rBook, Order order) { 
if (BUY.equals(order. sid e)) { 
} 
return match( order╖Book . sell Book , or der); 
} else { 
rP.lurn match(orderBook . buyBoo k, order); 
} 
Co ntext hanrll eC<incrl ( Order Book ord erBook, Order order) { 
1f (!or derBook. or der Map. cont ain s (order.orderld)) { 
return ERROR (CANNOT_ CAN CEL_A LRE ADY _MATCHED , order); 
} 
} 
re moveOrder( order ); 
se t Order Sta t us( order , CA NCELED); 
r╖etur n SUCCESS(CANCEL_SUCCESS, order); 
Context match(OrderBook book, Order order) { 
} 
Quantity leavesQuantity = orde r.qu ant ity - order.matchedQuantity; 
Iterator <Order > limitlter = book.limitMap.get( order .p rice). orders ; 
while (limitlter.h asNext() && leave sQuantity > 0) { 
} 
Quantity matched = min(limitlter.next . quantit y, order . quantity) ; 
order.matche dQuantity += matched ; 
leavesQuantity = order. quantity - order . matchedQuantity ; 
remove(limitl ter.next); 
generateMa tchedFill(); 
return SUCCESS(MATCH_SUCCESS, order); 
The pseudocode uses the FIFO (First In First Out) matchin g algorithm . The order that 
comes in first at a certain price level gets matched first, and the last one gets matched 
last. 
There are many matching algorithms. These algorithms are commonly used in futures 
trading. For example, a FIFO with LMM (Lead Market Maker) algorithm allocates acer¡
tain quantity to th e LMM based on a predefined ratio ahead of the FIFO queue, which the 
LMM firm negotiates with the exchange for the privilege. See more matching algorithms 
on the CME website [24]. The mat ching algorithms are used in many other scenarios . A 
typical one is a dark pool [25]. 
Determinism 
There is both functional determinism and latency determinism. We have covered func¡
tional determinism in previous sections. The design choices we make, such as sequencer 
and event sourcing, guarantee that if the events are replayed in the same order, the results 
will be the same. 
With functional determinism , the actual time when the event happens does not matter 
most of the time. What matters is the order of the events. In Figure 13.23, event times¡
tamps from discrete uneven dots in the time dimension are converted to continuo us dots, 
408 I Chapter 13. Stock Exchange 


[Page 410]
and the time spent on replay /recovery can be greatly reduced. 
event 1 event 2 event 3 event 6 
TI me 
Tlme 
Figure 13.23: Time in event sourcing 
Latency determinism means having almost the same latency through the system for each 
trade. This is key to the business. TI1ere is a math ematical way to measure this: the 99th 
percentile latency, or even more strict ly, the 99.99th percentile laten cy. We can leverage 
HdrHistogram [26) to calculate latency. If the 99th percentile latency is low, the exchange 
otf ers stable perfom1ance across almost all the trades . 
It is important to investigate larg e latency fluctuations. For example, in Java, safe points 
are often the cause . The HotSpo t JVM [27) Stop-the-World garbage collection is a well ¡
known example. 
lhis concludes our deep dive on the critical trading path. In the remainder of this chap¡
ter. we take a closer look at some of the more interesting aspects of other parts of the 
exchange. 
Market data publisher optimizations 
As we can see from the matching algorithm, the L3 order book data gives us a better view 
of the market. We can get free one-day candlestick data from Google Finance, but it is 
expensive to get the more detailed L2/L3 order book data. Many hedge funds record the 
data themselves via the exchange real-time API to build their own candlestick charts and 
other charts for technical analysis. 
The market data publisher (MDP) receives matched result s from the matching engine and 
rebuilds the order book and candlestick charts based on that . It then publishes the dat a 
to the subscri bers. 
The order book rebuild is similar to the pseudocode mentioned in the matchin g algo¡
rithms section above. MDP is a service with many levels. For example, a retail client can 
only view 5 levels of L2 data by default and needs to pay extra to get 10 levels. MDP 's 
memory cannot exp and forever , so we need to have an upper limit on the candlesticks. 
Refer to the data models section for a review of the candlestick charts. The design of the 
MDP is in Figure 13.24. 
Step 3 - Design Deep Dive I 409 


[Page 411]
Matching 
Engine 
MOP 
Candlestick Charts 
Orders. matched results -. 
Persistence 
Data Service 
Figure 13.24: Market Data Publisher 
Ring buffer 
Hold recent 1 00 ticks 
This design utilizes ring buffers. A ring buffer, also called a circular buffer, is a fixed-
ize queue with the head connec ted to the tail. A producer continuously produ ces data 
and one or more consumers pull data off it. The space in a ring buffer is pre-allocated. 
There is no object creation or deallocation necessary . The data structure is also lock-free. 
TI1ere are other techniq ues to make the dat a structur e even more efficient. For example, 
padding ensures that the ring buffer's sequence number is never in a cache line with 
anything else. Refer to [28] for more detail . 
Distribution fairness of market data 
In stock trading, having lower latency than others is like having an oracle that can see 
the future. For a regulated exchange, it is important to guarantee that all the receivers 
of market data get that data at the same time. Why is this important ? For example, the 
MDP holds a list of data subscribers, and the order of the subscribers is decided by the 
order in which they connect to the publisher , with the first one always receiving data 
first. Guess what happens, then ? Smart clients will fight to be the first on the list when 
the market opens. 
There are some ways to mitigate this. Multicast using reliable UDP is a good solution to 
broadcast updates to many participants at once. The MDP could also assign a random 
order when the subscriber connects to it. We look at multicast in more detail. 
Multicast 
Data can be transported over the internet by three different types of protocols. Let's take 
a quick look. 
1. Unicast: from one source to one destination. 
2. Broadcast: from one source to an entire subnetwork. 
3. Multicast: from one source to a set of hosts that can be on different subnetworks . 
410 I Chapter 13. Stock Exchange 


[Page 412]
Multicast is a commonly-used pro toco l in rx chan ge design. By configurin g scvern l re 
ceivcrs in the sa me multi cas t gro up, th ey will in the ory receive data al the sAme tim e. 
Howevn UDP is an unreliable protocol and th e datl'lgrnm might nol rea ch all the re¡
ceivers. There are solutions to handl e retransmis sion (291. 
Colocation 
\Vlule we are on th e subject of fairness, il is a fact that a lot of exchang es offer coloca¡
tion services. which put h edge funds or brokers' servers in the same data center as the 
e ╖change. The latency in placing an order to the matching engine is essentially propor ¡
tional to the lengt h of the cable. Colocation does not break the notion of fairness. It can 
hr conside red as a paid-for VIP service. 
Network security 
An e ╖change usually provides some public interfaces and a DDoS attack is a real chal¡
lenge. Here are a few techniques to combat DDoS: 
t. Isolate pub lic services and data from private services , so DDoS attacks don 't impact 
the most important clients . In case the same data is served, we can have multiple 
read-o nly copies to isolate problems. 
2. Use a caching layer to store data that is infrequently upd ated. With good caching, 
most queries won 't hit databases. 
3. Harden URLs against DDoS attac ks. For example, with an URL like https://my. 
website.com/data?from=123&to=456, an attacker can easily generate many differ¡
ent requests by changing the query string. Instead , URLs like this work better: 
https: // my.website. com/ data/ recent. It can also be cached at the CDN layer. 
4. An effective safelist/blocklist mechanism is needed. Many network gateway prod¡
ucts provide this type of functionality . 
5. Rate limiti ng is frequently used to defend agains t DDoS attacks. 
Step 4 - Wrap Up 
After reading this chapter , you may come to the conclusion that an ideal deployment 
model for a big exc hange is to put everything on a sing le gigantic server or even one 
single process. Indeed , this is exactly h ow some exchanges are designe d! 
With the recent development of the cryptocur rency industry , many crypto exchanges u se 
cloud infrastructure lo deplo y their services [30]. Some decentralized finance proj ec ts are 
based on the notion of AMM (Automatic Market Making) and don 't even need an order 
book. 
The convenience provided by the cloud ecosystem changes some of the design s and low¡
ers the thresho ld for entering the industry. This will sure ly inject innovativ e e nergy into 
the financial world . 
Congratulations on getting this far! Now give yourself a pat on the back . Good job! 
Step 4 - Wrap Up I 411 
. -


[Page 413]
Chapter Summary 
step l 
step 2 
Stock Exchange 
step 3 
llVallAhilily: nfl fl!J3 
filu It lolrrnncr 
nnn -funclinna l rcq 
milliscco nd-levr l lntr ncy 
securit y 
< 
I 00 symbols 
es tim ation 
2 t 5k pc11k QPS 
L trading Oow 
high-lm l d"ign '\_ m"ket dolo llow 
reporting Oow 
order 
execution 
api design 
order book 
historica l pri ces 
L produ ct, order, execution 
data model ~ order book 
performanc e candlestick chart 
eve nt sourcing 
high availability 
fault tolerance 
matching algo rithm s 
determinism 
mark et data publish er optimi zation 
fairness 
multic ast 
colocation 
network secu rity 
step 4 - - wrap up 
412 I Chapter 13. Stock Exchange 


[Page 414]
Reference Material 
[l] LMAX exchange was famous for its open-source Disruptor. http s://www .lmax.com 
/exchange . 
[2) JEX attracts investors by "playing fair", also is the "Flash Boys Exchan ge". htt ps: 
//en.wikipedia.org /wiki /IEX. 
[3] NYSE matched volume. http s://www.nyse .com/markets /us-equity-volumes. 
[ 4) HKEX daily trading volume. http s://www .hkex.eom.hk/Market- Data /Stat.istics/C 
onsolidated-Reports /Securities-Statistics -Archive/Trading_ Value_ Volume_And_N 
um her_ Of_ Deals? sc _ lang=en #selectl =0. 
[5] All of the World's Stock Exchanges by Size. http: //money .visuakapitalist.com /all 
-of-the-worlds-stoc k-exchanges-by-size /. 
[ 6] Denial of service attack https ://en.wikipedia.org/wiki /Denial-of-service _attack. 
[7] Market impact. https: //en. wikipedia.org /wiki/Market_impact. 
[8] Fix tradin g. https: //www .fixtrading.org/. 
[9] Event Sourcing. https :/ /martinfowler.com /eaaDev/EventSourcing.html. 
[10] ClvlE Co-Location and Data Center Services. https ://www.cmegroup .com/trading 
/colocation /co-location-services .html. 
[11] Epoch . https: //www.epochlOl.com/. 
[ 12] Order book. https ://www .investopedia.com/terms / o/ order-book.asp. 
[13] Order book https ://en.wikipedia.org /wiki/Order_book. 
[14] How to Build a Fast Limit Order Book. https://bit.ly/3ngMtEO. 
[15] Developing with kdb+ and the q language . https: //code.kx.com/q/. 
[16] Latency Numbers Every Programmer Should Know. https: //gist.github.corn/jboner 
/2841832. 
[17] rnmap. https: //en.wikipedia.org /wiki/Memory _map. 
[18] Context switc h. https ://bit.ly/3pva7A6. 
[19] Reliable User Datagram Protocol. https ://en.wikipedia.org/wiki/Reliable_User_Dat 
agram_Protocol. 
[20] Aeron. https ://github .com/real-logic/aeron/wiki/Design-Overview. 
[ 21] Chaos engineering. https :/ I en. wikipedia.org/wiki/Chaos_ engineering. 
[22] Raft. https: //raft .github.io /. 
[23) Designing for Understandability: the Raft Consensus Algorithm. http s:/ /raft.githu 
b.io/slides/uiuc2016.pdf . 
Reference Material I 413 


[Page 415]
I 
[24) Supp orted MAtching Algori thm s. hltps ://hit.1 naYoCEo 
(25) Dark pool. https : /www invC'stnpC'<liA.com / lcnn s/d/<lark pool.asp. 
[26] HdrHistog:ram : A High Oynmnic Rant?;C' Histogram . http ://hdrhi slogrnm .org/. 
[27] HotSpot (virtual machine) . htlps ://<'11.\: ikipc clia .org /wiki /Ilo tSpol _(virtual_mAchi 
ne ). 
[2R] C'achC' line padding . https: / /b1t.l /3lZTI:Wz . 
[29) NACK -Oriented Reliable Multicast. htlps ://en.wikipcdia .org/wiki/NACK -O rie nte 
d_Reliable _ 1ulticast . 
[30] AV1,-..... Coinbasr Case tudy . htlps ://aws.amazon.co m /solu tions/case -studi es/coinba 
se . 
414 I Chapter 13. Stock Exchange 


[Page 416]
Afterword 
Congra lulations! You h ave completed this interview guide. You have accumulated skills 
and know ledge v.rith which l o design complex systems. Not everyone has the disciplin e 
to do what you h ave done, to learn whal you have learned. Take a moment to pat yourself 
on lhe back. Your hard work will pay off. 
Landing your dream job is a long journey and requires lots of time and effort. Practi ce 
makes perfect. Best of luck! 
Thank you for buying and reading this book. Without readers like you, our work would 
not exist. We hope you have enjoyed the book! 
If you have comments or questions about this book, feel free to send us an email at 
hi@byte bytego.co m. If you notice any error s, please let us know so we can make correc¡
tions for the next edition . Thank you! 
Join the community 
We crea ted a m embers-only Discord group. It is designed for community discussions on 
the following topics: 
ò System d esign fundamentals. 
ò Showcasing design diagrams and getting feedback. 
ò Finding mock interview buddies. 
ò General chat with community members. 
Come join us and introdu ce yourself to the community, today! Use the link below or 
scan the QR code. 
http: //bit.ly/systemdiscord 
Reference Material I 415 


[Page 417]
416 I Chapter 13. Stock Exchange 


[Page 418]
Index 
Symbols 
2PC,22 1, 346, 347, 349- 351 
A 
N' pathfinclin g algorithm s, 64, 84 
ACID, 199,2 10, 219,221 , 321 
Aclive MQ, 92 
adjacency lists, 77 
Advance d M essage Queuing Protoco l, 
125 
Aeron, 405 
aggregati on window , 164, 176 
Airbnb, 195, 201, 337 
Amazo n, 137, 201, 317 
Amazon API Gateway, 304 
Amazon W eb Services, 253, 303 
AML/CIT, 318 
AMM, 411 
AMQP, 125 
Apache James, 232 
append-only,3 62, 366 
Apple, 395 
Apple Pay, 315 
application loop, 400 
ask price, 382 
asynchron ous, 328 
At-least once, 122 
at-leas t once, 93, 123 
at-leas t-on ce, 331 
at-most once, 93, 122 
at-most-on ce, 331 
ato mic commit , 167 
atomic operation, 220 
audit, 360 
- - -╖ -
Autom atic Mark et Making, 411 
Availability Zone, 255 
Availability Zones , 271 
availability zones , 28 
AVRO, 165 
A\VS,253, 303, 304 
A \VS Lambda, 304 
AZ, 271 
B 
B+ tre e, 269 
Backblaze, 274 
base32, 12 
BEAM, 55 
bid price, 382 
Bigtable, 137,237 , 245 
Blue/green deployment, 19 
brokers, 95, 96, 98, 102, 104- 106, 113, 
118, 120, 122 
buy order, 395 
c 
California Consumer Privacy Act, 
2 
candlestick chart, 383 
candlestick charts, 385, 388, 398, 
409 
CAP theorem, 79 
Index I 417 


[Page 419]
Card schemes, 318 
card verificalion va lue. 336 
cartesian tiers . 9 
Cassandra , 45, 70, 77, 79. 137, 152. 186, 
233.237.245.3 09 
CCPA, 2. 36 
CDC, 218 
CDN. 72- 74, 76, 201. 411 
Ceph, 260 
change data captur e, 218 
Channel, 41 
channel, 41-43, 46-54 
channels, 41 
Chaos engineering, 406 
Charles Schwab , 382 
checkslll11, 275, 276, 283, 284 
che cksmn s, 275 
Choreography, 354 
circu lar buffer, 410 
click-t hrough rate, 159 
ClickHo use, 189 
CloudWatch, 143 
cluster, 39, 40, 51, 55 
CME, 408 
CockroachDB, 335 
Colocation, 411 
collll11nar databa se, 398 
Command , 356 
Command-query responsibility 
segregation , 360 
commission rebate , 382 
compensating transaction , 34 7 
compensation, 350 
Consistent hashing , 266 
consistent hashing , 49 
Consumer group, 96 
consumer group , 95, 96, 106 
content delivery network , 201 
conversion rate , 159 
CQRS, 361, 364, 368, 373, 375 
CRC, 101 
ere, 100 
cross engine, 386 
CTR, 159 
418 I Chapter Index 
~ ........... __________ ~ 
CVR. 159 
CVV, 336 
Cyclic redu ndan cy check, 101 
D 
DAG, 167, 170 
daily active users, 290 
dark pool, 408 
Database constraints, 211 
Datadog, 132 
D.AU,37, 59, 68, 161,290,310,312 
DB-engines, 137 
DBA, 320 
DDD, 355 
DDoS, 336, 381, 411 
Dead letter queue, 330 
Deadlo cks, 212 
Debezium , 218 
determinism , 404 
Dijkstra , 64 
directed acyclic graph , 16 7 
Discovery, 318 
distributed denial-of-service , 381 
distributed transaction , 181, 371 
DKIM, 242 
DMARC, 242 
DNS, 6, 28, 227, 229 
Domain name service , 227 
Domain-Driven Design, 355 
DomainKeys Identified Mail, 242 
DoorDash, 88 
double-entry, 322 
double-reservation, 206 
Downsampling, 150 
Druid , 189 
DynamoDB , 309, 310 
E 
E*Trade, 382 
ElasticSearch , 189 
Elasticsearch, 22, 133, 244 
Elixir, 55 
ELK, 133 
equator, 10 
/ 


[Page 420]
-
eras ure codin g, 271 - 274, 276 
Erlang. 55 
ETA 59 
etcd. 48. 98. 140 
even grid. 9 
Event sourci ng, 343, 357, 361, 365 
event sourcing,355 - 357, 359-362, 364, 
365, 367-369,37 1-373,37 5, 
387, 401- 403 
even t store, 399. 406 
even t., 356 
eventuall y consistent , 361 
Exactly once, 123 
exaclly once, 93, 167, 181 
exactly-o nce, 325, 331 
exchange,379-382,38 4, 385, 387-390, 
398, 399,404,408,409, 
411 
Exponential backoff , 235, 332 
F 
Facebook , 132, 159, 160 
fault-tolerance, 331 
FC, 254 
Fibre Channel, 254 
Fidelity, 382 
FIF0,95 , 356, 358,408 
fills, 385, 386 
financial instrument , 395 
First In First Out, 408 
FIX, 384, 402 
FIX protocol , 384 
fixed window , 177 
Flink, 146, 190 
G 
Garbage collection, 284 
garbage collection , 409 
GDPR, 2, 36, 247 
General Data Prot ec tion Regulatio n, 
2 
Geoco ding, 62 
geoco ding, 76, 83 
geofe n ce, 21 
Geofc ncing, 21 
geofenci ng, 21 
geograp hic informa tion systems, 
62 
Geohash, 7, 10-13 , 22 
geohas h, 9, 10, 12, 13, 15, 22, 25- 27, 
29-31, 53,54 
Geohashing, 13, 62, 63 
geohashing, 63, 72, 75 
geospatial , 4, 9 
geos patial databases, 7 
geospatial ind exing, 9 
GIS, 62 
Global-Local Aggrega tion, 187 
grn:map lOl , 60 
Gmail, 228, 241 
Goog le, 21, 132, 160 
Goog le Cloud, 304 
Goog le Cloud Functions, 304 
Goog le Design, 80 
Goog le Finan ce, 409 
Goog le Maps, 1, 22, 59, 62, 68, 70, 80, 88, 
89 
Goog le Pay, 315 
Goog le Places API, 4 
Goog le 52, 9, 20 
Gorilla, 14 7 
gPRC, 202 
Grafana , 153 
Grap hite , 143 
gRPC, 264 
H 
Hadoop, 137 
hard disk drives, 253 
hash ring, 49, 50, 52 
hash slot, 306 
hash table, 344 
HBase, 137 
HDD, 253 
HDFS, 126, 179, 180,364 
HdrHistogram, 409 
heartbeats, 107 
hedge fund , 382 
Index I 419 


[Page 421]
hedge funds . 409. 411 
Hierarchical time w heel, 125 
Hilbert curve , 20 
Hive . 189 
HKEX , 379 
HMAC. 275 
hopping window. 177 
hot -warm. 405 
hot pot. 186 
Hol pot JVM, 409 
lAM. 259 
Idempotency. 333 
idempolen cy, 198, 206, 208, 320, 331, 
333-336 
IN\AP, 226,227, 230 
imrnutable , 359, 362, 364,366 
In-sync Repli cas, 112 
In-sy nc rep licas, 113 
InfluxDB , 137, 148, 149 
in ode, 258, 26 7 
Institutional client , 382 
Internet Mail Access Protoco l, 
227 
interpolation , 62 
inverted index , 233 
IOPS, 237, 256 
iSCSI, 254 
isolation , 210 
ISP, 243 
ISR, 113, 114, 116, 117 
J 
]MAP, 232 
]SON , 25, 164 
]SON Meta App lication Protocol, 
232 
]WZ algorithm, 240 
K 
k-nearest , 1, 23 
Kafka, 71,80, 85, 92, 111, 125, 146, 147, 
152, 153, 166, 167, 169, 178, 
420 I Chapter Index 
179. 183, 187. 188, 190 , 244, 
294. 329 33 1, 358. %2, 365, 
387, 401 . 402 
Knppl\ flrchilcclurc, 173, 171 
KDB. 398 
keep-alive, 71 
Kiban::l, 133 
Know Your Client , 381 
KYC, 381 
L 
lambda, 173 
Latitude , 61 
latilud e, 3,8 , 62,75 , 82, 83 
LBS, 2,5,6 , 16,30,31 
Lead Mark et Maker , 408 
leade r election, 406 
Leas t Recently Use d, 217 
levels, 12 
limit orde r, 380, 382 
link ed list, 47 
Linkedln , 257 
LMM, 408 
load balan cer, 6 
Location-base d serv ice, 6 
loca tion -based service, 2, 5 
lock. 211 
lock contentio n, 400, 403 
lock-free , 410 
Log-S tru ctured Merge-Tr ee, 245 
log-str uctur ed m erge-tree , 363 
Logstash , 133 
long polling , 87, 232 
longitude, 3, 8, 61, 62, 75, 82, 83 
low latency , 382 
LRU, 217 
LSM,245 ,363 
Lyft, 22, 88 
M 
market data publi sher, 388, 409 
market making , 382 
market order, 381, 382 
Marriott International , 195 
-


[Page 422]
MasterCard, 318, 324 
matching engine , 385- 388, 393, 395, 
404. 405, 409, 411 
MAU, 290, 302 
MDS, 275 
mdS, 283 
N\DP,388,409,4 10 
Mercator proj ection, 62 
meridian, 1 O 
message store, 403 
Metr icsDB, 137 
Microservice , 220 
rnicroservice , 201, 203,2 19-22 1, 
353-355 
Microsoft, 304 
Microsoft Azure Function s, 304 
Microsoft Exchange, 245 
Microsoft Outlook, 227 
MIME, 228 
nunap , 362, 399, 401, 403, 406 
mmap(2), 401 
MongoDB , 22, 309 
monolithic , 219 
monthly active users, 290 
multicast, 411 
Mult ipurpose Internet Mail Extension , 
228 
MX reco rd, 227 
MySQL, 4, 99, 136, 211, 216, 237, 303, 
306, 309,3 13 
N 
Nasdaq , 379 
Netflix, 201 
NewSQL, 321 
NFS, 254 
NOP, 348, 349, 352 
NoSQL, 41, 79, 99, 137, 165, 233, 237, 
240,295,3 03, 309,3 12, 
321 
NYSE, 379, 381 
0 
Offi.ce365, 241 
offset, 95, 100, l 04, I 06, 110, 111. 1t 3. 
122 
OLAP, 164, 189 
OpenTSDB, 135, 137 
Optimistic locking, 211, 213, 214 
ORC, 165 
Orchestration , 354 
order b ook, 380, 381, 386, 388, 392, 395, 
397, 409 
OTP, 55 
Out-of-order, 353 
out- of-order , 350, 352, 353 
p 
PagerDuty , 132, 152 
Pagination , 3 
Parquet , 165 
Partition , 121 
partition , 95, 97, 99- 104, 106-108 , 
111- 114, 116- 121 
Paxos , 265,335 
payload , 255 
Payment Service Provider , 318 
PayPal , 315, 322,333,341 
PCI DSS, 322, 336 
peer-to-peer , 3 7 
pension fund , 382 
percentile , 381, 398, 400, 409 
pers onally identifiable informati on, 
247 
Pessimistic locking, 211 
pessimistic locking, 211 
PII, 247 
point of presence, 73 
POP, 73, 226, 227, 229, 230 
Post Office Prot ocol, 227 
PostGIS, 7 
Postgres, 7 
PostgreSQL, 23 7 
precision, 22 
pri ce level, 395 
Prometheus, 135, 148 
PSP,318- 327, 333-336 
Pull model, 105 
Index I 421 


[Page 423]
ru l!'ar. 02 
r'u . h model. I 04 
pu. h mc1dcl. 142 
Q 
qu.,dranl.. l 6 
qtrnd trcc. 9. 16- 19. 22, 23, 25- 27, 
31 
R 
Rabbit 1Q. 92. 93 
rack. 2 0 
Radiu . 13 
radrn. 1-3. 6. 7, 13, 15. 21, 30 
Rado Gateway . 260 
Raft.265.335.366-368 , 373, 375, 406, 
407 
RAID. 100 
Rate limiting , 336 
RDS.295. 296 
read-only , 361 
Real-Time Biddin g, 159 
reconciliatio n, 327 
Recovery Point Objective , 405, 
407 
Recovery Time Objective , 405, 
407 
redirect URL, 325, 326 
Redis , 7, 22, 27, 28,3 0, 31, 40, 45, 47,48, 
56, 217, 218, 233, 295, 297,3 00, 
302-306, 308, 309,3 12,3 13, 
344, 345, 355,374 
Redis Pub/Sub, 41- 43, 46- 52, 
54- 56 
Region Cover algorithm , 22 
reliable UDP, 405 
Reprod u cibili ty, 359, 360 
RESTful , 3, 197, 231, 234, 236, 253- 255, 
259, 264, 304,319,343, 
390 
RESTful API, 39, 40, 45, 56 
retail clie nt, 382 
Retrya ble failur es, 331 
return on inves tment, 177 
422 I Chapter Index 
reverse pro xy. %9 
rin g buffer , 403 
ring buffer s, 410 
risk manager , 385 
Robin hood, 382 
RockcLMQ, 92. 125 
RocksDB, 245, 269, 363 
ROI, 177 
round Lrip latency, 381 
round -ro bin , 106 
Roulin g tiles, 65, 66 
routin g tiles. 64, 65, 77, 80, 84- 86 
RPC, 202 
RPO, 405, 407 
RTB, 159, 160, 188 
RTO, 405, 407 
RTree, 9 
s 
S2, 21, 22 
S3, 77, 78, 165, 179, 180, 233, 235, 237, 
248, 253- 256, 278 
Saas, 132 
Saga,22 1, 353- 355,3 71- 373, 375 
SATA, 256 
search radiu s, 40, 41, 43, 44, 46 
sec urit y, 395 
segments, 99 
sell order, 382, 395 
Send er Policy Fram ework , 242 
sequencer, 385- 387, 394, 399, 403, 
408 
seriali zable, 210 
Ser ver-Se nt Events, 87 
Servi ce Discovery, 140 
session wind ow, 177 
SHAl , 275 
shard , 45, 47 
sharding, 24- 26, 31, 45, 47, 48, 95, 205, 
221,277, 305, 310, 312, 344, 
345 
shortest -path , 84 
Simple Mail Transf er Protocol , 
227 


[Page 424]
Simp le Storage Service, 253 
sing le-poin t-of-failure . 404 
sing le-threaded, 400 
skip list . 297, 299 
LA 255 
Liding window , 177 
MB/CIFS. 254 
SMTP, 226, 227, 229, 230, 
234- 236 
snaps ho t, 188, 364 
solid -state drives , 253 
sorted, 297 
Sorted se ts, 299 
Spark, 146, 190 
PF, 242 
Split Dis tinct Aggregatio n, 187 
split vote, 407 
Splunk , 132 
SQLite, 269, 363 
SSD, 253 
SSE, 87 
SSL, 336 
SSTable, 269 
star schema, 172 
state , 357 
state machine, 354, 357-359 , 361, 364, 
370 
Statista, 241 
Stop-the-World , 409 
Storm , 146 
Stripe, 315,32 5, 333 
symbo l, 386 
synchronous , 328 
T 
TC/C,347 - 355,37 1,375 
term, 407 
Tight coup ling, 329 
TikTok, 159 
Time to Live, 40 
time-to-live , 217 
Timestream , 13 7 
Tinder, 21, 22 
Tipalti, 323 
-
lnp-k shortest pnlhs. R4 
Topic, 96 
topic, 94- 101, 11 ::\, 11 6, 11 8, 11 9, 
121- 123 
Topics. 94 
topics , 41 , 95-98, 123, 124 
trading hours, 380 
Try -Confirm/Cancel, 347 
TTL, 40, 45- 47, 217 
tumbling window , 177 
Twit ter, 137, 201 
Two-p hase commit , 221 
two -phase commit, 346 
u 
Uber, 88, 201, 337 
UDP, 411 
UNIX, 257, 258, 401 
v 
virtual private network, 202 
Visa, 318, 324 
VPN, 202 
w 
WAL, 99, 100, 268 
watermark, 177 
Web Mercator , 62 
WebGL, 81 
webhook, 325 
WebSocket ,3 9- 47, 49-56 ,87, 232, 
236 
write shardin g, 310 
Write -ahead log, 99 
writ e-ahead log, 268 
x 
X/Open XA, 34 7 
y 
Yahoo Mail, 241 
YAML, 151 
YARN, 185 
Yelp, 1, 30, 178 
Index I 423 


[Page 425]
Yelp business endpoi nts. 4 
Yexl, 19 
YouTube , 159 
Yui;abytcDB . 335 
424 l Chapter Index 
z 
ZrroMQ. 92 
ZooKecprr. 4 8, 98, 99. 1 l l , J 12. 140, 344, 
345 


[Page 426]
Made in United States 
North Haven. CT 
20 September 2022 
11111111111m11111~ 11m1 
24375513 R00239 


[Page 427]

