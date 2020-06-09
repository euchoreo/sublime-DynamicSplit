DynamicSplit is a [Sublime Text 2][sublime] plugin that tries to create some of the functionality of emacs style Window splitting.

---

Unlike Sublime's default Window splitting feature, this package splits the current Window in half, either vertically or horizontally.
It also duplicates the view of the current file into the newly created view.  

Ctrl+8 - horizontal split
Ctrl+9 - vertical split
Ctrl+0 - undo split (hacked for now)


For example:


    ------------------------
    |          |           |
    |          |           |
    |  A       |    B      |
    |          |           |
    |          |           |
    |          |           |
    |          |           |
    ------------------------
    
    
    
    If you do Ctrl-8 while editing file named "B in the above scenario, you get
    
    ------------------------
    |          |           |
    |          |           |
    |  A       |    B      |
    |          |---------- |
    |          |           |
    |          |    B      |
    |          |           |
    ------------------------
    
    
    If you do Ctrl-9, you get
    
    ------------------------
    |          |     |     |
    |          |     |     |
    |  A       | B   |  B  |
    |          |     |     |
    |          |     |     |
    |          |     |     |
    |          |     |     |
    ------------------------
    
    
    
(tested with 3beta) 


    
