import math

class McCascadeRes:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "aspect_ratio": (
                    [
                        "1:1 1024x1024",
                        "2:1 2048x1024",
                        "2:1 1024x512",
                        "1:2 512x1024",
                        "2:3 1360x2048",
                        "3:2 2048x1360",
                        "4:3 2048x1536",
                        "4:3 3072x2304",
                        "3:4 1536x2048",
                        "3:4 2304x3072",
                        "16:9 2048x1152",
                        "16:9 3072x1728",
                        "9:16 1152x2048",
                        "9:16 1728x3072",
                    ],
                ),
            }
        }

    RETURN_TYPES = ("STRING", "INT", "INT")
    RETURN_NAMES = ("ratio", "width", "height")

    FUNCTION = "prova_mc"
    CATEGORY = "MC nodi/DEPRECATED"

    def prova_mc(self,  aspect_ratio):
        width, height = 1024, 1024

        if aspect_ratio == "1:1 1024x1024":
            width, height = 1024, 1024
        elif aspect_ratio == "2:1 2048x1024":
            width, height = 2048, 1024
        elif aspect_ratio == "2:1 1024x512":
            width, height = 1024, 512
        elif aspect_ratio == "1:2 512x1024":
            width, height = 512, 1024
        elif aspect_ratio == "2:3 1360x2048":
            width, height = 1360, 2048 
        elif aspect_ratio == "3:2 2048x1360":
            width, height = 2048, 1360  
        elif aspect_ratio == "4:3 2048x1536":
            width, height = 2048, 1536
        elif aspect_ratio == "3:4 1536x2048":
            width, height = 1536, 2048
        elif aspect_ratio == "3:4 2304x3072":
            width, height = 2304, 3072
        elif aspect_ratio == "4:3 3072x2304":
            width, height = 3072,2304
        elif aspect_ratio == "16:9 2048x1152":
            width, height = 2048, 1152
        elif aspect_ratio == "16:9 3072x1728":
            width, height = 3072, 1728
        elif aspect_ratio == "9:16 1152x2048":
            width, height = 1152, 2048
        elif aspect_ratio == "9:16 1728x3072":
            width, height = 1728, 3072
        return (aspect_ratio, width, height)




class McCascadeRes2:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "width": ("INT", {
                    "default": 1024,
                    "step": 2,
                    "min": 256,
                    "max": 6000,
                }),
                "height": ("INT", {
                    "default": 1024,
                    "step": 2,
                    "min": 256,
                    "max": 6000,
                }),
                "resolution": (
                    [
                        "Custom",
                        "1:1 1024x1024",
                        "2:1 2048x1024",
                        "2:1 1024x512",
                        "3:2 2048x1360",
                        "4:3 2048x1536",
                        "4:3 3072x2304",
                        "16:9 2048x1152",
                        "16:9 3072x1728",
                    ],
                ),
                "swap_dimension": (
                    "BOOLEAN", {"default": False, "label_on": "Yes", "label_off": "No"}
                    )
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")

    FUNCTION = "prova_mc_2"
    CATEGORY = "MC nodi/DEPRECATED"

    def prova_mc_2(self,  resolution, swap_dimension, width, height):
        #width, height = 1024, 1024
        if resolution == "Custom":
            width, height = width, height
        elif resolution == "1:1 1024x1024":
            width, height = 1024, 1024
        elif resolution == "2:1 2048x1024":
            width, height = 2048, 1024
        elif resolution == "2:1 1024x512":
            width, height = 1024, 512
        elif resolution == "3:2 2048x1360":
            width, height = 2048, 1360
        elif resolution == "4:3 2048x1536":
            width, height = 2048, 1536
        elif resolution == "4:3 3072x2304":
            width, height = 3072,2304
        elif resolution == "16:9 2048x1152":
            width, height = 2048, 1152
        elif resolution == "16:9 3072x1728":
            width, height = 3072, 1728
            
            
        a = width
        b = height
        
        if swap_dimension:
            width = b
            height = a
            
        return (width, height)
        
       
class McCascadeRatio:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "max_size": ("INT", {
                    "default": 1024,
                    "step": 2,
                    "min": 512,
                    "max": 6000,
                    }
                ),
                "aspect_ratio": (
                    [
                        "1:1",
                        "1:2",
                        "2:3",
                        "3:4",
                        "5:8",
                        "9:16",
                    ],
                ),
                

                "swap_dimension": (
                    "BOOLEAN", {"default": False, "label_on": "Yes", "label_off": "No"}
                    )
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")

    FUNCTION = "prova_mc_3"
    CATEGORY = "MC nodi/DEPRECATED"

    def prova_mc_3(self, max_size, aspect_ratio, swap_dimension):
        
        size = max_size
        
        def calc_ratio(aspect_ratio, size):
           
            height = size
            width = size           
            s = aspect_ratio.split(":")
            s1 = int(s[0])
            s2 = int(s[1])
            width = int(size*s1/s2)
         
            return (width, height)
                   
        width, height = calc_ratio(aspect_ratio, size)

        a = width
        b = height
        
        if swap_dimension:
            width = b
            height = a
            
        return (width, height)

        
        



class AspectSize_mc:

    # original https://github.com/MushroomFleet/DJZ-Nodes/blob/main/AspectSize.py
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_type": (["SD","SDXL","Cascade"],),
                "aspect_ratio_width": ("INT",{
                    "default": 1,
                    "step":1,
                    "display": "number"
                }),
                "aspect_ratio_height": ("INT",{
                    "default": 1,
                    "step":1,
                    "display": "number"
                }),
                "multiple_of": (
                    [
                        "2",
                        "4",
                        "8",
                        "16",
                        "64",
                    ],
                )
            }
        }

    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("Width", "Height", )

    FUNCTION = "run"

    CATEGORY = "MC nodi/DEPRECATED"

    def run(self, model_type, aspect_ratio_width, aspect_ratio_height,  multiple_of):
        # Define the total pixel counts for SD and SDXL
        total_pixels = {
            'SD': 512 * 512,
            'SDXL': 1024 * 1024,
            'Cascade': 2048 * 2048
        }
        
        downscale_factor = int(multiple_of)
    
        # Calculate the number of total pixels based on model type
        pixels = total_pixels.get(model_type, 0)
    
        # Calculate the aspect ratio decimal
        aspect_ratio_decimal = aspect_ratio_width / aspect_ratio_height
    
        # Calculate width and height
        width = math.sqrt(pixels * aspect_ratio_decimal)
        height = pixels / width
    
        # Adjust the width and height to be divisible by the downscale_factor
        width = math.ceil(width / downscale_factor) * downscale_factor
        height = math.ceil(height / downscale_factor) * downscale_factor
    
        # Return the width and height as a tuple of integers
        return (int(width), int(height))        


class AspectSize2_mc:

    
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "megapixel": ("FLOAT",{
                    "default": 1,
                    "step":0.1,
                    "display": "number"
                }),
                "aspect_ratio_width": ("INT",{
                    "default": 1,
                    "step":1,
                    "display": "number"
                }),
                "aspect_ratio_height": ("INT",{
                    "default": 1,
                    "step":1,
                    "display": "number"
                }),
                "multiple_of": (
                    [
                        "2",
                        "4",
                        "8",
                        "16",
                        "32",
                        "64",
                    ],
                )
            }
        }

    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("Width", "Height", )

    FUNCTION = "run"

    CATEGORY = "MC nodi/DEPRECATED"
   

    def run(self, megapixel, aspect_ratio_width, aspect_ratio_height,  multiple_of):
    
        def arrotonda_a_multiplo(valore, multiplo):
            #Arrotonda il valore al multiplo più vicino.
            return round(valore / multiplo) * multiplo
        
        # Define the total pixel counts for SD and SDXL
        base_pixel = 1024 * megapixel
        
        
        downscale_factor = int(multiple_of)
    
        # Calculate the number of total pixels based on megapixel
        pixels = base_pixel * base_pixel
        
        # Calculate the aspect ratio decimal
        aspect_ratio_decimal = aspect_ratio_width / aspect_ratio_height
    
        # Calculate width and height
        width = math.sqrt(pixels * aspect_ratio_decimal)
        height = pixels / width
    
        # Adjust the width and height to be divisible by the downscale_factor
        #width = math.ceil(width / downscale_factor) * downscale_factor
        #height = math.ceil(height / downscale_factor) * downscale_factor
        
        # Arrotondiamo alle dimensioni più vicine al multiplo specificato
        larghezza_arrotondata = arrotonda_a_multiplo(width, downscale_factor)
        altezza_arrotondata = arrotonda_a_multiplo(height, downscale_factor)
        
        # Verifica se il numero di pixel rimane all'interno del limite dei megapixel forniti
        while larghezza_arrotondata * altezza_arrotondata > pixels:
            # Riduciamo leggermente le dimensioni per rispettare i megapixel
            larghezza_arrotondata -= downscale_factor
            altezza_arrotondata = arrotonda_a_multiplo(math.sqrt(pixels * aspect_ratio_height / aspect_ratio_width), downscale_factor)
    
        # Return the width and height as a tuple of integers
        return (int(larghezza_arrotondata), int(altezza_arrotondata))  
        
        
class AspectSize3_mc:

    
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "megapixel": ("FLOAT",{
                    "default": 1,
                    "step":0.1,
                    "display": "number"
                }),
                "aspect_ratio_width": ("INT",{
                    "default": 1,
                    "step":1,
                    "display": "number"
                }),
                "aspect_ratio_height": ("INT",{
                    "default": 1,
                    "step":1,
                    "display": "number"
                }),
                "swap_hw": ("BOOLEAN", {"default": False}),
                "multiple_of": (
                    [
                        "2",
                        "4",
                        "8",
                        "16",
                        "32",
                        "64",
                    ],
                )
            }
        }

    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("Width", "Height", )

    FUNCTION = "run"

    CATEGORY = "MC nodi"
   

    def run(self, megapixel, aspect_ratio_width, aspect_ratio_height,  multiple_of, swap_hw):
    
        def arrotonda_a_multiplo(valore, multiplo):
            #Arrotonda il valore al multiplo più vicino.
            return round(valore / multiplo) * multiplo
        
        # Define the total pixel counts for SD and SDXL
        base_pixel = 1024 * megapixel
        
        
        downscale_factor = int(multiple_of)
    
        # Calculate the number of total pixels based on megapixel
        pixels = base_pixel * base_pixel
        
        # Calculate the aspect ratio decimal
        aspect_ratio_decimal = aspect_ratio_width / aspect_ratio_height
    
        # Calculate width and height
        width = math.sqrt(pixels * aspect_ratio_decimal)
        height = pixels / width
    
        # Adjust the width and height to be divisible by the downscale_factor
        #width = math.ceil(width / downscale_factor) * downscale_factor
        #height = math.ceil(height / downscale_factor) * downscale_factor
        
        # Arrotondiamo alle dimensioni più vicine al multiplo specificato
        larghezza_arrotondata = arrotonda_a_multiplo(width, downscale_factor)
        altezza_arrotondata = arrotonda_a_multiplo(height, downscale_factor)
        
        # Verifica se il numero di pixel rimane all'interno del limite dei megapixel forniti
        while larghezza_arrotondata * altezza_arrotondata > pixels:
            # Riduciamo leggermente le dimensioni per rispettare i megapixel
            larghezza_arrotondata -= downscale_factor
            altezza_arrotondata = arrotonda_a_multiplo(math.sqrt(pixels * aspect_ratio_height / aspect_ratio_width), downscale_factor)
        
        if swap_hw == True:
            altezza_arrotondata, larghezza_arrotondata = larghezza_arrotondata, altezza_arrotondata
    
        # Return the width and height as a tuple of integers
        return (int(larghezza_arrotondata), int(altezza_arrotondata))  
        
NODE_CLASS_MAPPINGS = {
    # "McCascadeRes": McCascadeRes,
    # "McCascadeRes2": McCascadeRes2,
    # "McCascadeRatio": McCascadeRatio,
    # "AspectSize_mc": AspectSize_mc,
    # "AspectSize2_mc": AspectSize2_mc,
    "AspectSize3_mc": AspectSize3_mc
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # "McCascadeRes": "Cascade resolution by MC",
    # "McCascadeRes2": "Cascade resolution V2 by MC",
    # "McCascadeRatio": "Image aspect ratio calculator by MC",
    # "AspectSize_mc": "Aspect ratio universal",
    # "AspectSize2_mc": "Aspect ratio universal v2",
    "AspectSize3_mc": "Aspect ratio universal v3"

}
