# Advanced API Project — Custom and Generic Views

## Endpoints
- `/api/books/` → List all books (public)
- `/api/books/<id>/` → Retrieve single book (public)
- `/api/books/create/` → Create book (authenticated only)
- `/api/books/<id>/update/` → Update book (authenticated only)
- `/api/books/<id>/delete/` → Delete book (authenticated only)

## Permissions
- Public read-only access
- Create/Update/Delete requires login

