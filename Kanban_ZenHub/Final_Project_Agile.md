# Final Kanban Board Project for Agile Course #
**This is a step-by-step document which shows you how to create a Kanban board using ZenHub**

## Step 1: GitHub Repository for the Project
1. Sign in or sign up a GitHub account
2. Create a GitHub repository called "agile-final-project" and make it public.
3. Create a ZenHub account for free. You may still use ZenHub later for open source project. Alternatively, you can log into ZenHub using your GitHub account.
4. Create a workspace in ZenHub called "Final Project" that is linked to the repository.
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
   *Here should not have space between the backtick \`, add it just for the markdown syntax*

   - edit the template name to 'User Story' and add some description to it
   - press 'Propose changes' and then 'Commit changes' to save the change. After that, you should now have a new folder in your repository called '.github/ISSUE_TEMPLATES', which will contain your new user story template.

6. Create all the user stories
   - select 'new issue'
   - from the 'Template' dropdown, select 'User Story'
   - enter the title for the first story and fill out just the user story section (i.e., As a, I need, So that) for now. For the first step of a Kanban board only the first part of the user story need to be filled out. The second and the third parts should be refined later by the Backlog refinement.
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

7. According to the assignment, now we are in the phase of **backlog refinement**.  
   - move the No. 7 and 8 into the 'icebox' (with drag and drop)
   - move the rest of the stories into the 'Backlog'
   - now order the stories in the backlog according to its priority. (1, 2, 3, 4, 9, 10, 5, & 6)
   
