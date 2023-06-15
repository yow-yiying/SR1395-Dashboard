from enquiry.enquiry import Enquiry

with Enquiry() as bot:
    bot.land_ssnet_login(env="dev")
    bot.login(
        username="fsccaseworker1401"
    )
    bot.create_new_enquiry(
        input_date_of_referral="03/06/2023",
        # input_source_of_referral="Community - Schools",
        # input_source_of_referral="Community - Family / Friends",
        # input_source_of_referral="Self-Referral",
        # input_date_of_ack="23/05/2023",
        input_immediate_assist="No",
    )
    bot.fill_enquiry_outcome(
        hasOutcome=True,
        input_outcome_for_enquiry="New Intake",
        # input_date_of_outcome="today",
        # input_updated_ref_source_date="today"
    )
    bot.search_nric(
        input_nric="S6029914E"
    )
    bot.save_enquiry()
    bot.print_success_msg()

    # while True:
    #     pass
