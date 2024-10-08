<?php

namespace Database\Seeders;

use App\Models\User;
// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        // User::factory(10)->create();

        $users = [
            [
                'first_name' => 'kent',
                'last_name' => 'escoto',
                'middle_initial' => 'l',
                'gender' => 'male',
                'phone_number' => '+639507541450',
                'status' => 'active',
                'role' => 'superadmin',
                'username' => 'kentoy',
                'password' => Hash::make('password'), 
                'email' => 'kentescoto24@gmail.com',
            ],
            [
                'first_name' => 'luis',
                'last_name' => 'suizo',
                'middle_initial' => 'l',
                'gender' => 'male',
                'phone_number' => '+639810921795',
                'status' => 'active',
                'role' => 'admin',
                'username' => 'luis',
                'password' => Hash::make('password'), 
                'email' => 'luis@gmail.com',
            ],
            [
                'first_name' => 'rochy',
                'last_name' => 'cocjin',
                'middle_initial' => 'r',
                'gender' => 'female',
                'phone_number' => '+639156783366',
                'status' => 'active',
                'role' => 'client',
                'username' => 'rochyyy',
                'password' => Hash::make('password'), 
                'email' => 'rochyyy@gmail.com',
            ],
        ];

        foreach ($users as $user) {
            User::create($user);
        }
    }
}