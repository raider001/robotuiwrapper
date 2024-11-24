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
    def move_mouse(self, x_relative: int, y_relative: int) -> None:
        self._remote.run_keyword("moveMouse", [x_relative, y_relative], None)

    @keyword
    def move_mouse_to(self, x: int | None = None, y: int | None = None, image: str | None = None, display: str | None = None, window: str | None = None) -> None:
        self._remote.run_keyword("moveMouseTo", [], self._filtered(locals()))

    @keyword
    def click(self, button: str = "LEFT", times: int = 1, x: int | None = None, y: int | None = None, image: str | None = None, display: str | None = None, window: str | None = None) -> None:
        self._remote.run_keyword("click", [], self._filtered(locals()))

    @keyword
    def press_mouse_button(self, button: str) -> None:
        self._remote.run_keyword("pressMouseButton", [button], None)

    @keyword
    def release_mouse_button(self, button: str) -> None:
        self._remote.run_keyword("releaseMouseButton", [button], None)

    @keyword
    def get_mouse_position(self) -> dict[str, int]:
        return self._remote.run_keyword("getMousePosition", [], None) # type: ignore

    @keyword
    def mouse_scroll(self, scroll_arount: int) -> None:
        self._remote.run_keyword("mouseScroll", [scroll_arount], None)
    
    @keyword
    def set_mouse_move_speed(self, speed: int) -> None:
        self._remote.run_keyword("setMouseMoveSpeed", [speed], None)

    #OCR
    @keyword
    def get_words(self, x: int | None = None, y: int | None = None, display: str | None = None, window: str | None = None) -> list[dict]:
        return self._remote.run_keyword("getWords", [], self._filtered(locals())) # type: ignore

    @keyword
    def get_text(self, x: int | None = None, y: int | None = None, display: str | None = None, window: str | None = None) -> str:
        return self._remote.run_keyword("getText", [], self._filtered(locals())) # type: ignore
    
    @keyword
    def set_ocr_mode(self, mode: str) -> None:
        self._remote.run_keyword("setOcrMode", [mode], None)

    @keyword
    def set_page_seg_mode(self, mode: str) -> None:
        self._remote.run_keyword("setPageSegMode", [mode], None)

    @keyword
    def set_data_path(self, path: str) -> None:
        self._remote.run_keyword("setDataPath", [path], None)

    #Screen Keywords
    @keyword
    def verify_image_exists(self, image_name: str, min_match_score: float, wait_time: int = 200) -> None:
        self._remote.run_keyword("verifyImageExists", [image_name, min_match_score, wait_time], None)

    @keyword
    def verify_image_does_not_exist(self, image_name: str, min_match_score: float, wait_time: int = 200) -> None:
        self._remote.run_keyword("verifyImageDoesNotExist", [image_name, min_match_score, wait_time], None)

    @keyword
    def verify_image_exists_on_display(self, image_name: str, display_name: str, min_match_score: float, wait_time: int = 200) -> None:
        self._remote.run_keyword("verifyImageExistsOnDisplay", [image_name, display_name, min_match_score, wait_time], None)

    @keyword
    def verify_image__does_not_exist_on_display(self, image_name: str, display_name: str, min_match_score: float, wait_time: int = 200) -> None:
        self._remote.run_keyword("verifyImageDoesNotExistOnDisplay", [image_name, display_name, min_match_score, wait_time], None)

    @keyword
    def verify_image_exists_on_window(self, image_name: str, window_name: str, min_match_score: float, wait_time: int = 200) -> None:
        self._remote.run_keyword("verifyImageExistsOnWindow", [image_name, window_name, min_match_score, wait_time], None)

    @keyword
    def verify_image__does_not_exist_on_window(self, image_name: str, window_name: str, min_match_score: float, wait_time: int = 200) -> None:
        self._remote.run_keyword("verifyImageDoesNotExistOnWindow", [image_name, window_name, min_match_score, wait_time], None)

    @keyword
    def get_image_bounds(self, image: str, minMatchScore: float = -1, waitTime: int = 200, display: str | None = None, window: str | None = None) -> None:
        vals: dict = self._filtered(locals())
        vals.pop("image")
        self._remote.run_keyword("getImageBounds", [image], vals)

    #Settings
    @keyword
    def set_timeout_time(self, timeout_time: int) -> None:
        self._remote.run_keyword("setTimeoutTime", [timeout_time], None)

    def get_image_paths(self) -> list[str]:
        return self._remote.run_keyword("getImagePaths", [], None) # type: ignore

    @keyword
    def set_poll_rate(self, poll_rate: int) -> None:
        self._remote.run_keyword("setPollRate", [poll_rate], None)

    @keyword
    def set_result_path(self, path: str) -> None:
        self._remote.run_keyword("setResultPath", [path], None)

    @keyword
    def set_match_percentage(self, min_similarity: float) -> None:
        self._remote.run_keyword("setMatchPercentage", [min_similarity], None)

    @keyword
    def add_image_location(self, image_location: str) -> None:
        self._remote.run_keyword("addImageLocation", [image_location], None)

    @keyword
    def set_keystroke_speed(self, delay_speed: int) -> None:
        self._remote.run_keyword("setKeystrokeSpeed", [delay_speed], None)

    def _filtered(self, args: dict) -> dict:
        return {k: v for k, v in args.items() if v is not None}