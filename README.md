Backend Tech Stack:
- Django Framework 
- ORM 
- PostgreSQL Relational Database

Backend Languages:
- Python 
- SQL

Data Structure Diagram:
[Link to Canva File](https://www.canva.com/design/DAFRuhtn9Pc/rZ5cUC7uPvzlXqN5w0VbeQ/view?utm_content=DAFRuhtn9Pc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
Future Database ER Diagram:
[Link to Lucid App File](https://lucid.app/lucidchart/72e0d6f7-f28b-4d48-b3b6-4a4d29c5fadb/edit?viewport_loc=-289%2C-192%2C1540%2C1473%2C0_0&invitationId=inv_d0ac2e0d-b1e8-4eb4-871b-9e6fb19f9631)

Views:
- Generics

### Flow of Invite Creation:
1. Frontend: Determine if User is Host 
2. Frontend: Get Party associated with User --> With authUserId in URL Parameters
3. Backend: Call CreateInvite API with Guest Id & Party Id as fields in body of the anonymous call

Since Party automatically associated with Host Id, no need to pass Id of authenticated User when making POST Request