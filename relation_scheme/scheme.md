# Support database relational schema

```mermaid
erDiagram
  
  User {
    Int32 Id PK
    String UserName    
    String Email
    String PasswordHash
    String FirstName
    String LastName
    Int32 Role
  }

  Request {
    Int32 Id PK
    String Title "Only 75 characters are allowed"
    Int32 UserId FK
    Int32 CurrentManagerId
    Int32 Status
    Int32 Visibility
    Int32 CategoryId FK
  }
  
  RequestCategory {
    Int32 Id PK
    String Title
  }
  
  Message {
    Int32 Id PK
    Int32 RequestId FK
    DateTime TimeStamp
    Int32 UserId FK
    String Text "❓ max len = 2000"
  }
  
  RequestCategory ||--|| Request : "Request.CategoryId = RequestCategory.Id"
  Request ||--|{ Message : "Message.RequestId = Request.Id"
  Request ||--|| User : "Request.UserId = User.Id"
  Request ||--|| User : "Request.CurrentManagerId = User.Id"
  
  Message ||--|| User : "Message.UserId = User.Id"
```
---

[About Mermaid entity relationship diagrams](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)

Conventions of relationships between entities:

```mermaid
erDiagram

ExactlyOne {  
}

ZeroOrOne {  
}

ZeroOrMore {
}

OneOrMore {
}

ExactlyOne ||--o| ZeroOrOne : "to"
ExactlyOne ||--o{ ZeroOrMore : "to"
ExactlyOne ||--|{ OneOrMore : "to"
  
```
