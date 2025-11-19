from typing_extensions import override
from comfy_api.latest import ComfyExtension, io
from math import sqrt

class AspectSize3_mc(io.ComfyNode):
    """
    Calcola larghezza e altezza rispetto a megapixel, ratio e multiplo, con eventuale swap.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="AspectSize3_mc",
            display_name="Aspect ratio universal v3",
            category="MC nodi",
            inputs=
            [
                io.Float.Input
                ("megapixel", default=1.0, min=0.1,max=100.0, step=0.1, display_mode=io.NumberDisplay.number),
                
                io.Int.Input
                ("aspect_ratio_width", default=1, min=1, max=100, step=1, display_mode=io.NumberDisplay.number),
                
                io.Int.Input
                ("aspect_ratio_height", default=1, min=1, max=100, step=1,display_mode=io.NumberDisplay.number),
                
                io.Boolean.Input
                ("swap_hw", default=False ),      
                
                io.Combo.Input
                ("multiple_of", options=["2", "4", "8", "16", "32", "64"])
            ],
            outputs=[
                io.Int.Output(display_name="Width"),
                io.Int.Output(display_name="Height"),
            ],
        )

    @classmethod
    def execute(cls, megapixel, aspect_ratio_width, aspect_ratio_height, multiple_of, swap_hw) -> io.NodeOutput:
        def round_to_multiple(val, multiple):
            return round(val / multiple) * multiple

        base_pixel = 1024 * megapixel
        downscale_factor = int(multiple_of)
        pixels = base_pixel * base_pixel
        aspect_ratio_decimal = aspect_ratio_width / aspect_ratio_height

        width = sqrt(pixels * aspect_ratio_decimal)
        height = pixels / width

        rounded_width = round_to_multiple(width, downscale_factor)
        rounded_height = round_to_multiple(height, downscale_factor)

        while rounded_width * rounded_height > pixels:
            rounded_width -= downscale_factor
            rounded_height = round_to_multiple(sqrt(pixels * aspect_ratio_height / aspect_ratio_width), downscale_factor)

        if swap_hw:
            rounded_height, rounded_width = rounded_width, rounded_height

        return io.NodeOutput(int(rounded_width), int(rounded_height))
        
        
class LTXVsize_mc(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="LTXVsize_mc",
            display_name="LTXV resolutions mc",
            category="MC nodi/Ltxv",
            inputs=
            [
                io.Combo.Input("resolutions", default="768x512",
                options=
                    [
                    "1216x704",
                    "1088x704",
                    "1056x640",
                    "992x608",
                    "896x608",
                    "896x544",
                    "832x544",
                    "800x512",
                    "768x512",
                    "800x480",
                    "736x480",
                    "704x480",
                    "704x448",
                    "672x448",
                    "640×416",
                    "672х384",
                    "640x384",
                    "608×384",
                    "576x384",
                    "608x352",
                    "576x352",
                    "544x352"               
                    ]),
                    
                io.Boolean.Input
                ("swap_hw", default=False )
            ],
                
            outputs=[
                io.Int.Output(display_name="Width"),
                io.Int.Output(display_name="Height"),
                ],
            )
        
    @classmethod
    def execute(cls,resolutions, swap_hw) -> io.NodeOutput:
        larghezza, altezza = map(int, resolutions.split('x'))
        
        if swap_hw:
            larghezza,  altezza = altezza, larghezza
        

        return io.NodeOutput(larghezza, altezza)
    

    
class Wan_frames_mc(io.ComfyNode):
    
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="Wan frames mc",
            display_name="Wan video frames",
            category="MC nodi/Wan",
            inputs=
            [
                io.Int.Input
                ("frames", default=81, min=1, max=4096, step=4, display_mode=io.NumberDisplay.number)          
            ],
            outputs=
            [
                io.Int.Output(display_name="frames")
            ],
        )
    @classmethod
    def execute(cls,frames) -> io.NodeOutput:
    
        return io.NodeOutput(frames)
        
        
        
    
class MCAspectSizeExtension(ComfyExtension):
    @override
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [
            AspectSize3_mc,
            LTXVsize_mc,
            Wan_frames_mc,
        ]

async def comfy_entrypoint() -> MCAspectSizeExtension:
    return MCAspectSizeExtension()
