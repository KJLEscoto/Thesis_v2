import { reactive } from 'vue';

// Initialize the user object
export const user = reactive({
  first_name: '',
  last_name: '',
  middle_initial: '',
  gender: '',
  phone_number: '',
  email: '',
  role: '',
  status: '',
  username: '',
  password: '',
  created_at: '',
  updated_at: '',
  
  get name() {
    return `${this.first_name} ${this.middle_initial ? this.middle_initial + '. ' : ''}${this.last_name}`;
  }
});


// Fetch user data from the API and update the reactive state
export async function fetchUser() {
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/user`, {
      method: 'GET',
      headers: {
        Authorization: 'Bearer ' + localStorage.getItem('_token') // Use 'Bearer' prefix for token
      }
    });

    if (response.ok) {
      const data = await response.json();
      console.log('Fetched user data:', data);
      // Update user properties with the fetched data
      user.first_name = data.first_name;
      user.last_name = data.last_name;
      user.middle_initial = data.middle_initial;
      user.gender = data.gender;
      user.phone_number = data.phone_number;
      user.email = data.email;
      user.role = data.role || user.role;
      user.status = data.status || user.status;
      user.username = data.username || user.username;
      user.created_at = data.created_at || user.created_at;
      user.updated_at = data.updated_at || user.updated_at;
    } else {
      console.error('No data found in response:', response);
    }
  } catch (error) {
    console.error('Error fetching user:', error);
    if (error.response) {
      console.error('Error response:', error.response);
    } else {
      console.error('Network error');
    }
  }
}
