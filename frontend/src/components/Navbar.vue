<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const links = [
  {
    label: 'Home',
    path: '/home',
    icon: 'HomeIcon'
  },
  {
    label: 'Meus Estudos',
    path: '/estudos',
    icon: 'BookOpenIcon'
  },
  {
    label: 'Estatísticas',
    path: '/stats',
    icon: 'ChartBarIcon'
  },
  {
    label: 'Perfil',
    path: '/perfil',
    icon: 'UserIcon'
  }
];

const isActive = (path) => {
  return route.path === path;
};

const userName = computed(() => {
  return localStorage.getItem('usuario') || 'Usuário';
});
</script>

<template>
  <nav class="bg-white border-b border-gray-100 shadow-sm w-full">
    <div class="container mx-auto px-4 py-3">
      <div class="flex justify-between items-center">
        <!-- Logo e título -->
        <div class="flex items-center">
          <div class="bg-gradient-to-r from-indigo-600 to-blue-500 h-9 w-9 rounded-lg flex items-center justify-center text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
          </div>
          <h1 class="ml-2 text-xl font-bold text-gray-800">EstudaSync</h1>
        </div>

        <!-- Links de navegação para telas médias e grandes -->
        <div class="hidden md:flex items-center space-x-1">
          <router-link 
            v-for="(link, index) in links" 
            :key="index" 
            :to="link.path" 
            class="px-3 py-2 rounded-lg text-gray-700 font-medium transition-all duration-200 hover:bg-indigo-50 hover:text-indigo-600 flex items-center"
            :class="{ 'bg-indigo-50 text-indigo-600': isActive(link.path) }"
          >
            <svg v-if="link.icon === 'HomeIcon'" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            <svg v-if="link.icon === 'BookOpenIcon'" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
            <svg v-if="link.icon === 'ChartBarIcon'" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            <svg v-if="link.icon === 'UserIcon'" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
            <span>{{ link.label }}</span>
          </router-link>
        </div>

        <!-- Avatar de usuário -->
        <div class="flex items-center">
          <span class="text-sm text-gray-700 mr-2 hidden sm:block">{{ userName }}</span>
          <div class="h-8 w-8 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-600 font-medium">
            {{ userName.charAt(0).toUpperCase() }}
          </div>
        </div>
      </div>

      <!-- Menu móvel: visível apenas em telas pequenas -->
      <div class="md:hidden flex justify-between mt-3 pt-3 border-t border-gray-100">
        <router-link 
          v-for="(link, index) in links" 
          :key="index" 
          :to="link.path" 
          class="flex-1 flex flex-col items-center py-1 text-xs font-medium text-gray-700 transition-colors duration-200"
          :class="{ 'text-indigo-600': isActive(link.path) }"
        >
          <svg v-if="link.icon === 'HomeIcon'" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
          </svg>
          <svg v-if="link.icon === 'BookOpenIcon'" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
          </svg>
          <svg v-if="link.icon === 'ChartBarIcon'" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
          </svg>
          <svg v-if="link.icon === 'UserIcon'" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
          </svg>
          <span class="mt-1">{{ link.label }}</span>
        </router-link>
      </div>
    </div>
  </nav>
</template>