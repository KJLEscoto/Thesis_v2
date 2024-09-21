
import { faker } from '@faker-js/faker';

const roleOptions = ['Client', 'Admin'];
const statusOptions = ['Active', 'Inactive'];

// fake data
export const generateData = () => {
    const data = [];
    for (let i = 1; i <= 25; i++) {
    const firstname = faker.person.firstName();
    const lastname = faker.person.lastName();
    const middle_initial = faker.string.alpha().toUpperCase();
    const name = `${firstname} ${middle_initial}. ${lastname}`;

    data.push({
        id: i,
        username: faker.internet.userName(),
        role: faker.helpers.arrayElement(roleOptions),
        status: faker.helpers.arrayElement(statusOptions),
        name: name
    });
    }
    return data;
};