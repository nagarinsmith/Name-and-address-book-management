# Name-and-address-book-management
Assignment 05-07 P05

  The following information may be stored in a name and address book:
    -Person: <personID>, <name>, <phone number>, <address>
    -Activity: <activityID>, <personIDs>, <date>, <time>, <description>
  Create an application which allows the user to:
    1. Manage the list of persons and activities. The application must allow the user to add, remove,
  update, and list both persons and activities.
    2. Add/remove activities. Each activity can be performed together with one or several other
  persons, who are already in the user’s address book. Activities must not overlap (not have the
  same starting date/time).
    3. Search for persons or activities. Persons can be searched for using name or phone number.
    Activities can be searched for using date/time or description. The search must work using
  case-insensitive, partial string matching, and must return all matching items.
    4. Create statistics:
      o Activities for a given day/week. List the activities for a given day, in the order of their
    start time, or their date/time.
      o Busiest days. This will provide the list of upcoming days with activities, sorted in
    descending order of the number of activities in each day.
      o Activities with a given person. List all upcoming activities to which a given person will
    participate.
      o List all persons in the address book, sorted in descending order of the number of
    upcoming activities to which they will participate.
    5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation
  performed by the user. Undo/redo operations must cascade and have a memory-efficient
  implementation (no superfluous list copying).
