# Data sources, ids of google sheets where the core date is stored.

# Specific for MY
localised_sheets = "13XUkS7VbGJSg1xiOb2tVOIFcoiochpxqaQeBTk2Ibns"

# shared with all deployments

# messages in templates
#T_C_onboarding_ID = "12ddvTz_ZfC-9-b0yxjVrSzczciUUE3GosLUFeOLIv9I"
#T_content_ID = "1hcH8pFdiHZN0UvZgyv3Zht9ARBTx-VXhNBI2o8L7fHU"
#safeguarding = "1PHgUhJnZdE0lK6C9teK-hwA6Tf-6Pgj1_OVdxoTgVOA"
#T_delivery_ID = "1yf6T8FsNF5SIS7ktj05Wj7ha_Hkfrf66r63kfUWhJbI"
#T_C_menu_ID = "1lf80mIiuv_F6xAa9j5zGvXas50WxdSsLj6vrPccGNwY"


#C_modules_ID = "1435mczruh5CZoI7u0fWNuKGnJw062Si9j7er_NOwqT0"
#C_dictionaries_ID = "1uc4WOOlyHTEV8fUGb8nPCYcPj446TRtsV8fucrOCxC4"  # update?
#C_home_activity_checkin_ID = "112bPyJgsE2BHxeJ7AN61o_5Uvf94YUCBR_drdAU5tHM"
#C_ltp_activities_ID = "1AdcFsatjGdbDYRqgw359JEhSZn6nkRbZHVZr-5yQe6I"
#C_goal_checkin_ID = "115XSdB5AJ9A9Nwr7Cs1PER5htOjctWcVTnqxipFiRUY"
#C_dev_asess_tool_ID = "1azmH-v6DIJe6w_hpkvkI5scla2pgcC5c3Iyg7hBkyq8"
#>

T_content_ID = "1hcH8pFdiHZN0UvZgyv3Zht9ARBTx-VXhNBI2o8L7fHU"
onboarding_data = "1_m_Plv3EgM6bSyokcI4qgY5sCE8s6zf4Bz1qli2zDSk"
edited_onboarding = "1Sl0Jl_N4cGQi2INmE_EnX_aYUMUrUB6cKbuWVPzirtY"
C_modules_ID = "1435mczruh5CZoI7u0fWNuKGnJw062Si9j7er_NOwqT0"
C_dictionaries_ID = "1uc4WOOlyHTEV8fUGb8nPCYcPj446TRtsV8fucrOCxC4"  # update?
C_ltp_activities_ID = "1AdcFsatjGdbDYRqgw359JEhSZn6nkRbZHVZr-5yQe6I"
C_goal_checkin_ID = "115XSdB5AJ9A9Nwr7Cs1PER5htOjctWcVTnqxipFiRUY"
C_dev_asess_tool_ID = "1azmH-v6DIJe6w_hpkvkI5scla2pgcC5c3Iyg7hBkyq8"
safeguarding_data = "1BKwGQJvtvIlZhirvaZ5UFOmMxVe0pB4eM3_4F0_Snu4"
edited_safeguarding = "1bWOyM5yShTTJSaxwqRCrjUzkwbp7DF6_nSF_96YcZ2c"
edited_delivery = "1q6E2c4Bg_UvqTmhxAsTIQngwAtj0aFoqu8wsPHnqmaU"
delivery_data = "1JcWCrDWTWQsg5yV0wHmeS-Ln8JPpVET5U6akOJIFUK4"
edited_menu = "1lIiFjZKS0eXzzo6XwDdqYv4e1A73WFCpWZg5ju-tCZE"
menu_data = "1W42uFzCBUbiYXCUh-nxgCDMsjcJMC4IZXG00TVGUZxA"




# "filename" is how it will be generally named in the pipeline.
# "crowdin_name" will be the name of the file that is produced to send to the
# translators
# tags are used to identify flows to be process
# "split_no" is used to divide the file at the final step to get it to a
# manageable size that can be uploaded to rapidpro

sources = [
    {
        "filename": "parenttext_del",
        "spreadsheet_ids": [
            onboarding_data,
            edited_onboarding,
            C_ltp_activities_ID,
            edited_delivery,
            delivery_data,
            C_modules_ID,
            C_dictionaries_ID,
            edited_menu,
            menu_data,
            C_goal_checkin_ID,
            T_content_ID,
            C_dev_asess_tool_ID,
            safeguarding_data,
            edited_safeguarding,
            localised_sheets],
        # crowdin names: home_activity_checkin_child dev_assess_tools
        # modules_child delivery_menu onboarding goal_checkins_child
        "crowdin_name": "delivery_menu",
        # possible values for tag 1: onboarding dev_assess ltp_activity
        # home_activity_checkin module goal_checkin safeguarding menu delivery
        "tags": [1,"onboarding",2, "malaysia", 3, "child"],
        "split_no": 1,
        #"archive": "https://drive.usercontent.google.com/download?id=1l_43DHz-WUZkrfouJ-GM4QxEA-2exlRy&export=download&authuser=0&confirm=t&uuid=6341bfe2-5b61-4366-a25f-86a04dc80a80&at=APZUnTXFyA2XHo5xC9fmls7UG3PA:1699289412671",  # noqa: E501
     },
]

# Data used when modifying expiration times
special_expiration = "./edits/specific_expiration.json"
default_expiration = 1440

# Model that is used as part of the process when the data is extracted from excel
model = "models.parenttext_models"

# Languages that will be looked for to localize back into the flows, "language" is the 3 letter code used in RapidPro, "code" is the 2 letter code used in crowdin
languages = [
    {"language": "msa", "code": "ms"}
]

# Location where translations are stored, at the moment pointing to a locally cloned repo, should maybe be adapted so we can provide a link to an online repo
translation_repo = "https://github.com/IDEMSInternational/plh-digital-content"
folder_within_repo = "translations/parent_text_v2_malaysia"

# Desination file for all files (including intermediary files and log files)
outputpath = "./output"

# In one of the latter stages we have the option to modify the quick replies,
# 1 - We may want to remove the quick replies and add them to message text and give numerical prompts to allow basic phone users to use the app - for this use reference code "move"
# 2 - We may want to reformat the quick replies so that long ones are added to the message text as above - for this use reference code "reformat"
# 3 - We may not want to do anything, for this use reference code "none"
qr_treatment = "reformat"


# This is the default phrase we want to add in if the quick replies are being moved to message text
select_phrases = "./edits/select_phrases.json"

# If we are in scenario 1 above, we may wish to add some basic numerical quick replies back in, if so we need to specify add_selectors as "yes"
add_selectors = "yes"

# Some words we always want to keep as full quick replies, they are specified in this file
special_words = "./edits/special_words.json"

# In scenario 2 we set limits on the number of quick replies and the length of the quick replies. 
#   count_threshold (relates to number of quick replies)
#   length_threshold (relates to length of the longest quick reply)
# If the number of QRs is below or equal the count_threshold and the longest QR is shorter than or equal to the length_threshold then the QR are to be left in place the node will not be changed. 
# In places where the QR are too long. We will make the changes to make the QRs numbers and add the number references to the message text as example 1.
# Thresholds should be entered as strings
count_threshold = "3"
length_threshold = "18"

#Google sheet ID containing ab testing data
ab_testing_sheet_ID = "1i_oqiJYkeoMsYdeFOcKlvvjnNCEdQnZlsm17fgNvK0s" #same for all deployments
localisation_sheet_ID = "1RhsMtslpwyTmMLsZJZaaNqweKX7ONpmwR4-rQVpo_qw" #malaysia specific

#Google sheet ID containing dict edits data
eng_edits_sheet_ID = "1Ab8H_s26EuOiS4nZ6HGADjD4CZw55586LL66fl8tEWI" #same for all deployments
transl_edits_sheet_ID = "1tbwzqlie87UMOe7yhdeeUxkTa4NtqRyivgX9NtxAFe8" #south africa specific

#Names of redirect flows to be modified as part of safegurading process
redirect_flow_names = '["safeguarding_redirect_to_topic_all", "safeguarding_redirect_to_topic_highrisk", "safeguarding_redirect_to_topic_trigger"]'

def create_config():
    return {
        "ab_testing_sheet_id": ab_testing_sheet_ID,
        "add_selectors": add_selectors,
        "count_threshold": count_threshold,
        "default_expiration": default_expiration,
        "eng_edits_sheet_id": eng_edits_sheet_ID,
        "folder_within_repo": folder_within_repo,
        "languages": languages,
        "length_threshold": length_threshold,
        "localisation_sheet_id": localisation_sheet_ID,
        "model": model,
        "qr_treatment": qr_treatment,
        "redirect_flow_names": redirect_flow_names,
        "select_phrases": select_phrases,
        "sg_flow_id": "b83315a6-b25c-413a-9aa0-953bf60f223c",
        "sg_flow_name": "safeguarding_wfr_interaction",
        "sg_sources": [
            {"key": "msa", "path": "excel_files/safeguarding malaysia.xlsx"}
        ],
        "sources": sources,
        "special_expiration": special_expiration,
        "special_words": special_words,
        "translation_repo": translation_repo,
        "transl_edits_sheet_id": transl_edits_sheet_ID,
    }
