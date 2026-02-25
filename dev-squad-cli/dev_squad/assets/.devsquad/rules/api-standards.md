---
trigger: model_decision
---

# Rule: API Specification Standards

## 1. Objective

Ensures consistent, predictable, and FHIR-compliant API design across all services. This project operates in the **Healthcare domain** and all APIs MUST conform to the **HL7 FHIR R4** standard unless explicitly documented as an internal/non-clinical API.

---

## 2. Versioning

- **Strategy**: Header-based versioning via the custom HTTP header `API-Version`.
- **Format**: The value is a **positive integer** (e.g., `API-Version: 1`, `API-Version: 2`). No semantic versioning (`v1.2.3`) and no URL path versioning (`/v1/`).
- **Mandatory**: Every request MUST include the `API-Version` header. Requests missing this header MUST be rejected with `400 Bad Request`.
- **Backward Compatibility**: A new version MUST be introduced for any breaking change. Non-breaking additions (new optional fields) are allowed within the same version.
- **Documentation**: The `API-Version` header MUST be documented in the OpenAPI spec as a required request header on every operation.

---

## 3. FHIR Compliance (HL7 FHIR R4)

All clinical and patient-facing APIs MUST conform to **HL7 FHIR R4**.

### Resource Naming & Structure

- Use FHIR resource types as the resource name (e.g., `/Patient`, `/Observation`, `/DiagnosticReport`, `/Encounter`).
- FHIR resource names are **singular and PascalCase**, not plural snake_case (e.g., `/Patient`, NOT `/patients`).
- Every FHIR resource response MUST include the mandatory fields: `resourceType`, `id`, `meta`.

### Content Type

- Requests and responses MUST use `Content-Type: application/fhir+json` for FHIR endpoints.
- Standard JSON (`application/json`) is acceptable only for internal non-clinical APIs.

### Error Responses (OperationOutcome)

- All FHIR API errors MUST return an **`OperationOutcome`** resource, not a generic error JSON object.
  ```json
  {
    "resourceType": "OperationOutcome",
    "issue": [
      {
        "severity": "error",
        "code": "not-found",
        "diagnostics": "Patient with id 'abc123' was not found."
      }
    ]
  }
  ```
- FHIR severity levels: `fatal`, `error`, `warning`, `information`.

### Search & Queries

- Use FHIR standard search parameters (e.g., `_id`, `_count`, `_include`, `_revinclude`, `_sort`).
- Paginated results MUST be returned as a **FHIR `Bundle`** with `type: searchset`.
- Bundle MUST include `total`, `link` (self, next, previous), and `entry` arrays.

### Profiles & Extensions

- All resources MUST declare the applicable FHIR Profile in `meta.profile`.
- Custom extensions MUST use a namespaced URI (e.g., `https://your-org.com/fhir/StructureDefinition/custom-extension`).

---

## 4. RESTful Design Patterns

- **HTTP Methods**: Use standard methods appropriately:
  - `GET` — Read a resource or search.
  - `POST` — Create a resource or invoke an operation (`$operation`).
  - `PUT` — Full update (replace) of an existing resource.
  - `PATCH` — Partial update using a FHIR Patch (JSON Patch or FHIR Patch).
  - `DELETE` — Logical delete (FHIR resources are soft-deleted by default).
- **HTTP Status Codes**: Align with FHIR expectations:
  - `200 OK` — Successful read or search.
  - `201 Created` — Successful resource creation (MUST include `Location` header).
  - `204 No Content` — Successful operation with no response body.
  - `400 Bad Request` — Invalid FHIR resource or missing required header.
  - `401 Unauthorized` — Missing or invalid auth token.
  - `403 Forbidden` — Authenticated but not authorized.
  - `404 Not Found` — Resource does not exist.
  - `422 Unprocessable Entity` — Semantically invalid FHIR resource.

---

## 5. Documentation

- Every API MUST have an **OpenAPI 3.x** definition AND a **FHIR CapabilityStatement** (`/metadata` endpoint).
- Document ALL headers (e.g., `Authorization`, `API-Version`, `X-Correlation-ID`, `Content-Type`).
- Every operation MUST document its FHIR profile, search parameters, and supported `_include` values.

---

## 6. Performance & Security

- **Pagination**: All list/search endpoints MUST return paginated FHIR Bundles. Default page size: 20. Maximum: 100.
- **Rate Limiting**: Thresholds MUST be defined per endpoint and communicated via `Retry-After` headers.
- **Authentication**: All endpoints except `/metadata` (CapabilityStatement) and health probes MUST require a valid Bearer token (OAuth 2.0 / SMART on FHIR).
- **SMART on FHIR**: For patient-facing applications, use **SMART on FHIR** authorization scopes (e.g., `patient/Patient.read`, `user/Observation.write`).

---

## 7. Competency Boundary

- Enforced by the **Solution Architect** and **Senior Security Engineer** (for SMART/OAuth).
- Reviewed by the **API Specification Reviewer** skill and the **Compliance Auditor** skill (HIPAA alignment).
