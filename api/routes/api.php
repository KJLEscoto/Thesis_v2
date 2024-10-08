<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController; // Corrected
use App\Http\Controllers\MotionsController;
use App\Http\Controllers\NotificationsController;

Route::post('register', [AuthController::class, 'register']);
Route::post('login', [AuthController::class, 'login']);

Route::post('auth/login', [AuthController::class, 'authenticateUser']);
Route::post('login/admin', [AuthController::class, 'loginAdmin']);
Route::middleware('auth:sanctum')->get('/user', [AuthController::class, 'getUser']);
Route::middleware('auth:sanctum')->post('/user/logout', [AuthController::class, 'logoutUser']);
Route::middleware('auth:sanctum')->put('/user/update', [AuthController::class, 'updateMainUser']);
Route::post('logout', [AuthController::class, 'logout'])->middleware('auth:sanctum');


Route::apiResource('motions', MotionsController::class);


Route::middleware('auth:sanctum')->group(function () {
    Route::apiResource('notifications', NotificationsController::class);
});


Route::middleware('auth:sanctum')->group(function () {
    Route::get('/users', [AuthController::class, 'getAllUsers']); // Get all users
    Route::get('/users/{username}', [AuthController::class, 'getUserById']); // Get a specific user by ID
    Route::put('/users/{username}', [AuthController::class, 'updateUser']); // Update a specific user
});

Route::put('status/{id}', [AuthController::class, 'setStatus']);