# Taken from TCER v0.2
# Removed some repeated test case data from some test scenarios

# "*In receiving a referral from other agencies, SWP to acknowledge receipt of the case and inform referral agency on the assigned caseworker within 3 working days."
PS1_overdue_positive = ["ENQ147968"]
PS1_overdue_negative = ["ENQ147969", "ENQ147970",
                        "ENQ147971", "ENQ147972", "ENQ147973"]

# "*SWP to provide referring agency with an update/outcome (whether taken up, referred out or closed at intake) within 10 working days of the referral."
PS2_overdue_positive = ["ENQ147974", "ENQ148480"]
PS2_overdue_negative = ["ENQ147975", "ENQ147976", "ENQ147977"]

PS2_1To5_positive = ["ENQ148482", "ENQ148481"]
PS2_1To5_negative = ["ENQ148483", "ENQ148484", "ENQ148485"]

PS2_6To10_positive = ["ENQ148488", "ENQ148489"]
PS2_6To10_negative = ["ENQ148490", "ENQ148491", "ENQ148492"]

# "Intake interview is conducted within (a) 1 calendar day for referrals (i.e. cases) with risks and safety concerns"
PS3_overdue_positive = ["ENQ148493", "ENQ148496", "ENQ148494", "ENQ149505"]
PS3_overdue_negative = ["ENQ149506", "ENQ149507"]

# "Intake interview is conducted within (b) 14 calendar days from receipt of other referrals (i.e. cases)"
PS4_overdue_positive = ["ENQ149508", "ENQ149510", "ENQ149511", "ENQ149512"]
PS4_overdue_negative = ["ENQ149513", "ENQ149514"]

PS4_1To7_positive = ["ENQ149515", "ENQ149516"]
PS4_1To7_negative = ["ENQ149517"]

PS4_8To14_positive = ["ENQ149518", "ENQ149519"]
PS4_8To14_negative = ["ENQ149520"]

# "*For cases with risk or safety concerns, a home visit should be done within 1 month from case open."
PS5_overdue_positive = ["OTP270850", "OTP270851"]
PS5_overdue_negative = ["OTP270852", "OTP274432"]

PS5_1To15_positive = ["OTP270853", "OTP270855"]
PS5_1To15_negative = ["OTP270856"]

PS5_16To30_positive = ["OTP270857", "OTP270858"]
PS5_16To30_negative = ["OTP270859"]

# "*Face-to-face sessions with clients to be held Minimally once a month​(CSWP 3 or 4 or those with known risk or safety concerns)"
PS6_overdue_positive = ["OTP269313", "OTP269314", "OTP269316",
                        "OTP269317", "OTP269318", "OTP269319", "OTP269322", "OTP269324"]
# PS6_overdue_negative = []

PS6_1To15_positive = ["OTP269330", "OTP269333", "OTP269336",
                      "OTP269343", "OTP269345", "OTP269568", "OTP269824", "OTP269825"]
# PS6_1To15_negative = []

PS6_16To30_positive = ["OTP270083", "OTP270084", "OTP270087",
                       "OTP270088", "OTP270337", "OTP270339", "OTP270340", "OTP270342"]
# PS6_16To30_negative = []

# "*For families where there are difficulties contacting them Minimally 3 efforts within 5 working days​"
PS7_overdue_positive = ["OTP270609", "OTP270610",
                        "OTP270346", "OTP270349", "OTP270356"]
PS7_overdue_negative = ["OTP270361", "OTP270363"]

PS7_1To3_positive = ["OTP270365", "OTP270366", "OTP270371"]
PS7_1To3_negative = ["OTP270373", "OTP270375"]

PS7_4To5_positive = ["OTP270377", "OTP270378", "OTP270379"]
PS7_4To5_negative = ["OTP270380", "OTP270381"]

# "Uncontactable case tagging with risk or safety Concerns"
PS8_positive = ["OTP270592", "OTP270593"]
PS8_negative = ["OTP270594"]

# "*To ensure a comprehensive assessment on all cases, there should at least be a home visit done once case is opened, where possible."
PS9_positive = ["OTP270595", "OTP270596"]
PS9_negative = ["OTP270597"]

# "*Face-to-face sessions with clients to be held minimally once every 2 months(CSWP 2 or those with no known risk or safety concerns)"
PS10_overdue_positive = ["OTP270374", "OTP270376"]
# PS10_overdue_negative = []

PS10_1To30_positive = ["OTP270360", "OTP270362", "OTP270364", "OTP270368"]
# PS10_1To30_negative = []

PS10_31To60_positive = ["OTP270350", "OTP270352", "OTP270354", "OTP270355"]
# PS10_31To60_negative = []

# "*For families where there are difficulties contacting them Minimally 3 efforts within 10 working days"
PS11_overdue_positive = ["OTP252687", "OTP265987",
                         "OTP260365", "OTP251685", "OTP251691"]
PS11_overdue_negative = ["OTP259340", "OTP257817"]

PS11_1To5_positive = ["OTP252440", "OTP251694"]
PS11_1To5_negative = ["OTP251697", "OTP251700"]

PS11_6To10_positive = ["OTP251703", "OTP251682", "OTP251689"]
PS11_6To10_negative = ["OTP251147", "OTP251141"]

# "General cases with uncontactable case tagging"
PS12_positive = ["OTP251142", "OTP251144"]
PS12_negative = ["OTP251145"]

# "Outstanding follow-up action to track (passed deadline)"
PS13_overdue_positive = ["OTP270602", "OTP251149",
                         "OTP270336", "OTP251148", "OTP251156", "OTP251168"]
# PS13_overdue_negative = []

# "In-progress follow-up action to track"
PS14_1To7_positive = ["OTP251169", "OTP251174", "OTP251175"]
# PS14_1To7_negative = []

PS14_8To14_positive = ["OTP251176", "OTP251177", "OTP251136"]
# PS14_8To14_negative = []

PS14_moreThan14_positive = ["OTP251139", "OTP250624"]
# PS14_moreThan14_negative = []

# "No in-progress follow-up action to track"
PS15_positive = ["OTP250619", "OTP250620", "OTP250627", "OTP250628"]
PS15_negative = ["OTP251169", "OTP251174", "OTP251175"]

# "*SWP to make an effort to contact other professionals, stakeholders, or significant others within 10 working days from the time case is opened."
PS16_overdue_positive = ["OTP260360", "OTP260367", "OTP260368"]
PS16_overdue_negative = ["OTP243466", "OTP243467", "OTP242957"]

PS16_1To5_positive = ["OTP267265", "OTP269332"]
# PS16_1To5_negative = []

PS16_6To10_positive = ["OTP269346", "OTP269347"]
# PS16_6To10_negative = []

# "*For uncontactable clients, a discussion between SWPs and other stakeholders/professionals should be conducted by the 2nd month should efforts to engage family not be successful."
PS17_overdue_positive = ["OTP251140", "OTP251150", "OTP251155",
                         "OTP251156", "OTP250629", "OTP250618", "OTP250113", "OTP249603"]
# PS17_overdue_negative = []

PS17_1To30_positive = ["OTP270085", "OTP270086",
                       "OTP270089", "OTP270353", "OTP270357"]
# PS17_1To30_negative = []

PS17_31To60_positive = ["OTP270359", "OTP270367",
                        "OTP270369", "OTP270370", "OTP270372"]
# PS17_31To60_negative = []

# "*Efforts to contact family (Outcome Plan) members or significant others Within the first 2 months of the case being opened"
PS18_overdue_positive = ["OTP269320", "OTP269321", "OTP269323", "OTP269325"]
# PS18_overdue_negative =

PS18_1To30_positive = ["OTP269326", "OTP269327", "OTP269328", "OTP269329"]
# PS18_1To30_negative =

PS18_31To60_positive = ["OTP273152", "OTP273153", "OTP270080", "OTP270081"]
# PS18_31To60_negative =

# "Latest case recording session date"
PS19_moreThan90_positive = ["OTP273158", "OTP273154", "OTP273155"]
# PS19_moreThan90_negative =

PS19_60To90_positive = ["OTP273159", "OTP273156", "OTP273157"]
# PS19_60To90_negative =

# "The first Assessment and Case Plan for each case is to be completed within 60 calendar days for new cases."
PS20_overdue_positive = ["OTP275464", "OTP269334", "OTP269335", "OTP269337"]
# PS20_overdue_negative =

PS20_1To30_positive = ["OTP269338", "OTP269339", "OTP269340"]
# PS20_1To30_negative =

PS20_31To60_positive = ["OTP269341", "OTP269342", "OTP270094"]
# PS20_31To60_negative =

# "All cases are to be reviewed at least once every six months (i.e. 180 calendar days)"
PS21_overdue_positive = ["OTP203520", "OTP270096"]
# PS21_overdue_negative =

PS21_1To30_positive = ["OTP270336", "OTP270338", "OTP270602", "OTP270604"]
# PS21_1To30_negative =

PS21_31To60_positive = ["OTP252170", "OTP270341", "OTP270343", "OTP270344"]
# PS21_31To60_negative =
