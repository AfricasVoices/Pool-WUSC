from core_data_modules.cleaners import swahili

from src.pipeline_configuration_spec import *

rapid_pro_uuid_filter = UuidFilter(
    uuid_file_url="gs://avf-project-datasets/2021/WUSC_POOL/initial_wusc_kakuma_kalobeyei_pool_deidentified_uuids.json")

PIPELINE_CONFIGURATION = PipelineConfiguration(
    pipeline_name="CREATE-KAKUMA-WUSC-POOL",
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
                token_file_url="gs://avf-credentials/wusc-keep-II-kakuma-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("wusc_keep_ii_kakuma_demogs", "household_language",
                                            "kakuma_household_language"),
                    FlowResultConfiguration("wusc_keep_ii_kakuma_demogs", "age", "kakuma_age"),
                    FlowResultConfiguration("wusc_keep_ii_kakuma_demogs", "location", "kakuma_location"),
                    FlowResultConfiguration("wusc_keep_ii_kakuma_demogs", "nationality", "kakuma_nationality"),
                    FlowResultConfiguration("wusc_keep_ii_kakuma_demogs", "gender", "kakuma_gender"),

                    FlowResultConfiguration("wusc_covid19_adaptation_kakuma_demogs", "household_language",
                                            "kakuma_household_language"),
                    FlowResultConfiguration("wusc_covid19_adaptation_kakuma_demogs", "age", "kakuma_age"),
                    FlowResultConfiguration("wusc_covid19_adaptation_kakuma_demogs", "location", "kakuma_location"),
                    FlowResultConfiguration("wusc_covid19_adaptation_kakuma_demogs", "nationality", "kakuma_nationality"),
                    FlowResultConfiguration("wusc_covid19_adaptation_kakuma_demogs", "gender", "kakuma_gender"),

                    FlowResultConfiguration("wusc_keep_ii_s03_kakuma_demogs", "household_language",
                                            "kakuma_household_language"),
                    FlowResultConfiguration("wusc_keep_ii_s03_kakuma_demogs", "age", "kakuma_age"),
                    FlowResultConfiguration("wusc_keep_ii_s03_kakuma_demogs", "location", "kakuma_location"),
                    FlowResultConfiguration("wusc_keep_ii_s03_kakuma_demogs", "nationality", "kakuma_nationality"),
                    FlowResultConfiguration("wusc_keep_ii_s03_kakuma_demogs", "gender", "kakuma_gender")
                ]
            )
        ),
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/wusc-leap-kalobeyei-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("wusc_leap_s01_kalobeyei_demogs", "household language",
                                            "kakuma_household_language"),
                    FlowResultConfiguration("wusc_leap_s01_kalobeyei_demogs", "age", "kakuma_age"),
                    FlowResultConfiguration("wusc_leap_s01_kalobeyei_demogs", "location", "kakuma_location"),
                    FlowResultConfiguration("wusc_leap_s01_kalobeyei_demogs", "nationality", "kakuma_nationality"),
                    FlowResultConfiguration("wusc_leap_s01_kalobeyei_demogs", "gender", "kakuma_gender")
                ]
            )
        )
    ],
    coda_sync=CodaConfiguration(
        coda=CodaClientConfiguration(credentials_file_url="gs://avf-credentials/coda-production.json"),
        sync_config=CodaSyncConfiguration(
            dataset_configurations=[
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_kakuma_gender",
                    engagement_db_dataset="kakuma_gender",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/gender"), auto_coder=swahili.DemographicCleaner.clean_gender)
                    ],
                    ws_code_string_value="kakuma gender"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_kakuma_location",
                    engagement_db_dataset="kakuma_location",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/location"), auto_coder=None),
                    ],
                    ws_code_string_value="kakuma location"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_kakuma_household_language",
                    engagement_db_dataset="kakuma_household_language",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/household_language"), auto_coder=None),
                    ],
                    ws_code_string_value="kakuma household language"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_kakuma_age",
                    engagement_db_dataset="kakuma_age",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/age"), auto_coder=lambda x:
                        str(swahili.DemographicCleaner.clean_age_within_range(x))),
                    ],
                    ws_code_string_value="kakuma age"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC_kakuma_old_rqa_datasets",
                    engagement_db_dataset="kakuma_old_rqa_datasets",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("kakuma_old_rqa_datasets"), auto_coder=None)
                    ],
                    ws_code_string_value="kakuma old rqa datasets"
                ),
            ],
            ws_correct_dataset_code_scheme=load_code_scheme("ws_correct_dataset"),
            project_users_file_url="gs://avf-project-datasets/2021/WUSC-LEAP/coda_users.json",
            default_ws_dataset="kakuma_old_rqa_datasets"
        )
    ),
    rapid_pro_target=RapidProTarget(
        rapid_pro=RapidProClientConfiguration(
            domain="textit.com",
            token_file_url="gs://avf-credentials/wusc-leap-kalobeyei-textit-token.txt"
        ),
        sync_config=EngagementDBToRapidProConfiguration(
            normal_datasets=[
                DatasetConfiguration(
                    engagement_db_datasets=["age"],
                    rapid_pro_contact_field=ContactField(key="pool_wusc_age", label="pool wusc age")
                ),
                DatasetConfiguration(
                    engagement_db_datasets=["gender"],
                    rapid_pro_contact_field=ContactField(key="pool_wusc_gender", label="pool wusc gender")
                ),
                DatasetConfiguration(
                    engagement_db_datasets=["location"],
                    rapid_pro_contact_field=ContactField(key="pool_wusc_location", label="pool wusc location")
                ),
                DatasetConfiguration(
                    engagement_db_datasets=["disabled"],
                    rapid_pro_contact_field=ContactField(key="pool_wusc_disabled", label="pool wusc disabled")
                ),
            ],
            consent_withdrawn_dataset=DatasetConfiguration(
                engagement_db_datasets=["age", "gender", "location", "disabled", "kakuma_old_rqa_datasets"],
                rapid_pro_contact_field=ContactField(key="pool_wusc_consent_withdrawn", label="pool wusc consent withdrawn")
            ),
        )
    ),
    archive_configuration=ArchiveConfiguration(
        archive_upload_bucket="gs://pipeline-execution-backup-archive",
        bucket_dir_path="2022/POOL-WUSC/"
    )
)
