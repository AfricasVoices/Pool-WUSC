from core_data_modules.cleaners import swahili
from src.pipeline_configuration_spec import *

NUM_EPISODES = 6

def generate_rqa_coda_dataset_configs():
    configurations = []
    for i in range(1, NUM_EPISODES + 1):
        episode_num = str(i).zfill(2)
        configuration = CodaDatasetConfiguration(
            coda_dataset_id=f"LEAP_s06e{episode_num}",
            engagement_db_dataset=f"leap_s06e{episode_num}",
            code_scheme_configurations=[
                CodeSchemeConfiguration(
                    code_scheme=load_code_scheme(f"rqas/leap_s06/s06e{episode_num}"),
                    auto_coder=None,
                    coda_code_schemes_count=3
                )
            ],
            ws_code_match_value=f"leap s06e{episode_num}"
        )
        configurations.append(configuration)
    return configurations

def generate_rqa_analysis_dataset_configs():
    configurations = []
    for i in range(1, NUM_EPISODES + 1):
        episode_num = str(i).zfill(2)
        config = AnalysisDatasetConfiguration(
            engagement_db_datasets=[f"leap_s06e{episode_num}"],
            dataset_type=DatasetTypes.RESEARCH_QUESTION_ANSWER,
            raw_dataset=f"leap_s06e{episode_num}_raw",
            coding_configs=[
                CodingConfiguration(
                    code_scheme=load_code_scheme(f"rqas/leap_s06/s06e{episode_num}"),
                    analysis_dataset=f"s06e{episode_num}"
                )
            ]
        )
        configurations.append(config)
    return configurations


demogs_question_configurations = [
    KoboToolBoxQuestionConfiguration(data_column_name="Gender", engagement_db_dataset="kakuma_gender"),
    KoboToolBoxQuestionConfiguration(data_column_name="Age", engagement_db_dataset="kakuma_age"),
    KoboToolBoxQuestionConfiguration(data_column_name="Location", engagement_db_dataset="kakuma_location"),
    KoboToolBoxQuestionConfiguration(data_column_name="Disability", engagement_db_dataset="kakuma_disabled"),
    KoboToolBoxQuestionConfiguration(data_column_name="Nationality", engagement_db_dataset="kakuma_nationality"),
]   

PIPELINE_CONFIGURATION = PipelineConfiguration(
    pipeline_name="leap_s06",
    engagement_database=EngagementDatabaseClientConfiguration(
        credentials_file_url="gs://avf-credentials/avf-engagement-databases-firebase-credentials-file.json",
        database_path="engagement_databases/POOL-WUSC"
    ),
    uuid_table=UUIDTableClientConfiguration(
        credentials_file_url="gs://avf-credentials/avf-id-infrastructure-firebase-adminsdk-6xps8-b9173f2bfd.json",
        table_name="avf-global-urn-to-participant-uuid",
        uuid_prefix="avf-participant-uuid-"
    ),
    operations_dashboard=OperationsDashboardConfiguration(
        credentials_file_url="gs://avf-credentials/avf-dashboards-firebase-adminsdk-gvecb-ef772e79b6.json",
    ),
    rapid_pro_sources=[
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com", 
                token_file_url="gs://avf-credentials/wusc-leap-kalobeyei-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("wusc_leap_s06e01_kalobeyei_activation", "rqa_s06e01", "leap_s06e01"),
                    FlowResultConfiguration("wusc_leap_s06e02_kalobeyei_activation", "rqa_s06e02", "leap_s06e02"),
                    FlowResultConfiguration("wusc_leap_s06e03_kalobeyei_activation", "rqa_s06e03", "leap_s06e03"),
                    FlowResultConfiguration("wusc_leap_s06e04_kalobeyei_activation", "rqa_s06e04", "leap_s06e04"),
                    FlowResultConfiguration("wusc_leap_s06e05_kalobeyei_activation", "rqa_s06e05", "leap_s06e05"),
                    FlowResultConfiguration("wusc_leap_s06e06_kalobeyei_activation", "rqa_s06e06", "leap_s06e06"),
                    
                    FlowResultConfiguration("wusc_leap_s06_kalobeyei_demogs", "age", "kakuma_age"),
                    FlowResultConfiguration("wusc_leap_s06_kalobeyei_demogs", "gender", "kakuma_gender"),
                    FlowResultConfiguration("wusc_leap_s06_kalobeyei_demogs", "location", "kakuma_location"),
                    FlowResultConfiguration("wusc_leap_s06_kalobeyei_demogs", "disability", "kakuma_disabled"),
                    FlowResultConfiguration("wusc_leap_s06_kalobeyei_demogs", "nationality", "kakuma_nationality"),
                    FlowResultConfiguration("wusc_leap_s06_kalobeyei_demogs", "household language", "kakuma_preffered_language"),
                ]
            )
        ),
    ],
    kobotoolbox_sources=[
        KoboToolBoxSource(
            token_file_url="gs://avf-credentials/wusc-kobotoolbox-token.json",
            sync_config=KoboToolBoxToEngagementDBConfiguration(    
                asset_uid="a7iCcdsCJd98ahbKvfjFEa",
                participant_id_configuration=KoboToolBoxParticipantIdConfiguration(
                    data_column_name="Contacts",
                    id_type=KoboToolBoxParticipantIdTypes.KENYA_MOBILE_NUMBER
                ),
                ignore_invalid_mobile_numbers=True,
                question_configurations=[
                    KoboToolBoxQuestionConfiguration(data_column_name="leap_s06e01", engagement_db_dataset="leap_s06e01"),
                ] + demogs_question_configurations
            )
        ),
        KoboToolBoxSource(
            token_file_url="gs://avf-credentials/wusc-kobotoolbox-token.json",
            sync_config=KoboToolBoxToEngagementDBConfiguration(    
                asset_uid="aNjXWyQUTohwfFZpK2zJ2D",
                participant_id_configuration=KoboToolBoxParticipantIdConfiguration(
                    data_column_name="Contacts",
                    id_type=KoboToolBoxParticipantIdTypes.KENYA_MOBILE_NUMBER
                ),
                ignore_invalid_mobile_numbers=True,
                question_configurations=[
                    KoboToolBoxQuestionConfiguration(data_column_name="leap_s06e02", engagement_db_dataset="leap_s06e02"),
                ] + demogs_question_configurations
            )
        ),
        KoboToolBoxSource(
            token_file_url="gs://avf-credentials/wusc-kobotoolbox-token.json",
            sync_config=KoboToolBoxToEngagementDBConfiguration(
                asset_uid="aDy2KhyTLMwCRmfcGJwvLw",
                participant_id_configuration=KoboToolBoxParticipantIdConfiguration(
                    data_column_name="Contacts",
                    id_type=KoboToolBoxParticipantIdTypes.KENYA_MOBILE_NUMBER
                ),
                ignore_invalid_mobile_numbers=True,
                question_configurations=[
                    KoboToolBoxQuestionConfiguration(data_column_name="leap_s06e03", engagement_db_dataset="leap_s06e03"),
                ] + demogs_question_configurations
            )
        ),
        KoboToolBoxSource(
            token_file_url="gs://avf-credentials/wusc-kobotoolbox-token.json",
            sync_config=KoboToolBoxToEngagementDBConfiguration(
                asset_uid="a7mtvFKGS4Ccj3LGSbAXDG",
                participant_id_configuration=KoboToolBoxParticipantIdConfiguration(
                    data_column_name="Contacts",
                    id_type=KoboToolBoxParticipantIdTypes.KENYA_MOBILE_NUMBER
                ),
                ignore_invalid_mobile_numbers=True,
                question_configurations=[
                    KoboToolBoxQuestionConfiguration(data_column_name="leap_s06e04", engagement_db_dataset="leap_s06e04"),
                ] + demogs_question_configurations
            )
        ),
    ],
    coda_sync=CodaConfiguration(
        coda=CodaClientConfiguration(credentials_file_url="gs://avf-credentials/coda-production.json"),
        sync_config=CodaSyncConfiguration(
            dataset_configurations= generate_rqa_coda_dataset_configs() + [
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_kakuma_gender",
                    engagement_db_dataset="kakuma_gender",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/gender"),
                                                auto_coder=swahili.DemographicCleaner.clean_gender,
                                                coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="kakuma gender"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_kakuma_age",
                    engagement_db_dataset="kakuma_age",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/age"),
                                                auto_coder=lambda x:str(swahili.DemographicCleaner.clean_age_within_range(x)),
                                                coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="kakuma age"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_kakuma_location",
                    engagement_db_dataset="kakuma_location",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/location"),
                                                auto_coder=None),
                    ],
                    ws_code_match_value="kakuma location"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_kakuma_nationality",
                    engagement_db_dataset="kakuma_nationality",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/nationality"),
                                                auto_coder=None),
                    ],
                    ws_code_match_value="kakuma nationality"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_kakuma_preffered_language",
                    engagement_db_dataset="kakuma_preffered_language",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/preffered_language"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="kakuma preffered language"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_kakuma_household_language",
                    engagement_db_dataset="kakuma_household_language",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/household_language"),
                                                auto_coder=None, coda_code_schemes_count=3),
                    ],
                    ws_code_match_value="kakuma household language"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_kakuma_disabled",
                    engagement_db_dataset="kakuma_disabled",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/disabled"),
                                                auto_coder=None, coda_code_schemes_count=3)
                    ],
                    ws_code_match_value="kakuma disabled"
                ),
            ],
            ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
            project_users_file_url="gs://avf-project-datasets/2021/WUSC-LEAP/coda_users.json",
            default_ws_dataset="kakuma_old_rqa_datasets"
        )
    ),
    analysis=AnalysisConfiguration(
        google_drive_upload=GoogleDriveUploadConfiguration(
            credentials_file_url="gs://avf-credentials/pipeline-runner-service-acct-avf-data-core-64cc71459fe7.json",
            drive_dir="leap_s06_analysis_output"
        ),
        dataset_configurations=generate_rqa_analysis_dataset_configs() + [
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["kakuma_gender"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="gender_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/gender"),
                        analysis_dataset="gender"
                    )
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["kakuma_location"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="location_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/location"),
                        analysis_dataset="location"
                    ),
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["kakuma_preffered_language"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="preffered_language_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/preffered_language"),
                        analysis_dataset="preffered_language"
                    ),
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["kakuma_nationality"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="nationality_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/nationality"),
                        analysis_dataset="nationality"
                    ),
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["kakuma_disabled"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="disabled_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/disabled"),
                        analysis_dataset="disabled"
                    ),
                ]
            ),
            AnalysisDatasetConfiguration(
                engagement_db_datasets=["kakuma_age"],
                dataset_type=DatasetTypes.DEMOGRAPHIC,
                raw_dataset="age_raw",
                coding_configs=[
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/age"),
                        analysis_dataset="age"
                    ),
                    CodingConfiguration(
                        code_scheme=load_code_scheme("demographics/age_category"),
                        analysis_dataset="age_category",
                        age_category_config=AgeCategoryConfiguration(
                            age_analysis_dataset="age",
                            categories={
                                (10, 14): "10 to 14",
                                (15, 17): "15 to 17",
                                (18, 35): "18 to 35",
                                (36, 54): "36 to 54",
                                (55, 99): "55 to 99"
                            }
                        )
                    ),
                ],
            ),
        ],
        ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
    ),
    rapid_pro_target=RapidProTarget(
        rapid_pro=RapidProClientConfiguration(
            domain="textit.com",
            token_file_url="gs://avf-credentials/wusc-leap-kalobeyei-textit-token.txt"
        ),
        sync_config=EngagementDBToRapidProConfiguration(
            normal_datasets=[
                DatasetConfiguration(
                    engagement_db_datasets=["kakuma_preffered_language"],
                    rapid_pro_contact_field=ContactField(key="pool_wusc_preferred_language", label="pool_wusc_preferred_language")
                ),
                DatasetConfiguration(
                    engagement_db_datasets=["kakuma_gender"],
                    rapid_pro_contact_field=ContactField(key="pool_wusc_gender", label="pool wusc gender")
                ),
                DatasetConfiguration(
                    engagement_db_datasets=["kakuma_location"],
                    rapid_pro_contact_field=ContactField(key="pool_wusc_location", label="pool wusc location")
                ),
                DatasetConfiguration(
                    engagement_db_datasets=["kakuma_nationality"],
                    rapid_pro_contact_field=ContactField(key="pool_wusc_nationality", label="pool wusc nationality")
                ),
                DatasetConfiguration(
                    engagement_db_datasets=["kakuma_age"],
                    rapid_pro_contact_field=ContactField(key="pool_wusc_age", label="pool wusc age"),
                ),
                DatasetConfiguration(
                    engagement_db_datasets=["kakuma_disabled"],
                    rapid_pro_contact_field=ContactField(key="pool_wusc_disabled", label="pool wusc disabled")
                ),
            ],
            consent_withdrawn_dataset=DatasetConfiguration(
                engagement_db_datasets=["kakuma_age", "kakuma_gender", "kakuma_location", "kakuma_disabled",
                                        "kakuma_preffered_language", "kakuma_nationality", "kakuma_old_rqa_datasets",
                                        "leap_s04e01","leap_s04e02","leap_s04e03", "leap_s04e04",
                                        "leap_s04e05", "leap_s04e06", "leap_s05e01","leap_s05e02","leap_s05e03", 
                                        "leap_s05e04", "leap_s05e05", "leap_s05e06"],
                rapid_pro_contact_field=ContactField(key="pool_wusc_consent_withdrawn",
                                                     label="pool wusc consent withdrawn")
            ),
            write_mode=WriteModes.CONCATENATE_TEXTS,
            allow_clearing_fields=False,
            weekly_advert_contact_field=ContactField(key="leap_s06_advert_contact",
                                                     label="leap s06 advert contact"),
            sync_advert_contacts=True,
        )
    ),
    archive_configuration=ArchiveConfiguration(
        archive_upload_bucket="gs://pipeline-execution-backup-archive",
        bucket_dir_path="2022/POOL-WUSC/S06"
    )
)
