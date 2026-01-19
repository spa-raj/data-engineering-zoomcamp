variable "project" {
  type        = string
  default     = "project-778881d8-11ba-45b5-b3d"
  description = "Project ID"
}
variable "location" {
  description = "Project Location"
  default     = "us-central1"
}
variable "gcs_bucket_name" {
  description = "The name of the GCS bucket"
  default     = "de-zoomcamp-nyc-taxi"
}
variable "bq_dataset_name" {
  description = "The name of the BigQuery dataset"
  default     = "de_zoomcamp_nyc_taxi_data"
}
