from robot.libraries.Remote import Remote
from robot.api.deco import keyword, library
 
@library(scope='GLOBAL', version='1.0.1')
class RobotUIWrapper(): 

    _remote: Remote 
    def __init__(self, url: str ="", port: int=0):
 
        try:
            self._remote = Remote(f"http://{url}:{str(port)}/")
        except Exception as e:
            print(e) 

    # Display Keywords
    @keyword
    def set_primary_display_reference(self, referenceName: str) -> None:
        self._remote.run_keyword("setPrimaryDisplayReference", [referenceName], None) # type: ignore

    @keyword
    def set_display_by_id(self, displayId: int) -> None:
        self._remote.run_keyword("setDisplayById", [displayId], None) # type: ignore

    @keyword
    def set_display_reference(self, origin_reference: str, relative_state: str, new_reference: str) -> None:
        self._remote.run_keyword("setDisplayReference", [origin_reference,relative_state,new_reference], None) # type: ignore

    @keyword
    def set_monitored_area(self, x: int, y: int, width: int, height:int) -> None:
        self._remote.run_keyword("setMonitoredArea", [x,y,width,height], None) # type: ignore
    
    @keyword
    def reset_monitored_area(self) -> None:
        self._remote.run_keyword("resetMonitoredArea", [], None) # type: ignore

    @keyword
    def set_monitored_area_for_display_Id(self, display_id: int, x: int, y: int, width: int, height: int) -> None:
        self._remote.run_keyword("setMonitoredAreaForDisplayId", [display_id,x,y,width,height], None) # type: ignore

    @keyword
    def reset_monitored_area_for_id(self, display_id: int) -> None:
        self._remote.run_keyword("resetMonitoredAreaForId", [display_id], None)

    @keyword
    def set_monitored_area_for_display(self, display_reference: str, x: int, y: int, width: int, height: int) -> None:
        self._remote.run_keyword("setMonitoredAreaForDisplay", [display_reference,x,y,width,height], None) # type: ignore

    @keyword
    def reset_monitored_area_for_display(self, display_reference: str) -> None:
        self._remote.run_keyword("resetMonitoredAreaForDisplay", [display_reference], None)

    @keyword
    def set_monitored_display(self, display: str) -> None:
        self._remote.run_keyword("setMonitoredDisplay", [display], None)

    @keyword
    def get_selected_display_dimensions(self) -> dict[str, int]:
        return self._remote.run_keyword("getSelectedDisplayDimensions", [], None) # type: ignore

    @keyword
    def get_selected_display_monitored_area(self) -> dict[str, int]:
        return self._remote.run_keyword("getSelectedDisplayMonitoredArea", [], None) # type: ignore

    @keyword
    def get_display_dimensions(self, display: str) -> dict[str, int]:
        return self._remote.run_keyword("getDisplayDimensions", [display], None) # type: ignore
    
    @keyword
    def get_display_monitored_area(self, display: str) -> dict[str, int]:
        return self._remote.run_keyword("getDisplayMonitoredArea", [display], None) # type: ignore

    # keyboard keywords
    @keyword
    def type(self, message: str) -> None:
        self._remote.run_keyword("type", [message], None)

    @keyword
    def hold_key(self, key: str) -> None:
        self._remote.run_keyword("holdKey", [key], None)

    @keyword
    def release_key(self, key: str) -> None:
        self._remote.run_keyword("releaseKey", [key], None)

    @keyword
    def press_keys(self, key1: str, key2: str | None = None, key3: str | None = None, key4: str | None = None, key5: str | None = None) -> None:
        vals: dict [str, str | None] = {"key2": key2, "key3": key3, "key4": key4, "key5": key5}
        self._remote.run_keyword("pressKeys", [key1], self._filtered(vals))

    # Mouse keywords
    @keyword
    def move_mouse_to(self, x: int | None = None, y: int | None = None, image: str | None = None, display: str | None = None, window: str | None = None) -> None:
        vals: dict = {"x": x, "y": y, "image": image, "display": display, "window": window}
        self._remote.run_keyword("moveMouseTo", [], self._filtered(locals()))

    def _filtered(self, args: dict) -> dict:
        return {k: v for k, v in args.items() if v is not None}