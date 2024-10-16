function generateAvatar(width, height) {
    const avatars = [];
    let number_of_avatars = 120    // 20 avatars

    for(let i = 1; i <= number_of_avatars; i++) {
        let robohash = 'https://robohash.org/set_set1/bgset_bg1/' + i + '.png?size=' + width + 'x' + height;
        avatars.push(robohash); 
    }

    return avatars;
}

export const avatar = generateAvatar(1000, 1000);


// import { avatar } from '~/assets/js/avatar'
