import unittest
import pytest
from selenium import webdriver
import page
import practice_standards as PS
import dev_testdata


class DashboardSearchTest(unittest.TestCase):

    # runs before every test function
    def setUp(self):
        print("\n.....Start running test....")
        self.driver = webdriver.Chrome()
        dev_env = "https://dev.one.ssnet.gov.sg/mockServer/mock-ad.html"
        sit_env = "https://sit.one.ssnet.gov.sg/mockServer/mock-ad.html"
        self.driver.get(sit_env)
        mainPage = page.MainPage(self.driver)
        mainPage.login()
        mainPage.navigate_to_dashboard()
        # print("​".replace('\u200b', 'yoyo'))

    def check(self, practice_standard, link_index, true_ref_numbers, false_ref_numbers):
        dashboard = page.DashboardPage(self.driver)
        dashboard.click_case_count(link_index)
        results = page.ResultPage(self.driver)

        # checks if we are on the correct practice standard page
        print("\n <== Verifying whether practice standard liner matches... ==>\n")
        with self.subTest():
            if not results.is_practise_standard_matches(practice_standard):
                print(
                    "Practice standard (from Dashboard Requirements_v1.3):\n", practice_standard)
                raise AssertionError(
                    "ERROR: Practice standard doesn't match!")

        # checks if the correct enq numbers are in
        print(
            "\n <== Verifying whether these POSITIVE test data are in the listing... ==>\n")
        for ref_no in true_ref_numbers:
            with self.subTest(input_data=ref_no):
                print("Reference No:", ref_no)
                if not results.is_record_found(ref_no):
                    raise AssertionError(
                        f"ERROR: {ref_no} is missing from the listing!\n")

        # checks if false enq numbers are not in
        print("\n <== Verifying whether these NEGATIVE test data are not in the listing... ==>\n")
        for ref_no in false_ref_numbers:
            with self.subTest(input_data=ref_no):
                print("Reference No:", ref_no)
                if results.is_record_found(ref_no):
                    raise AssertionError(
                        f"ERROR: {ref_no} was found - not supposed to be in the listing!\n")

    # runs after every test function
    def tearDown(self):
        print("\n....Finished running test.....")
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_1_PS1_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_1
        link_index = 0
        true_ref_numbers = dev_testdata.PS1_overdue_positive
        false_ref_numbers = dev_testdata.PS1_overdue_negative

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=2)
    def test_3_PS2_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_2
        link_index = 1
        true_ref_numbers = dev_testdata.PS2_overdue_positive
        false_ref_numbers = dev_testdata.PS2_overdue_negative + \
            dev_testdata.PS2_1To5_positive + dev_testdata.PS2_6To10_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=3)
    def test_5_PS2_1To5(self):
        practice_standard = PS.PRACTICE_STANDARD_2
        link_index = 2
        true_ref_numbers = dev_testdata.PS2_1To5_positive
        false_ref_numbers = dev_testdata.PS2_1To5_negative + \
            dev_testdata.PS2_overdue_positive + dev_testdata.PS2_6To10_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=4)
    def test_6_PS2_6To10(self):
        practice_standard = PS.PRACTICE_STANDARD_2
        link_index = 3
        true_ref_numbers = dev_testdata.PS2_6To10_positive
        false_ref_numbers = dev_testdata.PS2_6To10_negative + \
            dev_testdata.PS2_1To5_positive + dev_testdata.PS2_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=5)
    def test_7_PS3_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_3
        link_index = 4
        true_ref_numbers = dev_testdata.PS3_overdue_positive
        false_ref_numbers = dev_testdata.PS3_overdue_negative

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=6)
    def test_8_PS4_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_4
        link_index = 5
        true_ref_numbers = dev_testdata.PS4_overdue_positive
        false_ref_numbers = dev_testdata.PS4_overdue_negative + \
            dev_testdata.PS4_1To7_positive + dev_testdata.PS4_8To14_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=7)
    def test_9_PS4_1To7(self):
        practice_standard = PS.PRACTICE_STANDARD_4
        link_index = 6
        true_ref_numbers = dev_testdata.PS4_1To7_positive
        false_ref_numbers = dev_testdata.PS4_1To7_negative + \
            dev_testdata.PS4_8To14_positive + dev_testdata.PS4_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=8)
    def test_10_PS4_8To14(self):
        practice_standard = PS.PRACTICE_STANDARD_4
        link_index = 7
        true_ref_numbers = dev_testdata.PS4_8To14_positive
        false_ref_numbers = dev_testdata.PS4_8To14_negative + \
            dev_testdata.PS4_1To7_positive + dev_testdata.PS4_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=9)
    def test_11_PS5_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_5
        link_index = 8
        true_ref_numbers = dev_testdata.PS5_overdue_positive
        false_ref_numbers = dev_testdata.PS5_overdue_negative + \
            dev_testdata.PS5_16To30_positive + dev_testdata.PS5_1To15_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=10)
    def test_13_PS5_1To15(self):
        practice_standard = PS.PRACTICE_STANDARD_5
        link_index = 9
        true_ref_numbers = dev_testdata.PS5_1To15_positive
        false_ref_numbers = dev_testdata.PS5_1To15_negative + \
            dev_testdata.PS5_16To30_positive + dev_testdata.PS5_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=11)
    def test_14_PS5_16To30(self):
        practice_standard = PS.PRACTICE_STANDARD_5
        link_index = 10
        true_ref_numbers = dev_testdata.PS5_16To30_positive
        false_ref_numbers = dev_testdata.PS5_16To30_negative + \
            dev_testdata.PS5_1To15_positive + dev_testdata.PS5_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=12)
    def test_15_PS6_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_6
        link_index = 11
        true_ref_numbers = dev_testdata.PS6_overdue_positive
        false_ref_numbers = dev_testdata.PS6_16To30_positive + \
            dev_testdata.PS6_1To15_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=13)
    def test_17_PS6_1To15(self):
        practice_standard = PS.PRACTICE_STANDARD_6
        link_index = 12
        true_ref_numbers = dev_testdata.PS6_1To15_positive
        false_ref_numbers = dev_testdata.PS6_16To30_positive + \
            dev_testdata.PS6_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=14)
    def test_18_PS6_16To30(self):
        practice_standard = PS.PRACTICE_STANDARD_6
        link_index = 13
        true_ref_numbers = dev_testdata.PS6_16To30_positive
        false_ref_numbers = dev_testdata.PS6_overdue_positive + \
            dev_testdata.PS6_1To15_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=15)
    def test_19_PS7_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_7
        link_index = 14
        true_ref_numbers = dev_testdata.PS7_overdue_positive
        false_ref_numbers = dev_testdata.PS7_overdue_negative + \
            dev_testdata.PS7_1To3_positive + dev_testdata.PS7_4To5_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=16)
    def test_21_PS7_1To3(self):
        practice_standard = PS.PRACTICE_STANDARD_7
        link_index = 15
        true_ref_numbers = dev_testdata.PS7_1To3_positive
        false_ref_numbers = dev_testdata.PS7_1To3_negative + \
            dev_testdata.PS7_4To5_positive + dev_testdata.PS7_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=17)
    def test_22_PS7_4To5(self):
        practice_standard = PS.PRACTICE_STANDARD_7
        link_index = 16
        true_ref_numbers = dev_testdata.PS7_4To5_positive
        false_ref_numbers = dev_testdata.PS7_4To5_negative + \
            dev_testdata.PS7_1To3_positive + dev_testdata.PS7_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=18)
    def test_23_PS8(self):
        practice_standard = PS.PRACTICE_STANDARD_8
        link_index = 17
        true_ref_numbers = dev_testdata.PS8_positive
        false_ref_numbers = dev_testdata.PS8_negative

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=19)
    def test_24_PS9(self):
        practice_standard = PS.PRACTICE_STANDARD_9
        link_index = 18
        true_ref_numbers = dev_testdata.PS9_positive
        false_ref_numbers = dev_testdata.PS9_negative

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=20)
    def test_26_PS10_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_10
        link_index = 19
        true_ref_numbers = dev_testdata.PS10_overdue_positive
        false_ref_numbers = dev_testdata.PS10_1To30_positive + \
            dev_testdata.PS10_31To60_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=21)
    def test_28_PS10_1To30(self):
        practice_standard = PS.PRACTICE_STANDARD_10
        link_index = 20
        true_ref_numbers = dev_testdata.PS10_1To30_positive
        false_ref_numbers = dev_testdata.PS10_31To60_positive + \
            dev_testdata.PS10_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=22)
    def test_29_PS10_31To60(self):
        practice_standard = PS.PRACTICE_STANDARD_10
        link_index = 21
        true_ref_numbers = dev_testdata.PS10_31To60_positive
        false_ref_numbers = dev_testdata.PS10_1To30_positive + \
            dev_testdata.PS10_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=23)
    def test_30_PS11_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_11
        link_index = 22
        true_ref_numbers = dev_testdata.PS11_overdue_positive
        false_ref_numbers = dev_testdata.PS11_overdue_negative + \
            dev_testdata.PS11_1To5_positive + dev_testdata.PS11_6To10_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=24)
    def test_32_PS11_1To5(self):
        practice_standard = PS.PRACTICE_STANDARD_11
        link_index = 23
        true_ref_numbers = dev_testdata.PS11_1To5_positive
        false_ref_numbers = dev_testdata.PS11_1To5_negative + \
            dev_testdata.PS11_6To10_positive + dev_testdata.PS11_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=25)
    def test_33_PS11_6To10(self):
        practice_standard = PS.PRACTICE_STANDARD_11
        link_index = 24
        true_ref_numbers = dev_testdata.PS11_6To10_positive
        false_ref_numbers = dev_testdata.PS11_6To10_negative + \
            dev_testdata.PS11_1To5_positive + dev_testdata.PS11_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=26)
    def test_34_PS12(self):
        practice_standard = PS.PRACTICE_STANDARD_12
        link_index = 25
        true_ref_numbers = dev_testdata.PS12_positive
        false_ref_numbers = dev_testdata.PS12_negative

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=27)
    def test_35_PS13(self):
        practice_standard = PS.PRACTICE_STANDARD_13
        link_index = 26
        true_ref_numbers = dev_testdata.PS13_overdue_positive
        false_ref_numbers = []

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=28)
    def test_36_PS14_1To7(self):
        practice_standard = PS.PRACTICE_STANDARD_14
        link_index = 27
        true_ref_numbers = dev_testdata.PS14_1To7_positive
        false_ref_numbers = dev_testdata.PS14_8To14_positive + \
            dev_testdata.PS14_moreThan14_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=29)
    def test_37_PS14_8To14(self):
        practice_standard = PS.PRACTICE_STANDARD_14
        link_index = 28
        true_ref_numbers = dev_testdata.PS14_8To14_positive
        false_ref_numbers = dev_testdata.PS14_1To7_positive + \
            dev_testdata.PS14_moreThan14_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=30)
    def test_38_PS14_moreThan14(self):
        practice_standard = PS.PRACTICE_STANDARD_14
        link_index = 29
        true_ref_numbers = dev_testdata.PS14_moreThan14_positive
        false_ref_numbers = dev_testdata.PS14_1To7_positive + \
            dev_testdata.PS14_8To14_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=31)
    def test_39_PS15(self):
        practice_standard = PS.PRACTICE_STANDARD_15
        link_index = 30
        true_ref_numbers = dev_testdata.PS15_positive
        false_ref_numbers = dev_testdata.PS15_negative

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=32)
    def test_40_PS16_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_16
        link_index = 31
        true_ref_numbers = dev_testdata.PS16_overdue_positive
        false_ref_numbers = dev_testdata.PS16_overdue_negative + \
            dev_testdata.PS16_1To5_positive + dev_testdata.PS16_6To10_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=33)
    def test_42_PS16_1To5(self):
        practice_standard = PS.PRACTICE_STANDARD_16
        link_index = 32
        true_ref_numbers = dev_testdata.PS16_1To5_positive
        false_ref_numbers = dev_testdata.PS16_6To10_positive + \
            dev_testdata.PS16_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=34)
    def test_43_PS16_6To10(self):
        practice_standard = PS.PRACTICE_STANDARD_16
        link_index = 33
        true_ref_numbers = dev_testdata.PS16_6To10_positive
        false_ref_numbers = dev_testdata.PS16_1To5_positive + \
            dev_testdata.PS16_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=35)
    def test_44_PS17_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_17
        link_index = 34
        true_ref_numbers = dev_testdata.PS17_overdue_positive
        false_ref_numbers = dev_testdata.PS17_1To30_positive + \
            dev_testdata.PS17_31To60_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=36)
    def test46_PS17_1To30(self):
        practice_standard = PS.PRACTICE_STANDARD_17
        link_index = 35
        true_ref_numbers = dev_testdata.PS17_1To30_positive
        false_ref_numbers = dev_testdata.PS17_31To60_positive + \
            dev_testdata.PS17_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=37)
    def test_47_PS17_31To60(self):
        practice_standard = PS.PRACTICE_STANDARD_17
        link_index = 36
        true_ref_numbers = dev_testdata.PS17_31To60_positive
        false_ref_numbers = dev_testdata.PS17_1To30_positive + \
            dev_testdata.PS17_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=38)
    def test_48_PS18_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_18
        link_index = 37
        true_ref_numbers = dev_testdata.PS18_overdue_positive
        false_ref_numbers = dev_testdata.PS18_31To60_positive + \
            dev_testdata.PS18_1To30_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=39)
    def test_50_PS18_1To30(self):
        practice_standard = PS.PRACTICE_STANDARD_18
        link_index = 38
        true_ref_numbers = dev_testdata.PS18_1To30_positive
        false_ref_numbers = dev_testdata.PS18_31To60_positive + \
            dev_testdata.PS18_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=40)
    def test_51_PS18_31To60(self):
        practice_standard = PS.PRACTICE_STANDARD_18
        link_index = 39
        true_ref_numbers = dev_testdata.PS18_31To60_positive
        false_ref_numbers = dev_testdata.PS18_1To30_positive + \
            dev_testdata.PS18_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=41)
    def test_52_PS19_moreThan90(self):
        practice_standard = PS.PRACTICE_STANDARD_19
        link_index = 40
        true_ref_numbers = dev_testdata.PS19_moreThan90_positive
        false_ref_numbers = dev_testdata.PS19_60To90_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=42)
    def test_53_PS19_60To90(self):
        practice_standard = PS.PRACTICE_STANDARD_19
        link_index = 41
        true_ref_numbers = dev_testdata.PS19_60To90_positive
        false_ref_numbers = dev_testdata.PS19_moreThan90_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=43)
    def test_54_PS20_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_20
        link_index = 42
        true_ref_numbers = dev_testdata.PS20_overdue_positive
        false_ref_numbers = dev_testdata.PS20_31To60_positive + \
            dev_testdata.PS20_1To30_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=44)
    def test_55_PS20_1To30(self):
        practice_standard = PS.PRACTICE_STANDARD_20
        link_index = 43
        true_ref_numbers = dev_testdata.PS20_1To30_positive
        false_ref_numbers = dev_testdata.PS20_31To60_positive + \
            dev_testdata.PS20_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=45)
    def test_56_PS20_31To60(self):
        practice_standard = PS.PRACTICE_STANDARD_20
        link_index = 44
        true_ref_numbers = dev_testdata.PS20_31To60_positive
        false_ref_numbers = dev_testdata.PS20_1To30_positive + \
            dev_testdata.PS20_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=46)
    def test_57_PS21_overdue(self):
        practice_standard = PS.PRACTICE_STANDARD_21
        link_index = 45
        true_ref_numbers = dev_testdata.PS21_overdue_positive
        false_ref_numbers = dev_testdata.PS21_31To60_positive + \
            dev_testdata.PS21_1To30_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=47)
    def test_58_PS21_1To30(self):
        practice_standard = PS.PRACTICE_STANDARD_21
        link_index = 46
        true_ref_numbers = dev_testdata.PS21_1To30_positive
        false_ref_numbers = dev_testdata.PS21_31To60_positive + \
            dev_testdata.PS21_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)

    @pytest.mark.run(order=48)
    def test_59_PS21_31To60(self):
        practice_standard = PS.PRACTICE_STANDARD_21
        link_index = 47
        true_ref_numbers = dev_testdata.PS21_31To60_positive
        false_ref_numbers = dev_testdata.PS21_1To30_positive + \
            dev_testdata.PS21_overdue_positive

        self.check(practice_standard, link_index,
                   true_ref_numbers, false_ref_numbers)


if __name__ == "__main__":
    unittest.main()
