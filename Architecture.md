# Program Organization

[Diagram](https://docs.google.com/drawings/d/1TUbR1T9_B6WfCYGCicQKSH8qjjn9X43obXvX7nI2Zt0/edit?usp=sharing)

[In-Depth Description](https://docs.google.com/document/d/1FA4I41uiwIgKB1tqMOyXJnYcXf9lOJA9ilg85u-RlCQ/edit?usp=sharing)

# Major Classes

[Diagram](https://drive.google.com/file/d/1NqDpVnVrYHD-SCcfD8B3sug9F6vCOEDB/view?usp=sharing)

[Class Descriptions](https://docs.google.com/document/d/1n7qOdXY2i-A0tg3gyodm_GhEKr2NwJpASYI_jcA4ivU/edit?usp=sharing)

# Data Design

[Database Schemas](https://docs.google.com/document/d/1E3cikrkHcXE-PxppXv7h1ovNXgMTyPIy-kNyr7d9zvQ/edit?usp=sharing)

# Business Rules

The software needs to follow the rules of DnD to allow users to create characters and perform actions that are relevant to the DnD universe.

# User Interface Design

[Diagram](https://drive.google.com/file/d/1WVBX7nz-pJ9zIM4E0k-gchcGm-XRzGoa/view?usp=sharing)

[User Stories](https://docs.google.com/document/d/1NZeqT6CyVsro24gmO0C-WLZbVaCbVZdCNq2G_n58w24/edit?usp=sharing)

# Resource Management

Resource Management is not a concern of this project as we are working with simple operations on a database instead of complex algorithms with expensive computation costs.

# Security

Security for this project will be handled by django and the use of user profiles requiring a username and password. Accessing an account and the characters/campaigns contained within will require authentication.

# Performance

Performance is not a concern of this project.

# Scalability

Because we are creating a web page style project, if we need to add things in the future to expand on the system we can easily add new pages and features that can acheive this.

# Interoperability

Interoperability will be handled by django as it standardizes the ways in which things are done, making information exchange easy.

# Internationalization/Localization

Internationalization and Localization are not a concern for this project. It will designed like it is being pushed to American markets.

# Input/Output

# Error Processing

Error processing for this project will be done by sending error messages and will be handled by Django.

# Fault Tolerance

Tolerance for faults will be minimal. If a field is incorrect or void, we will simply reject the field and require the user fill it in properly before allowing them to continue.

# Architectural Feasibility

The architecture is feasible for what we are trying to accomplish as we simply need an interface for a database to hold the user's data.

# Overengineering

As mentioned in error processing and fault tolerance, we will not be allowing errors to be passed through the system. Therefore, the system will lean heavily towards doing the simplest thing possible.

# Build-vs-Buy Decisions

Third Party Systems

  * Crispy Forms - Renders forms for easier readability of forms
  
  * Bootstrap 4 - This allows us to easily create attractive HTML for the site without having to manually write all HTML
  
  * Pillow - Image handling library
  

# Reuse

We are using Bootstrap and Django to create a lot of what we are working on, but we are creating the code and other components from the ground up. Thus, this is not a concern for the project.

# Change Strategy

To handle changes to the system, we will meet with the team, expand the application, and implement the new features using a test-driven delevopment approach.
