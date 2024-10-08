export const generateData = (gdata) => {
    return gdata;
};

export async function fetchUsers() {
    console.log('Fetching users...');
    try {
        const response = await fetch('http://127.0.0.1:8000/api/users', {
            method: 'GET',
            headers: {
                Authorization: 'Bearer ' + localStorage.getItem('_token') // Use 'Bearer' prefix for token
            }
        });
        
        if (!response.ok) {
            throw new Error(`No data found in response: ${response.statusText}`);
        }

        const data = await response.json();
        console.log('Fetched users data:', data);

        // Ensure we handle multiple users dynamically
        const generate_data = data.map(user => ({
            id: user.id,
            username: user.username,
            role: user.role,
            status: user.status,
            name: `${user.first_name} ${user.middle_initial ? user.middle_initial + '. ' : ''}${user.last_name}`
        }));

        return generateData(generate_data);

    } catch (error) {
        console.error('Error fetching users:', error.message);
    }
}
