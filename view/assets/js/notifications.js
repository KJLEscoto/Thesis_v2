import { user } from '~/assets/js/userLogged'

// Initialize the motion object
export const notifications = [
    {
        get username() {
            return `${ user.username }`;
        },
        motion_detected: 'grab',
        description: 'This action is to take something.',
        screenshot: null,
        threshold: 78,
        date_captured: '2024/09/20',
        deleted_at: null
    },
    {
        get username() {
            return `${ user.username }`;
        },
        motion_detected: 'walking',
        description: 'This action is just walking.',
        screenshot: '/sample.jpg',
        threshold: 58,
        date_captured: '2024/09/20',
        deleted_at: null
    },
    // Add more motions as needed
];
