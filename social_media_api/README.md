## 📘 API Endpoints

### 🔐 Authentication
- `POST /api/accounts/register/` → Register user
- `POST /api/accounts/login/` → Login and receive token

### 📝 Posts
- `GET /api/posts/` → List posts
- `POST /api/posts/` → Create post (auth required)
- `PUT /api/posts/{id}/` → Update own post
- `DELETE /api/posts/{id}/` → Delete own post

### 💬 Comments
- `GET /api/comments/` → List comments
- `POST /api/comments/` → Create comment
- `PUT /api/comments/{id}/` → Update own comment
- `DELETE /api/comments/{id}/` → Delete own comment

### 🔍 Filtering
- Search posts by title/content: `GET /api/posts/?search=keyword`

### 📄 Pagination
- Default page size: 10
- Use `?page=2` to navigate

## 👥 Follow Management

- `POST /api/accounts/follow/<user_id>/` → Follow a user
- `POST /api/accounts/unfollow/<user_id>/` → Unfollow a user

## 📰 Feed

- `GET /api/feed/` → View posts from followed users (ordered by newest)

## 🔄 User Model Update

- `followers`: ManyToMany to self (non-symmetrical)
- Access:
  - `user.following.all()` → users they follow
  - `user.followers.all()` → users who follow them