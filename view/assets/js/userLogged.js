import { reactive } from "vue";

// Initialize the user object
export const user = reactive({
  first_name: "kent joemar",
  last_name: "escoto",
  mi: "l",
  gender: "male",
  phone: "09123456789",
  email: 'kentescoto24@gmail.com',

  // statically change it for now just to test (client, admin, superadmin)
  role: "admin",

  status: "active",
  username: "kentoy123",
  password: "password",
  account_created: "2024/05/26",
  updated_at: "2024/05/26",
  
  get name() {
    return `${this.first_name} ${this.mi}. ${this.last_name}`;
  }
});

