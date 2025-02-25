from core.assets.assets import Assets
from core.utils.colors import Colors
from core.utils.settings import Settings

import pygame


class Itembar:
    def __init__(self):
        self.game = None

    def draw(self):
        backgrounditembar = pygame.Rect(Settings.Game.WIDTH / 2 - 320, Settings.Game.HEIGHT - 150, 640, 80)
        pygame.draw.rect(self.game.screen, (75, 75, 75), backgrounditembar)

        if self.game.player.inventory.selectedslot == 0:
            slot1 = pygame.Rect(Settings.Game.WIDTH / 2 - 320, Settings.Game.HEIGHT - 150, 80, 80)
            pygame.draw.rect(self.game.screen, Colors.WHITE, slot1)
        elif self.game.player.inventory.selectedslot == 1:
            slot2 = pygame.Rect(Settings.Game.WIDTH / 2 - 240, Settings.Game.HEIGHT - 150, 80, 80)
            pygame.draw.rect(self.game.screen, Colors.WHITE, slot2)
        elif self.game.player.inventory.selectedslot == 2:
            slot3 = pygame.Rect(Settings.Game.WIDTH / 2 - 160, Settings.Game.HEIGHT - 150, 80, 80)
            pygame.draw.rect(self.game.screen, Colors.WHITE, slot3)
        elif self.game.player.inventory.selectedslot == 3:
            slot4 = pygame.Rect(Settings.Game.WIDTH / 2 - 80, Settings.Game.HEIGHT - 150, 80, 80)
            pygame.draw.rect(self.game.screen, Colors.WHITE, slot4)
        elif self.game.player.inventory.selectedslot == 4:
            slot5 = pygame.Rect(Settings.Game.WIDTH / 2 - 0, Settings.Game.HEIGHT - 150, 80, 80)
            pygame.draw.rect(self.game.screen, Colors.WHITE, slot5)
        elif self.game.player.inventory.selectedslot == 5:
            slot6 = pygame.Rect(Settings.Game.WIDTH / 2 + 80, Settings.Game.HEIGHT - 150, 80, 80)
            pygame.draw.rect(self.game.screen, Colors.WHITE, slot6)
        elif self.game.player.inventory.selectedslot == 6:
            slot7 = pygame.Rect(Settings.Game.WIDTH / 2 + 160, Settings.Game.HEIGHT - 150, 80, 80)
            pygame.draw.rect(self.game.screen, Colors.WHITE, slot7)

        itembarrects = [pygame.Rect(Settings.Game.WIDTH / 2 - 310, Settings.Game.HEIGHT - 140, 60, 60),
                        pygame.Rect(Settings.Game.WIDTH / 2 - 230, Settings.Game.HEIGHT - 140, 60, 60),
                        pygame.Rect(Settings.Game.WIDTH / 2 - 150, Settings.Game.HEIGHT - 140, 60, 60),
                        pygame.Rect(Settings.Game.WIDTH / 2 - 70, Settings.Game.HEIGHT - 140, 60, 60),
                        pygame.Rect(Settings.Game.WIDTH / 2 + 10, Settings.Game.HEIGHT - 140, 60, 60),
                        pygame.Rect(Settings.Game.WIDTH / 2 + 90, Settings.Game.HEIGHT - 140, 60, 60),
                        pygame.Rect(Settings.Game.WIDTH / 2 + 170, Settings.Game.HEIGHT - 140, 60, 60)]

        itembar = [(Settings.Game.WIDTH / 2 - 310, Settings.Game.HEIGHT - 140),
                   (Settings.Game.WIDTH / 2 - 230, Settings.Game.HEIGHT - 140),
                   (Settings.Game.WIDTH / 2 - 150, Settings.Game.HEIGHT - 140),
                   (Settings.Game.WIDTH / 2 - 70, Settings.Game.HEIGHT - 140),
                   (Settings.Game.WIDTH / 2 + 10, Settings.Game.HEIGHT - 140),
                   (Settings.Game.WIDTH / 2 + 90, Settings.Game.HEIGHT - 140),
                   (Settings.Game.WIDTH / 2 + 170, Settings.Game.HEIGHT - 140),
                   (Settings.Game.WIDTH / 2 + 250, Settings.Game.HEIGHT - 140)]

        pygame.draw.rect(self.game.screen, (50, 50, 50), itembarrects[0])
        pygame.draw.rect(self.game.screen, (50, 50, 50), itembarrects[1])
        pygame.draw.rect(self.game.screen, (50, 50, 50), itembarrects[2])
        pygame.draw.rect(self.game.screen, (50, 50, 50), itembarrects[3])
        pygame.draw.rect(self.game.screen, (50, 50, 50), itembarrects[4])
        pygame.draw.rect(self.game.screen, (50, 50, 50), itembarrects[5])
        pygame.draw.rect(self.game.screen, (50, 50, 50), itembarrects[6])
        self.game.screen.blit(pygame.transform.scale(Assets.BACKPACK1.value.image, (60, 60)), itembar[7])

        self.helditem = (Settings.Game.WIDTH / 2 - 44, Settings.Game.HEIGHT / 2 - 6)
        for i, item in enumerate(self.game.player.inventory.getslots()):
            self.game.screen.blit(pygame.transform.scale(item.item.image, (60, 60)), itembar[i])
            if i == self.game.player.inventory.selectedslot:
                self.game.screen.blit(pygame.transform.flip(pygame.transform.scale(item.item.image, (30,30)), True, False), self.helditem)
