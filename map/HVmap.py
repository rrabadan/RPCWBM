#!/usr/bin/env python
import copy

# HV map
# DB:OMDS, table:CMS_RPC_PVSS_COND.FWCAENCHANNEL
# DB:DB:cms_orcoff_prep, table:CMS_COND_RPC_NOISE.RPCPVSSPERRUN

#mapLast
#map03Nov
#map26Aug 

mapLast = {}
mapLast[3143]= "WM2_S01_RB1in"
mapLast[3144]= "WM2_S01_RB1out"
mapLast[3145]= "WM2_S01_RB2in"
mapLast[3146]= "WM2_S01_RB2out"
mapLast[3147]= "WM2_S01_RB3minus"
mapLast[3148]= "WM2_S01_RB3plus"
mapLast[3150]= "WM2_S01_RB4minus"
mapLast[3151]= "WM2_S01_RB4plus"
mapLast[3152]= "WM2_S02_RB1in"
mapLast[3153]= "WM2_S02_RB1out"
mapLast[3154]= "WM2_S02_RB2in"
mapLast[3155]= "WM2_S02_RB2out"
mapLast[3157]= "WM2_S02_RB3minus"
mapLast[3158]= "WM2_S02_RB3plus"
mapLast[3159]= "WM2_S02_RB4minus"
mapLast[3160]= "WM2_S02_RB4plus"
mapLast[3161]= "WM2_S03_RB1in"
mapLast[3162]= "WM2_S03_RB1out"
mapLast[3164]= "WM2_S03_RB2in"
mapLast[3165]= "WM2_S03_RB2out"
mapLast[3166]= "WM2_S03_RB3minus"
mapLast[3167]= "WM2_S03_RB3plus"
mapLast[3168]= "WM2_S03_RB4minus"
mapLast[3169]= "WM2_S03_RB4plus"
mapLast[3171]= "WM2_S04_RB1in"
mapLast[3172]= "WM2_S04_RB1out"
mapLast[3173]= "WM2_S04_RB2in"
mapLast[3174]= "WM2_S04_RB2out"
mapLast[3175]= "WM2_S04_RB3minus"
mapLast[3176]= "WM2_S04_RB3plus"
mapLast[3178]= "WM2_S04_RB4minusminus"
mapLast[3179]= "WM2_S04_RB4minus"
mapLast[3180]= "WM2_S04_RB4plus"
mapLast[3181]= "WM2_S04_RB4plusplus"
mapLast[3182]= "WM2_S05_RB1in"
mapLast[3183]= "WM2_S05_RB1out"
mapLast[3185]= "WM2_S05_RB2in"
mapLast[3186]= "WM2_S05_RB2out"
mapLast[3187]= "WM2_S05_RB3minus"
mapLast[3188]= "WM2_S05_RB3plus"
mapLast[3189]= "WM2_S05_RB4minus"
mapLast[3190]= "WM2_S05_RB4plus"
mapLast[3192]= "WM2_S06_RB1in"
mapLast[3193]= "WM2_S06_RB1out"
mapLast[3194]= "WM2_S06_RB2in"
mapLast[3195]= "WM2_S06_RB2out"
mapLast[3196]= "WM2_S06_RB3minus"
mapLast[3197]= "WM2_S06_RB3plus"
mapLast[3199]= "WM2_S06_RB4minus"
mapLast[3200]= "WM2_S06_RB4plus"
mapLast[3201]= "WM2_S07_RB1in"
mapLast[3202]= "WM2_S07_RB1out"
mapLast[3203]= "WM2_S07_RB2in"
mapLast[3204]= "WM2_S07_RB2out"
mapLast[3206]= "WM2_S07_RB3minus"
mapLast[3207]= "WM2_S07_RB3plus"
mapLast[3208]= "WM2_S07_RB4minus"
mapLast[3209]= "WM2_S07_RB4plus"
mapLast[3210]= "WM2_S08_RB1in"
mapLast[3211]= "WM2_S08_RB1out"
mapLast[3213]= "WM2_S08_RB2in"
mapLast[3214]= "WM2_S08_RB2out"
mapLast[3215]= "WM2_S08_RB3minus"
mapLast[3216]= "WM2_S08_RB3plus"
mapLast[3217]= "WM2_S08_RB4minus"
mapLast[3218]= "WM2_S08_RB4plus"
mapLast[3220]= "WM2_S09_RB1in"
mapLast[3221]= "WM2_S09_RB1out"
mapLast[3222]= "WM2_S09_RB2in"
mapLast[3223]= "WM2_S09_RB2out"
mapLast[3224]= "WM2_S09_RB3minus"
mapLast[3225]= "WM2_S09_RB3plus"
mapLast[3227]= "WM2_S09_RB4"
mapLast[3228]= "WM2_S10_RB1in"
mapLast[3229]= "WM2_S10_RB1out"
mapLast[3230]= "WM2_S10_RB2in"
mapLast[3231]= "WM2_S10_RB2out"
mapLast[3232]= "WM2_S10_RB3minus"
mapLast[3234]= "WM2_S10_RB3plus"
mapLast[3235]= "WM2_S10_RB4minus"
mapLast[3236]= "WM2_S10_RB4plus"
mapLast[3237]= "WM2_S11_RB1in"
mapLast[3238]= "WM2_S11_RB1out"
mapLast[3239]= "WM2_S11_RB2in"
mapLast[3241]= "WM2_S11_RB2out"
mapLast[3242]= "WM2_S11_RB3minus"
mapLast[3243]= "WM2_S11_RB3plus"
mapLast[3244]= "WM2_S11_RB4"
mapLast[3245]= "WM2_S12_RB1in"
mapLast[3246]= "WM2_S12_RB1out"
mapLast[3269]= "WM2_S12_RB2in"
mapLast[3270]= "WM2_S12_RB2out"
mapLast[3271]= "WM2_S12_RB3minus"
mapLast[3272]= "WM2_S12_RB3plus"
mapLast[3273]= "WM2_S12_RB4minus"
mapLast[3274]= "WM2_S12_RB4plus"
mapLast[3038]= "WM1_S01_RB1in"
mapLast[3039]= "WM1_S01_RB1out"
mapLast[3040]= "WM1_S01_RB2in"
mapLast[3041]= "WM1_S01_RB2out"
mapLast[3042]= "WM1_S01_RB3minus"
mapLast[3043]= "WM1_S01_RB3plus"
mapLast[3045]= "WM1_S01_RB4minus"
mapLast[3046]= "WM1_S01_RB4plus"
mapLast[3047]= "WM1_S02_RB1in"
mapLast[3048]= "WM1_S02_RB1out"
mapLast[3049]= "WM1_S02_RB2in"
mapLast[3050]= "WM1_S02_RB2out"
mapLast[3052]= "WM1_S02_RB3minus"
mapLast[3053]= "WM1_S02_RB3plus"
mapLast[3054]= "WM1_S02_RB4minus"
mapLast[3055]= "WM1_S02_RB4plus"
mapLast[3056]= "WM1_S03_RB1in"
mapLast[3057]= "WM1_S03_RB1out"
mapLast[3059]= "WM1_S03_RB2in"
mapLast[3060]= "WM1_S03_RB2out"
mapLast[3061]= "WM1_S03_RB3minus"
mapLast[3062]= "WM1_S03_RB3plus"
mapLast[3063]= "WM1_S03_RB4minus"
mapLast[3064]= "WM1_S03_RB4plus"
mapLast[3066]= "WM1_S04_RB1in"
mapLast[3067]= "WM1_S04_RB1out"
mapLast[3068]= "WM1_S04_RB2in"
mapLast[3069]= "WM1_S04_RB2out"
mapLast[3070]= "WM1_S04_RB3minus"
mapLast[3071]= "WM1_S04_RB3plus"
mapLast[3073]= "WM1_S04_RB4minusminus"
mapLast[3074]= "WM1_S04_RB4minus"
mapLast[3075]= "WM1_S04_RB4plus"
mapLast[3076]= "WM1_S04_RB4plusplus"
mapLast[3077]= "WM1_S05_RB1in"
mapLast[3078]= "WM1_S05_RB1out"
mapLast[3080]= "WM1_S05_RB2in"
mapLast[3081]= "WM1_S05_RB2out"
mapLast[3082]= "WM1_S05_RB3minus"
mapLast[3083]= "WM1_S05_RB3plus"
mapLast[3084]= "WM1_S05_RB4minus"
mapLast[3085]= "WM1_S05_RB4plus"
mapLast[3087]= "WM1_S06_RB1in"
mapLast[3088]= "WM1_S06_RB1out"
mapLast[3089]= "WM1_S06_RB2in"
mapLast[3090]= "WM1_S06_RB2out"
mapLast[3091]= "WM1_S06_RB3minus"
mapLast[3092]= "WM1_S06_RB3plus"
mapLast[3094]= "WM1_S06_RB4minus"
mapLast[3095]= "WM1_S06_RB4plus"
mapLast[3096]= "WM1_S07_RB1in"
mapLast[3097]= "WM1_S07_RB1out"
mapLast[3098]= "WM1_S07_RB2in"
mapLast[3099]= "WM1_S07_RB2out"
mapLast[3101]= "WM1_S07_RB3minus"
mapLast[3102]= "WM1_S07_RB3plus"
mapLast[3103]= "WM1_S07_RB4minus"
mapLast[3104]= "WM1_S07_RB4plus"
mapLast[3105]= "WM1_S08_RB1in"
mapLast[3106]= "WM1_S08_RB1out"
mapLast[3108]= "WM1_S08_RB2in"
mapLast[3109]= "WM1_S08_RB2out"
mapLast[3110]= "WM1_S08_RB3minus"
mapLast[3111]= "WM1_S08_RB3plus"
mapLast[3112]= "WM1_S08_RB4minus"
mapLast[3113]= "WM1_S08_RB4plus"
mapLast[3115]= "WM1_S09_RB1in"
mapLast[3116]= "WM1_S09_RB1out"
mapLast[3117]= "WM1_S09_RB2in"
mapLast[3118]= "WM1_S09_RB2out"
mapLast[3119]= "WM1_S09_RB3minus"
mapLast[3120]= "WM1_S09_RB3plus"
mapLast[3122]= "WM1_S09_RB4"
mapLast[3123]= "WM1_S10_RB1in"
mapLast[3124]= "WM1_S10_RB1out"
mapLast[3125]= "WM1_S10_RB2in"
mapLast[3126]= "WM1_S10_RB2out"
mapLast[3127]= "WM1_S10_RB3minus"
mapLast[3129]= "WM1_S10_RB3plus"
mapLast[3130]= "WM1_S10_RB4minus"
mapLast[3131]= "WM1_S10_RB4plus"
mapLast[3132]= "WM1_S11_RB1in"
mapLast[3133]= "WM1_S11_RB1out"
mapLast[3134]= "WM1_S11_RB2in"
mapLast[3136]= "WM1_S11_RB2out"
mapLast[3137]= "WM1_S11_RB3minus"
mapLast[3138]= "WM1_S11_RB3plus"
mapLast[3139]= "WM1_S11_RB4"
mapLast[3140]= "WM1_S12_RB1in"
mapLast[3141]= "WM1_S12_RB1out"
mapLast[3262]= "WM1_S12_RB2in"
mapLast[3263]= "WM1_S12_RB2out"
mapLast[3264]= "WM1_S12_RB3minus"
mapLast[3265]= "WM1_S12_RB3plus"
mapLast[3266]= "WM1_S12_RB4minus"
mapLast[3267]= "WM1_S12_RB4plus"
mapLast[3033]= "W00_S01_RB1in"
mapLast[6409]= "W00_S01_RB1out"
mapLast[6411]= "W00_S01_RB2in"
mapLast[6413]= "W00_S01_RB2out"
mapLast[6415]= "W00_S01_RB3minus"
mapLast[6418]= "W00_S01_RB3plus"
mapLast[6421]= "W00_S01_RB4minus"
mapLast[6423]= "W00_S01_RB4plus"
mapLast[6425]= "W00_S02_RB1in"
mapLast[6427]= "W00_S02_RB1out"
mapLast[6429]= "W00_S02_RB2in"
mapLast[6431]= "W00_S02_RB2out"
mapLast[6433]= "W00_S02_RB3minus"
mapLast[6435]= "W00_S02_RB3plus"
mapLast[6437]= "W00_S02_RB4minus"
mapLast[6439]= "W00_S02_RB4plus"
mapLast[6441]= "W00_S03_RB1in"
mapLast[6443]= "W00_S03_RB1out"
mapLast[6445]= "W00_S03_RB2in"
mapLast[6447]= "W00_S03_RB2out"
mapLast[6449]= "W00_S03_RB3minus"
mapLast[6451]= "W00_S03_RB3plus"
mapLast[6453]= "W00_S03_RB4minus"
mapLast[6455]= "W00_S03_RB4plus"
mapLast[6457]= "W00_S04_RB1in"
mapLast[6459]= "W00_S04_RB1out"
mapLast[6461]= "W00_S04_RB2in"
mapLast[6463]= "W00_S04_RB2out"
mapLast[6465]= "W00_S04_RB3minus"
mapLast[6467]= "W00_S04_RB3plus"
mapLast[6469]= "W00_S04_RB4minusminus"
mapLast[6471]= "W00_S04_RB4minus"
mapLast[6473]= "W00_S04_RB4plus"
mapLast[6475]= "W00_S04_RB4plusplus"
mapLast[6477]= "W00_S05_RB1in"
mapLast[6479]= "W00_S05_RB1out"
mapLast[6481]= "W00_S05_RB2in"
mapLast[6483]= "W00_S05_RB2out"
mapLast[6485]= "W00_S05_RB3minus"
mapLast[6487]= "W00_S05_RB3plus"
mapLast[6489]= "W00_S05_RB4minus"
mapLast[6491]= "W00_S05_RB4plus"
mapLast[6493]= "W00_S06_RB1in"
mapLast[6495]= "W00_S06_RB1out"
mapLast[6497]= "W00_S06_RB2in"
mapLast[6499]= "W00_S06_RB2out"
mapLast[6501]= "W00_S06_RB3minus"
mapLast[6503]= "W00_S06_RB3plus"
mapLast[6505]= "W00_S06_RB4minus"
mapLast[6507]= "W00_S06_RB4plus"
mapLast[6509]= "W00_S07_RB1in"
mapLast[6511]= "W00_S07_RB1out"
mapLast[6513]= "W00_S07_RB2in"
mapLast[6515]= "W00_S07_RB2out"
mapLast[6517]= "W00_S07_RB3minus"
mapLast[6519]= "W00_S07_RB3plus"
mapLast[6521]= "W00_S07_RB4minus"
mapLast[6523]= "W00_S07_RB4plus"
mapLast[6525]= "W00_S08_RB1in"
mapLast[6527]= "W00_S08_RB1out"
mapLast[6529]= "W00_S08_RB2in"
mapLast[6531]= "W00_S08_RB2out"
mapLast[6533]= "W00_S08_RB3minus"
mapLast[6535]= "W00_S08_RB3plus"
mapLast[6537]= "W00_S08_RB4minus"
mapLast[6539]= "W00_S08_RB4plus"
mapLast[6541]= "W00_S09_RB1in"
mapLast[6543]= "W00_S09_RB1out"
mapLast[6545]= "W00_S09_RB2in"
mapLast[6547]= "W00_S09_RB2out"
mapLast[6549]= "W00_S09_RB3minus"
mapLast[6551]= "W00_S09_RB3plus"
mapLast[6553]= "W00_S09_RB4"
mapLast[6555]= "W00_S10_RB1in"
mapLast[6557]= "W00_S10_RB1out"
mapLast[6559]= "W00_S10_RB2in"
mapLast[6561]= "W00_S10_RB2out"
mapLast[6563]= "W00_S10_RB3minus"
mapLast[6565]= "W00_S10_RB3plus"
mapLast[6567]= "W00_S10_RB4minus"
mapLast[6569]= "W00_S10_RB4plus"
mapLast[6571]= "W00_S11_RB1in"
mapLast[6573]= "W00_S11_RB1out"
mapLast[6575]= "W00_S11_RB2in"
mapLast[6577]= "W00_S11_RB2out"
mapLast[6579]= "W00_S11_RB3minus"
mapLast[6581]= "W00_S11_RB3plus"
mapLast[3034]= "W00_S11_RB4"
mapLast[3035]= "W00_S12_RB1in"
mapLast[3036]= "W00_S12_RB1out"
mapLast[3255]= "W00_S12_RB2in"
mapLast[3256]= "W00_S12_RB2out"
mapLast[3257]= "W00_S12_RB3minus"
mapLast[3258]= "W00_S12_RB3plus"
mapLast[3259]= "W00_S12_RB4minus"
mapLast[3260]= "W00_S12_RB4plus"
mapLast[2928]= "WP1_S01_RB1in"
mapLast[2929]= "WP1_S01_RB1out"
mapLast[2930]= "WP1_S01_RB2in"
mapLast[2931]= "WP1_S01_RB2out"
mapLast[2932]= "WP1_S01_RB3minus"
mapLast[2933]= "WP1_S01_RB3plus"
mapLast[2935]= "WP1_S01_RB4minus"
mapLast[2936]= "WP1_S01_RB4plus"
mapLast[2937]= "WP1_S02_RB1in"
mapLast[2938]= "WP1_S02_RB1out"
mapLast[2939]= "WP1_S02_RB2in"
mapLast[2940]= "WP1_S02_RB2out"
mapLast[2942]= "WP1_S02_RB3minus"
mapLast[2943]= "WP1_S02_RB3plus"
mapLast[2944]= "WP1_S02_RB4minus"
mapLast[2945]= "WP1_S02_RB4plus"
mapLast[2946]= "WP1_S03_RB1in"
mapLast[2947]= "WP1_S03_RB1out"
mapLast[2949]= "WP1_S03_RB2in"
mapLast[2950]= "WP1_S03_RB2out"
mapLast[2951]= "WP1_S03_RB3minus"
mapLast[2952]= "WP1_S03_RB3plus"
mapLast[2953]= "WP1_S03_RB4minus"
mapLast[2954]= "WP1_S03_RB4plus"
mapLast[2956]= "WP1_S04_RB1in"
mapLast[2957]= "WP1_S04_RB1out"
mapLast[2958]= "WP1_S04_RB2in"
mapLast[2959]= "WP1_S04_RB2out"
mapLast[2960]= "WP1_S04_RB3minus"
mapLast[2961]= "WP1_S04_RB3plus"
mapLast[2963]= "WP1_S04_RB4minusminus"
mapLast[2964]= "WP1_S04_RB4minus"
mapLast[2965]= "WP1_S04_RB4plus"
mapLast[2966]= "WP1_S04_RB4plusplus"
mapLast[2967]= "WP1_S05_RB1in"
mapLast[2968]= "WP1_S05_RB1out"
mapLast[2970]= "WP1_S05_RB2in"
mapLast[2971]= "WP1_S05_RB2out"
mapLast[2972]= "WP1_S05_RB3minus"
mapLast[2973]= "WP1_S05_RB3plus"
mapLast[2974]= "WP1_S05_RB4minus"
mapLast[2975]= "WP1_S05_RB4plus"
mapLast[2977]= "WP1_S06_RB1in"
mapLast[2978]= "WP1_S06_RB1out"
mapLast[2979]= "WP1_S06_RB2in"
mapLast[2980]= "WP1_S06_RB2out"
mapLast[2981]= "WP1_S06_RB3minus"
mapLast[2982]= "WP1_S06_RB3plus"
mapLast[2984]= "WP1_S06_RB4minus"
mapLast[2985]= "WP1_S06_RB4plus"
mapLast[2986]= "WP1_S07_RB1in"
mapLast[2987]= "WP1_S07_RB1out"
mapLast[2988]= "WP1_S07_RB2in"
mapLast[2989]= "WP1_S07_RB2out"
mapLast[2991]= "WP1_S07_RB3minus"
mapLast[2992]= "WP1_S07_RB3plus"
mapLast[2993]= "WP1_S07_RB4minus"
mapLast[2994]= "WP1_S07_RB4plus"
mapLast[2995]= "WP1_S08_RB1in"
mapLast[2996]= "WP1_S08_RB1out"
mapLast[2998]= "WP1_S08_RB2in"
mapLast[2999]= "WP1_S08_RB2out"
mapLast[3000]= "WP1_S08_RB3minus"
mapLast[3001]= "WP1_S08_RB3plus"
mapLast[3002]= "WP1_S08_RB4minus"
mapLast[3003]= "WP1_S08_RB4plus"
mapLast[3005]= "WP1_S09_RB1in"
mapLast[3006]= "WP1_S09_RB1out"
mapLast[3007]= "WP1_S09_RB2in"
mapLast[3008]= "WP1_S09_RB2out"
mapLast[3009]= "WP1_S09_RB3minus"
mapLast[3010]= "WP1_S09_RB3plus"
mapLast[3012]= "WP1_S09_RB4"
mapLast[3013]= "WP1_S10_RB1in"
mapLast[3014]= "WP1_S10_RB1out"
mapLast[3015]= "WP1_S10_RB2in"
mapLast[3016]= "WP1_S10_RB2out"
mapLast[3017]= "WP1_S10_RB3minus"
mapLast[3019]= "WP1_S10_RB3plus"
mapLast[3020]= "WP1_S10_RB4minus"
mapLast[3021]= "WP1_S10_RB4plus"
mapLast[3022]= "WP1_S11_RB1in"
mapLast[3023]= "WP1_S11_RB1out"
mapLast[3024]= "WP1_S11_RB2in"
mapLast[3026]= "WP1_S11_RB2out"
mapLast[3027]= "WP1_S11_RB3minus"
mapLast[3028]= "WP1_S11_RB3plus"
mapLast[3029]= "WP1_S11_RB4"
mapLast[3030]= "WP1_S12_RB1in"
mapLast[3031]= "WP1_S12_RB1out"
mapLast[3248]= "WP1_S12_RB2in"
mapLast[3249]= "WP1_S12_RB2out"
mapLast[3250]= "WP1_S12_RB3minus"
mapLast[3251]= "WP1_S12_RB3plus"
mapLast[3252]= "WP1_S12_RB4minus"
mapLast[3253]= "WP1_S12_RB4plus"
mapLast[315]= "WP2_S01_RB1in"
mapLast[316]= "WP2_S01_RB1out"
mapLast[317]= "WP2_S01_RB2in"
mapLast[318]= "WP2_S01_RB2out"
mapLast[319]= "WP2_S01_RB3minus"
mapLast[320]= "WP2_S01_RB3plus"
mapLast[322]= "WP2_S01_RB4minus"
mapLast[323]= "WP2_S01_RB4plus"
mapLast[324]= "WP2_S02_RB1in"
mapLast[325]= "WP2_S02_RB1out"
mapLast[326]= "WP2_S02_RB2in"
mapLast[327]= "WP2_S02_RB2out"
mapLast[329]= "WP2_S02_RB3minus"
mapLast[330]= "WP2_S02_RB3plus"
mapLast[331]= "WP2_S02_RB4minus"
mapLast[332]= "WP2_S02_RB4plus"
mapLast[333]= "WP2_S03_RB1in"
mapLast[334]= "WP2_S03_RB1out"
mapLast[336]= "WP2_S03_RB2in"
mapLast[337]= "WP2_S03_RB2out"
mapLast[338]= "WP2_S03_RB3minus"
mapLast[339]= "WP2_S03_RB3plus"
mapLast[340]= "WP2_S03_RB4minus"
mapLast[341]= "WP2_S03_RB4plus"
mapLast[343]= "WP2_S04_RB1in"
mapLast[344]= "WP2_S04_RB1out"
mapLast[345]= "WP2_S04_RB2in"
mapLast[346]= "WP2_S04_RB2out"
mapLast[347]= "WP2_S04_RB3minus"
mapLast[348]= "WP2_S04_RB3plus"
mapLast[350]= "WP2_S04_RB4minusminus"
mapLast[351]= "WP2_S04_RB4minus"
mapLast[352]= "WP2_S04_RB4plus"
mapLast[353]= "WP2_S04_RB4plusplus"
mapLast[354]= "WP2_S05_RB1in"
mapLast[355]= "WP2_S05_RB1out"
mapLast[357]= "WP2_S05_RB2in"
mapLast[358]= "WP2_S05_RB2out"
mapLast[359]= "WP2_S05_RB3minus"
mapLast[360]= "WP2_S05_RB3plus"
mapLast[361]= "WP2_S05_RB4minus"
mapLast[362]= "WP2_S05_RB4plus"
mapLast[364]= "WP2_S06_RB1in"
mapLast[365]= "WP2_S06_RB1out"
mapLast[366]= "WP2_S06_RB2in"
mapLast[367]= "WP2_S06_RB2out"
mapLast[368]= "WP2_S06_RB3minus"
mapLast[369]= "WP2_S06_RB3plus"
mapLast[371]= "WP2_S06_RB4minus"
mapLast[372]= "WP2_S06_RB4plus"
mapLast[373]= "WP2_S07_RB1in"
mapLast[374]= "WP2_S07_RB1out"
mapLast[375]= "WP2_S07_RB2in"
mapLast[376]= "WP2_S07_RB2out"
mapLast[378]= "WP2_S07_RB3minus"
mapLast[379]= "WP2_S07_RB3plus"
mapLast[380]= "WP2_S07_RB4minus"
mapLast[381]= "WP2_S07_RB4plus"
mapLast[382]= "WP2_S08_RB1in"
mapLast[383]= "WP2_S08_RB1out"
mapLast[385]= "WP2_S08_RB2in"
mapLast[386]= "WP2_S08_RB2out"
mapLast[387]= "WP2_S08_RB3minus"
mapLast[388]= "WP2_S08_RB3plus"
mapLast[389]= "WP2_S08_RB4minus"
mapLast[390]= "WP2_S08_RB4plus"
mapLast[392]= "WP2_S09_RB1in"
mapLast[393]= "WP2_S09_RB1out"
mapLast[394]= "WP2_S09_RB2in"
mapLast[395]= "WP2_S09_RB2out"
mapLast[396]= "WP2_S09_RB3minus"
mapLast[397]= "WP2_S09_RB3plus"
mapLast[399]= "WP2_S09_RB4"
mapLast[400]= "WP2_S10_RB1in"
mapLast[401]= "WP2_S10_RB1out"
mapLast[402]= "WP2_S10_RB2in"
mapLast[403]= "WP2_S10_RB2out"
mapLast[404]= "WP2_S10_RB3minus"
mapLast[406]= "WP2_S10_RB3plus"
mapLast[407]= "WP2_S10_RB4minus"
mapLast[408]= "WP2_S10_RB4plus"
mapLast[409]= "WP2_S11_RB1in"
mapLast[410]= "WP2_S11_RB1out"
mapLast[411]= "WP2_S11_RB2in"
mapLast[413]= "WP2_S11_RB2out"
mapLast[414]= "WP2_S11_RB3minus"
mapLast[415]= "WP2_S11_RB3plus"
mapLast[416]= "WP2_S11_RB4"
mapLast[417]= "WP2_S12_RB1in"
mapLast[418]= "WP2_S12_RB1out"
mapLast[420]= "WP2_S12_RB2in"
mapLast[421]= "WP2_S12_RB2out"
mapLast[422]= "WP2_S12_RB3minus"
mapLast[423]= "WP2_S12_RB3plus"
mapLast[424]= "WP2_S12_RB4minus"
mapLast[425]= "WP2_S12_RB4plus"

mapLast[142816]= "EP1_R1_C01_TOP"
mapLast[142817]= "EP1_R1_C01_BOT"
mapLast[142818]= "EP1_R1_C02_TOP"
mapLast[142819]= "EP1_R1_C02_BOT"
mapLast[142820]= "EP1_R1_C03_TOP"
mapLast[142821]= "EP1_R1_C03_BOT"
mapLast[142823]= "EP1_R3_C33"
mapLast[142824]= "EP1_R3_C29_EP2_R3_C02"
mapLast[142825]= "EP1_R2_C29_EP1_R3_C31"
mapLast[142826]= "EP1_R3_C35_EP2_R3_C03"
mapLast[142827]= "EP1_R3_C06_EP2_R3_C07"
mapLast[142828]= "EP1_R2_C36_EP1_R3_C09"
mapLast[142830]= "EP1_R2_C33_EP1_R3_C34"
mapLast[142831]= "EP1_R2_C02_EP2_R2_C02"
mapLast[142832]= "EP1_R2_C07_EP1_R2_C10"
mapLast[142833]= "EP1_R3_C03_EP1_R3_C36"
mapLast[142834]= "EP1_R2_C06_EP2_R3_C04"
mapLast[142835]= "EP2_R2_C03_EP2_R3_C05"
mapLast[142837]= "EP2_R2_C06_EP2_R2_C08"
mapLast[142838]= "EP2_R2_C07_EP2_R3_C06"
mapLast[142839]= "EP1_R2_C30_EP1_R3_C10"
mapLast[142840]= "EP1_R2_C34_EP1_R3_C02"
mapLast[142841]= "EP1_R3_C07_EP2_R2_C05"
mapLast[142842]= "EP1_R3_C32_EP2_R3_C01"
mapLast[142844]= "EP1_R2_C09_EP1_R2_C32"
mapLast[142845]= "EP1_R2_C31_EP2_R3_C08"
mapLast[142846]= "EP1_R3_C30_EP2_R2_C01"
mapLast[142847]= "EP1_R2_C35_EP2_R3_C09"
mapLast[142848]= "EP1_R3_C05_EP2_R2_C09"
mapLast[142849]= "EP1_R2_C08_EP1_R3_C08"
mapLast[142851]= "EP1_R2_C04_EP2_R2_C04"
mapLast[142852]= "EP1_R2_C01_EP1_R2_C03"
mapLast[142853]= "EP1_R2_C05_EP1_R3_C01"
mapLast[142854]= "EP3_R3_C30"
mapLast[142855]= "EP2_R2_C31_EP2_R2_C32"
mapLast[142856]= "EP2_R2_C10_EP2_R2_C29"
mapLast[142858]= "EP2_R3_C30_EP3_R2_C10"
mapLast[142859]= "EP3_R2_C03_EP3_R3_C32"
mapLast[142860]= "EP2_R3_C29_EP3_R3_C10"
mapLast[142861]= "EP2_R2_C36_EP3_R2_C35"
mapLast[142862]= "EP2_R3_C31_EP3_R3_C04"
mapLast[142863]= "EP3_R2_C09_EP3_R2_C31"
mapLast[142865]= "EP3_R2_C06_EP3_R3_C07"
mapLast[142866]= "EP3_R2_C01_EP3_R2_C08"
mapLast[142867]= "EP3_R2_C02_EP3_R3_C03"
mapLast[142868]= "EP3_R2_C04_EP3_R2_C32"
mapLast[142869]= "EP3_R2_C05_EP3_R3_C01"
mapLast[142870]= "EP3_R2_C34_EP3_R3_C29"
mapLast[142872]= "EP3_R3_C06_EP3_R3_C09"
mapLast[142873]= "EP3_R3_C05_EP3_R3_C34"
mapLast[142874]= "EP3_R3_C02_EP3_R3_C31"
mapLast[142875]= "EP3_R3_C33_EP3_R3_C36"
mapLast[142876]= "EP3_R2_C29_EP3_R3_C35"
mapLast[142877]= "EP3_R2_C30_EP3_R2_C36"
mapLast[142882]= "EP1_R2_C21_EP2_R3_C15"
mapLast[142883]= "EP1_R2_C23_EP2_R3_C16"
mapLast[142884]= "EP1_R2_C17_EP1_R3_C18"
mapLast[142885]= "EP1_R2_C12_EP1_R3_C11"
mapLast[142886]= "EP1_R3_C21_EP1_R3_C26"
mapLast[142887]= "EP1_R3_C22_EP1_R3_C23"
mapLast[142889]= "EP1_R2_C22_EP1_R2_C26"
mapLast[142890]= "EP1_R2_C11_EP1_R2_C15"
mapLast[142891]= "EP1_R2_C28_EP1_R3_C14"
mapLast[142892]= "EP1_R3_C27_EP2_R3_C19"
mapLast[142893]= "EP1_R3_C16_EP2_R3_C14"
mapLast[142894]= "EP2_R2_C18_EP2_R3_C11"
mapLast[142896]= "EP1_R2_C20_EP2_R3_C13"
mapLast[142897]= "EP1_R2_C18_EP2_R2_C19"
mapLast[142898]= "EP1_R2_C25_EP2_R2_C16"
mapLast[142899]= "EP1_R3_C19_EP1_R3_C25"
mapLast[142900]= "EP1_R3_C20_EP1_R3_C24"
mapLast[142901]= "EP1_R3_C13_EP1_R3_C17"
mapLast[142903]= "EP1_R2_C27_EP2_R2_C13"
mapLast[142904]= "EP2_R3_C17_EP2_R3_C18"
mapLast[142905]= "EP1_R2_C16_EP2_R3_C12"
mapLast[142906]= "EP1_R2_C19_EP2_R2_C17"
mapLast[142907]= "EP2_R2_C11_EP2_R2_C12"
mapLast[142908]= "EP1_R2_C24_EP2_R2_C14"
mapLast[142910]= "EP1_R2_C14_EP1_R3_C12"
mapLast[142911]= "EP1_R2_C13_EP2_R2_C15"
mapLast[142912]= "EP1_R3_C15_EP1_R3_C28"
mapLast[142913]= "EP2_R2_C22_EP3_R3_C24"
mapLast[142914]= "EP3_R2_C18_EP3_R3_C25"
mapLast[142915]= "EP3_R2_C14_EP3_R2_C24"
mapLast[142917]= "EP3_R2_C11_EP3_R2_C16"
mapLast[142918]= "EP3_R2_C23_EP3_R3_C28"
mapLast[142919]= "EP3_R2_C20_EP3_R2_C25"
mapLast[142920]= "EP3_R2_C22_EP3_R3_C23"
mapLast[142921]= "EP3_R2_C19_EP3_R3_C19"
mapLast[142922]= "EP2_R3_C23_EP3_R2_C26"
mapLast[142924]= "EP2_R3_C27_EP3_R3_C27"
mapLast[142925]= "EP3_R3_C18_EP3_R3_C20"
mapLast[142926]= "EP2_R2_C27_EP3_R2_C17"
mapLast[142927]= "EP3_R2_C27_EP3_R3_C17"
mapLast[142928]= "EP3_R2_C28_EP3_R3_C26"
mapLast[142929]= "EP3_R3_C16_EP3_R3_C22"
mapLast[142931]= "EP2_R3_C28_EP3_R2_C13"
mapLast[142932]= "EP2_R2_C20_EP2_R2_C26"
mapLast[142933]= "EP3_R2_C15_EP3_R3_C15"
mapLast[142934]= "EP2_R3_C21_EP3_R2_C21"
mapLast[142935]= "EP2_R3_C26_EP3_R3_C21"
mapLast[142936]= "EP2_R3_C22_EP3_R2_C12"
mapLast[142938]= "EP3_R3_C11_EP3_R3_C14"
mapLast[142939]= "EP2_R2_C28_EP2_R3_C20"
mapLast[142940]= "EP2_R2_C24_EP2_R3_C25"
mapLast[142941]= "EP2_R3_C24_EP3_R3_C12"
mapLast[142942]= "EP2_R2_C23_EP3_R3_C13"
mapLast[142943]= "EP2_R2_C21_EP2_R2_C25"
mapLast[142948]= "EN1_R3_C31"
mapLast[142949]= "EN2_R3_C04"
mapLast[142950]= "EN1_R2_C01_EN2_R2_C04"
mapLast[142951]= "EN1_R2_C36_EN1_R3_C06"
mapLast[142952]= "EN1_R3_C03_EN1_R3_C05"
mapLast[142953]= "EN1_R2_C32_EN1_R2_C35"
mapLast[142955]= "EN1_R2_C05_EN1_R2_C08"
mapLast[142956]= "EN1_R2_C07_EN1_R2_C09"
mapLast[142957]= "EN1_R2_C04_EN1_R2_C30"
mapLast[142958]= "EN1_R2_C29_EN2_R2_C08"
mapLast[142959]= "EN1_R3_C02_EN2_R2_C03"
mapLast[142960]= "EN1_R2_C06_EN2_R2_C01"
mapLast[142962]= "EN2_R3_C01_EN2_R3_C02"
mapLast[142963]= "EN1_R2_C03_EN2_R2_C02"
mapLast[142964]= "EN1_R2_C31_EN2_R2_C07"
mapLast[142965]= "EN1_R3_C08_EN2_R2_C06"
mapLast[142966]= "EN1_R2_C02_EN1_R3_C01"
mapLast[142967]= "EN1_R2_C33_EN2_R3_C07"
mapLast[142969]= "EN1_R3_C33_EN2_R3_C06"
mapLast[142970]= "EN2_R2_C05_EN2_R2_C09"
mapLast[142971]= "EN2_R3_C05_EN2_R3_C09"
mapLast[142972]= "EN1_R3_C07_EN1_R3_C09"
mapLast[142973]= "EN1_R2_C10_EN1_R3_C34"
mapLast[142974]= "EN1_R2_C34_EN2_R3_C08"
mapLast[142976]= "EN1_R3_C29_EN1_R3_C35"
mapLast[142977]= "EN1_R3_C30_EN1_R3_C32"
mapLast[142978]= "EN1_R3_C36_EN2_R3_C03"
mapLast[142979]= "EN2_R2_C29_EN2_R2_C33"
mapLast[142980]= "EN2_R3_C29_EN2_R3_C35"
mapLast[142981]= "EN2_R2_C10_EN2_R2_C36"
mapLast[142983]= "EN2_R2_C30_EN2_R2_C34"
mapLast[142984]= "EN2_R3_C10_EN2_R3_C32"
mapLast[142985]= "EN2_R3_C31_EN2_R3_C34"
mapLast[142986]= "EN2_R3_C33_EN3_R3_C10"
mapLast[142987]= "EN2_R3_C30_EN3_R2_C35"
mapLast[142988]= "EN3_R2_C29_EN3_R3_C34"
mapLast[142990]= "EN2_R2_C32_EN3_R2_C07"
mapLast[142991]= "EN2_R2_C31_EN3_R2_C01"
mapLast[142992]= "EN2_R2_C35_EN3_R3_C02"
mapLast[142993]= "EN3_R2_C31_EN3_R3_C35"
mapLast[142994]= "EN3_R3_C03_EN3_R3_C04"
mapLast[142995]= "EN2_R3_C36_EN3_R3_C32"
mapLast[142997]= "EN3_R3_C29_EN3_R3_C30"
mapLast[142998]= "EN3_R2_C10_EN3_R3_C01"
mapLast[142999]= "EN3_R2_C36_EN3_R3_C09"
mapLast[143000]= "EN3_R2_C03_EN3_R2_C33"
mapLast[143001]= "EN3_R2_C09_EN3_R3_C06"
mapLast[143002]= "EN3_R2_C04_EN3_R2_C08"
mapLast[143004]= "EN3_R2_C06_EN3_R2_C32"
mapLast[143005]= "EN3_R3_C07_EN3_R3_C36"
mapLast[143006]= "EN3_R2_C02_EN3_R2_C05"
mapLast[143007]= "EN3_R3_C05_EN3_R3_C08"
mapLast[143008]= "EN3_R2_C34_EN3_R3_C33"
mapLast[143009]= "EN3_R2_C30_EN3_R3_C31"
mapLast[143014]= "EN1_R2_C15_EN1_R2_C17"
mapLast[143015]= "EN1_R2_C11_EN1_R2_C13"
mapLast[143016]= "EN1_R2_C12_EN2_R2_C12"
mapLast[143017]= "EN1_R2_C14_EN1_R2_C22"
mapLast[143018]= "EN1_R3_C24_EN2_R3_C12"
mapLast[143019]= "EN1_R3_C21_EN2_R3_C19"
mapLast[143021]= "EN1_R2_C19_EN1_R2_C20"
mapLast[143022]= "EN1_R2_C25_EN2_R2_C13"
mapLast[143023]= "EN1_R3_C25_EN1_R3_C26"
mapLast[143024]= "EN1_R3_C16"
mapLast[143025]= "EN1_R3_C18_EN2_R3_C16"
mapLast[143026]= "EN1_R3_C15_EN1_R3_C27"
mapLast[143028]= "EN1_R3_C14_EN2_R3_C14"
mapLast[143029]= "EN2_R3_C15_EN2_R3_C18"
mapLast[143030]= "EN2_R2_C17_EN2_R3_C11"
mapLast[143031]= "EN2_R2_C16_EN2_R3_C17"
mapLast[143032]= "EN1_R2_C16_EN2_R2_C19"
mapLast[143033]= "EN2_R2_C14_EN2_R2_C18"
mapLast[143035]= "EN1_R2_C28_EN1_R3_C12"
mapLast[143036]= "EN1_R3_C11"
mapLast[143037]= "EN1_R3_C17_EN1_R3_C22"
mapLast[143038]= "EN1_R3_C19_EN2_R2_C15"
mapLast[143039]= "EN1_R2_C26_EN2_R3_C13"
mapLast[143040]= "EN1_R2_C21_EN1_R3_C13"
mapLast[143042]= "EN1_R2_C23_EN1_R2_C27"
mapLast[143043]= "EN1_R2_C24_EN1_R3_C20"
mapLast[143044]= "EN1_R3_C23_EN1_R3_C28"
mapLast[143045]= "EN3_R2_C17"
mapLast[143046]= "EN3_R3_C17_EN3_R3_C28"
mapLast[143047]= "EN2_R3_C21_EN2_R3_C27"
mapLast[143049]= "EN2_R3_C25_EN2_R3_C26"
mapLast[143050]= "EN2_R3_C22_EN3_R2_C12"
mapLast[143051]= "EN2_R3_C24_EN3_R3_C14"
mapLast[143052]= "EN2_R2_C21_EN2_R2_C22"
mapLast[143053]= "EN2_R2_C26_EN2_R2_C27"
mapLast[143054]= "EN2_R2_C23_EN2_R2_C24"
mapLast[143056]= "EN2_R3_C23_EN3_R2_C13"
mapLast[143057]= "EN2_R2_C25_EN3_R2_C11"
mapLast[143058]= "EN3_R2_C16_EN3_R2_C18"
mapLast[143059]= "EN2_R2_C28_EN3_R2_C15"
mapLast[143060]= "EN3_R3_C16_EN3_R3_C18"
mapLast[143061]= "EN3_R2_C14_EN3_R2_C21"
mapLast[143063]= "EN3_R3_C11_EN3_R3_C19"
mapLast[143064]= "EN3_R2_C25_EN3_R3_C15"
mapLast[143065]= "EN2_R3_C28_EN3_R2_C27"
mapLast[143066]= "EN2_R2_C20_EN3_R2_C20"
mapLast[143067]= "EN3_R2_C26_EN3_R3_C12"
mapLast[143068]= "EN2_R3_C20_EN3_R3_C26"
mapLast[143070]= "EN3_R2_C23_EN3_R3_C25"
mapLast[143071]= "EN3_R2_C19_EN3_R3_C24"
mapLast[143072]= "EN3_R3_C13_EN3_R3_C21"
mapLast[143073]= "EN3_R2_C22_EN3_R2_C28"
mapLast[143074]= "EN3_R3_C20_EN3_R3_C23"
mapLast[143075]= "EN3_R2_C24_EN3_R3_C27"
mapLast[203812]= "EP4_R2_C01_EP4_R3_C01"   
mapLast[203813]= "EP4_R2_C02_EP4_R3_C02"   
mapLast[203814]= "EP4_R2_C03_EP4_R3_C03"   
mapLast[203815]= "EP4_R2_C04_EP4_R3_C04"   
mapLast[203816]= "EP4_R2_C05_EP4_R3_C05"   
mapLast[203817]= "EP4_R2_C06_EP4_R3_C06"   
mapLast[203818]= "EP4_R2_C07_EP4_R3_C07"   
mapLast[203819]= "EP4_R2_C08_EP4_R3_C08"   
mapLast[203820]= "EP4_R2_C09_EP4_R3_C09"   
mapLast[203821]= "EP4_R2_C10_EP4_R3_C10"   
mapLast[203822]= "EP4_R2_C29_EP4_R3_C29"   
mapLast[203823]= "EP4_R2_C30_EP4_R3_C30"   
mapLast[203824]= "EP4_R2_C31_EP4_R3_C31"   
mapLast[203825]= "EP4_R2_C32_EP4_R3_C32"   
mapLast[203826]= "EP4_R2_C33_EP4_R3_C33"   
mapLast[203827]= "EP4_R2_C34_EP4_R3_C34"   
mapLast[203828]= "EP4_R2_C35_EP4_R3_C35"   
mapLast[203829]= "EP4_R2_C36_EP4_R3_C36"   
mapLast[203830]= "EP4_R2_C11_EP4_R3_C11"   
mapLast[203831]= "EP4_R2_C12_EP4_R3_C12"   
mapLast[203832]= "EP4_R2_C13_EP4_R3_C13"   
mapLast[203833]= "EP4_R2_C14_EP4_R3_C14"   
mapLast[203834]= "EP4_R2_C15_EP4_R3_C15"   
mapLast[203835]= "EP4_R2_C16_EP4_R3_C16"   
mapLast[203836]= "EP4_R2_C17_EP4_R3_C17"   
mapLast[203837]= "EP4_R2_C18_EP4_R3_C18"   
mapLast[203838]= "EP4_R2_C19_EP4_R3_C19"   
mapLast[203839]= "EP4_R2_C20_EP4_R3_C20"   
mapLast[203840]= "EP4_R2_C21_EP4_R3_C21"   
mapLast[203841]= "EP4_R2_C22_EP4_R3_C22"   
mapLast[203842]= "EP4_R2_C23_EP4_R3_C23"   
mapLast[203843]= "EP4_R2_C24_EP4_R3_C24"   
mapLast[203844]= "EP4_R2_C25_EP4_R3_C25"   
mapLast[203845]= "EP4_R2_C26_EP4_R3_C26"   
mapLast[203846]= "EP4_R2_C27_EP4_R3_C27"   
mapLast[203847]= "EP4_R2_C28_EP4_R3_C28"   
mapLast[203848]= "EN4_R2_C01_EN4_R3_C01"   
mapLast[203849]= "EN4_R2_C02_EN4_R3_C02"   
mapLast[203850]= "EN4_R2_C03_EN4_R3_C03"   
mapLast[203851]= "EN4_R2_C04_EN4_R3_C04"   
mapLast[203852]= "EN4_R2_C05_EN4_R3_C05"   
mapLast[203853]= "EN4_R2_C06_EN4_R3_C06"   
mapLast[203854]= "EN4_R2_C07_EN4_R3_C07"   
mapLast[203855]= "EN4_R2_C08_EN4_R3_C08"   
mapLast[203856]= "EN4_R2_C09_EN4_R3_C09"   
mapLast[203857]= "EN4_R2_C10_EN4_R3_C10"   
mapLast[203858]= "EN4_R2_C29_EN4_R3_C29"   
mapLast[203859]= "EN4_R2_C30_EN4_R3_C30"   
mapLast[203860]= "EN4_R2_C31_EN4_R3_C31"   
mapLast[203861]= "EN4_R2_C32_EN4_R3_C32"   
mapLast[203862]= "EN4_R2_C33_EN4_R3_C33"   
mapLast[203863]= "EN4_R2_C34_EN4_R3_C34"   
mapLast[203864]= "EN4_R2_C35_EN4_R3_C35"   
mapLast[203865]= "EN4_R2_C36_EN4_R3_C36"   
mapLast[203866]= "EN4_R2_C11_EN4_R3_C11"   
mapLast[203867]= "EN4_R2_C12_EN4_R3_C12"   
mapLast[203868]= "EN4_R2_C13_EN4_R3_C13"   
mapLast[203869]= "EN4_R2_C14_EN4_R3_C14"   
mapLast[203870]= "EN4_R2_C15_EN4_R3_C15"   
mapLast[203871]= "EN4_R2_C16_EN4_R3_C16"   
mapLast[203872]= "EN4_R2_C17_EN4_R3_C17"   
mapLast[203873]= "EN4_R2_C18_EN4_R3_C18"   
mapLast[203874]= "EN4_R2_C19_EN4_R3_C19"   
mapLast[203875]= "EN4_R2_C20_EN4_R3_C20"   
mapLast[203876]= "EN4_R2_C21_EN4_R3_C21"   
mapLast[203877]= "EN4_R2_C22_EN4_R3_C22"   
mapLast[203878]= "EN4_R2_C23_EN4_R3_C23"   
mapLast[203879]= "EN4_R2_C24_EN4_R3_C24"   
mapLast[203880]= "EN4_R2_C25_EN4_R3_C25"   
mapLast[203881]= "EN4_R2_C26_EN4_R3_C26"   
mapLast[203882]= "EN4_R2_C27_EN4_R3_C27"   
mapLast[203883]= "EN4_R2_C28_EN4_R3_C28"   
mapLast[216665]= "EP2_R2_C33_EP2_R2_C35"
mapLast[216666]= "EP2_R2_C30_EP2_R3_C10"
mapLast[216667]= "EP2_R3_C36_EP3_R3_C08"
mapLast[216668]= "EP2_R2_C34_EP2_R3_C34"
mapLast[216669]= "EP2_R3_C32_EP3_R2_C07"
mapLast[216670]= "EP2_R3_C35_EP3_R2_C33"
mapLast[216671]= "EP1_R1_C04_TOP"
mapLast[216672]= "EP1_R1_C04_BOT"
mapLast[216673]= "EP1_R3_C04"
mapLast[216674]= "EP2_R3_C33"
mapLast[216689]= "EN1_R3_C04_EN1_R3_C10"
mapLast[216701]= "EN1_R2_C18_EN2_R2_C11"

map03Nov = copy.deepcopy(mapLast)
#map(only changed it) before the time 03 Nov 2014.
map03Nov[42823]=  "EP1_R2_C01_EP1_R2_C02"    
map03Nov[142826]= "EP1_R2_C07_EP1_R2_C08"    
map03Nov[142827]= "EP1_R2_C09_EP1_R2_C10"    
map03Nov[142828]= "EP1_R2_C29_EP1_R2_C30"    
map03Nov[142830]= "EP1_R2_C31_EP1_R2_C32"    
map03Nov[142831]= "EP1_R2_C33_EP1_R2_C34"    
map03Nov[142832]= "EP1_R2_C35_EP1_R2_C36"    
map03Nov[142834]= "EP1_R3_C03_EP1_R3_C04"    
map03Nov[142835]= "EP1_R3_C05_EP1_R3_C06"    
map03Nov[142837]= "EP1_R3_C07_EP1_R3_C08"    
map03Nov[142838]= "EP1_R3_C09_EP1_R3_C10"    
map03Nov[142839]= "EP1_R3_C29_EP1_R3_C30"    
map03Nov[142840]= "EP1_R3_C31_EP1_R3_C32"    
map03Nov[142841]= "EP1_R3_C33_EP1_R3_C34"    
map03Nov[142842]= "EP1_R3_C35_EP1_R3_C36"    
map03Nov[142844]= "EP2_R2_C01_EP2_R3_C01"    
map03Nov[142845]= "EP2_R2_C02_EP2_R3_C02"    
map03Nov[142846]= "EP2_R2_C03_EP2_R3_C03"    
map03Nov[142847]= "EP2_R2_C04_EP2_R3_C04"    
map03Nov[142848]= "EP2_R2_C05_EP2_R3_C05"    
map03Nov[142849]= "EP2_R2_C06_EP2_R3_C06"    
map03Nov[142851]= "EP2_R2_C07_EP2_R3_C07"    
map03Nov[142852]= "EP2_R2_C08_EP2_R3_C08"    
map03Nov[142853]= "EP2_R2_C09_EP2_R3_C09"    
map03Nov[142854]= "EP2_R2_C10_EP2_R3_C10"    
map03Nov[142855]= "EP2_R2_C29_EP2_R3_C29"    
map03Nov[142856]= "EP2_R2_C30_EP2_R3_C30"    
map03Nov[142858]= "EP3_R2_C01_EP3_R3_C01"    
map03Nov[142859]= "EP3_R2_C02_EP3_R3_C02"    
map03Nov[142860]= "EP3_R2_C03_EP3_R3_C03"    
map03Nov[142861]= "EP3_R2_C04_EP3_R3_C04"    
map03Nov[142862]= "EP3_R2_C05_EP3_R3_C05"    
map03Nov[142863]= "EP3_R2_C06_EP3_R3_C06"    
map03Nov[142865]= "EP3_R2_C07_EP3_R3_C07"    
map03Nov[142866]= "EP3_R2_C08_EP3_R3_C08"    
map03Nov[142867]= "EP3_R2_C09_EP3_R3_C09"    
map03Nov[142868]= "EP3_R2_C10_EP3_R3_C10"    
map03Nov[142869]= "EP3_R2_C29_EP3_R3_C29"    
map03Nov[142870]= "EP3_R2_C30_EP3_R3_C30"    
map03Nov[142872]= "EP3_R2_C31_EP3_R3_C31"    
map03Nov[142873]= "EP3_R2_C32_EP3_R3_C32"    
map03Nov[142874]= "EP3_R2_C33_EP3_R3_C33"    
map03Nov[142875]= "EP3_R2_C34_EP3_R3_C34"    
map03Nov[142876]= "EP3_R2_C35_EP3_R3_C35"    
map03Nov[142877]= "EP3_R2_C36_EP3_R3_C36"    
map03Nov[142882]= "EP1_R2_C11_EP1_R2_C12"    
map03Nov[142883]= "EP1_R2_C13_EP1_R2_C14"    
map03Nov[142884]= "EP1_R2_C15_EP1_R2_C16"    
map03Nov[142885]= "EP1_R2_C17_EP1_R2_C18"    
map03Nov[142886]= "EP1_R2_C19_EP1_R2_C20"    
map03Nov[142887]= "EP1_R2_C21_EP1_R2_C22"    
map03Nov[142889]= "EP1_R2_C23_EP1_R2_C24"    
map03Nov[142890]= "EP1_R2_C25_EP1_R2_C26"    
map03Nov[142891]= "EP1_R2_C27_EP1_R2_C28"    
map03Nov[142892]= "EP1_R3_C11_EP1_R3_C12"    
map03Nov[142893]= "EP1_R3_C13_EP1_R3_C14"    
map03Nov[142894]= "EP1_R3_C15_EP1_R3_C16"    
map03Nov[142896]= "EP1_R3_C17_EP1_R3_C18"    
map03Nov[142897]= "EP1_R3_C19_EP1_R3_C20"    
map03Nov[142898]= "EP1_R3_C21_EP1_R3_C22"    
map03Nov[142899]= "EP1_R3_C23_EP1_R3_C24"    
map03Nov[142900]= "EP1_R3_C25_EP1_R3_C26"    
map03Nov[142901]= "EP1_R3_C27_EP1_R3_C28"    
map03Nov[142903]= "EP2_R2_C11_EP2_R3_C11"    
map03Nov[142904]= "EP2_R2_C12_EP2_R3_C12"    
map03Nov[142905]= "EP2_R2_C13_EP2_R3_C13"    
map03Nov[142906]= "EP2_R2_C14_EP2_R3_C14"    
map03Nov[142907]= "EP2_R2_C15_EP2_R3_C15"    
map03Nov[142908]= "EP2_R2_C16_EP2_R3_C16"    
map03Nov[142910]= "EP2_R2_C17_EP2_R3_C17"    
map03Nov[142911]= "EP2_R2_C18_EP2_R3_C18"    
map03Nov[142912]= "EP2_R2_C19_EP2_R3_C19"    
map03Nov[142913]= "EP2_R2_C20_EP2_R3_C20"    
map03Nov[142914]= "EP2_R2_C21_EP2_R3_C21"    
map03Nov[142915]= "EP2_R2_C22_EP2_R3_C22"    
map03Nov[142917]= "EP2_R2_C23_EP2_R3_C23"    
map03Nov[142918]= "EP2_R2_C24_EP2_R3_C24"    
map03Nov[142919]= "EP2_R2_C25_EP2_R3_C25"    
map03Nov[142920]= "EP2_R2_C26_EP2_R3_C26"    
map03Nov[142921]= "EP2_R2_C27_EP2_R3_C27"    
map03Nov[142922]= "EP2_R2_C28_EP2_R3_C28"    
map03Nov[142924]= "EP3_R2_C11_EP3_R3_C11"    
map03Nov[142925]= "EP3_R2_C12_EP3_R3_C12"    
map03Nov[142926]= "EP3_R2_C13_EP3_R3_C13"    
map03Nov[142927]= "EP3_R2_C14_EP3_R3_C14"    
map03Nov[142928]= "EP3_R2_C15_EP3_R3_C15"    
map03Nov[142929]= "EP3_R2_C16_EP3_R3_C16"    
map03Nov[142931]= "EP3_R2_C17_EP3_R3_C17"    
map03Nov[142932]= "EP3_R2_C18_EP3_R3_C18"    
map03Nov[142933]= "EP3_R2_C19_EP3_R3_C19"    
map03Nov[142934]= "EP3_R2_C20_EP3_R3_C20"    
map03Nov[142935]= "EP3_R2_C21_EP3_R3_C21"    
map03Nov[142936]= "EP3_R2_C22_EP3_R3_C22"    
map03Nov[142938]= "EP3_R2_C23_EP3_R3_C23"    
map03Nov[142939]= "EP3_R2_C24_EP3_R3_C24"    
map03Nov[142940]= "EP3_R2_C25_EP3_R3_C25"    
map03Nov[142941]= "EP3_R2_C26_EP3_R3_C26"    
map03Nov[142942]= "EP3_R2_C27_EP3_R3_C27"    
map03Nov[142943]= "EP3_R2_C28_EP3_R3_C28"    
map03Nov[142948]= "EN1_R2_C01_EN1_R2_C02"   
map03Nov[142949]= "EN1_R2_C03_EN1_R2_C04"   
map03Nov[142950]= "EN1_R2_C05_EN1_R2_C06"   
map03Nov[142951]= "EN1_R2_C07_EN1_R2_C08"   
map03Nov[142952]= "EN1_R2_C09_EN1_R2_C10"   
map03Nov[142953]= "EN1_R2_C29_EN1_R2_C30"   
map03Nov[142955]= "EN1_R2_C31_EN1_R2_C32"   
map03Nov[142956]= "EN1_R2_C33_EN1_R2_C34"   
map03Nov[142957]= "EN1_R2_C35_EN1_R2_C36"   
map03Nov[142958]= "EN1_R3_C01_EN1_R3_C02"   
map03Nov[142959]= "EN1_R3_C03_EN1_R3_C04"   
map03Nov[142960]= "EN1_R3_C05_EN1_R3_C06"   
map03Nov[142962]= "EN1_R3_C07_EN1_R3_C08"   
map03Nov[142963]= "EN1_R3_C09_EN1_R3_C10"   
map03Nov[142964]= "EN1_R3_C29_EN1_R3_C30"   
map03Nov[142965]= "EN1_R3_C31_EN1_R3_C32"   
map03Nov[142966]= "EN1_R3_C33_EN1_R3_C34"   
map03Nov[142967]= "EN1_R3_C35_EN1_R3_C36"   
map03Nov[142969]= "EN2_R2_C01_EN2_R3_C01"    
map03Nov[142970]= "EN2_R2_C02_EN2_R3_C02"    
map03Nov[142971]= "EN2_R2_C03_EN2_R3_C03"    
map03Nov[142972]= "EN2_R2_C04_EN2_R3_C04"    
map03Nov[142973]= "EN2_R2_C05_EN2_R3_C05"    
map03Nov[142974]= "EN2_R2_C06_EN2_R3_C06"    
map03Nov[142976]= "EN2_R2_C07_EN2_R3_C07"    
map03Nov[142977]= "EN2_R2_C08_EN2_R3_C08"    
map03Nov[142978]= "EN2_R2_C09_EN2_R3_C09"    
map03Nov[142979]= "EN2_R2_C10_EN2_R3_C10"    
map03Nov[142980]= "EN2_R2_C29_EN2_R3_C29"    
map03Nov[142981]= "EN2_R2_C30_EN2_R3_C30"    
map03Nov[142983]= "EN2_R2_C31_EN2_R3_C31"    
map03Nov[142984]= "EN2_R2_C32_EN2_R3_C32"    
map03Nov[142985]= "EN2_R2_C33_EN2_R3_C33"    
map03Nov[142986]= "EN2_R2_C34_EN2_R3_C34"    
map03Nov[142987]= "EN2_R2_C35_EN2_R3_C35"    
map03Nov[142988]= "EN2_R2_C36_EN2_R3_C36"    
map03Nov[142990]= "EN3_R2_C01_EN3_R3_C01"    
map03Nov[142991]= "EN3_R2_C02_EN3_R3_C02"    
map03Nov[142992]= "EN3_R2_C03_EN3_R3_C03"    
map03Nov[142993]= "EN3_R2_C04_EN3_R3_C04"    
map03Nov[142994]= "EN3_R2_C05_EN3_R3_C05"    
map03Nov[142995]= "EN3_R2_C06_EN3_R3_C06"    
map03Nov[142997]= "EN3_R2_C07_EN3_R3_C07"    
map03Nov[142998]= "EN3_R2_C08_EN3_R3_C08"    
map03Nov[142999]= "EN3_R2_C09_EN3_R3_C09"    
map03Nov[143000]= "EN3_R2_C10_EN3_R3_C10"    
map03Nov[143001]= "EN3_R2_C29_EN3_R3_C29"    
map03Nov[143002]= "EN3_R2_C30_EN3_R3_C30"    
map03Nov[143004]= "EN3_R2_C31_EN3_R3_C31"    
map03Nov[143005]= "EN3_R2_C32_EN3_R3_C32"    
map03Nov[143006]= "EN3_R2_C33_EN3_R3_C33"    
map03Nov[143007]= "EN3_R2_C34_EN3_R3_C34"    
map03Nov[143008]= "EN3_R2_C35_EN3_R3_C35"    
map03Nov[143009]= "EN3_R2_C36_EN3_R3_C36"    
map03Nov[143014]= "EN1_R2_C11_EN1_R2_C12"    
map03Nov[143015]= "EN1_R2_C13_EN1_R2_C14"    
map03Nov[143016]= "EN1_R2_C15_EN1_R2_C16"    
map03Nov[143017]= "EN1_R2_C17_EN1_R2_C18"    
map03Nov[143018]= "EN1_R2_C19_EN1_R2_C20"    
map03Nov[143019]= "EN1_R2_C21_EN1_R2_C22"    
map03Nov[143021]= "EN1_R2_C23_EN1_R2_C24"    
map03Nov[143022]= "EN1_R2_C25_EN1_R2_C26"    
map03Nov[143023]= "EN1_R2_C27_EN1_R2_C28"    
map03Nov[143024]= "EN1_R3_C11_EN1_R3_C12"    
map03Nov[143025]= "EN1_R3_C13_EN1_R3_C14"    
map03Nov[143026]= "EN1_R3_C15_EN1_R3_C16"    
map03Nov[143028]= "EN1_R3_C17_EN1_R3_C18"    
map03Nov[143029]= "EN1_R3_C19_EN1_R3_C20"    
map03Nov[143030]= "EN1_R3_C21_EN1_R3_C22"    
map03Nov[143031]= "EN1_R3_C23_EN1_R3_C24"    
map03Nov[143032]= "EN1_R3_C25_EN1_R3_C26"    
map03Nov[143033]= "EN1_R3_C27_EN1_R3_C28"    
map03Nov[143035]= "EN2_R2_C11_EN2_R3_C11"    
map03Nov[143036]= "EN2_R2_C12_EN2_R3_C12"    
map03Nov[143037]= "EN2_R2_C13_EN2_R3_C13"    
map03Nov[143038]= "EN2_R2_C14_EN2_R3_C14"    
map03Nov[143039]= "EN2_R2_C15_EN2_R3_C15"    
map03Nov[143040]= "EN2_R2_C16_EN2_R3_C16"    
map03Nov[143042]= "EN2_R2_C17_EN2_R3_C17"    
map03Nov[143043]= "EN2_R2_C18_EN2_R3_C18"    
map03Nov[143044]= "EN2_R2_C19_EN2_R3_C19"    
map03Nov[143045]= "EN2_R2_C20_EN2_R3_C20"    
map03Nov[143046]= "EN2_R2_C21_EN2_R3_C21"    
map03Nov[143047]= "EN2_R2_C22_EN2_R3_C22"    
map03Nov[143049]= "EN2_R2_C23_EN2_R3_C23"    
map03Nov[143050]= "EN2_R2_C24_EN2_R3_C24"    
map03Nov[143051]= "EN2_R2_C25_EN2_R3_C25"    
map03Nov[143052]= "EN2_R2_C26_EN2_R3_C26"    
map03Nov[143053]= "EN2_R2_C27_EN2_R3_C27"    
map03Nov[143054]= "EN2_R2_C28_EN2_R3_C28"    
map03Nov[143056]= "EN3_R2_C11_EN3_R3_C11"    
map03Nov[143057]= "EN3_R2_C12_EN3_R3_C12"    
map03Nov[143058]= "EN3_R2_C13_EN3_R3_C13"    
map03Nov[143059]= "EN3_R2_C14_EN3_R3_C14"    
map03Nov[143060]= "EN3_R2_C15_EN3_R3_C15"    
map03Nov[143061]= "EN3_R2_C16_EN3_R3_C16"    
map03Nov[143063]= "EN3_R2_C17_EN3_R3_C17"    
map03Nov[143064]= "EN3_R2_C18_EN3_R3_C18"    
map03Nov[143065]= "EN3_R2_C19_EN3_R3_C19"    
map03Nov[143066]= "EN3_R2_C20_EN3_R3_C20"    
map03Nov[143067]= "EN3_R2_C21_EN3_R3_C21"    
map03Nov[143068]= "EN3_R2_C22_EN3_R3_C22"    
map03Nov[143070]= "EN3_R2_C23_EN3_R3_C23"    
map03Nov[143071]= "EN3_R2_C24_EN3_R3_C24"    
map03Nov[143072]= "EN3_R2_C25_EN3_R3_C25"    
map03Nov[143073]= "EN3_R2_C26_EN3_R3_C26"    
map03Nov[143074]= "EN3_R2_C27_EN3_R3_C27"    
map03Nov[143075]= "EN3_R2_C28_EN3_R3_C28"    
map03Nov[216665]= "EP2_R2_C31_EP2_R3_C31"    
map03Nov[216666]= "EP2_R2_C32_EP2_R3_C32"    
map03Nov[216667]= "EP2_R2_C33_EP2_R3_C33"    
map03Nov[216668]= "EP2_R2_C34_EP2_R3_C34"    
map03Nov[216669]= "EP2_R2_C35_EP2_R3_C35"    
map03Nov[216670]= "EP2_R2_C36_EP2_R3_C36"    

map26Aug = copy.deepcopy(map03Nov)
#  map(only changed it ) before the time 26 Aug 2014.
map26Aug[142816]= "EP1_R2_C01_EP1_R2_C02"     
map26Aug[142817]= "EP1_R2_C03_EP1_R2_C04"     
map26Aug[142818]= "EP1_R2_C05_EP1_R2_C06"     
map26Aug[142819]= "EP1_R2_C07_EP1_R2_C08"     
map26Aug[142820]= "EP1_R2_C09_EP1_R2_C10"     
map26Aug[142821]= "EP1_R2_C29_EP1_R2_C30"     
map26Aug[142823]= "EP1_R2_C31_EP1_R2_C32"     
map26Aug[142824]= "EP1_R2_C33_EP1_R2_C34"     
map26Aug[142825]= "EP1_R2_C35_EP1_R2_C36"     
map26Aug[142826]= "EP1_R3_C01_EP1_R3_C02"     
map26Aug[142827]= "EP1_R3_C03_EP1_R3_C04"     
map26Aug[142828]= "EP1_R3_C05_EP1_R3_C06"     
map26Aug[142830]= "EP1_R3_C07_EP1_R3_C08"     
map26Aug[142831]= "EP1_R3_C09_EP1_R3_C10"     
map26Aug[142832]= "EP1_R3_C29_EP1_R3_C30"     
map26Aug[142833]= "EP1_R3_C31_EP1_R3_C32"     
map26Aug[142834]= "EP1_R3_C33_EP1_R3_C34"     
map26Aug[142835]= "EP1_R3_C35_EP1_R3_C36"     
map26Aug[142837]= "EP2_R2_C01_EP2_R3_C01"     
map26Aug[142838]= "EP2_R2_C02_EP2_R3_C02"     
map26Aug[142839]= "EP2_R2_C03_EP2_R3_C03"     
map26Aug[142840]= "EP2_R2_C04_EP2_R3_C04"     
map26Aug[142841]= "EP2_R2_C05_EP2_R3_C05"     
map26Aug[142842]= "EP2_R2_C06_EP2_R3_C06"     
map26Aug[142844]= "EP2_R2_C07_EP2_R3_C07"     
map26Aug[142845]= "EP2_R2_C08_EP2_R3_C08"     
map26Aug[142846]= "EP2_R2_C09_EP2_R3_C09"     
map26Aug[142847]= "EP2_R2_C10_EP2_R3_C10"     
map26Aug[142848]= "EP2_R2_C29_EP2_R3_C29"     
map26Aug[142849]= "EP2_R2_C30_EP2_R3_C30"     
map26Aug[142851]= "EP2_R2_C31_EP2_R3_C31"     
map26Aug[142852]= "EP2_R2_C32_EP2_R3_C32"     
map26Aug[142853]= "EP2_R2_C33_EP2_R3_C33"     
map26Aug[142854]= "EP2_R2_C34_EP2_R3_C34"     
map26Aug[142855]= "EP2_R2_C35_EP2_R3_C35"     
map26Aug[142856]= "EP2_R2_C36_EP2_R3_C36"     
