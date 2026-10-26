# Census Data API User Guide
# https://www.census.gov/content/dam/Census/data/developers/api-user-guide/api-guide.pdf 

import os
import sys
### add system path to get other library directories
sys.path.append('Data/gva_gen/gen_files/')

import pandas as pd
import sys
import requests
from create_city_list import city_list
city_list

# Census API places to search from
places_orig = [["NAME","B01001_001E","state","place"],
["O'Fallon city, Missouri","93651","29","54074"],
["St. Louis city, Missouri","293310","29","65000"],
["Passaic city, New Jersey","69637","34","56550"],
["Nashua city, New Hampshire","91122","33","50260"],
["Rochester city, Minnesota","121471","27","54880"],
["Paterson city, New Jersey","157783","34","57000"],
["Warren city, Michigan","138142","26","84000"],
["Lee's Summit city, Missouri","102506","29","41348"],
["Gastonia city, North Carolina","81159","37","25580"],
["Minneapolis city, Minnesota","425338","27","43000"],
["East Orange city, New Jersey","68893","34","19390"],
["Westland city, Michigan","84528","26","86000"],
["Elizabeth city, New Jersey","135405","34","21000"],
["Cary town, North Carolina","178508","37","10740"],
["Fargo city, North Dakota","124843","38","25700"],
["St. Cloud city, Minnesota","69809","27","56896"],
["Las Cruces city, New Mexico","112907","35","39380"],
["Springfield city, Missouri","169850","29","70000"],
["Wyoming city, Michigan","76747","26","88940"],
["St. Paul city, Minnesota","307176","27","58000"],
["Charlotte city, North Carolina","879697","37","12000"],
["Buffalo city, New York","276804","36","11000"],
["Rochester Hills city, Michigan","76021","26","69035"],
["Woodbury city, Minnesota","76994","27","71428"],
["Omaha city, Nebraska","487299","31","37000"],
["Concord city, North Carolina","107688","37","14100"],
["Bayonne city, New Jersey","69195","34","03580"],
["Albany city, New York","98624","36","01000"],
["Bismarck city, North Dakota","74141","38","07200"],
["Jacksonville city, North Carolina","72881","37","34200"],
["Albuquerque city, New Mexico","562591","35","02000"],
["Greensboro city, North Carolina","298250","37","28000"],
["Greenville city, North Carolina","88733","37","28080"],
["Independence city, Missouri","122083","29","35000"],
["Asheville city, North Carolina","94070","37","02140"],
["Newark city, New Jersey","307216","34","51000"],
["High Point city, North Carolina","115287","37","31400"],
["Southfield city, Michigan","75901","26","74900"],
["Durham city, North Carolina","285439","37","19000"],
["Kansas City city, Missouri","508415","29","38000"],
["Cheektowaga CDP, New York","76676","36","15000"],
["Sterling Heights city, Michigan","133256","26","76460"],
["Camden city, New Jersey","71771","34","10000"],
["Akron city, Ohio","189343","39","01000"],
["Plymouth city, Minnesota","79833","27","51730"],
["Jersey City city, New Jersey","283943","34","36000"],
["St. Charles city, Missouri","70832","29","64082"],
["Clifton city, New Jersey","89382","34","13690"],
["Troy city, Michigan","86837","26","80700"],
["Fayetteville city, North Carolina","208792","37","22920"],
["St. Joseph city, Missouri","75763","29","64550"],
["Manchester city, New Hampshire","115470","33","45140"],
["Lakewood CDP, New Jersey","66405","34","38580"],
["Coral Springs city, Florida","132822","12","14400"],
["Bridgeport city, Connecticut","148345","09","08000"],
["Davie town, Florida","104873","12","16475"],
["Daytona Beach city, Florida","74435","12","16525"],
["Deerfield Beach city, Florida","86355","12","16725"],
["Delray Beach city, Florida","66579","12","17100"],
["Deltona city, Florida","95771","12","17200"],
["Doral city, Florida","75954","12","17935"],
["Fort Lauderdale city, Florida","181666","12","24000"],
["Fort Myers city, Florida","92244","12","24125"],
["Washington city, District of Columbia","670050","11","50000"],
["Anchorage municipality, Alaska","288121","02","03000"],
["Alafaya CDP, Florida","95779","12","00410"],
["Boca Raton city, Florida","95785","12","07300"],
["Boynton Beach city, Florida","80083","12","07875"],
["Brandon CDP, Florida","116994","12","08150"],
["Cape Coral city, Florida","204519","12","10275"],
["Clearwater city, Florida","116667","12","12875"],
["Charleston city, South Carolina","152046","45","13330"],
["Schenectady city, New York","66985","36","65508"],
["Arlington city, Texas","392802","48","04000"],
["Rock Hill city, South Carolina","74107","45","61405"],
["Reading city, Pennsylvania","94834","42","63624"],
["Lubbock city, Texas","260990","48","45000"],
["Sammamish city, Washington","66630","53","61115"],
["Kenosha city, Wisconsin","99285","55","39225"],
["Pearland city, Texas","120694","48","56348"],
["Racine city, Wisconsin","77131","55","66000"],
["Cleveland city, Ohio","368006","39","16000"],
["Eugene city, Oregon","175102","41","23850"],
["Medford city, Oregon","86374","41","47000"],
["Raleigh city, North Carolina","469502","37","55000"],
["Greenville city, South Carolina","72103","45","30850"],
["Atascocita CDP, Texas","85808","48","04462"],
["Carrollton city, Texas","132569","48","13024"],
["Sioux Falls city, South Dakota","196528","46","59020"],
["Provo city, Utah","114085","49","62470"],
["Denton city, Texas","148139","48","19972"],
["Carolina zona urbana, Puerto Rico","141050","72","14290"],
["Richmond city, Virginia","226604","51","67000"],
["Roanoke city, Virginia","98865","51","68000"],
["Seattle city, Washington","733904","53","63000"],
["McAllen city, Texas","143922","48","45384"],
["McKinney city, Texas","202680","48","45744"],
["Pflugerville city, Texas","66700","48","57176"],
["Pharr city, Texas","79697","48","57200"],
["Lawton city, Oklahoma","91058","40","41850"],
["Austin city, Texas","964000","48","05000"],
["Cedar Park city, Texas","78326","48","13552"],
["Centreville CDP, Virginia","75010","51","14440"],
["Fort Worth city, Texas","940437","48","27000"],
["Houston city, Texas","2287047","48","35000"],
["Mansfield city, Texas","74106","48","46452"],
["South Hill CDP, Washington","66875","53","65922"],
["Plano city, Texas","287037","48","58016"],
["Columbus city, Ohio","907310","39","18000"],
["Mount Pleasant town, South Carolina","92398","45","48535"],
["Murfreesboro city, Tennessee","157509","47","51560"],
["Nashville-Davidson metropolitan government (balance), Tennessee","678845","47","52006"],
["St. George city, Utah","99965","49","65330"],
["Chesapeake city, Virginia","251269","51","16000"],
["Edinburg city, Texas","102477","48","22660"],
["Auburn city, Washington","87061","53","03180"],
["Frisco city, Texas","210735","48","27684"],
["Kennewick city, Washington","84478","53","35275"],
["Kent city, Washington","134837","53","35415"],
["Spokane city, Washington","229065","53","67000"],
["Spokane Valley city, Washington","105912","53","67167"],
["Columbia city, South Carolina","137960","45","16000"],
["Parma city, Ohio","79984","39","61000"],
["Jackson city, Tennessee","68114","47","37640"],
["Salt Lake City city, Utah","200475","49","67000"],
["Sandy city, Utah","95038","49","67440"],
["Bellevue city, Washington","149429","53","05210"],
["Garland city, Texas","241870","48","29000"],
["Kirkland city, Washington","92105","53","35940"],
["Beaverton city, Oregon","98204","41","05350"],
["Bend city, Oregon","102079","41","05800"],
["Cranston city, Rhode Island","82568","44","19180"],
["Wilmington city, North Carolina","117642","37","74440"],
["Erie city, Pennsylvania","94013","42","24000"],
["Johnson City city, Tennessee","70889","47","38320"],
["Yonkers city, New York","209506","36","84000"],
["Toledo city, Ohio","268504","39","77000"],
["South Jordan city, Utah","80142","49","70850"],
["Bellingham city, Washington","92290","53","05280"],
["El Paso city, Texas","678422","48","24000"],
["Georgetown city, Texas","75407","48","29336"],
["Appleton city, Wisconsin","72951","55","02375"],
["Irving city, Texas","254190","48","37000"],
["Laredo city, Texas","258014","48","41464"],
["Mesquite city, Texas","148087","48","47892"],
["Tacoma city, Washington","219203","53","70000"],
["Midland city, Texas","131292","48","48072"],
["Santa Fe city, New Mexico","88196","35","70500"],
["Winston-Salem city, North Carolina","250337","37","75000"],
["Pawtucket city, Rhode Island","75379","44","54640"],
["Providence city, Rhode Island","189697","44","59000"],
["Abilene city, Texas","129601","48","01000"],
["North Charleston city, South Carolina","117463","45","50875"],
["Layton city, Utah","83299","49","43660"],
["Lehi city, Utah","79979","49","44320"],
["Dale City CDP, Virginia","79782","51","21088"],
["Hampton city, Virginia","137746","51","35000"],
["Madison city, Wisconsin","269162","55","48000"],
["Mission city, Texas","86215","48","48768"],
["Missouri City city, Texas","76462","48","48804"],
["Richardson city, Texas","116369","48","61796"],
["Warwick city, Rhode Island","83014","44","74300"],
["Rochester city, New York","210594","36","63000"],
["Knoxville city, Tennessee","192657","47","40000"],
["League City city, Texas","114664","48","41980"],
["Leander city, Texas","68993","48","42016"],
["Ponce zona urbana, Puerto Rico","112005","72","63820"],
["Waukesha city, Wisconsin","71254","55","84250"],
["Gresham city, Oregon","113106","41","31250"],
["Dayton city, Ohio","137581","39","21000"],
["Allentown city, Pennsylvania","125934","42","02000"],
["Portland city, Oregon","642218","41","59000"],
["Bethlehem city, Pennsylvania","75134","42","06088"],
["Tulsa city, Oklahoma","411905","40","75000"],
["Baytown city, Texas","79676","48","06128"],
["Brownsville city, Texas","187840","48","10768"],
["Alexandria city, Virginia","154706","51","01000"],
["Grand Prairie city, Texas","197338","48","30464"],
["Everett city, Washington","110820","53","22640"],
["Philadelphia city, Pennsylvania","1576251","42","60000"],
["Newport News city, Virginia","184587","51","56000"],
["Green Bay city, Wisconsin","107020","55","31000"],
["Lewisville city, Texas","112853","48","42508"],
["Vancouver city, Washington","192176","53","74060"],
["Milwaukee city, Wisconsin","569326","55","53000"],
["Round Rock city, Texas","127130","48","63500"],
["Hillsboro city, Oregon","106651","41","34100"],
["Franklin city, Tennessee","85473","47","27740"],
["Beaumont city, Texas","112559","48","07000"],
["Bryan city, Texas","86851","48","10912"],
["College Station city, Texas","120032","48","15976"],
["Federal Way city, Washington","99028","53","23515"],
["Pittsburgh city, Pennsylvania","300454","42","61000"],
["Norfolk city, Virginia","235089","51","57000"],
["Guaynabo zona urbana, Puerto Rico","72088","72","32522"],
["Pasco city, Washington","84190","53","53545"],
["Suffolk city, Virginia","96194","51","76432"],
["San Angelo city, Texas","101063","48","64472"],
["San Antonio city, Texas","1451863","48","65000"],
["San Marcos city, Texas","68578","48","65600"],
["Broken Arrow city, Oklahoma","117775","40","09050"],
["Mount Vernon city, New York","72584","36","49121"],
["Allen city, Texas","106868","48","01924"],
["Arlington CDP, Virginia","232965","51","03000"],
["Conroe city, Texas","94401","48","16432"],
["New Braunfels city, Texas","96630","48","50820"],
["Canton city, Ohio","70438","39","12000"],
["Salem city, Oregon","177727","41","64900"],
["West Jordan city, Utah","116544","49","82950"],
["West Valley City city, Utah","139094","49","83470"],
["Harlingen city, Texas","71928","48","32372"],
["Killeen city, Texas","156260","48","39148"],
["Scranton city, Pennsylvania","75867","42","69000"],
["San Juan zona urbana, Puerto Rico","320456","72","76770"],
["Yakima city, Washington","96565","53","80010"],
["Spring CDP, Texas","71893","48","69596"],
["Norman city, Oklahoma","128087","40","52500"],
["Chattanooga city, Tennessee","182111","47","14000"],
["Amarillo city, Texas","198781","48","03000"],
["Rapid City city, South Dakota","76173","46","52980"],
["Corpus Christi city, Texas","317768","48","17000"],
["Longview city, Texas","81877","48","43888"],
["North Richland Hills city, Texas","70212","48","52356"],
["Sugar Land city, Texas","109337","48","70808"],
["Temple city, Texas","85428","48","72176"],
["Toms River CDP, New Jersey","93947","34","73110"],
["Trenton city, New Jersey","90458","34","74000"],
["Lorain city, Ohio","65440","39","44856"],
["New Rochelle city, New York","81590","36","50617"],
["New York city, New York","8467513","36","51000"],
["Oklahoma City city, Oklahoma","687691","40","55000"],
["Clarksville city, Tennessee","170966","47","15160"],
["Bayam zona urbana, Puerto Rico","168592","72","06593"],
["Cheyenne city, Wyoming","65048","56","13900"],
["Redmond city, Washington","76360","53","57535"],
["Renton city, Washington","105200","53","57745"],
["Virginia Beach city, Virginia","457672","51","82000"],
["Odessa city, Texas","116436","48","53388"],
["Oshkosh city, Wisconsin","66594","55","60500"],
["The Woodlands CDP, Texas","116251","48","72656"],
["Tyler city, Texas","107199","48","74144"],
["Union City city, New Jersey","65639","34","74630"],
["Syracuse city, New York","146124","36","73000"],
["Memphis city, Tennessee","628118","47","48000"],
["Ogden city, Utah","86800","49","55980"],
["Marysville city, Washington","71151","53","43955"],
["Portsmouth city, Virginia","97840","51","64000"],
["Victoria city, Texas","65384","48","75428"],
["Waco city, Texas","139601","48","76000"],
["Rio Rancho city, New Mexico","105839","35","63460"],
["Edmond city, Oklahoma","95334","40","23200"],
["Orem city, Utah","97872","49","57300"],
["Dallas city, Texas","1288441","48","19000"],
["Flower Mound town, Texas","78375","48","26232"],
["Caguas zona urbana, Puerto Rico","76577","72","10334"],
["Lynchburg city, Virginia","79009","51","47672"],
["Eau Claire city, Wisconsin","69196","55","22300"],
["Janesville city, Wisconsin","65953","55","37825"],
["Pasadena city, Texas","148629","48","56000"],
["Wichita Falls city, Texas","102986","48","79000"],
["Cincinnati city, Ohio","308913","39","15000"],
["Victorville city, California","135952","06","82590"],
["Lincoln city, Nebraska","292648","31","28000"],
["Spring Hill CDP, Florida","123509","12","68350"],
["Sunrise city, Florida","96031","12","69700"],
["Tallahassee city, Florida","197103","12","70600"],
["Tamarac city, Florida","71522","12","70675"],
["Tampa city, Florida","387037","12","71000"],
["Dothan city, Alabama","71283","01","21184"],
["Gilbert town, Arizona","273138","04","27400"],
["Glendale city, Arizona","249627","04","27820"],
["Daly City city, California","101221","06","17918"],
["Davis city, California","66798","06","18100"],
["Downey city, California","111637","06","19766"],
["Dublin city, California","71680","06","20018"],
["Springfield city, Illinois","114340","17","72000"],
["Hammond city, Indiana","76991","18","31000"],
["Jurupa Valley city, California","106937","06","37692"],
["Lake Elsinore city, California","71573","06","39486"],
["Lake Forest city, California","85732","06","39496"],
["Shreveport city, Louisiana","183489","22","70000"],
["Lowell city, Massachusetts","114005","25","37000"],
["Pittsburg city, California","76551","06","57456"],
["Lynn city, Massachusetts","100831","25","37490"],
["San Marcos city, California","94927","06","68196"],
["San Mateo city, California","102175","06","68252"],
["Lansing city, Michigan","111833","26","46000"],
["Visalia city, California","142976","06","82954"],
["Vista city, California","98671","06","82996"],
["Novi city, Michigan","66575","26","59440"],
["Town 'n' Country CDP, Florida","87862","12","72145"],
["Fort Collins city, Colorado","168535","08","27425"],
["Buena Park city, California","83017","06","08786"],
["Burbank city, California","105407","06","08954"],
["Goodyear city, Arizona","101744","04","28380"],
["Albany city, Georgia","67146","13","01052"],
["Alpharetta city, Georgia","66108","13","01696"],
["Athens-Clarke County unified government (balance), Georgia","126006","13","03440"],
["Atlanta city, Georgia","496480","13","04000"],
["Mobile city, Alabama","184960","01","50000"],
["Montgomery city, Alabama","198659","01","51000"],
["El Monte city, California","106913","06","22230"],
["Indianapolis city (balance), Indiana","882327","18","36003"],
["Lafayette city, Indiana","72041","18","40788"],
["Cedar Rapids city, Iowa","136464","19","12000"],
["Lakewood city, California","80607","06","39892"],
["Lancaster city, California","170134","06","40130"],
["Bowling Green city, Kentucky","73513","21","08902"],
["Manteca city, California","85799","06","45484"],
["Malden city, Massachusetts","65057","25","37875"],
["Pleasanton city, California","78250","06","57792"],
["Pomona city, California","148339","06","58072"],
["San Ramon city, California","86939","06","68378"],
["Sparks city, Nevada","109788","32","68400"],
["Spring Valley CDP, Nevada","213552","32","68585"],
["Sunrise Manor CDP, Nevada","196147","32","71400"],
["Walnut Creek city, California","69705","06","83346"],
["Wesley Chapel CDP, Florida","77319","12","75875"],
["Weston city, Florida","67322","12","76582"],
["West Palm Beach city, Florida","117253","12","76600"],
["Augusta-Richmond County consolidated government (balance), Georgia","200032","13","04204"],
["East Los Angeles CDP, California","115803","06","20802"],
["Joliet city, Illinois","152563","17","38570"],
["Davenport city, Iowa","101010","19","19000"],
["Des Moines city, Iowa","212333","19","21000"],
["Livermore city, California","86812","06","41992"],
["Lodi city, California","67020","06","42202"],
["Long Beach city, California","456063","06","43000"],
["Santa Ana city, California","309468","06","69000"],
["Santa Barbara city, California","88252","06","69070"],
["Santa Clara city, California","127155","06","69084"],
["Santa Clarita city, California","224588","06","69088"],
["Stockton city, California","322107","06","75000"],
["Silver Spring CDP, Maryland","80265","24","72450"],
["Maple Grove city, Minnesota","70730","27","40166"],
["Stamford city, Connecticut","136312","09","73000"],
["Fayetteville city, Arkansas","95231","05","23290"],
["Camarillo city, California","70838","06","10046"],
["Little Rock city, Arkansas","201984","05","41000"],
["Waukegan city, Illinois","85791","17","79293"],
["Santa Maria city, California","109709","06","69196"],
["Enterprise CDP, Nevada","245286","32","23770"],
["Santa Monica city, California","91103","06","70000"],
["Billings city, Montana","117453","30","06550"],
["Gulfport city, Mississippi","72096","28","29700"],
["Livonia city, Michigan","94407","26","49000"],
["Gainesville city, Florida","140406","12","25175"],
["Anaheim city, California","345935","06","02000"],
["Buckeye city, Arizona","101314","04","07940"],
["Antioch city, California","114801","06","02252"],
["Apple Valley town, California","76217","06","02364"],
["Grand Junction city, Colorado","66951","08","31660"],
["Greeley city, Colorado","109340","08","32155"],
["Fort Smith city, Arkansas","89574","05","24550"],
["Columbus city, Georgia","205617","13","19000"],
["Arlington Heights village, Illinois","75579","17","02154"],
["Aurora city, Illinois","183491","17","03012"],
["Boise City city, Idaho","237457","16","08830"],
["Noblesville city, Indiana","71810","18","54180"],
["Los Angeles city, California","3849306","06","44000"],
["Rancho Cordova city, California","80423","06","59444"],
["Rancho Cucamonga city, California","175138","06","59451"],
["New Bedford city, Massachusetts","100947","25","45000"],
["Blaine city, Minnesota","70953","27","06382"],
["Newton city, Massachusetts","87455","25","45560"],
["Ellicott City CDP, Maryland","76286","24","26000"],
["Bloomington city, Minnesota","89308","27","06616"],
["Santa Rosa city, California","176942","06","70098"],
["Sunnyvale city, California","152258","06","77000"],
["West Covina city, California","107031","06","84200"],
["Hialeah city, Florida","220479","12","30000"],
["Boulder city, Colorado","104178","08","07850"],
["Birmingham city, Alabama","196410","01","07000"],
["Arden-Arcade CDP, California","100613","06","02553"],
["Casas Adobes CDP, Arizona","73450","04","10670"],
["Carlsbad city, California","115291","06","11194"],
["Waterbury city, Connecticut","113820","09","80000"],
["Highlands Ranch CDP, Colorado","98239","08","36410"],
["Carmichael CDP, California","81039","06","11390"],
["Carson city, California","93526","06","11530"],
["Folsom city, California","81212","06","24638"],
["Fontana city, California","210786","06","24680"],
["Springdale city, Arkansas","87255","05","66080"],
["Madera city, California","67956","06","45022"],
["Menifee city, California","106396","06","46842"],
["Merced city, California","89292","06","46898"],
["Milpitas city, California","79074","06","47766"],
["Mission Viejo city, California","92449","06","48256"],
["Modesto city, California","218782","06","48354"],
["Redding city, California","93466","06","59920"],
["Redlands city, California","73280","06","59962"],
["Redondo Beach city, California","69779","06","60018"],
["Westminster city, California","90213","06","84550"],
["Hollywood city, Florida","152139","12","32000"],
["Homestead city, Florida","80523","12","32275"],
["Wilmington city, Delaware","70750","10","77580"],
["Broomfield city, Colorado","75325","08","09280"],
["Chandler city, Arizona","279445","04","12000"],
["Hartford city, Connecticut","120593","09","37000"],
["Bloomington city, Illinois","78283","17","06613"],
["Bolingbrook village, Illinois","74526","17","07133"],
["Eastvale city, California","71374","06","21230"],
["Idaho Falls city, Idaho","66895","16","39700"],
["Westminster city, Colorado","114573","08","83835"],
["Iowa City city, Iowa","74582","19","38595"],
["Moreno Valley city, California","211607","06","49270"],
["Baltimore city, Maryland","576498","24","04000"],
["Mountain View city, California","81517","06","49670"],
["Redwood City city, California","81653","06","60102"],
["Brooklyn Park city, Minnesota","84533","27","07966"],
["Rialto city, California","104380","06","60466"],
["Farmington Hills city, Michigan","83289","26","27440"],
["Worcester city, Massachusetts","205917","25","82000"],
["Jacksonville city, Florida","954624","12","35000"],
["Alameda city, California","76352","06","00562"],
["Kendall CDP, Florida","81524","12","36100"],
["Kissimmee city, Florida","79440","12","36950"],
["Castro Valley CDP, California","66408","06","11964"],
["Tucson city, Arizona","543215","04","77000"],
["Urban Honolulu CDP, Hawaii","345532","15","71550"],
["South Bend city, Indiana","104523","18","71000"],
["Murrieta city, California","112984","06","50076"],
["Napa city, California","78824","06","50258"],
["Newport Beach city, California","84784","06","51182"],
["Bethesda CDP, Maryland","68014","24","07125"],
["Richmond city, California","115642","06","60620"],
["Frederick city, Maryland","79588","24","30325"],
["Henderson city, Nevada","322202","32","31900"],
["Duluth city, Minnesota","86373","27","17000"],
["Eagan city, Minnesota","68646","27","17288"],
["Temecula city, California","110863","06","78120"],
["Whittier city, California","85306","06","85292"],
["Lakeland city, Florida","115401","12","38250"],
["Largo city, Florida","82333","12","39425"],
["Lauderhill city, Florida","73461","12","39550"],
["Lehigh Acres CDP, Florida","126557","12","39925"],
["Castle Rock town, Colorado","76366","08","12415"],
["Centennial city, Colorado","106957","08","12815"],
["Bakersfield city, California","407581","06","03526"],
["Baldwin Park city, California","70634","06","03666"],
["Lakewood city, Colorado","156612","08","43000"],
["Chico city, California","102340","06","13014"],
["Johns Creek city, Georgia","82078","13","42425"],
["Champaign city, Illinois","89116","17","12385"],
["Chicago city, Illinois","2696561","17","14000"],
["Naperville city, Illinois","148863","17","51622"],
["Yuma city, Arizona","97097","04","85540"],
["Fremont city, California","227523","06","26000"],
["Kansas City city, Kansas","154804","20","36000"],
["Lawrence city, Kansas","95251","20","38900"],
["Kenner city, Louisiana","65376","22","39475"],
["Norwalk city, California","100369","06","52526"],
["Boston city, Massachusetts","654281","25","07000"],
["Oakland city, California","433797","06","53000"],
["Quincy city, Massachusetts","101131","25","55745"],
["Riverside city, California","317257","06","62000"],
["Gaithersburg city, Maryland","69109","24","31175"],
["Rocklin city, California","72986","06","62364"],
["Flint city, Michigan","80628","26","29000"],
["Waldorf CDP, Maryland","80123","24","81175"],
["Arvada city, Colorado","123829","08","03455"],
["Alhambra city, California","81219","06","00884"],
["Chino city, California","92988","06","13210"],
["Chino Hills city, California","78675","06","13214"],
["Mesa city, Arizona","509492","04","46000"],
["Chula Vista city, California","277211","06","13392"],
["Citrus Heights city, California","87411","06","13588"],
["Macon-Bibb County, Georgia","156762","13","49008"],
["Cicero town, Illinois","83167","17","14351"],
["Escondido city, California","150656","06","22804"],
["Fresno city, California","544500","06","27000"],
["Fullerton city, California","141875","06","28000"],
["Meridian city, Idaho","125959","16","52120"],
["Portland city, Maine","68329","23","60545"],
["Lafayette city, Louisiana","121763","22","40735"],
["Lake Charles city, Louisiana","81102","22","41155"],
["Brockton city, Massachusetts","105455","25","09000"],
["Cambridge city, Massachusetts","117097","25","11000"],
["Oceanside city, California","172990","06","53322"],
["Germantown CDP, Maryland","85247","24","32025"],
["Jackson city, Mississippi","149813","28","36000"],
["Las Vegas city, Nevada","646776","32","40000"],
["Thousand Oaks city, California","125766","06","78582"],
["Melbourne city, Florida","85091","12","43975"],
["Miami city, Florida","439906","12","45000"],
["Miami Beach city, Florida","80673","12","45025"],
["Miami Gardens city, Florida","110881","12","45060"],
["Miramar city, Florida","135066","12","45975"],
["New Britain city, Connecticut","73835","09","50370"],
["Colorado Springs city, Colorado","483969","08","16000"],
["New Haven city, Connecticut","135076","09","52000"],
["Bellflower city, California","77407","06","04982"],
["Longmont city, Colorado","100427","08","45970"],
["Clovis city, California","122985","06","14218"],
["Loveland city, Colorado","77185","08","46465"],
["Surprise city, Arizona","149191","04","71510"],
["Decatur city, Illinois","70676","17","18823"],
["El Cajon city, California","105431","06","21712"],
["Palatine village, Illinois","66272","17","57225"],
["Thornton city, Colorado","142599","08","77290"],
["Garden Grove city, California","170492","06","29000"],
["Rogers city, Arkansas","71114","05","60410"],
["Glendale city, California","192376","06","30000"],
["Nampa city, Idaho","106186","16","56260"],
["Tuscaloosa city, Alabama","100606","01","77256"],
["Hawthorne city, California","86093","06","32548"],
["Hayward city, California","159839","06","33000"],
["Ann Arbor city, Michigan","121541","26","03000"],
["Ontario city, California","177961","06","53896"],
["Orange city, California","137287","06","53980"],
["Roseville city, California","151902","06","62938"],
["Glen Burnie CDP, Maryland","71019","24","32650"],
["Simi Valley city, California","125967","06","72016"],
["Kalamazoo city, Michigan","73255","26","42160"],
["Torrance city, California","143589","06","80000"],
["Lakeville city, Minnesota","72805","27","35180"],
["North Port city, Florida","80027","12","49675"],
["Avondale city, Arizona","90562","04","04720"],
["Berkeley city, California","117147","06","06000"],
["San Tan Valley CDP, Arizona","103399","04","64210"],
["Pueblo city, Colorado","112358","08","62000"],
["Peoria city, Illinois","110915","17","59000"],
["Hemet city, California","90446","06","33182"],
["Hesperia city, California","100959","06","33434"],
["Olathe city, Kansas","143006","20","52575"],
["Overland Park city, Kansas","197113","20","53775"],
["Oxnard city, California","201898","06","54652"],
["Fall River city, Massachusetts","93883","25","23000"],
["Palmdale city, California","165795","06","55156"],
["Sacramento city, California","525028","06","64000"],
["Salinas city, California","162780","06","64224"],
["Somerville city, Massachusetts","79819","25","62535"],
["Tracy city, California","95384","06","80238"],
["Orlando city, Florida","309193","12","53000"],
["Palm Bay city, Florida","122932","12","54000"],
["Palm Coast city, Florida","93845","12","54200"],
["Aurora city, Colorado","389675","08","04000"],
["Auburn city, Alabama","78552","01","03076"],
["Norwalk city, Connecticut","91203","09","55990"],
["Denver city, Colorado","711463","08","20000"],
["Compton city, California","93584","06","15044"],
["Concord city, California","124091","06","16000"],
["Corona city, California","159749","06","16350"],
["Roswell city, Georgia","92532","13","67284"],
["Sandy Springs city, Georgia","107179","13","68516"],
["Elgin city, Illinois","117850","17","23074"],
["Evanston city, Illinois","77532","17","24582"],
["Bloomington city, Indiana","78988","18","05860"],
["Lynwood city, California","65502","06","44574"],
["Metairie CDP, Louisiana","144999","22","50115"],
["Lexington-Fayette urban county, Kentucky","321793","21","46027"],
["Palo Alto city, California","66666","06","55282"],
["Framingham city, Massachusetts","71260","25","24960"],
["San Bernardino city, California","222194","06","65000"],
["San Buenaventura (Ventura) city, California","109938","06","65042"],
["Dearborn city, Michigan","108419","26","21000"],
["San Diego city, California","1381600","06","66000"],
["North Las Vegas city, Nevada","274146","32","51800"],
["Tulare city, California","70724","06","80644"],
["Columbia city, Missouri","126850","29","15670"],
["Turlock city, California","72673","06","80812"],
["Tustin city, California","79428","06","80854"],
["Yorba Linda city, California","67992","06","86832"],
["Yuba City city, California","69544","06","86972"],
["Missoula city, Montana","74834","30","50200"],
["Pembroke Pines city, Florida","169388","12","55775"],
["Pine Hills CDP, Florida","85927","12","56825"],
["Plantation city, Florida","92981","12","57425"],
["Poinciana CDP, Florida","65257","12","57900"],
["Pompano Beach city, Florida","111356","12","58050"],
["Conway city, Arkansas","65126","05","15190"],
["Costa Mesa city, California","110750","06","16532"],
["Hoover city, Alabama","92588","01","35896"],
["Huntsville city, Alabama","215482","01","37000"],
["Peoria city, Arizona","194910","04","54050"],
["Savannah city, Georgia","147087","13","69000"],
["Scottsdale city, Arizona","242754","04","65000"],
["South Fulton city, Georgia","108573","13","72122"],
["Rockford city, Illinois","148539","17","65000"],
["Fairfield city, California","119710","06","23182"],
["Carmel city, Indiana","100780","18","10342"],
["Huntington Beach city, California","196650","06","36000"],
["Indio city, California","90421","06","36448"],
["Inglewood city, California","105179","06","36546"],
["Sioux City city, Iowa","86369","19","73335"],
["Shawnee city, Kansas","67521","20","64500"],
["New Orleans city, Louisiana","376971","22","55000"],
["Louisville\/Jefferson County metro government (balance), Kentucky","628577","21","48006"],
["Pasadena city, California","135745","06","56000"],
["Haverhill city, Massachusetts","67356","25","29405"],
["Springfield city, Massachusetts","154788","25","67000"],
["San Francisco city, California","815201","06","67000"],
["Grand Rapids city, Michigan","197423","26","34000"],
["Paradise CDP, Nevada","185849","32","54600"],
["South Gate city, California","91148","06","73080"],
["Union City city, California","68668","06","81204"],
["Rockville city, Maryland","67133","24","67675"],
["Upland city, California","79264","06","81344"],
["Port Charlotte CDP, Florida","65671","12","58350"],
["Port St. Lucie city, Florida","217535","12","58715"],
["Riverview CDP, Florida","114560","12","60950"],
["Flagstaff city, Arizona","76984","04","23620"],
["Phoenix city, Arizona","1624539","04","55000"],
["Tempe city, Arizona","184109","04","73000"],
["Irvine city, California","309014","06","36770"],
["Ames city, Iowa","66422","19","01855"],
["Topeka city, Kansas","125969","20","71000"],
["Perris city, California","79831","06","56700"],
["Columbia CDP, Maryland","104043","24","19125"],
["Lawrence city, Massachusetts","88511","25","34550"],
["Detroit city, Michigan","632589","26","22000"],
["San Jose city, California","983530","06","68000"],
["San Leandro city, California","88878","06","68084"],
["Reno city, Nevada","268843","32","60600"],
["Vacaville city, California","103092","06","81554"],
["Vallejo city, California","124869","06","81666"],
["St. Petersburg city, Florida","258214","12","63000"],
["Danbury city, Connecticut","86749","09","18430"],
["Jonesboro city, Arkansas","79330","05","35710"],
["Queen Creek town, Arizona","69311","04","58150"],
["Warner Robins city, Georgia","82252","13","80508"],
["Elk Grove city, California","178988","06","22020"],
["Schaumburg village, Illinois","75913","17","68003"],
["Skokie village, Illinois","66410","17","70122"],
["Evansville city, Indiana","117273","18","22000"],
["Fishers city, Indiana","103081","18","23278"],
["Fort Wayne city, Indiana","263814","18","25000"],
["Ankeny city, Iowa","70289","19","02305"],
["Waterloo city, Iowa","66934","19","82425"],
["West Des Moines city, Iowa","69951","19","83910"],
["Wichita city, Kansas","395707","20","79000"],
["Baton Rouge city, Louisiana","222177","22","05000"]]

identifiers = [' city', ' municipality']
places = []
for place in places_orig:
    if 'St.' in place[0]:
        place[0] = place[0].replace('St.', 'Saint')
    new_place = []
    for item in place:
        contains_substring = any(identifier in item for identifier in identifiers)
        if contains_substring:
            for identifier in identifiers:
                if identifier in item:
                    updated = item.replace(identifier, '').strip()
                    new_place.append(updated)
        else:
            new_place.append(item)
    places.append(new_place)
places.pop(0) # removes heading row

#####################################
#####################################
## YEAR OVER YEAR ACS

# Find places code for each city in list
city_exceptions = ['Athens, Georgia', 'Augusta, Georgia', 'Boise, Idaho', 'Cary, North Carolina', 'Gilbert, Arizona', 'Honolulu, Hawaii', 'Indianapolis, Indiana', 'Lexington, Kentucky', 'Louisville, Kentucky', 'Nashville, Tennessee', 'Port Saint Lucie, Florida', 'Saint George, Utah', 'Saint Louis, Missouri', 'Saint Paul, Minnesota', 'Saint Petersburg, Florida', 'Ventura, California']

place_list = []
for city in city_list:
    if city in city_exceptions:
        city, state = city.split(',')
        for place in places:
            if city in place[0]:
                place[0] = city + ',' + state
                place_list.append(place) 
    else:
        for place in places:
            if city == place[0]:
                place_list.append(place)  
place_list
# Missing Check                
# place_matches = []
# for place in place_list:
#     place_matches.append(place[0])
# len(place_matches)
# place_matches

# missing = [item for item in city_list if item not in place_matches]
# missing

acs_vars_oneyear = {'B01003_001E':'Estimate!!Total population!!Total population',
            'B01001_026E':'Estimate!!Total:!!Female:',
            'B01002_001E':'Estimate!!Median age --!!Total:',
            'B23025_001E':'Estimate!!Total:16 Years and Over',
            'B23025_002E':'Estimate!!Total:!!In labor force:',
            'B17001_002E':'Estimate!!Total:!!Income in the past 12 months below poverty level:',
            'B17002_001E':'Estimate!!Total:Ratio Income to Poverty Level past 12 months',
            'B22003_002E':'Estimate!!Total:!!Household received Food Stamps/SNAP in the past 12 months:',
            'B02001_002E':'Estimate!!Total:!!White alone',
            'B02001_003E':'Estimate!!Total:!!Black or African American alone',
            'B03001_003E':'Estimate!!Total:!!Hispanic or Latino:',
            'B19013_001E':'Estimate!!Median household income in the past 12 months (in 2021 inflation-adjusted dollars)'
            }

census_2020 = {'P1_001N':'TOTAL POPULATION'}

#######
####### TESTING
r = requests.get(f'https://api.census.gov/data/2020/dec/dhc?get=NAME,{",".join(str(i) for i in acs_vars_oneyear)}&for=place:11000&in=state:36&key=9d770ba2775550d6234ed8c12dd756762be8b9f5').json()
r = requests.get(f'https://api.census.gov/data/2020/acs/acs1?get=NAME,{",".join(str(i) for i in acs_vars_oneyear)}&for=place:*&key=9d770ba2775550d6234ed8c12dd756762be8b9f5').json()
curr_df = pd.DataFrame(columns = r[0], data = r[1:])
curr_df

r = requests.get('https://api.census.gov/data/2020/dec/dhc?get=NAME,P1_001N&for=place:51000&in=state:36&key=9d770ba2775550d6234ed8c12dd756762be8b9f5').json()
curr_df = pd.DataFrame(columns = r[0], data = r[1:])
curr_df

find = [item for item in place_list if 'Los Angeles' in item[0]]

#########
########


# year_range = [*range(2015,2022)] # 2020 not working
year_range = [2015, 2016, 2017, 2018, 2019, 2021, 2022]

def gen_cities_acs_df_oneyr(places_list, var_list, exception_dict, suffix_list, year_range, key='9d770ba2775550d6234ed8c12dd756762be8b9f5'):
    print('requesting '+str(year_range[0])+ f' for {places_list[0][3]} & in=state:{places_list[0][2]}')
    response = requests.get(f'https://api.census.gov/data/{str(year_range[0])}/acs/acs1?get=NAME,{",".join(str(i) for i in var_list)}&for=place:{places_list[0][3]}&in=state:{places_list[0][2]}&key={key}').json()
    curr_df = pd.DataFrame(columns = response[0])
    print(curr_df.columns)
    curr_df['year'] = []

    for year in year_range:
        for place in places_list:
            if 'Buckeye' in place[0]:
                pass
            else:
                print(f'getting acs from {place[0]} in year {year}, code: place:{place[3]}&in=state:{place[2]}')
                response = requests.get(f'https://api.census.gov/data/{str(year)}/acs/acs1?get=NAME,{",".join(str(i) for i in var_list)}&for=place:{place[3]}&in=state:{place[2]}&key={key}').json()
                add_df = pd.DataFrame(columns = response[0], data = response[1:])
                add_df['year'] = year
                curr_df = pd.concat([curr_df, add_df], ignore_index=True)

    curr_df = curr_df.rename(columns=acs_vars_oneyear)

    def clean_cities_acs(df, exception_dict, suffix_list):
        df[['city', 'state']] = df['NAME'].str.split(',', expand=True)
        for exception in exception_dict.keys():
            df.loc[df['city'] == exception, 'city'] = exception_dict[exception]
        for suffix in suffix_list:
            df['city'] = df['city'].str.removesuffix(suffix)
            df['city'] = df['city'].str.strip()
        return df

    final_df = clean_cities_acs(curr_df, exception_dict, suffix_list)
    final_df = final_df.drop('NAME', axis=1)
    return final_df

key ='9d770ba2775550d6234ed8c12dd756762be8b9f5'
acs_vars_list = [i for i in acs_vars_oneyear]

suffixes = ['city', 'municipality']
city_exceptions = {'Boise City city':'Boise',
                   'Urban Honolulu CDP':'Honolulu',
                   'Indianapolis city (balance)':'Indianapolis',
                   'Lexington-Fayette urban county':'Lexington',
                   'Louisville/Jefferson County metro government (balance)':'Louisville',
                   'Nashville-Davidson metropolitan government (balance)':'Nashville',
                   'Athens-Clarke County unified government (balance)': 'Athens',
                   'Augusta-Richmond County consolidated government (balance)': 'Augusta',
                   'San Buenaventura (Ventura)': 'Ventura'}

cities_acs = gen_cities_acs_df_oneyr(place_list, acs_vars_list, city_exceptions, suffixes, year_range, key='9d770ba2775550d6234ed8c12dd756762be8b9f5')


# Dumb brute force way to make 2021 acs data fit to 2020, 2022, 2023
yr2021 = cities_acs[cities_acs['year'] == 2021]

yr2021['year'] = 2020
cities_acs = pd.concat([cities_acs, yr2021], ignore_index=True)

yr2021['year'] = 2022
cities_acs = pd.concat([cities_acs, yr2021], ignore_index=True)

yr2021['year'] = 2023
cities_acs = pd.concat([cities_acs, yr2021], ignore_index=True)


cities_acs.to_csv('RedBlue/Data/Components/cities_acs.csv', index=False)




#####################################
#####################################
#####################################
#####################################
#####################################
#####################################



#####################################
## DEPRECATED (ONLY ONE YEAR)
#####################################
places_orig = [["NAME","S0101_C01_001E","state","place"],
["O'Fallon city, Missouri","93651","29","54074"],
["St. Louis city, Missouri","293310","29","65000"],
["Passaic city, New Jersey","69637","34","56550"],
["Nashua city, New Hampshire","91122","33","50260"],
["Rochester city, Minnesota","121471","27","54880"],
["Paterson city, New Jersey","157783","34","57000"],
["Warren city, Michigan","138142","26","84000"],
["Lee's Summit city, Missouri","102506","29","41348"],
["Gastonia city, North Carolina","81159","37","25580"],
["Minneapolis city, Minnesota","425338","27","43000"],
["East Orange city, New Jersey","68893","34","19390"],
["Westland city, Michigan","84528","26","86000"],
["Elizabeth city, New Jersey","135405","34","21000"],
["Cary town, North Carolina","178508","37","10740"],
["Fargo city, North Dakota","124843","38","25700"],
["St. Cloud city, Minnesota","69809","27","56896"],
["Las Cruces city, New Mexico","112907","35","39380"],
["Springfield city, Missouri","169850","29","70000"],
["Wyoming city, Michigan","76747","26","88940"],
["St. Paul city, Minnesota","307176","27","58000"],
["Charlotte city, North Carolina","879697","37","12000"],
["Buffalo city, New York","276804","36","11000"],
["Rochester Hills city, Michigan","76021","26","69035"],
["Woodbury city, Minnesota","76994","27","71428"],
["Omaha city, Nebraska","487299","31","37000"],
["Concord city, North Carolina","107688","37","14100"],
["Bayonne city, New Jersey","69195","34","03580"],
["Albany city, New York","98624","36","01000"],
["Bismarck city, North Dakota","74141","38","07200"],
["Jacksonville city, North Carolina","72881","37","34200"],
["Albuquerque city, New Mexico","562591","35","02000"],
["Greensboro city, North Carolina","298250","37","28000"],
["Greenville city, North Carolina","88733","37","28080"],
["Independence city, Missouri","122083","29","35000"],
["Asheville city, North Carolina","94070","37","02140"],
["Newark city, New Jersey","307216","34","51000"],
["High Point city, North Carolina","115287","37","31400"],
["Southfield city, Michigan","75901","26","74900"],
["Durham city, North Carolina","285439","37","19000"],
["Kansas City city, Missouri","508415","29","38000"],
["Cheektowaga CDP, New York","76676","36","15000"],
["Sterling Heights city, Michigan","133256","26","76460"],
["Camden city, New Jersey","71771","34","10000"],
["Akron city, Ohio","189343","39","01000"],
["Plymouth city, Minnesota","79833","27","51730"],
["Jersey City city, New Jersey","283943","34","36000"],
["St. Charles city, Missouri","70832","29","64082"],
["Clifton city, New Jersey","89382","34","13690"],
["Troy city, Michigan","86837","26","80700"],
["Fayetteville city, North Carolina","208792","37","22920"],
["St. Joseph city, Missouri","75763","29","64550"],
["Manchester city, New Hampshire","115470","33","45140"],
["Lakewood CDP, New Jersey","66405","34","38580"],
["Coral Springs city, Florida","132822","12","14400"],
["Bridgeport city, Connecticut","148345","09","08000"],
["Davie town, Florida","104873","12","16475"],
["Daytona Beach city, Florida","74435","12","16525"],
["Deerfield Beach city, Florida","86355","12","16725"],
["Delray Beach city, Florida","66579","12","17100"],
["Deltona city, Florida","95771","12","17200"],
["Doral city, Florida","75954","12","17935"],
["Fort Lauderdale city, Florida","181666","12","24000"],
["Fort Myers city, Florida","92244","12","24125"],
["Washington city, District of Columbia","670050","11","50000"],
["Anchorage municipality, Alaska","288121","02","03000"],
["Alafaya CDP, Florida","95779","12","00410"],
["Boca Raton city, Florida","95785","12","07300"],
["Boynton Beach city, Florida","80083","12","07875"],
["Brandon CDP, Florida","116994","12","08150"],
["Cape Coral city, Florida","204519","12","10275"],
["Clearwater city, Florida","116667","12","12875"],
["Charleston city, South Carolina","152046","45","13330"],
["Schenectady city, New York","66985","36","65508"],
["Arlington city, Texas","392802","48","04000"],
["Rock Hill city, South Carolina","74107","45","61405"],
["Reading city, Pennsylvania","94834","42","63624"],
["Lubbock city, Texas","260990","48","45000"],
["Sammamish city, Washington","66630","53","61115"],
["Kenosha city, Wisconsin","99285","55","39225"],
["Pearland city, Texas","120694","48","56348"],
["Racine city, Wisconsin","77131","55","66000"],
["Cleveland city, Ohio","368006","39","16000"],
["Eugene city, Oregon","175102","41","23850"],
["Medford city, Oregon","86374","41","47000"],
["Raleigh city, North Carolina","469502","37","55000"],
["Greenville city, South Carolina","72103","45","30850"],
["Atascocita CDP, Texas","85808","48","04462"],
["Carrollton city, Texas","132569","48","13024"],
["Sioux Falls city, South Dakota","196528","46","59020"],
["Provo city, Utah","114085","49","62470"],
["Denton city, Texas","148139","48","19972"],
["Carolina zona urbana, Puerto Rico","141050","72","14290"],
["Richmond city, Virginia","226604","51","67000"],
["Roanoke city, Virginia","98865","51","68000"],
["Seattle city, Washington","733904","53","63000"],
["McAllen city, Texas","143922","48","45384"],
["McKinney city, Texas","202680","48","45744"],
["Pflugerville city, Texas","66700","48","57176"],
["Pharr city, Texas","79697","48","57200"],
["Lawton city, Oklahoma","91058","40","41850"],
["Austin city, Texas","964000","48","05000"],
["Cedar Park city, Texas","78326","48","13552"],
["Centreville CDP, Virginia","75010","51","14440"],
["Fort Worth city, Texas","940437","48","27000"],
["Houston city, Texas","2287047","48","35000"],
["Mansfield city, Texas","74106","48","46452"],
["South Hill CDP, Washington","66875","53","65922"],
["Plano city, Texas","287037","48","58016"],
["Columbus city, Ohio","907310","39","18000"],
["Mount Pleasant town, South Carolina","92398","45","48535"],
["Murfreesboro city, Tennessee","157509","47","51560"],
["Nashville-Davidson metropolitan government (balance), Tennessee","678845","47","52006"],
["St. George city, Utah","99965","49","65330"],
["Chesapeake city, Virginia","251269","51","16000"],
["Edinburg city, Texas","102477","48","22660"],
["Auburn city, Washington","87061","53","03180"],
["Frisco city, Texas","210735","48","27684"],
["Kennewick city, Washington","84478","53","35275"],
["Kent city, Washington","134837","53","35415"],
["Spokane city, Washington","229065","53","67000"],
["Spokane Valley city, Washington","105912","53","67167"],
["Columbia city, South Carolina","137960","45","16000"],
["Parma city, Ohio","79984","39","61000"],
["Jackson city, Tennessee","68114","47","37640"],
["Salt Lake City city, Utah","200475","49","67000"],
["Sandy city, Utah","95038","49","67440"],
["Bellevue city, Washington","149429","53","05210"],
["Garland city, Texas","241870","48","29000"],
["Kirkland city, Washington","92105","53","35940"],
["Beaverton city, Oregon","98204","41","05350"],
["Bend city, Oregon","102079","41","05800"],
["Cranston city, Rhode Island","82568","44","19180"],
["Wilmington city, North Carolina","117642","37","74440"],
["Erie city, Pennsylvania","94013","42","24000"],
["Johnson City city, Tennessee","70889","47","38320"],
["Yonkers city, New York","209506","36","84000"],
["Toledo city, Ohio","268504","39","77000"],
["South Jordan city, Utah","80142","49","70850"],
["Bellingham city, Washington","92290","53","05280"],
["El Paso city, Texas","678422","48","24000"],
["Georgetown city, Texas","75407","48","29336"],
["Appleton city, Wisconsin","72951","55","02375"],
["Irving city, Texas","254190","48","37000"],
["Laredo city, Texas","258014","48","41464"],
["Mesquite city, Texas","148087","48","47892"],
["Tacoma city, Washington","219203","53","70000"],
["Midland city, Texas","131292","48","48072"],
["Santa Fe city, New Mexico","88196","35","70500"],
["Winston-Salem city, North Carolina","250337","37","75000"],
["Pawtucket city, Rhode Island","75379","44","54640"],
["Providence city, Rhode Island","189697","44","59000"],
["Abilene city, Texas","129601","48","01000"],
["North Charleston city, South Carolina","117463","45","50875"],
["Layton city, Utah","83299","49","43660"],
["Lehi city, Utah","79979","49","44320"],
["Dale City CDP, Virginia","79782","51","21088"],
["Hampton city, Virginia","137746","51","35000"],
["Madison city, Wisconsin","269162","55","48000"],
["Mission city, Texas","86215","48","48768"],
["Missouri City city, Texas","76462","48","48804"],
["Richardson city, Texas","116369","48","61796"],
["Warwick city, Rhode Island","83014","44","74300"],
["Rochester city, New York","210594","36","63000"],
["Knoxville city, Tennessee","192657","47","40000"],
["League City city, Texas","114664","48","41980"],
["Leander city, Texas","68993","48","42016"],
["Ponce zona urbana, Puerto Rico","112005","72","63820"],
["Waukesha city, Wisconsin","71254","55","84250"],
["Gresham city, Oregon","113106","41","31250"],
["Dayton city, Ohio","137581","39","21000"],
["Allentown city, Pennsylvania","125934","42","02000"],
["Portland city, Oregon","642218","41","59000"],
["Bethlehem city, Pennsylvania","75134","42","06088"],
["Tulsa city, Oklahoma","411905","40","75000"],
["Baytown city, Texas","79676","48","06128"],
["Brownsville city, Texas","187840","48","10768"],
["Alexandria city, Virginia","154706","51","01000"],
["Grand Prairie city, Texas","197338","48","30464"],
["Everett city, Washington","110820","53","22640"],
["Philadelphia city, Pennsylvania","1576251","42","60000"],
["Newport News city, Virginia","184587","51","56000"],
["Green Bay city, Wisconsin","107020","55","31000"],
["Lewisville city, Texas","112853","48","42508"],
["Vancouver city, Washington","192176","53","74060"],
["Milwaukee city, Wisconsin","569326","55","53000"],
["Round Rock city, Texas","127130","48","63500"],
["Hillsboro city, Oregon","106651","41","34100"],
["Franklin city, Tennessee","85473","47","27740"],
["Beaumont city, Texas","112559","48","07000"],
["Bryan city, Texas","86851","48","10912"],
["College Station city, Texas","120032","48","15976"],
["Federal Way city, Washington","99028","53","23515"],
["Pittsburgh city, Pennsylvania","300454","42","61000"],
["Norfolk city, Virginia","235089","51","57000"],
["Guaynabo zona urbana, Puerto Rico","72088","72","32522"],
["Pasco city, Washington","84190","53","53545"],
["Suffolk city, Virginia","96194","51","76432"],
["San Angelo city, Texas","101063","48","64472"],
["San Antonio city, Texas","1451863","48","65000"],
["San Marcos city, Texas","68578","48","65600"],
["Broken Arrow city, Oklahoma","117775","40","09050"],
["Mount Vernon city, New York","72584","36","49121"],
["Allen city, Texas","106868","48","01924"],
["Arlington CDP, Virginia","232965","51","03000"],
["Conroe city, Texas","94401","48","16432"],
["New Braunfels city, Texas","96630","48","50820"],
["Canton city, Ohio","70438","39","12000"],
["Salem city, Oregon","177727","41","64900"],
["West Jordan city, Utah","116544","49","82950"],
["West Valley City city, Utah","139094","49","83470"],
["Harlingen city, Texas","71928","48","32372"],
["Killeen city, Texas","156260","48","39148"],
["Scranton city, Pennsylvania","75867","42","69000"],
["San Juan zona urbana, Puerto Rico","320456","72","76770"],
["Yakima city, Washington","96565","53","80010"],
["Spring CDP, Texas","71893","48","69596"],
["Norman city, Oklahoma","128087","40","52500"],
["Chattanooga city, Tennessee","182111","47","14000"],
["Amarillo city, Texas","198781","48","03000"],
["Rapid City city, South Dakota","76173","46","52980"],
["Corpus Christi city, Texas","317768","48","17000"],
["Longview city, Texas","81877","48","43888"],
["North Richland Hills city, Texas","70212","48","52356"],
["Sugar Land city, Texas","109337","48","70808"],
["Temple city, Texas","85428","48","72176"],
["Toms River CDP, New Jersey","93947","34","73110"],
["Trenton city, New Jersey","90458","34","74000"],
["Lorain city, Ohio","65440","39","44856"],
["New Rochelle city, New York","81590","36","50617"],
["New York city, New York","8467513","36","51000"],
["Oklahoma City city, Oklahoma","687691","40","55000"],
["Clarksville city, Tennessee","170966","47","15160"],
["Bayamón zona urbana, Puerto Rico","168592","72","06593"],
["Cheyenne city, Wyoming","65048","56","13900"],
["Redmond city, Washington","76360","53","57535"],
["Renton city, Washington","105200","53","57745"],
["Virginia Beach city, Virginia","457672","51","82000"],
["Odessa city, Texas","116436","48","53388"],
["Oshkosh city, Wisconsin","66594","55","60500"],
["The Woodlands CDP, Texas","116251","48","72656"],
["Tyler city, Texas","107199","48","74144"],
["Union City city, New Jersey","65639","34","74630"],
["Syracuse city, New York","146124","36","73000"],
["Memphis city, Tennessee","628118","47","48000"],
["Ogden city, Utah","86800","49","55980"],
["Marysville city, Washington","71151","53","43955"],
["Portsmouth city, Virginia","97840","51","64000"],
["Victoria city, Texas","65384","48","75428"],
["Waco city, Texas","139601","48","76000"],
["Rio Rancho city, New Mexico","105839","35","63460"],
["Edmond city, Oklahoma","95334","40","23200"],
["Orem city, Utah","97872","49","57300"],
["Dallas city, Texas","1288441","48","19000"],
["Flower Mound town, Texas","78375","48","26232"],
["Caguas zona urbana, Puerto Rico","76577","72","10334"],
["Lynchburg city, Virginia","79009","51","47672"],
["Eau Claire city, Wisconsin","69196","55","22300"],
["Janesville city, Wisconsin","65953","55","37825"],
["Pasadena city, Texas","148629","48","56000"],
["Wichita Falls city, Texas","102986","48","79000"],
["Cincinnati city, Ohio","308913","39","15000"],
["Victorville city, California","135952","06","82590"],
["Lincoln city, Nebraska","292648","31","28000"],
["Spring Hill CDP, Florida","123509","12","68350"],
["Sunrise city, Florida","96031","12","69700"],
["Tallahassee city, Florida","197103","12","70600"],
["Tamarac city, Florida","71522","12","70675"],
["Tampa city, Florida","387037","12","71000"],
["Dothan city, Alabama","71283","01","21184"],
["Gilbert town, Arizona","273138","04","27400"],
["Glendale city, Arizona","249627","04","27820"],
["Daly City city, California","101221","06","17918"],
["Davis city, California","66798","06","18100"],
["Downey city, California","111637","06","19766"],
["Dublin city, California","71680","06","20018"],
["Springfield city, Illinois","114340","17","72000"],
["Hammond city, Indiana","76991","18","31000"],
["Jurupa Valley city, California","106937","06","37692"],
["Lake Elsinore city, California","71573","06","39486"],
["Lake Forest city, California","85732","06","39496"],
["Shreveport city, Louisiana","183489","22","70000"],
["Lowell city, Massachusetts","114005","25","37000"],
["Pittsburg city, California","76551","06","57456"],
["Lynn city, Massachusetts","100831","25","37490"],
["San Marcos city, California","94927","06","68196"],
["San Mateo city, California","102175","06","68252"],
["Lansing city, Michigan","111833","26","46000"],
["Visalia city, California","142976","06","82954"],
["Vista city, California","98671","06","82996"],
["Novi city, Michigan","66575","26","59440"],
["The Villages CDP, Florida","-999999999","12","71625"],
["Town 'n' Country CDP, Florida","87862","12","72145"],
["Fort Collins city, Colorado","168535","08","27425"],
["Buena Park city, California","83017","06","08786"],
["Burbank city, California","105407","06","08954"],
["Goodyear city, Arizona","101744","04","28380"],
["Albany city, Georgia","67146","13","01052"],
["Alpharetta city, Georgia","66108","13","01696"],
["Athens-Clarke County unified government (balance), Georgia","126006","13","03440"],
["Atlanta city, Georgia","496480","13","04000"],
["Mobile city, Alabama","184960","01","50000"],
["Montgomery city, Alabama","198659","01","51000"],
["El Monte city, California","106913","06","22230"],
["Indianapolis city (balance), Indiana","882327","18","36003"],
["Lafayette city, Indiana","72041","18","40788"],
["Cedar Rapids city, Iowa","136464","19","12000"],
["Lakewood city, California","80607","06","39892"],
["Lancaster city, California","170134","06","40130"],
["Bowling Green city, Kentucky","73513","21","08902"],
["Manteca city, California","85799","06","45484"],
["Malden city, Massachusetts","65057","25","37875"],
["Pleasanton city, California","78250","06","57792"],
["Pomona city, California","148339","06","58072"],
["San Ramon city, California","86939","06","68378"],
["Sparks city, Nevada","109788","32","68400"],
["Spring Valley CDP, Nevada","213552","32","68585"],
["Sunrise Manor CDP, Nevada","196147","32","71400"],
["Walnut Creek city, California","69705","06","83346"],
["Wesley Chapel CDP, Florida","77319","12","75875"],
["Weston city, Florida","67322","12","76582"],
["West Palm Beach city, Florida","117253","12","76600"],
["Augusta-Richmond County consolidated government (balance), Georgia","200032","13","04204"],
["East Los Angeles CDP, California","115803","06","20802"],
["Joliet city, Illinois","152563","17","38570"],
["Davenport city, Iowa","101010","19","19000"],
["Des Moines city, Iowa","212333","19","21000"],
["Livermore city, California","86812","06","41992"],
["Lodi city, California","67020","06","42202"],
["Long Beach city, California","456063","06","43000"],
["Santa Ana city, California","309468","06","69000"],
["Santa Barbara city, California","88252","06","69070"],
["Santa Clara city, California","127155","06","69084"],
["Santa Clarita city, California","224588","06","69088"],
["Stockton city, California","322107","06","75000"],
["Silver Spring CDP, Maryland","80265","24","72450"],
["Maple Grove city, Minnesota","70730","27","40166"],
["Stamford city, Connecticut","136312","09","73000"],
["Fayetteville city, Arkansas","95231","05","23290"],
["Camarillo city, California","70838","06","10046"],
["Little Rock city, Arkansas","201984","05","41000"],
["Waukegan city, Illinois","85791","17","79293"],
["Santa Maria city, California","109709","06","69196"],
["Enterprise CDP, Nevada","245286","32","23770"],
["Santa Monica city, California","91103","06","70000"],
["Billings city, Montana","117453","30","06550"],
["Gulfport city, Mississippi","72096","28","29700"],
["Livonia city, Michigan","94407","26","49000"],
["Gainesville city, Florida","140406","12","25175"],
["Anaheim city, California","345935","06","02000"],
["Buckeye city, Arizona","101314","04","07940"],
["Antioch city, California","114801","06","02252"],
["Apple Valley town, California","76217","06","02364"],
["Grand Junction city, Colorado","66951","08","31660"],
["Greeley city, Colorado","109340","08","32155"],
["Fort Smith city, Arkansas","89574","05","24550"],
["Columbus city, Georgia","205617","13","19000"],
["Arlington Heights village, Illinois","75579","17","02154"],
["Aurora city, Illinois","183491","17","03012"],
["Boise City city, Idaho","237457","16","08830"],
["Noblesville city, Indiana","71810","18","54180"],
["Los Angeles city, California","3849306","06","44000"],
["Rancho Cordova city, California","80423","06","59444"],
["Rancho Cucamonga city, California","175138","06","59451"],
["New Bedford city, Massachusetts","100947","25","45000"],
["Blaine city, Minnesota","70953","27","06382"],
["Newton city, Massachusetts","87455","25","45560"],
["Ellicott City CDP, Maryland","76286","24","26000"],
["Bloomington city, Minnesota","89308","27","06616"],
["Santa Rosa city, California","176942","06","70098"],
["Sunnyvale city, California","152258","06","77000"],
["West Covina city, California","107031","06","84200"],
["Hialeah city, Florida","220479","12","30000"],
["Boulder city, Colorado","104178","08","07850"],
["Birmingham city, Alabama","196410","01","07000"],
["Arden-Arcade CDP, California","100613","06","02553"],
["Casas Adobes CDP, Arizona","73450","04","10670"],
["Carlsbad city, California","115291","06","11194"],
["Waterbury city, Connecticut","113820","09","80000"],
["Highlands Ranch CDP, Colorado","98239","08","36410"],
["Carmichael CDP, California","81039","06","11390"],
["Carson city, California","93526","06","11530"],
["Folsom city, California","81212","06","24638"],
["Fontana city, California","210786","06","24680"],
["Springdale city, Arkansas","87255","05","66080"],
["Madera city, California","67956","06","45022"],
["Menifee city, California","106396","06","46842"],
["Merced city, California","89292","06","46898"],
["Milpitas city, California","79074","06","47766"],
["Mission Viejo city, California","92449","06","48256"],
["Modesto city, California","218782","06","48354"],
["Redding city, California","93466","06","59920"],
["Redlands city, California","73280","06","59962"],
["Redondo Beach city, California","69779","06","60018"],
["Westminster city, California","90213","06","84550"],
["Hollywood city, Florida","152139","12","32000"],
["Homestead city, Florida","80523","12","32275"],
["Horizon West CDP, Florida","-999999999","12","32610"],
["Wilmington city, Delaware","70750","10","77580"],
["Broomfield city, Colorado","75325","08","09280"],
["Chandler city, Arizona","279445","04","12000"],
["Hartford city, Connecticut","120593","09","37000"],
["Bloomington city, Illinois","78283","17","06613"],
["Bolingbrook village, Illinois","74526","17","07133"],
["Eastvale city, California","71374","06","21230"],
["Idaho Falls city, Idaho","66895","16","39700"],
["Westminster city, Colorado","114573","08","83835"],
["Iowa City city, Iowa","74582","19","38595"],
["Moreno Valley city, California","211607","06","49270"],
["Baltimore city, Maryland","576498","24","04000"],
["Mountain View city, California","81517","06","49670"],
["Redwood City city, California","81653","06","60102"],
["Brooklyn Park city, Minnesota","84533","27","07966"],
["Rialto city, California","104380","06","60466"],
["Farmington Hills city, Michigan","83289","26","27440"],
["Worcester city, Massachusetts","205917","25","82000"],
["Jacksonville city, Florida","954624","12","35000"],
["Alameda city, California","76352","06","00562"],
["Kendall CDP, Florida","81524","12","36100"],
["Kissimmee city, Florida","79440","12","36950"],
["Castro Valley CDP, California","66408","06","11964"],
["Tucson city, Arizona","543215","04","77000"],
["Urban Honolulu CDP, Hawaii","345532","15","71550"],
["South Bend city, Indiana","104523","18","71000"],
["Murrieta city, California","112984","06","50076"],
["Napa city, California","78824","06","50258"],
["Newport Beach city, California","84784","06","51182"],
["Bethesda CDP, Maryland","68014","24","07125"],
["Richmond city, California","115642","06","60620"],
["Frederick city, Maryland","79588","24","30325"],
["Henderson city, Nevada","322202","32","31900"],
["Duluth city, Minnesota","86373","27","17000"],
["Eagan city, Minnesota","68646","27","17288"],
["Temecula city, California","110863","06","78120"],
["Whittier city, California","85306","06","85292"],
["Lakeland city, Florida","115401","12","38250"],
["Largo city, Florida","82333","12","39425"],
["Lauderhill city, Florida","73461","12","39550"],
["Lehigh Acres CDP, Florida","126557","12","39925"],
["Castle Rock town, Colorado","76366","08","12415"],
["Centennial city, Colorado","106957","08","12815"],
["Bakersfield city, California","407581","06","03526"],
["Baldwin Park city, California","70634","06","03666"],
["Lakewood city, Colorado","156612","08","43000"],
["Chico city, California","102340","06","13014"],
["Johns Creek city, Georgia","82078","13","42425"],
["Champaign city, Illinois","89116","17","12385"],
["Chicago city, Illinois","2696561","17","14000"],
["Naperville city, Illinois","148863","17","51622"],
["Yuma city, Arizona","97097","04","85540"],
["Fremont city, California","227523","06","26000"],
["Kansas City city, Kansas","154804","20","36000"],
["Lawrence city, Kansas","95251","20","38900"],
["Kenner city, Louisiana","65376","22","39475"],
["Norwalk city, California","100369","06","52526"],
["Boston city, Massachusetts","654281","25","07000"],
["Oakland city, California","433797","06","53000"],
["Quincy city, Massachusetts","101131","25","55745"],
["Riverside city, California","317257","06","62000"],
["Gaithersburg city, Maryland","69109","24","31175"],
["Rocklin city, California","72986","06","62364"],
["Flint city, Michigan","80628","26","29000"],
["Waldorf CDP, Maryland","80123","24","81175"],
["Arvada city, Colorado","123829","08","03455"],
["Alhambra city, California","81219","06","00884"],
["Chino city, California","92988","06","13210"],
["Chino Hills city, California","78675","06","13214"],
["Mesa city, Arizona","509492","04","46000"],
["Chula Vista city, California","277211","06","13392"],
["Citrus Heights city, California","87411","06","13588"],
["Macon-Bibb County, Georgia","156762","13","49008"],
["Cicero town, Illinois","83167","17","14351"],
["Escondido city, California","150656","06","22804"],
["Fresno city, California","544500","06","27000"],
["Fullerton city, California","141875","06","28000"],
["Meridian city, Idaho","125959","16","52120"],
["Portland city, Maine","68329","23","60545"],
["Lafayette city, Louisiana","121763","22","40735"],
["Lake Charles city, Louisiana","81102","22","41155"],
["Brockton city, Massachusetts","105455","25","09000"],
["Cambridge city, Massachusetts","117097","25","11000"],
["Oceanside city, California","172990","06","53322"],
["Germantown CDP, Maryland","85247","24","32025"],
["Jackson city, Mississippi","149813","28","36000"],
["Las Vegas city, Nevada","646776","32","40000"],
["Thousand Oaks city, California","125766","06","78582"],
["Melbourne city, Florida","85091","12","43975"],
["Miami city, Florida","439906","12","45000"],
["Miami Beach city, Florida","80673","12","45025"],
["Miami Gardens city, Florida","110881","12","45060"],
["Miramar city, Florida","135066","12","45975"],
["New Britain city, Connecticut","73835","09","50370"],
["Colorado Springs city, Colorado","483969","08","16000"],
["New Haven city, Connecticut","135076","09","52000"],
["Bellflower city, California","77407","06","04982"],
["Longmont city, Colorado","100427","08","45970"],
["Clovis city, California","122985","06","14218"],
["Loveland city, Colorado","77185","08","46465"],
["Surprise city, Arizona","149191","04","71510"],
["Decatur city, Illinois","70676","17","18823"],
["El Cajon city, California","105431","06","21712"],
["Palatine village, Illinois","66272","17","57225"],
["Thornton city, Colorado","142599","08","77290"],
["Garden Grove city, California","170492","06","29000"],
["Rogers city, Arkansas","71114","05","60410"],
["Glendale city, California","192376","06","30000"],
["Nampa city, Idaho","106186","16","56260"],
["Tuscaloosa city, Alabama","100606","01","77256"],
["Hawthorne city, California","86093","06","32548"],
["Hayward city, California","159839","06","33000"],
["Ann Arbor city, Michigan","121541","26","03000"],
["Ontario city, California","177961","06","53896"],
["Orange city, California","137287","06","53980"],
["Roseville city, California","151902","06","62938"],
["Glen Burnie CDP, Maryland","71019","24","32650"],
["Simi Valley city, California","125967","06","72016"],
["Kalamazoo city, Michigan","73255","26","42160"],
["Torrance city, California","143589","06","80000"],
["Lakeville city, Minnesota","72805","27","35180"],
["North Port city, Florida","80027","12","49675"],
["Avondale city, Arizona","90562","04","04720"],
["Berkeley city, California","117147","06","06000"],
["San Tan Valley CDP, Arizona","103399","04","64210"],
["Pueblo city, Colorado","112358","08","62000"],
["Peoria city, Illinois","110915","17","59000"],
["Hemet city, California","90446","06","33182"],
["Hesperia city, California","100959","06","33434"],
["Olathe city, Kansas","143006","20","52575"],
["Overland Park city, Kansas","197113","20","53775"],
["Oxnard city, California","201898","06","54652"],
["Fall River city, Massachusetts","93883","25","23000"],
["Palmdale city, California","165795","06","55156"],
["Sacramento city, California","525028","06","64000"],
["Salinas city, California","162780","06","64224"],
["Somerville city, Massachusetts","79819","25","62535"],
["Tracy city, California","95384","06","80238"],
["Orlando city, Florida","309193","12","53000"],
["Palm Bay city, Florida","122932","12","54000"],
["Palm Coast city, Florida","93845","12","54200"],
["Aurora city, Colorado","389675","08","04000"],
["Auburn city, Alabama","78552","01","03076"],
["Norwalk city, Connecticut","91203","09","55990"],
["Denver city, Colorado","711463","08","20000"],
["Compton city, California","93584","06","15044"],
["Concord city, California","124091","06","16000"],
["Corona city, California","159749","06","16350"],
["Roswell city, Georgia","92532","13","67284"],
["Sandy Springs city, Georgia","107179","13","68516"],
["Elgin city, Illinois","117850","17","23074"],
["Evanston city, Illinois","77532","17","24582"],
["Bloomington city, Indiana","78988","18","05860"],
["Lynwood city, California","65502","06","44574"],
["Metairie CDP, Louisiana","144999","22","50115"],
["Lexington-Fayette urban county, Kentucky","321793","21","46027"],
["Palo Alto city, California","66666","06","55282"],
["Framingham city, Massachusetts","71260","25","24960"],
["San Bernardino city, California","222194","06","65000"],
["San Buenaventura (Ventura) city, California","109938","06","65042"],
["Dearborn city, Michigan","108419","26","21000"],
["San Diego city, California","1381600","06","66000"],
["North Las Vegas city, Nevada","274146","32","51800"],
["Tulare city, California","70724","06","80644"],
["Columbia city, Missouri","126850","29","15670"],
["Turlock city, California","72673","06","80812"],
["Tustin city, California","79428","06","80854"],
["Yorba Linda city, California","67992","06","86832"],
["Yuba City city, California","69544","06","86972"],
["Missoula city, Montana","74834","30","50200"],
["Pembroke Pines city, Florida","169388","12","55775"],
["Pine Hills CDP, Florida","85927","12","56825"],
["Plantation city, Florida","92981","12","57425"],
["Poinciana CDP, Florida","65257","12","57900"],
["Pompano Beach city, Florida","111356","12","58050"],
["Conway city, Arkansas","65126","05","15190"],
["Costa Mesa city, California","110750","06","16532"],
["Hoover city, Alabama","92588","01","35896"],
["Huntsville city, Alabama","215482","01","37000"],
["Peoria city, Arizona","194910","04","54050"],
["Savannah city, Georgia","147087","13","69000"],
["Scottsdale city, Arizona","242754","04","65000"],
["South Fulton city, Georgia","108573","13","72122"],
["Rockford city, Illinois","148539","17","65000"],
["Fairfield city, California","119710","06","23182"],
["Carmel city, Indiana","100780","18","10342"],
["Huntington Beach city, California","196650","06","36000"],
["Indio city, California","90421","06","36448"],
["Inglewood city, California","105179","06","36546"],
["Sioux City city, Iowa","86369","19","73335"],
["Shawnee city, Kansas","67521","20","64500"],
["New Orleans city, Louisiana","376971","22","55000"],
["Louisville/Jefferson County metro government (balance), Kentucky","628577","21","48006"],
["Pasadena city, California","135745","06","56000"],
["Haverhill city, Massachusetts","67356","25","29405"],
["Springfield city, Massachusetts","154788","25","67000"],
["San Francisco city, California","815201","06","67000"],
["Grand Rapids city, Michigan","197423","26","34000"],
["Paradise CDP, Nevada","185849","32","54600"],
["South Gate city, California","91148","06","73080"],
["Union City city, California","68668","06","81204"],
["Rockville city, Maryland","67133","24","67675"],
["Upland city, California","79264","06","81344"],
["Port Charlotte CDP, Florida","65671","12","58350"],
["Port St. Lucie city, Florida","217535","12","58715"],
["Riverview CDP, Florida","114560","12","60950"],
["Flagstaff city, Arizona","76984","04","23620"],
["Phoenix city, Arizona","1624539","04","55000"],
["Tempe city, Arizona","184109","04","73000"],
["Irvine city, California","309014","06","36770"],
["Ames city, Iowa","66422","19","01855"],
["Topeka city, Kansas","125969","20","71000"],
["Perris city, California","79831","06","56700"],
["Columbia CDP, Maryland","104043","24","19125"],
["Lawrence city, Massachusetts","88511","25","34550"],
["Detroit city, Michigan","632589","26","22000"],
["San Jose city, California","983530","06","68000"],
["San Leandro city, California","88878","06","68084"],
["Reno city, Nevada","268843","32","60600"],
["Vacaville city, California","103092","06","81554"],
["Vallejo city, California","124869","06","81666"],
["St. Petersburg city, Florida","258214","12","63000"],
["Danbury city, Connecticut","86749","09","18430"],
["Jonesboro city, Arkansas","79330","05","35710"],
["Queen Creek town, Arizona","69311","04","58150"],
["Warner Robins city, Georgia","82252","13","80508"],
["Elk Grove city, California","178988","06","22020"],
["Schaumburg village, Illinois","75913","17","68003"],
["Skokie village, Illinois","66410","17","70122"],
["Evansville city, Indiana","117273","18","22000"],
["Fishers city, Indiana","103081","18","23278"],
["Fort Wayne city, Indiana","263814","18","25000"],
["Ankeny city, Iowa","70289","19","02305"],
["Waterloo city, Iowa","66934","19","82425"],
["West Des Moines city, Iowa","69951","19","83910"],
["Wichita city, Kansas","395707","20","79000"],
["Baton Rouge city, Louisiana","222177","22","05000"]]

places_split = []
for place in places_orig:
    new_place = []
    for item in place:
        if ',' in item:
            city, state = item.split(',')
            state = state.strip()
            new_place.append(city)
            new_place.append(state)
        else:
            new_place.append(item)
    places_split.append(new_place)
places_split  

identifiers = ['city', 'town', 'municipality']

places = []
for place in places_split:
    new_place = []
    for item in place:
        contains_substring = any(identifier in item for identifier in identifiers)
        if contains_substring:
            for identifier in identifiers:
                if identifier in item:
                    updated = item.replace(identifier, '').strip()
                    new_place.append(updated)
        else:
            new_place.append(item)
    places.append(new_place)
places.pop(0)

places

# df = census_all_vars('acs/acs1', '2021')

# Find places code for each city in list
city_exceptions = ['Boise', 'Honolulu', 'Indianapolis', 'Lexington', 'Louisville', 'Nashville']
city_dupes = {'Aurora':'Colorado',
              'Glendale':'Arizona',
              'Portland':'Oregon',
              'Columbus':'Ohio',
              'Jacksonville':'Florida',
              'Kansas City':'Missouri',
              'Richmond':'Virginia',}

# Create cities list from mayors
cities_df = pd.read_csv('RedBlue/Data/Components/100_mayors_23.csv')
cities_lst = cities_df['City'].unique().tolist()

cities_lst

place_list = []
for city in cities_lst:
    if city in city_exceptions:
        for place in places:
            if city in place[0]:
                place[0] = city
                place_list.append(place) 
    elif city in city_dupes.keys():
        for place in places:
            if city == place[0] and city_dupes[city] == place[1]:
                place_list.append(place)  
    else:
        for place in places:
            if city == place[0]:
                place_list.append(place)  
place_list


# Checks for completed and clean filter of places

# just_place = []
# for place in place_list:
#     just_place.append(place[0])
# just_place

# missing_cities = []
# for city in cities_lst:
#     if city not in just_place:
#         print(city)
#         missing_cities.append(city)
# missing_cities

# where_in_place = []
# for missing_city in missing_cities:
#     for place in places:
#         if place[0].startswith(missing_city):
#             where_in_place.append(place)
# where_in_place

acs_vars = {'S0101_C01_001E':'Estimate!!Total population!!Total population',
            'S0501_C01_003E':'Estimate!!Total!!Total population!!SEX AND AGE!!Female',
            'S0101_C01_032E':'Estimate!!Total!!Total population!!SUMMARY INDICATORS!!Median age (years)',

            'S2404_C01_001E':'Estimate!!Total!!Full-time, year-round civilian employed population 16 years and over',
            'S0501_C01_049E':'Estimate!!Total!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force',
            'S0501_C01_079E':'Estimate!!Total!!EARNINGS IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS) FOR FULL-TIME, YEAR-ROUND WORKERS!!Population 16 years and over with earnings',
            'S0501_C01_087E':'Estimate!!Total!!EARNINGS IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS) FOR FULL-TIME, YEAR-ROUND WORKERS!!Population 16 years and over with earnings!!Median earnings (dollars) for full-time, year-round workers:!!Male',
            'S0501_C01_088E':'Estimate!!Total!!EARNINGS IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS) FOR FULL-TIME, YEAR-ROUND WORKERS!!Population 16 years and over with earnings!!Median earnings (dollars) for full-time, year-round workers:!!Female',
            'S0501_C01_091E':'Estimate!!Total!!INCOME IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Households!!With earnings!!Mean earnings (dollars)',
            'S2201_C01_034E':'Estimate!!Total!!Households!!HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Median income (dollars)',
            'S0501_C01_096E':'Estimate!!Total!!INCOME IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Households!!With cash public assistance income',
            'S0501_C01_097E':'Estimate!!Total!!INCOME IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Households!!With cash public assistance income!!Mean cash public assistance income (dollars)',
            'S0501_C01_100E':'Estimate!!Total!!INCOME IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Households!!With Food Stamp/SNAP benefits',
            'S0501_C01_101E':'Estimate!!Total!!INCOME IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Households!!Median Household income (dollars)',
            'S0501_C01_104E':'Estimate!!Total!!POVERTY STATUS IN THE PAST 12 MONTHS!!Population for whom poverty status is determined!!Below 100 percent of the poverty level',
            'S0501_C01_105E':'Estimate!!Total!!POVERTY STATUS IN THE PAST 12 MONTHS!!Population for whom poverty status is determined!!100 to 199 percent of the poverty level',
            'S0501_C01_106E':'Estimate!!Total!!POVERTY STATUS IN THE PAST 12 MONTHS!!Population for whom poverty status is determined!!At or above 200 percent of the poverty level',
            'S0501_C01_107E':'Estimate!!Total!!POVERTY STATUS IN THE PAST 12 MONTHS!!POVERTY RATES FOR FAMILIES FOR WHOM POVERTY STATUS IS DETERMINED!!All families',

            'S0501_C01_015E':'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!White',
            'S0501_C01_016E':'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!Black or African American',
            'S0501_C01_017E':'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!American Indian and Alaska Native',
            'S0501_C01_018E':'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!Asian',
            'S0501_C01_019E':'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!Native Hawaiian and Other Pacific Islander',
            'S0501_C01_021E':'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!Two or more races',
            'S0501_C01_022E':'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!Hispanic or Latino origin (of any race)',


            'S0501_C01_039E':'Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Less than high school graduate',
            'S0501_C01_040E':'Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)',
            'S0501_C01_041E':'Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college or associate\'s degree',
            'S0501_C01_042E':'S0501_C01_042E	Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor\'s degree',
            'S0501_C01_043E':'Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree',

            'S0501_C01_046E':'Estimate!!Total!!LANGUAGE SPOKEN AT HOME AND ABILITY TO SPEAK ENGLISH!!Population 5 years and over!!Language other than English',
            'S0501_C01_026E':'Estimate!!Total!!Total population!!Average household size',

            'S1901_C01_001E': 'Estimate!!Households!!Total',
            'S1901_C01_002E':'Estimate!!Households!!Total!!Less than $10,000',
            'S1901_C01_003E': 'Estimate!!Households!!Total!!$10,000 to $14,999',
            'S1901_C01_004E':'Estimate!!Households!!Total!!$15,000 to $24,999',
            'S1901_C01_005E':'Estimate!!Households!!Total!!$25,000 to $34,999',
            'S1901_C01_006E':'Estimate!!Households!!Total!!$35,000 to $49,999',
            'S1901_C01_007E':'Estimate!!Households!!Total!!$50,000 to $74,999',
            'S1901_C01_008E':'Estimate!!Households!!Total!!$75,000 to $99,999',
            'S1901_C01_009E':'Estimate!!Households!!Total!!$100,000 to $149,999',
            'S1901_C01_010E':'Estimate!!Households!!Total!!$150,000 to $199,999',
            'S1901_C01_011E':'Estimate!!Households!!Total!!$200,000 or more',
            'S1901_C01_012E':'Estimate!!Households!!Median income (dollars)'}

def gen_cities_acs_df(places_list, var_list, exception_dict, suffix_list, key='9d770ba2775550d6234ed8c12dd756762be8b9f5'):
    response = requests.get(f'https://api.census.gov/data/2021/acs/acs5/subject?get=NAME,{",".join(str(i) for i in var_list)}&for=place:{places_list[0][4]}&in=state:{places_list[0][3]}&key={key}').json()
    curr_df = pd.DataFrame(columns = response[0], data = response[1:])
    places_list = places_list[1:]

    for place in places_list:
        response = requests.get(f'https://api.census.gov/data/2021/acs/acs5/subject?get=NAME,{",".join(str(i) for i in var_list)}&for=place:{place[4]}&in=state:{place[3]}&key={key}').json()
        add_df = pd.DataFrame(columns = response[0], data = response[1:])
        curr_df = pd.concat([curr_df, add_df], ignore_index=True)

    curr_df = curr_df.rename(columns=acs_vars)

    def clean_cities_acs(df, exception_dict, suffix_list):
        df[['city', 'state']] = df['NAME'].str.split(',', expand=True)
        for exception in exception_dict.keys():
            df.loc[df['city'] == exception, 'city'] = exception_dict[exception]
        for suffix in suffix_list:
            df['city'] = df['city'].str.removesuffix(suffix)
            df['city'] = df['city'].str.strip()
        return df

    final_df = clean_cities_acs(curr_df, exception_dict, suffix_list)
    final_df = final_df.drop('NAME', axis=1)
    return final_df

key ='9d770ba2775550d6234ed8c12dd756762be8b9f5'
acs_vars_list = list(acs_vars.keys())

suffixes = ['city', 'town', 'municipality']
city_exceptions = {'Boise City city':'Boise',
                   'Urban Honolulu CDP':'Honolulu',
                   'Indianapolis city (balance)':'Indianapolis',
                   'Lexington-Fayette urban county':'Lexington',
                   'Louisville/Jefferson County metro government (balance)':'Louisville',
                   'Nashville-Davidson metropolitan government (balance)':'Nashville'}



cities_acs = gen_cities_acs_df(place_list, acs_vars_list, city_exceptions, suffixes, key='9d770ba2775550d6234ed8c12dd756762be8b9f5')


### ALSO PULL GINI
def gen_gini_acs_df(places_list, exception_dict, suffix_list, key='9d770ba2775550d6234ed8c12dd756762be8b9f5'):
    response = requests.get(f'https://api.census.gov/data/2021/acs/acs5?get=NAME,B19083_001E&for=place:{places_list[0][4]}&in=state:{places_list[0][3]}&key={key}').json()
    print('here')
    curr_df = pd.DataFrame(columns = response[0], data = response[1:])
    places_list = places_list[1:]
    print('there')

    for place in places_list:
        response = requests.get(f'https://api.census.gov/data/2021/acs/acs5?get=NAME,B19083_001E&for=place:{place[4]}&in=state:{place[3]}&key={key}').json()
        ('one time')
        add_df = pd.DataFrame(columns = response[0], data = response[1:])
        curr_df = pd.concat([curr_df, add_df], ignore_index=True)

    curr_df = curr_df.rename(columns=acs_vars)

    def clean_cities_acs(df, exception_dict, suffix_list):
        df[['city', 'state']] = df['NAME'].str.split(',', expand=True)
        for exception in exception_dict.keys():
            df.loc[df['city'] == exception, 'city'] = exception_dict[exception]
        for suffix in suffix_list:
            df['city'] = df['city'].str.removesuffix(suffix)
            df['city'] = df['city'].str.strip()
        return df

    final_df = clean_cities_acs(curr_df, exception_dict, suffix_list)
    final_df = final_df.drop('NAME', axis=1)
    return final_df
gini = gen_gini_acs_df(place_list, city_exceptions, suffixes, key='9d770ba2775550d6234ed8c12dd756762be8b9f5')

cities_acs['gini'] = gini['B19083_001E']


### RENAMING ACS VARS #####
acs_clean = cities_acs.rename(columns ={'Estimate!!Total population!!Total population':'pop',
                                         'Estimate!!Total!!Total population!!SEX AND AGE!!Female':'female',
                                         'Estimate!!Total!!Total population!!SUMMARY INDICATORS!!Median age (years)':'med_age',
                                         'Estimate!!Total!!Full-time, year-round civilian employed population 16 years and over':'perc_full_time',
                                         'Estimate!!Total!!INCOME IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Households!!With earnings!!Mean earnings (dollars)':'mean_earnings_hh',
                                         'Estimate!!Total!!Households!!HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Median income (dollars)':'median_earnings_hh',
                                         'Estimate!!Total!!INCOME IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Households!!With Food Stamp/SNAP benefits':'income_food_stmps',
                                         'Estimate!!Total!!POVERTY STATUS IN THE PAST 12 MONTHS!!POVERTY RATES FOR FAMILIES FOR WHOM POVERTY STATUS IS DETERMINED!!All families':'pov_rate',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!White':'white',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!Black or African American':'black',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!American Indian and Alaska Native':'indig_pop',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!Asian':'asian',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!Native Hawaiian and Other Pacific Islander':'pacific_isl',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!Two or more races':'two_races',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!Hispanic or Latino origin (of any race)':'hisp',
                                         'Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Less than high school graduate':'no_highschool',
                                         'Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)':'highschool',
                                         'Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college or associate\'s degree':'ass_deg',
                                         'S0501_C01_042EEstimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor\'s degree':'bach_deg',
                                         'Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree':'adv_deg',
                                         'B19083_001E':'gini',})

acs_clean.columns

acs_clean.to_csv('RedBlue/Data/Components/cities_acs.csv', index=False)






def gen_gini_acs_df(places_list, exception_dict, suffix_list, key='9d770ba2775550d6234ed8c12dd756762be8b9f5'):
    response = requests.get(f'https://api.census.gov/data/2021/acs/acs5?get=NAME,B19083_001E&for=place:{places_list[0][4]}&in=state:{places_list[0][3]}&key={key}').json()
    print('here')
    curr_df = pd.DataFrame(columns = response[0], data = response[1:])
    places_list = places_list[1:]
    print('there')

    for place in places_list:
        response = requests.get(f'https://api.census.gov/data/2021/acs/acs5?get=NAME,B19083_001E&for=place:{place[4]}&in=state:{place[3]}&key={key}').json()
        ('one time')
        add_df = pd.DataFrame(columns = response[0], data = response[1:])
        curr_df = pd.concat([curr_df, add_df], ignore_index=True)

    curr_df = curr_df.rename(columns=acs_vars)

    def clean_cities_acs(df, exception_dict, suffix_list):
        df[['city', 'state']] = df['NAME'].str.split(',', expand=True)
        for exception in exception_dict.keys():
            df.loc[df['city'] == exception, 'city'] = exception_dict[exception]
        for suffix in suffix_list:
            df['city'] = df['city'].str.removesuffix(suffix)
            df['city'] = df['city'].str.strip()
        return df

    final_df = clean_cities_acs(curr_df, exception_dict, suffix_list)
    final_df = final_df.drop('NAME', axis=1)
    return final_df


gini = gen_gini_acs_df(place_list, city_exceptions, suffixes, key='9d770ba2775550d6234ed8c12dd756762be8b9f5')

cities_acs['gini'] = gini['B19083_001E']


### RENAMING ACS VARS #####
acs_clean = cities_acs.rename(columns ={'Estimate!!Total population!!Total population':'pop',
                                         'Estimate!!Total!!Total population!!SEX AND AGE!!Female':'female',
                                         'Estimate!!Total!!Total population!!SUMMARY INDICATORS!!Median age (years)':'med_age',
                                         'Estimate!!Total!!Full-time, year-round civilian employed population 16 years and over':'perc_full_time',
                                         'Estimate!!Total!!INCOME IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Households!!With earnings!!Mean earnings (dollars)':'mean_earnings_hh',
                                         'Estimate!!Total!!Households!!HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Median income (dollars)':'median_earnings_hh',
                                         'Estimate!!Total!!INCOME IN THE PAST 12 MONTHS (IN 2021 INFLATION-ADJUSTED DOLLARS)!!Households!!With Food Stamp/SNAP benefits':'income_food_stmps',
                                         'Estimate!!Total!!POVERTY STATUS IN THE PAST 12 MONTHS!!POVERTY RATES FOR FAMILIES FOR WHOM POVERTY STATUS IS DETERMINED!!All families':'pov_rate',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!White':'white',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!Black or African American':'black',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!American Indian and Alaska Native':'indig_pop',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!Asian':'asian',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!One race!!Native Hawaiian and Other Pacific Islander':'pacific_isl',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!Two or more races':'two_races',
                                         'Estimate!!Total!!Total population!!RACE AND HISPANIC OR LATINO ORIGIN!!Hispanic or Latino origin (of any race)':'hisp',
                                         'Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Less than high school graduate':'no_highschool',
                                         'Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)':'highschool',
                                         'Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college or associate\'s degree':'ass_deg',
                                         'S0501_C01_042EEstimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor\'s degree':'bach_deg',
                                         'Estimate!!Total!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree':'adv_deg',
                                         'B19083_001E':'gini',})

acs_clean.columns

acs_clean.to_csv('RedBlue/Data/Components/cities_acs.csv', index=False)

