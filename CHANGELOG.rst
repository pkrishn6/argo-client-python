Changelog
=========


v3.0.1 (2020-02-26)
-------------------

New
~~~
- Updated README compatibility matrix. [Marek Cermak]

Other
~~~~~
- :wrench: Patch 3.0.1. [Marek Cermak]


v3.0.0 (2020-02-26)
-------------------
- :tada: Release 3.0. [Marek Cermak]


v3.0.0-rc2 (2020-02-26)
-----------------------

New
~~~
- Generated models for Argo v2.5.0 release. [Marek Cermak]


v3.0.0-rc (2020-02-26)
----------------------

New
~~~
- Generated models for Argo 2.5.0-rc10. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  modified:   argo/workflows/client/__init__.py
  modified:   argo/workflows/client/api/v1alpha1_api.py
  modified:   argo/workflows/client/api_client.py
  modified:   argo/workflows/client/configuration.py
  modified:   argo/workflows/client/models/__init__.py
  modified:   argo/workflows/client/models/v1alpha1_archive_strategy.py
  modified:   argo/workflows/client/models/v1alpha1_arguments.py
  modified:   argo/workflows/client/models/v1alpha1_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_artifact_location.py
  modified:   argo/workflows/client/models/v1alpha1_artifact_repository_ref.py
  modified:   argo/workflows/client/models/v1alpha1_artifactory_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_artifactory_auth.py
  modified:   argo/workflows/client/models/v1alpha1_continue_on.py
  modified:   argo/workflows/client/models/v1alpha1_dag_task.py
  modified:   argo/workflows/client/models/v1alpha1_dag_template.py
  modified:   argo/workflows/client/models/v1alpha1_executor_config.py
  modified:   argo/workflows/client/models/v1alpha1_git_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_hdfs_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_hdfs_config.py
  modified:   argo/workflows/client/models/v1alpha1_hdfs_krb_config.py
  modified:   argo/workflows/client/models/v1alpha1_http_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_inputs.py
  modified:   argo/workflows/client/models/v1alpha1_metadata.py
  modified:   argo/workflows/client/models/v1alpha1_node_status.py
  modified:   argo/workflows/client/models/v1alpha1_outputs.py
  modified:   argo/workflows/client/models/v1alpha1_parameter.py
  modified:   argo/workflows/client/models/v1alpha1_pod_gc.py
  modified:   argo/workflows/client/models/v1alpha1_raw_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_resource_template.py
  modified:   argo/workflows/client/models/v1alpha1_retry_strategy.py
  modified:   argo/workflows/client/models/v1alpha1_s3_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_s3_bucket.py
  modified:   argo/workflows/client/models/v1alpha1_script_template.py
  modified:   argo/workflows/client/models/v1alpha1_sequence.py
  modified:   argo/workflows/client/models/v1alpha1_template.py
  modified:   argo/workflows/client/models/v1alpha1_template_ref.py
  modified:   argo/workflows/client/models/v1alpha1_user_container.py
  modified:   argo/workflows/client/models/v1alpha1_value_from.py
  modified:   argo/workflows/client/models/v1alpha1_workflow.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_list.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_spec.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_status.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_step.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_template.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_template_list.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_template_spec.py
  modified:   argo/workflows/client/rest.py
  modified:   openapi/swagger.json
  new file:   argo/workflows/client/models/v1alpha1_backoff.py
  new file:   argo/workflows/client/models/v1alpha1_cron_workflow.py
  new file:   argo/workflows/client/models/v1alpha1_cron_workflow_list.py
  new file:   argo/workflows/client/models/v1alpha1_cron_workflow_spec.py
  new file:   argo/workflows/client/models/v1alpha1_cron_workflow_status.py
  new file:   argo/workflows/client/models/v1alpha1_item_value.py
  new file:   argo/workflows/client/models/v1alpha1_parallel_steps.py
  new file:   argo/workflows/client/models/v1alpha1_suspend_template.py
  new file:   argo/workflows/client/models/v1alpha1_ttl_strategy.py
  new file:   docs/V1alpha1Backoff.md
  new file:   docs/V1alpha1CronWorkflow.md
  new file:   docs/V1alpha1CronWorkflowList.md
  new file:   docs/V1alpha1CronWorkflowSpec.md
  new file:   docs/V1alpha1CronWorkflowStatus.md
  new file:   docs/V1alpha1ItemValue.md
  new file:   docs/V1alpha1ParallelSteps.md
  new file:   docs/V1alpha1SuspendTemplate.md
  new file:   docs/V1alpha1TTLStrategy.md
- Added generated openapi/swagger.json to the git. [Marek Cermak]
- Added paths for the Argo v2.5.0 models. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   argo/workflows/client/api/v1alpha1_api.py
  modified:   docs/V1alpha1Api.md
  modified:   openapi/custom/paths.json
- Generate models for Argo 2.5.0-rc5. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  modified:   argo/workflows/client/__about__.py
  modified:   argo/workflows/client/__init__.py
  modified:   argo/workflows/client/api/v1alpha1_api.py
  modified:   argo/workflows/client/api_client.py
  modified:   argo/workflows/client/configuration.py
  modified:   argo/workflows/client/models/__init__.py
  modified:   argo/workflows/client/models/v1alpha1_archive_strategy.py
  modified:   argo/workflows/client/models/v1alpha1_arguments.py
  modified:   argo/workflows/client/models/v1alpha1_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_artifact_location.py
  modified:   argo/workflows/client/models/v1alpha1_artifact_repository_ref.py
  modified:   argo/workflows/client/models/v1alpha1_artifactory_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_artifactory_auth.py
  modified:   argo/workflows/client/models/v1alpha1_continue_on.py
  modified:   argo/workflows/client/models/v1alpha1_dag_task.py
  modified:   argo/workflows/client/models/v1alpha1_dag_template.py
  modified:   argo/workflows/client/models/v1alpha1_executor_config.py
  modified:   argo/workflows/client/models/v1alpha1_git_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_hdfs_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_hdfs_config.py
  modified:   argo/workflows/client/models/v1alpha1_hdfs_krb_config.py
  modified:   argo/workflows/client/models/v1alpha1_http_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_inputs.py
  modified:   argo/workflows/client/models/v1alpha1_metadata.py
  modified:   argo/workflows/client/models/v1alpha1_node_status.py
  modified:   argo/workflows/client/models/v1alpha1_outputs.py
  modified:   argo/workflows/client/models/v1alpha1_parameter.py
  modified:   argo/workflows/client/models/v1alpha1_pod_gc.py
  modified:   argo/workflows/client/models/v1alpha1_raw_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_resource_template.py
  modified:   argo/workflows/client/models/v1alpha1_retry_strategy.py
  modified:   argo/workflows/client/models/v1alpha1_s3_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_s3_bucket.py
  modified:   argo/workflows/client/models/v1alpha1_script_template.py
  modified:   argo/workflows/client/models/v1alpha1_sequence.py
  modified:   argo/workflows/client/models/v1alpha1_template.py
  modified:   argo/workflows/client/models/v1alpha1_template_ref.py
  modified:   argo/workflows/client/models/v1alpha1_user_container.py
  modified:   argo/workflows/client/models/v1alpha1_value_from.py
  modified:   argo/workflows/client/models/v1alpha1_workflow.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_list.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_spec.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_status.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_step.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_template.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_template_list.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_template_spec.py
  modified:   argo/workflows/client/rest.py
  modified:   docs/V1alpha1DAGTask.md
  modified:   docs/V1alpha1NodeStatus.md
  modified:   docs/V1alpha1RetryStrategy.md
  modified:   docs/V1alpha1ScriptTemplate.md
  modified:   docs/V1alpha1Template.md
  modified:   docs/V1alpha1UserContainer.md
  modified:   docs/V1alpha1Workflow.md
  modified:   docs/V1alpha1WorkflowList.md
  modified:   docs/V1alpha1WorkflowSpec.md
  modified:   docs/V1alpha1WorkflowStatus.md
  modified:   docs/V1alpha1WorkflowStep.md
  modified:   docs/V1alpha1WorkflowTemplate.md
  modified:   docs/V1alpha1WorkflowTemplateList.md
- Update README with workflow submission example. [Marek Cermak]


v2.1.4 (2019-12-19)
-------------------
- :wrench: Patch 2.1.4. [Marek Cermak]


v2.1.3 (2019-12-18)
-------------------
- :wrench: Patch 2.1.3. [Marek Cermak]


v2.1.2 (2019-11-25)
-------------------

Fix
~~~
- Patch DagTask template requirement. [Marek Cermak]

Other
~~~~~
- :wrench: Patch 2.1.2. [Marek Cermak]


v2.1.1 (2019-11-18)
-------------------

Fix
~~~
- Import all models from Kubernetes. [Marek Cermak]

Other
~~~~~
- :wrench: Patch 2.1.1. [Marek Cermak]


v1.3.0 (2019-11-07)
-------------------

Fix
~~~
- Fix new_client_from_config() [Marek Cermak]

Other
~~~~~
- :tada: Release 1.3. [Marek Cermak]


v2.1.0 (2019-11-07)
-------------------

Fix
~~~
- Fix new_client_from_config() [Marek Cermak]

Other
~~~~~
- :tada: Release 2.1. [Marek Cermak]


v2.0.0 (2019-10-30)
-------------------

New
~~~
- Argo v2.4.0. [Marek Cermak]

  Added new models and generated client for Argo 2.4.0

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  new file:   docs/V1alpha1WorkflowTemplateSpec.md
  new file:   docs/V1alpha1WorkflowTemplateList.md
  new file:   docs/V1alpha1WorkflowTemplate.md
  new file:   docs/V1alpha1PodGC.md
  new file:   docs/V1alpha1ExecutorConfig.md
  new file:   docs/V1alpha1ArtifactRepositoryRef.md
  new file:   argo/workflows/client/models/v1alpha1_workflow_template_spec.py
  new file:   argo/workflows/client/models/v1alpha1_workflow_template_list.py
  new file:   argo/workflows/client/models/v1alpha1_workflow_template.py
  new file:   argo/workflows/client/models/v1alpha1_pod_gc.py
  new file:   argo/workflows/client/models/v1alpha1_executor_config.py
  new file:   argo/workflows/client/models/v1alpha1_artifact_repository_ref.py
  modified:   docs/V1alpha1WorkflowStep.md
  modified:   docs/V1alpha1WorkflowSpec.md
  modified:   docs/V1alpha1UserContainer.md
  modified:   docs/V1alpha1Template.md
  modified:   docs/V1alpha1ScriptTemplate.md
  modified:   docs/V1alpha1S3Bucket.md
  modified:   docs/V1alpha1S3Artifact.md
  modified:   docs/V1alpha1ResourceTemplate.md
  modified:   docs/V1alpha1GitArtifact.md
  modified:   docs/V1alpha1DAGTemplate.md
  modified:   docs/V1alpha1DAGTask.md
  modified:   docs/V1alpha1Api.md
  modified:   argo/workflows/client/rest.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_step.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_status.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_spec.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_list.py
  modified:   argo/workflows/client/models/v1alpha1_workflow.py
  modified:   argo/workflows/client/models/v1alpha1_value_from.py
  modified:   argo/workflows/client/models/v1alpha1_user_container.py
  modified:   argo/workflows/client/models/v1alpha1_template_ref.py
  modified:   argo/workflows/client/models/v1alpha1_template.py
  modified:   argo/workflows/client/models/v1alpha1_sequence.py
  modified:   argo/workflows/client/models/v1alpha1_script_template.py
  modified:   argo/workflows/client/models/v1alpha1_s3_bucket.py
  modified:   argo/workflows/client/models/v1alpha1_s3_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_retry_strategy.py
  modified:   argo/workflows/client/models/v1alpha1_resource_template.py
  modified:   argo/workflows/client/models/v1alpha1_raw_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_parameter.py
  modified:   argo/workflows/client/models/v1alpha1_outputs.py
  modified:   argo/workflows/client/models/v1alpha1_node_status.py
  modified:   argo/workflows/client/models/v1alpha1_metadata.py
  modified:   argo/workflows/client/models/v1alpha1_inputs.py
  modified:   argo/workflows/client/models/v1alpha1_http_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_hdfs_krb_config.py
  modified:   argo/workflows/client/models/v1alpha1_hdfs_config.py
  modified:   argo/workflows/client/models/v1alpha1_hdfs_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_git_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_dag_template.py
  modified:   argo/workflows/client/models/v1alpha1_dag_task.py
  modified:   argo/workflows/client/models/v1alpha1_continue_on.py
  modified:   argo/workflows/client/models/v1alpha1_artifactory_auth.py
  modified:   argo/workflows/client/models/v1alpha1_artifactory_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_artifact_location.py
  modified:   argo/workflows/client/models/v1alpha1_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_arguments.py
  modified:   argo/workflows/client/models/v1alpha1_archive_strategy.py
  modified:   argo/workflows/client/models/__init__.py
  modified:   argo/workflows/client/configuration.py
  modified:   argo/workflows/client/api_client.py
  modified:   argo/workflows/client/api/v1alpha1_api.py
  modified:   argo/workflows/client/__init__.py

Other
~~~~~
- :tada: Release 2.0. [Marek Cermak]


v1.2.0 (2019-10-30)
-------------------

Fix
~~~
- Added security definitions. [Marek Cermak]

  Fixes missing Auth settings and authentication via bearer token.

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  new file:   openapi/custom/security.json

Other
~~~~~
- :tada: Release 1.2. [Marek Cermak]


v1.1.0 (2019-10-25)
-------------------

New
~~~
- Support for event streaming. [Marek Cermak]

  Argo now implements kubernetes Watch.

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   argo/workflows/__init__.py
  new file:   argo/workflows/watch/__init__.py

Fix
~~~
- Ignore release and merge commits. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   .gitchangelog.rc
  modified:   Makefile

Other
~~~~~
- :tada: Release 1.1. [Marek Cermak]


v1.0.0 (2019-10-23)
-------------------

New
~~~
- Validate Makefile target. [Marek Cermak]
- Makefile release target. [Marek Cermak]

  Added release target to Makefile for easier versioning.

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  modified:   Pipfile
- Script to generate CHANGELOG. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  new file:   .gitchangelog.rc
  new file:   CHANGELOG.md
  new file:   scripts/generate_changelog.sh
  modified:   MANIFEST.in

Changes
~~~~~~~
- Delete existing tag before creating changelog. [Marek Cermak]
- Remove WorkflowStatus related paths. [Marek Cermak]

  The WorkflowStatus is not defined for Argo v2.3.0 CRD
- Do not issue git push on make release. [Marek Cermak]
- Allow to import models from argo.workflows. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   README.md
  modified:   argo/workflows/__init__.py
- Release name contains only MAJOR.MINOR. [Marek Cermak]

Fix
~~~
- Fix missing shells in Makefile. [Marek Cermak]

Other
~~~~~
- :tada: Release 1.0. [Marek Cermak]


v1.0.0a1 (2019-10-22)
---------------------
- :tada: Release 1.0.0a1. [Marek Cermak]
- Added TemplateRef definition. [Marek Cermak]

  - Argo 2.3.0 misses TemplateRef schema definition

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  modified:   argo/workflows/client/__init__.py
  modified:   argo/workflows/client/models/__init__.py
  new file:   argo/workflows/client/models/v1alpha1_template_ref.py
  new file:   docs/V1alpha1TemplateRef.md
  new file:   openapi/definitions/TemplateRef.json
- Added NodeStatus definition. [Marek Cermak]

  - Argo 2.3.0 misses NodeStatus schema definition

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  modified:   argo/workflows/client/__init__.py
  modified:   argo/workflows/client/models/__init__.py
  new file:   argo/workflows/client/models/v1alpha1_node_status.py
  new file:   docs/V1alpha1NodeStatus.md
  new file:   openapi/definitions/NodeStatus.json
- Added WorkflowStatus definition. [Marek Cermak]

  - Argo 2.3.0 misses WorkflowStatus schema definition

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  modified:   Pipfile
  modified:   argo/workflows/client/__init__.py
  modified:   argo/workflows/client/models/__init__.py
  new file:   argo/workflows/client/models/v1alpha1_workflow_status.py
  new file:   docs/V1alpha1WorkflowStatus.md
  new file:   openapi/definitions/WorkflowStatus.json
- Generate client for Argo v2.3.0. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  modified:   argo/workflows/client/__init__.py
  modified:   argo/workflows/client/api/v1alpha1_api.py
  modified:   argo/workflows/client/api_client.py
  modified:   argo/workflows/client/configuration.py
  modified:   argo/workflows/client/models/__init__.py
  modified:   argo/workflows/client/models/v1alpha1_archive_strategy.py
  modified:   argo/workflows/client/models/v1alpha1_arguments.py
  modified:   argo/workflows/client/models/v1alpha1_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_artifact_location.py
  deleted:    argo/workflows/client/models/v1alpha1_artifact_repository_ref.py
  modified:   argo/workflows/client/models/v1alpha1_artifactory_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_artifactory_auth.py
  modified:   argo/workflows/client/models/v1alpha1_continue_on.py
  modified:   argo/workflows/client/models/v1alpha1_dag_task.py
  modified:   argo/workflows/client/models/v1alpha1_dag_template.py
  deleted:    argo/workflows/client/models/v1alpha1_executor_config.py
  modified:   argo/workflows/client/models/v1alpha1_git_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_hdfs_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_hdfs_config.py
  modified:   argo/workflows/client/models/v1alpha1_hdfs_krb_config.py
  modified:   argo/workflows/client/models/v1alpha1_http_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_inputs.py
  modified:   argo/workflows/client/models/v1alpha1_metadata.py
  deleted:    argo/workflows/client/models/v1alpha1_node_status.py
  modified:   argo/workflows/client/models/v1alpha1_outputs.py
  modified:   argo/workflows/client/models/v1alpha1_parameter.py
  deleted:    argo/workflows/client/models/v1alpha1_pod_gc.py
  modified:   argo/workflows/client/models/v1alpha1_raw_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_resource_template.py
  modified:   argo/workflows/client/models/v1alpha1_retry_strategy.py
  modified:   argo/workflows/client/models/v1alpha1_s3_artifact.py
  modified:   argo/workflows/client/models/v1alpha1_s3_bucket.py
  modified:   argo/workflows/client/models/v1alpha1_script_template.py
  modified:   argo/workflows/client/models/v1alpha1_sequence.py
  modified:   argo/workflows/client/models/v1alpha1_template.py
  deleted:    argo/workflows/client/models/v1alpha1_template_ref.py
  modified:   argo/workflows/client/models/v1alpha1_user_container.py
  modified:   argo/workflows/client/models/v1alpha1_value_from.py
  modified:   argo/workflows/client/models/v1alpha1_workflow.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_list.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_spec.py
  deleted:    argo/workflows/client/models/v1alpha1_workflow_status.py
  modified:   argo/workflows/client/models/v1alpha1_workflow_step.py
  deleted:    argo/workflows/client/models/v1alpha1_workflow_template.py
  deleted:    argo/workflows/client/models/v1alpha1_workflow_template_list.py
  deleted:    argo/workflows/client/models/v1alpha1_workflow_template_spec.py
  modified:   argo/workflows/client/rest.py
  deleted:    docs/V1alpha1ArtifactRepositoryRef.md
  modified:   docs/V1alpha1DAGTask.md
  modified:   docs/V1alpha1DAGTemplate.md
  deleted:    docs/V1alpha1ExecutorConfig.md
  modified:   docs/V1alpha1GitArtifact.md
  deleted:    docs/V1alpha1NodeStatus.md
  deleted:    docs/V1alpha1PodGC.md
  modified:   docs/V1alpha1ResourceTemplate.md
  modified:   docs/V1alpha1S3Artifact.md
  modified:   docs/V1alpha1S3Bucket.md
  modified:   docs/V1alpha1ScriptTemplate.md
  modified:   docs/V1alpha1Template.md
  deleted:    docs/V1alpha1TemplateRef.md
  modified:   docs/V1alpha1UserContainer.md
  modified:   docs/V1alpha1WorkflowSpec.md
  deleted:    docs/V1alpha1WorkflowStatus.md
  modified:   docs/V1alpha1WorkflowStep.md
  deleted:    docs/V1alpha1WorkflowTemplate.md
  deleted:    docs/V1alpha1WorkflowTemplateList.md
  deleted:    docs/V1alpha1WorkflowTemplateSpec.md
- :pushpin: Pin down versions. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  new file:   Pipfile
  modified:   requirements.txt
- Update README.md. [Marek Cermak]

  Add more information about code generation
- Update README.md and set version 1.0. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   README.md
  modified:   argo/workflows/__about__.py
- Fix relative imports and remaining packages. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   README.md
  modified:   argo/workflows/__init__.py
  modified:   setup.py
- Signed-off-by: Marek Cermak <macermak@redhat.com> [Marek Cermak]

  modified:   Makefile
  modified:   scripts/generate_client.sh
  modified:   setup.py
  renamed:    argo/__about__.py -> argo/workflows/__about__.py
  renamed:    argo/__init__.py -> argo/workflows/__init__.py
  renamed:    argo/client/api/__init__.py -> argo/workflows/client/api/__init__.py
  renamed:    argo/client/api/v1alpha1_api.py -> argo/workflows/client/api/v1alpha1_api.py
  renamed:    argo/client/api_client.py -> argo/workflows/client/api_client.py
  renamed:    argo/client/configuration.py -> argo/workflows/client/configuration.py
  renamed:    argo/client/models/v1alpha1_archive_strategy.py -> argo/workflows/client/models/v1alpha1_archive_strategy.py
  renamed:    argo/client/models/v1alpha1_arguments.py -> argo/workflows/client/models/v1alpha1_arguments.py
  renamed:    argo/client/models/v1alpha1_artifact.py -> argo/workflows/client/models/v1alpha1_artifact.py
  renamed:    argo/client/models/v1alpha1_artifact_location.py -> argo/workflows/client/models/v1alpha1_artifact_location.py
  renamed:    argo/client/models/v1alpha1_artifact_repository_ref.py -> argo/workflows/client/models/v1alpha1_artifact_repository_ref.py
  renamed:    argo/client/models/v1alpha1_artifactory_artifact.py -> argo/workflows/client/models/v1alpha1_artifactory_artifact.py
  renamed:    argo/client/models/v1alpha1_artifactory_auth.py -> argo/workflows/client/models/v1alpha1_artifactory_auth.py
  renamed:    argo/client/models/v1alpha1_continue_on.py -> argo/workflows/client/models/v1alpha1_continue_on.py
  renamed:    argo/client/models/v1alpha1_dag_task.py -> argo/workflows/client/models/v1alpha1_dag_task.py
  renamed:    argo/client/models/v1alpha1_dag_template.py -> argo/workflows/client/models/v1alpha1_dag_template.py
  renamed:    argo/client/models/v1alpha1_executor_config.py -> argo/workflows/client/models/v1alpha1_executor_config.py
  renamed:    argo/client/models/v1alpha1_git_artifact.py -> argo/workflows/client/models/v1alpha1_git_artifact.py
  renamed:    argo/client/models/v1alpha1_hdfs_artifact.py -> argo/workflows/client/models/v1alpha1_hdfs_artifact.py
  renamed:    argo/client/models/v1alpha1_hdfs_config.py -> argo/workflows/client/models/v1alpha1_hdfs_config.py
  renamed:    argo/client/models/v1alpha1_hdfs_krb_config.py -> argo/workflows/client/models/v1alpha1_hdfs_krb_config.py
  renamed:    argo/client/models/v1alpha1_http_artifact.py -> argo/workflows/client/models/v1alpha1_http_artifact.py
  renamed:    argo/client/models/v1alpha1_inputs.py -> argo/workflows/client/models/v1alpha1_inputs.py
  renamed:    argo/client/models/v1alpha1_metadata.py -> argo/workflows/client/models/v1alpha1_metadata.py
  renamed:    argo/client/models/v1alpha1_node_status.py -> argo/workflows/client/models/v1alpha1_node_status.py
  renamed:    argo/client/models/v1alpha1_outputs.py -> argo/workflows/client/models/v1alpha1_outputs.py
  renamed:    argo/client/models/v1alpha1_parameter.py -> argo/workflows/client/models/v1alpha1_parameter.py
  renamed:    argo/client/models/v1alpha1_pod_gc.py -> argo/workflows/client/models/v1alpha1_pod_gc.py
  renamed:    argo/client/models/v1alpha1_raw_artifact.py -> argo/workflows/client/models/v1alpha1_raw_artifact.py
  renamed:    argo/client/models/v1alpha1_resource_template.py -> argo/workflows/client/models/v1alpha1_resource_template.py
  renamed:    argo/client/models/v1alpha1_retry_strategy.py -> argo/workflows/client/models/v1alpha1_retry_strategy.py
  renamed:    argo/client/models/v1alpha1_s3_artifact.py -> argo/workflows/client/models/v1alpha1_s3_artifact.py
  renamed:    argo/client/models/v1alpha1_s3_bucket.py -> argo/workflows/client/models/v1alpha1_s3_bucket.py
  renamed:    argo/client/models/v1alpha1_script_template.py -> argo/workflows/client/models/v1alpha1_script_template.py
  renamed:    argo/client/models/v1alpha1_sequence.py -> argo/workflows/client/models/v1alpha1_sequence.py
  renamed:    argo/client/models/v1alpha1_template.py -> argo/workflows/client/models/v1alpha1_template.py
  renamed:    argo/client/models/v1alpha1_template_ref.py -> argo/workflows/client/models/v1alpha1_template_ref.py
  renamed:    argo/client/models/v1alpha1_user_container.py -> argo/workflows/client/models/v1alpha1_user_container.py
  renamed:    argo/client/models/v1alpha1_value_from.py -> argo/workflows/client/models/v1alpha1_value_from.py
  renamed:    argo/client/models/v1alpha1_workflow.py -> argo/workflows/client/models/v1alpha1_workflow.py
  renamed:    argo/client/models/v1alpha1_workflow_list.py -> argo/workflows/client/models/v1alpha1_workflow_list.py
  renamed:    argo/client/models/v1alpha1_workflow_spec.py -> argo/workflows/client/models/v1alpha1_workflow_spec.py
  renamed:    argo/client/models/v1alpha1_workflow_status.py -> argo/workflows/client/models/v1alpha1_workflow_status.py
  renamed:    argo/client/models/v1alpha1_workflow_step.py -> argo/workflows/client/models/v1alpha1_workflow_step.py
  renamed:    argo/client/models/v1alpha1_workflow_template.py -> argo/workflows/client/models/v1alpha1_workflow_template.py
  renamed:    argo/client/models/v1alpha1_workflow_template_list.py -> argo/workflows/client/models/v1alpha1_workflow_template_list.py
  renamed:    argo/client/models/v1alpha1_workflow_template_spec.py -> argo/workflows/client/models/v1alpha1_workflow_template_spec.py
  renamed:    argo/client/rest.py -> argo/workflows/client/rest.py
  renamed:    argo/config/__init__.py -> argo/workflows/config/__init__.py
- Update README.md. [Marek Cermak]
- Generate client for Argo v2.4.0. [Marek Cermak]
- Setup. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  new file:   MANIFEST.in
  new file:   requirements.txt
  new file:   setup.py
- Generate client for Argo v2.4.0. [Marek Cermak]
- Setup. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  new file:   MANIFEST.in
  new file:   requirements.txt
  new file:   setup.py
- Add V1Time definition and remove patch. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  modified:   README.md
  new file:   openapi/definitions/V1Time.json
  deleted:    openapi/patch/swagger.json
- Add remaining API endpoints. [Marek Cermak]
- Update paths. [Marek Cermak]

  - create_namespaced_workflow

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   openapi/custom/config.json
  modified:   openapi/custom/paths.json
- Argo config. [Marek Cermak]

  - wrapper around kubernetes.config
- Add swagger codegen info. [Marek Cermak]
- Add .gitignore. [Marek Cermak]
- Add swagger ignore file. [Marek Cermak]
- Migrate from openapi to swagger generator. [Marek Cermak]

  - import kubernetes models

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  modified:   scripts/generate_client.sh
  new file:   openapi/patch/swagger.json
- Fix incorrect python imports. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  deleted:    openapi/custom/info.json
  deleted:    openapi/custom/swagger.json
  modified:   Makefile
  modified:   openapi/custom/paths.json
  modified:   scripts/generate_client.sh
  renamed:    openapi/config.json -> openapi/custom/config.json
- Refactoring. [Marek Cermak]

  openapi.json -> swagger.json

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  new file:   openapi/custom/version.json
- Run docker container as the current user. [Marek Cermak]
- Fix permissions. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   scripts/generate_client.sh
  modified:   scripts/preprocess.py
- Use explicit jq parameters. [Marek Cermak]

  - implicit parameters may fail in non-tty terminals
- Minor refactoring. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  modified:   scripts/generate_client.sh
- Cleanup. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  modified:   Makefile
  modified:   scripts/generate_client.sh
  modified:   scripts/preprocess.py
- [WIP] generate client code. [Marek Cermak]

  Signed-off-by: Marek Cermak <macermak@redhat.com>

  new file:   Makefile
  new file:   openapi/config.json
  new file:   openapi/custom/info.json
  new file:   openapi/custom/paths.json
  new file:   openapi/custom/swagger.json
  new file:   scripts/generate_client.sh
  new file:   scripts/preprocess.py


