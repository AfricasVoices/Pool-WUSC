from core_data_modules.cleaners import swahili

from src.pipeline_configuration_spec import *
PIPELINE_CONFIGURATION = PipelineConfiguration(
    pipeline_name="CREATE-WUSC-DADAAB-POOL",
    engagement_database=EngagementDatabaseClientConfiguration(
        credentials_file_url="gs://avf-credentials/avf-engagement-databases-firebase-credentials-file.json",
        database_path="engagement_databases/WUSC-DADAAB"
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
                    FlowResultConfiguration("wusc_keep_ii_dadaab_demogs", "household_language",
                                            "household_language"),
                    FlowResultConfiguration("wusc_keep_ii_dadaab_demogs", "age", "age"),
                    FlowResultConfiguration("wusc_keep_ii_dadaab_demogs", "location", "location"),
                    FlowResultConfiguration("wusc_keep_ii_dadaab_demogs", "nationality", "nationality"),
                    FlowResultConfiguration("wusc_keep_ii_dadaab_demogs", "gender", "gender"),

                    FlowResultConfiguration("wusc_covid19_adaptation_dadaab_demogs", "household_language",
                                            "household_language"),
                    FlowResultConfiguration("wusc_covid19_adaptation_dadaab_demogs", "age", "age"),
                    FlowResultConfiguration("wusc_covid19_adaptation_dadaab_demogs", "location", "location"),
                    FlowResultConfiguration("wusc_covid19_adaptation_dadaab_demogs", "nationality", "nationality"),
                    FlowResultConfiguration("wusc_covid19_adaptation_dadaab_demogs", "gender", "gender"),

                    FlowResultConfiguration("wusc_keep_ii_s03_dadaab_demogs", "household_language",
                                            "household_language"),
                    FlowResultConfiguration("wusc_keep_ii_s03_dadaab_demogs", "age", "age"),
                    FlowResultConfiguration("wusc_keep_ii_s03_dadaab_demogs", "location", "location"),
                    FlowResultConfiguration("wusc_keep_ii_s03_dadaab_demogs", "nationality", "nationality"),
                    FlowResultConfiguration("wusc_keep_ii_s03_dadaab_demogs", "gender", "gender")
                ]
            )
        ),
    ],
    coda_sync=CodaConfiguration(
        coda=CodaClientConfiguration(credentials_file_url="gs://avf-credentials/coda-production.json"),
        sync_config=CodaSyncConfiguration(
            dataset_configurations=[
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_dadaab_gender",
                    engagement_db_dataset="gender",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/gender"),
                                                auto_coder=swahili.DemographicCleaner.clean_gender)
                    ],
                    ws_code_string_value="dadaab gender"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_dadaab_location",
                    engagement_db_dataset="location",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/dadaab_location"), auto_coder=None),
                    ],
                    ws_code_string_value="dadaab location"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_dadaab_household_language",
                    engagement_db_dataset="household_language",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/dadaab_household_language"), auto_coder=None),
                    ],
                    ws_code_string_value="dadaab household language"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_dadaab_age",
                    engagement_db_dataset="age",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/age"), auto_coder=lambda x:
                        str(swahili.DemographicCleaner.clean_age_within_range(x))),
                    ],
                    ws_code_string_value="dadaab age"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC-KEEP-II_dadaab_nationality",
                    engagement_db_dataset="nationality",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("demographics/nationality"), auto_coder=lambda x:
                        str(swahili.DemographicCleaner.clean_age_within_range(x))),
                    ],
                    ws_code_string_value="dadaab nationality"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="WUSC_dadaab_old_rqa_datasets",
                    engagement_db_dataset="dadaab_old_rqa_datasets",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("dadaab_old_rqa_datasets"), auto_coder=None)
                    ],
                    ws_code_string_value="dadaab old rqa datasets"
                ),
            ],
            ws_correct_dataset_code_scheme=load_code_scheme("dadaab_ws_correct_dataset"),
            project_users_file_url="gs://avf-project-datasets/2021/WUSC-LEAP/coda_users.json",
            default_ws_dataset="dadaab_old_rqa_datasets"
        )
    ),
    archive_configuration=ArchiveConfiguration(
        archive_upload_bucket="gs://pipeline-execution-backup-archive",
        bucket_dir_path="2022/CREATE-WUSC-POOL/"
    )
)
