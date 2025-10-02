# 🏷️ Tagging & 🔍 Search Features

## Tagging
- Add tags to posts using comma-separated input in the form.
- Tags are displayed on post detail pages.
- Clicking a tag shows all posts with that tag.

## Search
- Use the search bar to find posts by title, content, or tag.
- Results are shown on a dedicated search results page.

## URLs
- `/search/?q=keyword` → Search posts
- `/tags/<tag_name>/` → View posts by tag

## Notes
- Tags are created dynamically if they don’t exist.
- Search uses Django’s Q objects for flexible filtering.