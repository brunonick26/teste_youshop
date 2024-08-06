Models


Account
name: The name of the account.
created: Timestamp when the account was created.
active: Boolean indicating if the account is active.
users: Many-to-many relationship with User.

Profile
user: One-to-one relationship with User.
about: Additional information about the user.
joined: Timestamp when the profile was created.

Tree
name: Common name of the tree.
scientific_name: Scientific name of the tree.

PlantedTree
age: Age of the planted tree.
planted_at: Timestamp when the tree was planted.
user: Foreign key to User indicating who planted the tree.
tree: Foreign key to Tree indicating the type of tree.
account: Foreign key to Account indicating the associated account.
location_lat: Latitude of the planting location.
location_lon: Longitude of the planting location.


--------------------------------------------------------



Views


user_planted_trees(request)
Description: Displays all trees planted by the currently authenticated user.
Method: GET
Template: user_planted_trees.html
planted_tree_detail(request, tree_id)
Description: Shows details of a specific planted tree identified by tree_id.
Method: GET
Template: planted_tree_detail.html

add_planted_tree(request)
Description: Provides a form for users to add a new planted tree.
Method: GET, POST
Template: add_planted_tree.html

account_planted_trees(request)
Description: Displays all trees planted under the accounts associated with the current user.
Method: GET
Template: account_planted_trees.html
UserPlantedTreesView
Description: API view to list all trees planted by the authenticated user.
Method: GET
Serializer: PlantedTreeSerializer
Permissions: Authenticated users only


--------------------------------------------------


Admin Configuration


AccountAdmin
List Display: Shows name, created, and active.
Search Fields: Search by name.
List Filter: Filter by active.

TreeAdmin
List Display: Shows name and scientific_name.

PlantedTreeAdmin
List Display: Shows tree, user, age, planted_at, account, location_lat, location_lon.
List Filter: Filter by tree, user, and account.
Search Fields: Search by tree__name and user__username.
Queryset Optimization: Uses select_related to optimize queries.
User Name: Displays the username of the user who planted the tree.
