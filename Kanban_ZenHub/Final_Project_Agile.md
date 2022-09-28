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
   <!-- Here should not have space between ``` -->
   
   - edit the template name to 'User Story' and add some description to it
   - press 'Propose changes' and then 'Commit changes' to save the change. After that, you should now have a new folder in your repository called '.github/ISSUE_TEMPLATES', which will contain your new user story template.
