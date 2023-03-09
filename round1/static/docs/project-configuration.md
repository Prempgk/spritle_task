# ⚙️ Project Configuration

#### Architecture

Model–view–controller is a software design pattern commonly used for developing user interfaces that divide the 
related program logic into three interconnected elements.

Model
The Model component corresponds to all the data-related logic that the user works with. This can represent either the 
data that is being transferred between the View and Controller components or any other business logic-related data. 


View
The View component is used for all the UI logic of the application. For example, the User view will include all 
the UI components such as text boxes, dropdowns, etc. that the final user interacts with.

Controller
Controllers act as an interface between Model and View components to process all the business logic and incoming 
requests, manipulate data using the Model component and interact with the Views to render the final output. 
For example, the user controller will handle all the interactions and inputs from the user View and update
the database using the user Model. The same controller will be used to view the user data.
