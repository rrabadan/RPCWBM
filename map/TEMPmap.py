#!/usr/bin/env python
import copy

# Temperature map
# DB:OMDS, table:CMS_RPC_PVSS_COND.FWCAENCHANNELADC
# DB:DB:cms_orcoff_prep, table:CMS_COND_RPC_NOISE.RPCPVSSTEMPPERRUN

mapLast = {}
mapLast[38059] = "WM2_S01_RB1in"
mapLast[38058] = "WM2_S01_RB1out"
mapLast[38057] = "WM2_S01_RB2"
mapLast[38056] = "WM2_S01_RB3"
mapLast[38055] = "WM2_S01_RB4"
mapLast[38064] = "WM2_S02_RB1in"
mapLast[38063] = "WM2_S02_RB1out"
mapLast[38062] = "WM2_S02_RB2"
mapLast[38061] = "WM2_S02_RB3"
mapLast[38060] = "WM2_S02_RB4"
mapLast[38069] = "WM2_S03_RB1in"
mapLast[38068] = "WM2_S03_RB1out"
mapLast[38067] = "WM2_S03_RB2"
mapLast[38066] = "WM2_S03_RB3"
mapLast[38065] = "WM2_S03_RB4"
mapLast[98321] = "WM2_S04_RB1in"
mapLast[97207] = "WM2_S04_RB1out"
mapLast[97208] = "WM2_S04_RB2"
mapLast[97209] = "WM2_S04_RB3"
mapLast[97210] = "WM2_S04_RB4minus"
mapLast[97211] = "WM2_S04_RB4plus"
mapLast[98319] = "WM2_S05_RB1in"
mapLast[97202] = "WM2_S05_RB1out"
mapLast[97203] = "WM2_S05_RB2"
mapLast[97204] = "WM2_S05_RB3"
mapLast[97205] = "WM2_S05_RB4"
mapLast[98317] = "WM2_S06_RB1in"
mapLast[97197] = "WM2_S06_RB1out"
mapLast[97198] = "WM2_S06_RB2"
mapLast[97199] = "WM2_S06_RB3"
mapLast[97200] = "WM2_S06_RB4"
mapLast[38286] = "WM2_S07_RB1in"
mapLast[38285] = "WM2_S07_RB1out"
mapLast[38284] = "WM2_S07_RB2"
mapLast[38283] = "WM2_S07_RB3"
mapLast[38282] = "WM2_S07_RB4"
mapLast[38291] = "WM2_S08_RB1in"
mapLast[38290] = "WM2_S08_RB1out"
mapLast[38289] = "WM2_S08_RB2"
mapLast[38288] = "WM2_S08_RB3"
mapLast[38287] = "WM2_S08_RB4"
mapLast[38296] = "WM2_S09_RB1in"
mapLast[38295] = "WM2_S09_RB1out"
mapLast[38294] = "WM2_S09_RB2"
mapLast[38293] = "WM2_S09_RB3"
mapLast[38292] = "WM2_S09_RB4"
mapLast[38075] = "WM2_S10_RB1in"
mapLast[38074] = "WM2_S10_RB1out"
mapLast[38073] = "WM2_S10_RB2"
mapLast[38072] = "WM2_S10_RB3"
mapLast[38071] = "WM2_S10_RB4minus"
mapLast[38070] = "WM2_S10_RB4plus"
mapLast[38080] = "WM2_S11_RB1in"
mapLast[38079] = "WM2_S11_RB1out"
mapLast[38078] = "WM2_S11_RB2"
mapLast[38077] = "WM2_S11_RB3"
mapLast[38076] = "WM2_S11_RB4"
mapLast[38085] = "WM2_S12_RB1in"
mapLast[38084] = "WM2_S12_RB1out"
mapLast[38083] = "WM2_S12_RB2"
mapLast[38082] = "WM2_S12_RB3"
mapLast[98195] = "WM2_S12_RB4"
mapLast[97954] = "WM1_S01_RB1in"
mapLast[37776] = "WM1_S01_RB1out"
mapLast[37775] = "WM1_S01_RB2"
mapLast[37774] = "WM1_S01_RB3"
mapLast[37773] = "WM1_S01_RB4"
mapLast[37782] = "WM1_S02_RB1in"
mapLast[37781] = "WM1_S02_RB1out"
mapLast[37780] = "WM1_S02_RB2"
mapLast[37779] = "WM1_S02_RB3"
mapLast[37778] = "WM1_S02_RB4"
mapLast[37787] = "WM1_S03_RB1in"
mapLast[37786] = "WM1_S03_RB1out"
mapLast[37785] = "WM1_S03_RB2"
mapLast[37784] = "WM1_S03_RB3"
mapLast[37783] = "WM1_S03_RB4"
mapLast[37989] = "WM1_S04_RB1in"
mapLast[37988] = "WM1_S04_RB1out"
mapLast[37987] = "WM1_S04_RB2"
mapLast[37986] = "WM1_S04_RB3"
mapLast[37985] = "WM1_S04_RB4minus"
mapLast[37984] = "WM1_S04_RB4plus"
mapLast[37994] = "WM1_S05_RB1in"
mapLast[37993] = "WM1_S05_RB1out"
mapLast[37992] = "WM1_S05_RB2"
mapLast[37991] = "WM1_S05_RB3"
mapLast[37990] = "WM1_S05_RB4"
mapLast[37999] = "WM1_S06_RB1in"
mapLast[37998] = "WM1_S06_RB1out"
mapLast[37997] = "WM1_S06_RB2"
mapLast[37996] = "WM1_S06_RB3"
mapLast[37995] = "WM1_S06_RB4"
mapLast[38004] = "WM1_S07_RB1in"
mapLast[38003] = "WM1_S07_RB1out"
mapLast[38002] = "WM1_S07_RB2"
mapLast[38001] = "WM1_S07_RB3"
mapLast[38000] = "WM1_S07_RB4"
mapLast[38009] = "WM1_S08_RB1in"
mapLast[38008] = "WM1_S08_RB1out"
mapLast[38007] = "WM1_S08_RB2"
mapLast[38006] = "WM1_S08_RB3"
mapLast[38005] = "WM1_S08_RB4"
mapLast[38014] = "WM1_S09_RB1in"
mapLast[38013] = "WM1_S09_RB1out"
mapLast[38012] = "WM1_S09_RB2"
mapLast[38011] = "WM1_S09_RB3"
mapLast[38010] = "WM1_S09_RB4"
mapLast[37793] = "WM1_S10_RB1in"
mapLast[37792] = "WM1_S10_RB1out"
mapLast[37791] = "WM1_S10_RB2"
mapLast[37790] = "WM1_S10_RB3"
mapLast[37789] = "WM1_S10_RB4minus"
mapLast[37788] = "WM1_S10_RB4plus"
mapLast[37798] = "WM1_S11_RB1in"
mapLast[37797] = "WM1_S11_RB1out"
mapLast[37796] = "WM1_S11_RB2"
mapLast[37795] = "WM1_S11_RB3"
mapLast[37794] = "WM1_S11_RB4"
mapLast[37803] = "WM1_S12_RB1in"
mapLast[37802] = "WM1_S12_RB1out"
mapLast[37801] = "WM1_S12_RB2"
mapLast[37800] = "WM1_S12_RB3"
mapLast[37799] = "WM1_S12_RB4"
mapLast[9522] = "W00_S01_RB1in"
mapLast[9521] = "W00_S01_RB1out"
mapLast[9520] = "W00_S01_RB2"
mapLast[9519] = "W00_S01_RB3"
mapLast[9518] = "W00_S01_RB4"
mapLast[9527] = "W00_S02_RB1in"
mapLast[9526] = "W00_S02_RB1out"
mapLast[9525] = "W00_S02_RB2"
mapLast[9524] = "W00_S02_RB3"
mapLast[9523] = "W00_S02_RB4"
mapLast[9532] = "W00_S03_RB1in"
mapLast[9531] = "W00_S03_RB1out"
mapLast[9530] = "W00_S03_RB2"
mapLast[9529] = "W00_S03_RB3"
mapLast[9528] = "W00_S03_RB4"
mapLast[9664] = "W00_S04_RB1in"
mapLast[9663] = "W00_S04_RB1out"
mapLast[9662] = "W00_S04_RB2"
mapLast[9661] = "W00_S04_RB3"
mapLast[9660] = "W00_S04_RB4minus"
mapLast[9659] = "W00_S04_RB4plus"
mapLast[9669] = "W00_S05_RB1in"
mapLast[9668] = "W00_S05_RB1out"
mapLast[9667] = "W00_S05_RB2"
mapLast[9666] = "W00_S05_RB3"
mapLast[9665] = "W00_S05_RB4"
mapLast[9674] = "W00_S06_RB1in"
mapLast[9673] = "W00_S06_RB1out"
mapLast[9672] = "W00_S06_RB2"
mapLast[9671] = "W00_S06_RB3"
mapLast[9670] = "W00_S06_RB4"
mapLast[9679] = "W00_S07_RB1in"
mapLast[9678] = "W00_S07_RB1out"
mapLast[9677] = "W00_S07_RB2"
mapLast[9676] = "W00_S07_RB3"
mapLast[9675] = "W00_S07_RB4"
mapLast[9684] = "W00_S08_RB1in"
mapLast[9683] = "W00_S08_RB1out"
mapLast[9682] = "W00_S08_RB2"
mapLast[9681] = "W00_S08_RB3"
mapLast[9680] = "W00_S08_RB4"
mapLast[9689] = "W00_S09_RB1in"
mapLast[9688] = "W00_S09_RB1out"
mapLast[9687] = "W00_S09_RB2"
mapLast[9686] = "W00_S09_RB3"
mapLast[9685] = "W00_S09_RB4"
mapLast[9538] = "W00_S10_RB1in"
mapLast[9537] = "W00_S10_RB1out"
mapLast[9536] = "W00_S10_RB2"
mapLast[9535] = "W00_S10_RB3"
mapLast[9534] = "W00_S10_RB4minus"
mapLast[9533] = "W00_S10_RB4plus"
mapLast[9543] = "W00_S11_RB1in"
mapLast[9542] = "W00_S11_RB1out"
mapLast[9541] = "W00_S11_RB2"
mapLast[9540] = "W00_S11_RB3"
mapLast[9539] = "W00_S11_RB4"
mapLast[9548] = "W00_S12_RB1in"
mapLast[9547] = "W00_S12_RB1out"
mapLast[9546] = "W00_S12_RB2"
mapLast[9545] = "W00_S12_RB3"
mapLast[9544] = "W00_S12_RB4"
mapLast[9209] = "WP1_S01_RB1in"
mapLast[9208] = "WP1_S01_RB1out"
mapLast[9207] = "WP1_S01_RB2"
mapLast[9206] = "WP1_S01_RB3"
mapLast[9205] = "WP1_S01_RB4"
mapLast[9214] = "WP1_S02_RB1in"
mapLast[9213] = "WP1_S02_RB1out"
mapLast[9212] = "WP1_S02_RB2"
mapLast[9211] = "WP1_S02_RB3"
mapLast[9210] = "WP1_S02_RB4"
mapLast[9219] = "WP1_S03_RB1in"
mapLast[9218] = "WP1_S03_RB1out"
mapLast[9217] = "WP1_S03_RB2"
mapLast[9216] = "WP1_S03_RB3"
mapLast[9215] = "WP1_S03_RB4"
mapLast[9421] = "WP1_S04_RB1in"
mapLast[9420] = "WP1_S04_RB1out"
mapLast[9419] = "WP1_S04_RB2"
mapLast[9418] = "WP1_S04_RB3"
mapLast[9417] = "WP1_S04_RB4minus"
mapLast[9416] = "WP1_S04_RB4plus"
mapLast[9426] = "WP1_S05_RB1in"
mapLast[9425] = "WP1_S05_RB1out"
mapLast[9424] = "WP1_S05_RB2"
mapLast[9423] = "WP1_S05_RB3"
mapLast[9422] = "WP1_S05_RB4"
mapLast[9431] = "WP1_S06_RB1in"
mapLast[9430] = "WP1_S06_RB1out"
mapLast[9429] = "WP1_S06_RB2"
mapLast[9428] = "WP1_S06_RB3"
mapLast[9427] = "WP1_S06_RB4"
mapLast[9436] = "WP1_S07_RB1in"
mapLast[9435] = "WP1_S07_RB1out"
mapLast[9434] = "WP1_S07_RB2"
mapLast[9433] = "WP1_S07_RB3"
mapLast[9432] = "WP1_S07_RB4"
mapLast[9441] = "WP1_S08_RB1in"
mapLast[9440] = "WP1_S08_RB1out"
mapLast[9439] = "WP1_S08_RB2"
mapLast[9438] = "WP1_S08_RB3"
mapLast[9437] = "WP1_S08_RB4"
mapLast[9446] = "WP1_S09_RB1in"
mapLast[9445] = "WP1_S09_RB1out"
mapLast[9444] = "WP1_S09_RB2"
mapLast[9443] = "WP1_S09_RB3"
mapLast[9442] = "WP1_S09_RB4"
mapLast[9225] = "WP1_S10_RB1in"
mapLast[9224] = "WP1_S10_RB1out"
mapLast[9223] = "WP1_S10_RB2"
mapLast[9222] = "WP1_S10_RB3"
mapLast[9221] = "WP1_S10_RB4minus"
mapLast[9220] = "WP1_S10_RB4plus"
mapLast[9230] = "WP1_S11_RB1in"
mapLast[9229] = "WP1_S11_RB1out"
mapLast[9228] = "WP1_S11_RB2"
mapLast[9227] = "WP1_S11_RB3"
mapLast[9226] = "WP1_S11_RB4"
mapLast[9235] = "WP1_S12_RB1in"
mapLast[9234] = "WP1_S12_RB1out"
mapLast[9233] = "WP1_S12_RB2"
mapLast[9232] = "WP1_S12_RB3"
mapLast[9231] = "WP1_S12_RB4"
mapLast[36931] = "WP2_S01_RB1in"
mapLast[36930] = "WP2_S01_RB1out"
mapLast[36929] = "WP2_S01_RB2"
mapLast[36928] = "WP2_S01_RB3"
mapLast[36927] = "WP2_S01_RB4"
mapLast[36936] = "WP2_S02_RB1in"
mapLast[36935] = "WP2_S02_RB1out"
mapLast[36934] = "WP2_S02_RB2"
mapLast[36933] = "WP2_S02_RB3"
mapLast[36932] = "WP2_S02_RB4"
mapLast[36941] = "WP2_S03_RB1in"
mapLast[36940] = "WP2_S03_RB1out"
mapLast[36939] = "WP2_S03_RB2"
mapLast[36938] = "WP2_S03_RB3"
mapLast[36937] = "WP2_S03_RB4"
mapLast[37143] = "WP2_S04_RB1in"
mapLast[37142] = "WP2_S04_RB1out"
mapLast[37141] = "WP2_S04_RB2"
mapLast[37140] = "WP2_S04_RB3"
mapLast[37139] = "WP2_S04_RB4minus"
mapLast[37138] = "WP2_S04_RB4plus"
mapLast[37148] = "WP2_S05_RB1in"
mapLast[37147] = "WP2_S05_RB1out"
mapLast[37146] = "WP2_S05_RB2"
mapLast[37145] = "WP2_S05_RB3"
mapLast[37144] = "WP2_S05_RB4"
mapLast[37153] = "WP2_S06_RB1in"
mapLast[37152] = "WP2_S06_RB1out"
mapLast[37151] = "WP2_S06_RB2"
mapLast[37150] = "WP2_S06_RB3"
mapLast[37149] = "WP2_S06_RB4"
mapLast[9154] = "WP2_S07_RB1in"
mapLast[9153] = "WP2_S07_RB1out"
mapLast[9152] = "WP2_S07_RB2"
mapLast[9151] = "WP2_S07_RB3"
mapLast[9150] = "WP2_S07_RB4"
mapLast[9159] = "WP2_S08_RB1in"
mapLast[9158] = "WP2_S08_RB1out"
mapLast[9157] = "WP2_S08_RB2"
mapLast[9156] = "WP2_S08_RB3"
mapLast[9155] = "WP2_S08_RB4"
mapLast[9164] = "WP2_S09_RB1in"
mapLast[9163] = "WP2_S09_RB1out"
mapLast[9162] = "WP2_S09_RB2"
mapLast[9161] = "WP2_S09_RB3"
mapLast[9160] = "WP2_S09_RB4"
mapLast[36947] = "WP2_S10_RB1in"
mapLast[36946] = "WP2_S10_RB1out"
mapLast[36945] = "WP2_S10_RB2"
mapLast[36944] = "WP2_S10_RB3"
mapLast[36943] = "WP2_S10_RB4minus"
mapLast[36942] = "WP2_S10_RB4plus"
mapLast[36952] = "WP2_S11_RB1in"
mapLast[36951] = "WP2_S11_RB1out"
mapLast[36950] = "WP2_S11_RB2"
mapLast[36949] = "WP2_S11_RB3"
mapLast[36948] = "WP2_S11_RB4"
mapLast[36957] = "WP2_S12_RB1in"
mapLast[36956] = "WP2_S12_RB1out"
mapLast[36955] = "WP2_S12_RB2"
mapLast[36954] = "WP2_S12_RB3"
mapLast[36953] = "WP2_S12_RB4"
mapLast[143748] = "EN3_R2_C01"
mapLast[143749] = "EN3_R2_C07"
mapLast[143750] = "EN3_R2_C13"
mapLast[143751] = "EN3_R2_C19"
mapLast[143752] = "EN3_R2_C25"
mapLast[143753] = "EN3_R2_C31"
mapLast[143754] = "EN3_R3_C01"
mapLast[143755] = "EN3_R3_C07"
mapLast[143756] = "EN3_R3_C13"
mapLast[143757] = "EN3_R3_C19"
mapLast[143758] = "EN3_R3_C25"
mapLast[143759] = "EN3_R3_C31"
mapLast[143736] = "EN2_R2_C01"
mapLast[143737] = "EN2_R2_C07"
mapLast[143738] = "EN2_R2_C13"
mapLast[143739] = "EN2_R2_C19"
mapLast[143740] = "EN2_R2_C25"
mapLast[143741] = "EN2_R2_C31"
mapLast[143742] = "EN2_R3_C01"
mapLast[143743] = "EN2_R3_C07"
mapLast[143744] = "EN2_R3_C13"
mapLast[143745] = "EN2_R3_C19"
mapLast[143746] = "EN2_R3_C25"
mapLast[143747] = "EN2_R3_C31"
mapLast[143724] = "EN1_R2_C01"
mapLast[143725] = "EN1_R2_C07"
mapLast[143726] = "EN1_R2_C13"
mapLast[143727] = "EN1_R2_C19"
mapLast[143728] = "EN1_R2_C25"
mapLast[143729] = "EN1_R2_C31"
mapLast[143730] = "EN1_R3_C01"
mapLast[143731] = "EN1_R3_C07"
mapLast[143732] = "EN1_R3_C13"
mapLast[143733] = "EN1_R3_C19"
mapLast[143734] = "EN1_R3_C25"
mapLast[143735] = "EN1_R3_C31"
mapLast[143357] = "EP1_R2_C01"
mapLast[143358] = "EP1_R2_C07"
mapLast[143359] = "EP1_R2_C13"
mapLast[143360] = "EP1_R2_C19"
mapLast[143361] = "EP1_R2_C25"
mapLast[143362] = "EP1_R2_C31"
mapLast[143363] = "EP1_R3_C01"
mapLast[143364] = "EP1_R3_C07"
mapLast[143365] = "EP1_R3_C13"
mapLast[143366] = "EP1_R3_C19"
mapLast[143367] = "EP1_R3_C25"
mapLast[143368] = "EP1_R3_C31"
mapLast[143369] = "EP2_R2_C01"
mapLast[143370] = "EP2_R2_C07"
mapLast[143371] = "EP2_R2_C13"
mapLast[143372] = "EP2_R2_C19"
mapLast[143373] = "EP2_R2_C25"
mapLast[143374] = "EP2_R2_C31"
mapLast[143375] = "EP2_R3_C01"
mapLast[143376] = "EP2_R3_C07"
mapLast[143377] = "EP2_R3_C13"
mapLast[143378] = "EP2_R3_C19"
mapLast[143379] = "EP2_R3_C25"
mapLast[143380] = "EP2_R3_C31"
mapLast[143381] = "EP3_R2_C01"
mapLast[143382] = "EP3_R2_C07"
mapLast[143383] = "EP3_R2_C13"
mapLast[143384] = "EP3_R2_C19"
mapLast[143385] = "EP3_R2_C25"
mapLast[143386] = "EP3_R2_C31"
mapLast[143387] = "EP3_R3_C01"
mapLast[143388] = "EP3_R3_C07"
mapLast[143389] = "EP3_R3_C13"
mapLast[143390] = "EP3_R3_C19"
mapLast[143391] = "EP3_R3_C25"
mapLast[143392] = "EP3_R3_C31"
