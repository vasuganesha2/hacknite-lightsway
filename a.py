def create_hitboxes(map_data, hitbox_length, hitbox_width):
    global all_hitboxes
    temp_surface = pygame.Surface(win.get_size(), pygame.SRCALPHA)
    hitbox_x = 0
    hitbox_y = 0
    temp_surface.fill((0, 0, 0, 0))
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == 0:
                image = pygame.image.load(r"./tiles1.jpg")
                image = pygame.transform.scale(image, (hitbox_length, hitbox_width))
                image_rect = image.get_rect(center=(hitbox_x, hitbox_y))
                win.blit(image, image_rect)
            if map_data[i][j] == 4:
                hitbox = create_hitbox(hitbox_length, hitbox_width, hitbox_x, hitbox_y)
                all_hitboxes.append(hitbox)
                image = pygame.image.load(r"./tiles2.jpg")
                image = pygame.transform.scale(image, (hitbox_length, hitbox_width))
                image_rect = image.get_rect(center=(hitbox_x, hitbox_y))
                win.blit(image, image_rect)
            elif map_data[i][j] == 5:
                hitbox = create_hitbox(hitbox_length, hitbox_width, hitbox_x, hitbox_y)
                all_hitboxes.append(hitbox)
                pygame.draw.rect(win, (255, 255, 0), hitbox, 1)
                if man.hitbox.colliderect(hitbox):
                    man.has_key1 = True
                if man.hitbox.colliderect(hitbox):
                    man.has_key1 = True
            elif map_data[i][j] == 3:
                hitbox = create_hitbox(hitbox_length, hitbox_width, hitbox_x, hitbox_y)
                all_hitboxes.append(hitbox)
                pygame.draw.rect(win, (255, 255, 0), hitbox, 1)
                if man.hitbox.colliderect(hitbox):
                    map_data[i][j] = 0
                    man.has_key1 = True
                all_hitboxes.remove(hitbox)
            hitbox_x += hitbox_length
        hitbox_x = 0
        hitbox_y += hitbox_width
    win.blit(temp_surface, (0, 0))
    pygame.display.flip()
    return all_hitboxes
