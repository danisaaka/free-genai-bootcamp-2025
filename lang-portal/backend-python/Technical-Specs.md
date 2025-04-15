# Backend Server Technical Specs

## Business Goal:
* A langauge learning school wants to build a prototype of a learning portal which will act as 3 things
  1. Inventory of possible vocabulary that can be learned
  2. Acts as a Learning Record Store (LRS), providing correct and wrong score on practice vocabulary
  3. A unified launchpad to launch dofferent learning apps

## Technical Requirements
- The backend will be built using Go
- The database will be SQLite3
- The API will be buolt using Gin
- The API will always return JSON

## Database Schema
We will have the folowing tables:
1. words : stored vocabulary words
   1. id integer
   2. spanish_word string
   3. english string
   4. parts json
   
2. word_groups : join table for word and groups many-to-many
   1. id integer
   2. word_id integer
   3. group_id integer
    
3. groups : thematic groups of words
   1. id integer
   2. name string
   
4. study_sessions : records of study sessions grouping word_review_items
   1. id integer
   2. name string
   3. group_id integer
   
5. study_activities : a specific study activity, linking a study session to group
   1. id integer
   2. study_session_id integer
   3. group_id integer
   4. created_at datetime
   
6. word_review_items : a recrd of word practice, determining if the word was correct or not.
   1. id integer
   2. study_session_id integer
   3. word_id integer
   4. correct boolean
   5. created_at datetime

### API Endpoints
- GET /words
- GET /words/:id
- GET /groups
- GET /groups/:id
- GET /groups/:id/words



