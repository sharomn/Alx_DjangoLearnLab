# 💬 Comment System Documentation

## Overview
Users can view comments on blog posts. Authenticated users can add, edit, and delete their own comments.

## Features
- Add comment on post detail page
- Edit/delete own comments
- View all comments under each post

## Permissions
- Only logged-in users can comment
- Only comment authors can edit/delete

## URLs
- `/posts/<post_id>/comments/new/` → Add comment
- `/comments/<pk>/edit/` → Edit comment
- `/comments/<pk>/delete/` → Delete comment

## Testing
- Log in and add a comment
- Edit/delete your comment
- Try unauthorized actions (should be blocked)