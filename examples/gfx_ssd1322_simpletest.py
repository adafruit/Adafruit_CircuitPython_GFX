import board
import busio
import displayio
import adafruit_ssd1322
import adafruit_gfx as gfx

displayio.release_displays()

# Initialize screen
d_spi = busio.SPI(board.SCL, board.SDA)
d_cd = board.D6
d_dc = board.D9
d_rst = board.D5

d_bus = displayio.FourWire(d_spi, command=d_dc, chip_select=d_cd,
                           reset=d_rst, baudrate=1000000)

display = adafruit_ssd1322.SSD1322(d_bus, width=256, height=66, colstart=28)

# Create matrix for controlling pixels of screen
bitmap = displayio.Bitmap(display.width, display.height, 2)
palette = displayio.Palette(2)
palette[0] = 0x000000
palette[1] = 0xffffff
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
group = displayio.Group()
group.append(tile_grid)
display.show(group)

# Draw single pixel on screen at coord (x,y) w/ color (0 or 1)
def drawPixel(x,y):
    bitmap[int(x), int(y)] = 1

obj = gfx.GFX(display.width,display.height,drawPixel)
obj.fill_rect(123,27,10,10)
