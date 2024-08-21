POSTMOTERM TO SOKOFRESH WEB APP

The company website experienced a critical outage from 14:30 to 16:45 EAT on August 15, 2024. During this period, approximately 85% of users were unable to access the site, encountering "503 Service Unavailable" errors. The root cause was identified as a database connection pool exhaustion due to a poorly optimized query introduced in the latest deployment.
Timeline:
14:30 EAT - Issue detected through automated monitoring alert showing a spike in error rates.
14:35 EAT - Engineering team began investigating, initially focusing on recent code deployments.
14:50 EAT - Frontend and CDN ruled out as potential causes; focus shifted to backend services.
15:10 EAT - Database team noticed unusually high number of open connections.
15:25 EAT - Incident escalated to senior backend engineers and database administrators.
15:45 EAT - Root cause identified as a problematic database query in the latest code release.
16:15 EAT - Hotfix deployed to revert the problematic query.
16:45 EAT - Service fully restored and confirmed stable.
Root Cause and Resolution: The outage was caused by a new database query introduced in the latest code deployment. This query was not properly optimized and resulted in long-running database connections that weren't being closed promptly. As traffic increased, the connection pool was quickly exhausted, preventing new requests from establishing database connections.
The issue was resolved by identifying and reverting the problematic query to its previous, optimized version. Additionally, the database connection pool size was temporarily increased to accommodate the backlog of requests.
Corrective and Preventative Measures:
Improve code review process, focusing on database query performance.
Implement automated query performance testing in the CI/CD pipeline.
Enhance monitoring for database connection pool utilization.
Conduct regular performance audits of critical database queries.
TODO:
Set up query execution plan analysis in the development environment.
Create and document best practices for writing efficient database queries.
Implement alerts for sudden spikes in database connection usage.
Schedule monthly database performance review meetings.
Upgrade database monitoring tools to provide more granular insights.
Conduct a team-wide training session on database query optimization techniques.
This postmortem report provides a concise overview of the incident, its timeline, root cause, and steps to prevent similar issues in the future. It should serve as a valuable learning tool for the team and help improve the overall reliability of the website.

