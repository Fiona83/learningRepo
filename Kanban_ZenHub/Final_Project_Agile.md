# Final Kanban Board Project for Agile Course #
**This is a step-by-step document which shows you how to create a Kanban board using ZenHub**

## Step 1: GitHub Repository for the Project ##
1. Sign in or sign up a GitHub account
2. Create a GitHub repository called "agile-final-project" and make it public.

## Step 2: ZenHub Workspace linked to the GitHub Repository ##
3. Create a ZenHub account for free. You may still use ZenHub later for open source project. Alternatively, you can log into ZenHub using your GitHub account.
4. Create a workspace in ZenHub called "Final Project" that is linked to the repository.

## Step 3: Create the Issue Template  ##
5. Create an issue template in GitHub.
   - go to the GitHub and select the repository
   - select 'setting', scroll down to the 'Features' and setup the templates
   - from the dropdown list 'Add templates', select 'Custom template'
   - press 'Preview and edit' button
   - press pencil icon to edit the template
   - copy the template of the user story into it
   ```
     **As a** [role]  
     **I need** [function]  
     **So that** [benefit]  

     ### Details and Assumptions
     * [document what you know]

     ### Acceptance Criteria  

     ` ` `gherkin
     Given [some context]
     When [certain action is taken]
     Then [the outcome of action is observed]
     ` ` `
   ```
   *Here should not have space between the backquote \`, add it just for the markdown syntax*

   - edit the template name to 'User Story' and add some description to it
   - press 'Propose changes' and then 'Commit changes' to save the change. After that, you should now have a new folder in your repository called '.github/ISSUE_TEMPLATES', which will contain your new user story template.

## Step 4: Create the User Stories Using Template ##
6. Create all the user stories
   - select 'new issue'
   - from the 'Template' dropdown, select 'User Story'
   - enter the title for the first story and fill out just the user story section (i.e., As a, I need, So that) for now. For the first step of a Kanban board only the first part of the user story need to be filled out. The second and the third parts should be refined later by the product backlog refinement.
    ```
   These are the requirements from your stakeholders that you should use to create the user stories in ZenHub.
     1. Need the ability to create a product in the catalog.
     2. Need the ability to retrieve a product from the catalog.
     3. Need the ability to update a product in the catalog.
     4. Need the ability to delete a product from the catalog.
     5. Need the ability to "Like" a product in the catalog.
     6. Need the ability to "Dislike" a product in the catalog.
     7. Need the ability to list all products in the catalog.
     8. Need the ability to query a subset of products in the catalog.
     9. Must be hosted in the cloud.
     10. Must have automation to deploy new changes to the cloud.
   ```
## Step 5: Product Backlog Refinement ##
7. According to the assignment, now we are in the phase of **product backlog refinement**.  
   - move the No. 7 and 8 into the 'icebox' (with drag and drop)
   - move the rest of the stories into the 'product backlog'
   - now order the stories in the product backlog according to its priority. (1, 2, 3, 4, 9, 10, 5, & 6)
   - now detail the first 5 user stories in the product backlog with details and fill the acceptance criteria with Gherkin syntax

8. Create a new label in GitHub called 'technical debt'
   - sign into the GitHub account and select the 'agile-final-project' repository
   - in the repository site select 'issue'
   - on the right side select 'label' and then press 'new label'
   - then input the name of the label, give some description and choose a color
   - on the end press 'Create label'. The new label will be seen in the list below.

9. Add labels to the user stories
   - back to the ZenHub workspace
   - press the user story then press the 'Gear' icon on the right side assigned to 'label', set a label for the user story and press the 'X' key to exit the user story. Then a label will appear on the user story.

## Step 6: Srpint Planning ##
10. Now is the time to create a sprint.
   - click the '+' icon on the upper right side and then choose 'Setup sprints for your team'
   - disable the switch labeled 'Move unfinished Issues to the next sprint'. We don't need this kind of automation. The unfinished user story will be refined and move partially to the 'closed' pipeline, so that the team velocity won't be messed up.
   - pick a date range of 2 weeks for the sprint duration and then press 'Create sprints'

11. Setup the sprint plan (a sprint plan meeting should be conducted)
   - conduct a sprint plan meeting and the scrum team should decide the points of each user story
   - select each user story and select the responding points under the label 'Estimate'
   - press the 'Gear' icon assigned to 'Sprint' and select the current sprint date
   - move the user story to the 'Sprint' pipeline

## Step 7: Sprint in Progress ##
12. Now the develop/sprint phase begin. The scrum team member should read the Kanban Board and assign the user story to himself and then begin to develop
   - select the user story
   - press the 'Gear' icon under 'Assignees' and choose your name
   - close the user story and then drag the user story to the 'In progress' pipeline
   - after finish the user story, drag it into the 'Review/QA' pipeline and then assign the next user story to your self and drag it into 'In progress'
   - after the review finished, the user story will be dragged into 'Done' column
   - other stories will keep flowing on the Kanban board from 'Sprint backlog' to 'Review/QA' and finally to 'Done'

13. At the end of the sprint, we can check the burndown chart to see how the process went and how many points we achieved.
   - click the >> icon in the lower left-hand corner to open the side menu bar
   - from the side menu bar, select 'Reports' and then select 'Burndown Report'
   - make sure the current sprint is selected, then select 'Burndown Pipelines' on the right side and choose 'Done' from the dropdown list. Since we keep the user story in 'Done' pipeline until the sprint review, in this way we can see the progress in the burndown chart.

## Step 8: End of the Sprint ##
14. Now at the end of the sprint, a sprint review will be conducted. The product owner will check all the user stories in the 'Done' column and decides if he will accept the stories. If so, the stories will be moved into 'Closed'.

15. For the unfinished user stories in 'In progress', the team has to decide how much of it has been finished. Assume this is a story of 5 points and the team decides 3 points are finished. Then we will redefine this user story into two stories. One has a point of 3 and move it to 'Done' and later 'Closed' column. So that the velocity of the team is accurate. The other part of the story with the left 2 points should be moved back to the top of the product backlog for the next sprint.

16. Thus the current sprint is finished and we can move to the next sprint.
