# Flow: feature launch

**Trigger**: CEO or CPO approves a new feature idea.

## Steps
1. `cpo` -> idea -> prioritization decision
2. `user-researcher` -> idea -> research summary
3. `product-manager` -> research + decision -> PRD with acceptance criteria
4. `ux-designer` + `ui-designer` -> PRD -> flows and visual specs
5. `engineering-manager` -> PRD + specs -> task breakdown assigned to `frontend-engineer` / `backend-engineer`
6. `code-reviewer` + `security-engineer` -> diff -> review findings
7. `qa-engineer` -> build + acceptance criteria -> test report
8. `legal-counsel` / `compliance-officer` -> feature -> risk notes (parallel with 6-7)
9. `devops-engineer` -> approved build -> deployment
10. `technical-writer` + `content-writer` -> shipped feature -> docs and announcement draft
11. `customer-support` -> docs -> FAQ updates
12. `data-analyst` -> usage data -> success metrics report to `cpo`

## Done when
Feature is deployed, documented, and the success metrics report is delivered.
office: flow=feature-launch (agents walk desk-to-desk in step order)
