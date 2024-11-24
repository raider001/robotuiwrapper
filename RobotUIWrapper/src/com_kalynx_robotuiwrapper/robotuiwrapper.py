from robot.libraries.Remote import Remote

class RobotUIWrapper(): 

    _remote: Remote 
    def __init__(self, url: str ="", port: int=0):
 
        try:
            self._remote = Remote(f"http://{url}:{str(port)}/")
        except Exception as e:
            print(e) 

    def set_primary_display_reference(self, referenceName: str):
        self._remote.run_keyword("setPrimaryDisplayReference", [referenceName], None) # type: ignore

    def set_display_by_id(self, displayId: int):
        self._remote.run_keyword("setDisplayById", [displayId], None) # type: ignore

    def set_display_reference(self, origin_reference: str, relative_state: str, new_reference: str):
        self._remote.run_keyword("setDisplayReference", [origin_reference,relative_state,new_reference], None) # type: ignore

    def set_monitored_area(self, x: int, y: int, width: int, height:int):
        self._remote.run_keyword("setMonitoredArea", [x,y,width,height], None) # type: ignore
    
    def reset_monitored_area(self):
        self._remote.run_keyword("resetMonitoredArea", [], None) # type: ignore

    def set_monitored_area_for_display_Id(self, display_id: int, x: int, y: int, width: int, height: int):
        self._remote.run_keyword("setMonitoredAreaForDisplayId", [display_id,x,y,width,height], None) # type: ignore

    def set_monitored_area_for_display(self, display_reference: str, x: int, y: int, width: int, height: int):
        self._remote.run_keyword("setMonitoredAreaForDisplay", [display_reference,x,y,width,height], None) # type: ignore