"""
FileView split version 0.1 - some features missing

by James Liang (AbundantDotLife.com)
 this is meant to split files like emacs.  It cuts your current
 screen in half and automatically populates the new split with another view
 of your current file
 """
import sublime
import copy;
import sublime_plugin
g_hack_splitHistory = [];
class FileviewSplitCommand(sublime_plugin.WindowCommand):        
    def doSplit(self,i0,i1,colOrRow):
        global g_hack_splitHistory;
        newLayout = self.window.get_layout();
        g_hack_splitHistory.append(copy.deepcopy(newLayout));
        curIdx = self.window.active_group();
        oldBlock = newLayout['cells'][curIdx];
                                
        oldWidth=oldBlock[i1]-oldBlock[i0]
        if oldWidth==1:
            oldCoords = newLayout[colOrRow];            
            oldCoordVal = oldCoords[oldBlock[i0]];
            coordDist = oldCoords[oldBlock[i1]]-oldCoordVal;            
            newCoordIndex= oldBlock[i1]
            oldCoords.insert(newCoordIndex,  oldCoordVal+coordDist/2);           
            for theCell in newLayout['cells']:
                if theCell[i0]>=newCoordIndex:            
                    theCell[i0]+=1;
                
                if theCell[i1]>=newCoordIndex:                    
                    theCell[i1]+=1;
                    
        #print("new coords:"+str(newLayout));            
        oldWidth=oldBlock[i1]-oldBlock[i0]
        newBlock = oldBlock[:];
        newMid = oldWidth/2+oldBlock[i0];
        oldBlock[i1] = newMid;
        newBlock[i0]=newMid;
        newLayout['cells'].insert(curIdx+1,newBlock);        
        print("new layout:"+str(newLayout));        
        self.window.set_layout(newLayout);        
        
        # vertical split means a new column, but same rows
        
        self.window.run_command('clone_file')
        self.window.run_command('move_to_group', {"group": curIdx+1})

    def splitVertical(self):
        self.doSplit(0,2,"cols")        
    def splitHorizontal(self):        
        self.doSplit(1,3,"rows")
    def unsplit(self):        
        self.window.run_command('close') # reverse the clone file        
        global g_hack_splitHistory;
        if len(g_hack_splitHistory)<1:
            return;
        
        hackPrev = g_hack_splitHistory[-1]
        print("new layout:"+str(hackPrev));
        self.window.set_layout(hackPrev);
        del g_hack_splitHistory[-1]
        # TODO: do this for real.  anyone else reading this is welcome :)
        
    def run(self,splitDir):
        #print("Let's split (param="+splitDir+")"+str(self.window.active_group())+"\n");
        print("Old layout:"+str(self.window.get_layout()));
        # focus_group

        if (splitDir=="v"):
            self.splitVertical();
        elif (splitDir=='h'):
            self.splitHorizontal();
        else:
            self.unsplit();
