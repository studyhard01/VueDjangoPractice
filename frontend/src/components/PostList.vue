<template>
  <v-container class="mt-10">
    <v-data-table :headers="headers" :items="posts" :sort-by="id">
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Post List</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn outlined @click="dialogOpen('create', {})">
            New Post
          </v-btn>
        </v-toolbar>
      </template>
      <!-- eslint-disable-next-line vue/valid-v-slot -->
      <template v-slot:item.actions="{ item }">
        <v-icon class="mr-2" small @click="dialogOpen('update', item)">
          mdi-pencil
        </v-icon>
        <v-icon small @click="deleteItem(item)">
          mdi-delete
        </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="fetchPostList">
          Reset
        </v-btn>
      </template>
    </v-data-table>

    <v-dialog v-model="dialog" max-width="800px">
      <v-sheet>
        <v-toolbar dark color="primary">
          <v-toolbar-title>{{ formTitle }}</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn small icon dark @click="close">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar>

        <v-container>
          <v-form id="post-form">
            <v-row justify="center">
              <v-col cols="10">
                <v-text-field label="ID (readonly)" name="id" v-model="editedItem.id" readonly></v-text-field>
                <v-text-field label="TITLE" name="title" v-model="editedItem.title"></v-text-field>
                <v-text-field label="DESCRIPTION" name="description" v-model="editedItem.description"></v-text-field>
                <v-textarea label="CONTENT" name="content" v-model="editedItem.content"></v-textarea>
                <v-text-field label="OWNER (readonly)" name="owner" v-model="editedItem.owner" readonly></v-text-field>
                <v-text-field label="TAGS" name="tags" v-model="editedItem.tags"></v-text-field>
              </v-col>
            </v-row>
          </v-form>

          <v-row justify="center">
            <v-btn color="bg-grey-lighten-1" variant="tonal" size="small" class="ma-3" @click="reset">
              Reset
            </v-btn>
            <v-btn color="primary" variant="tonal" size="small" class="ma-3" @click="save">
              Save
            </v-btn>
          </v-row>
        </v-container>
      </v-sheet>
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const dialog = ref(false)
const headers = ref([
  {
    text: 'ID',
    align: 'start',
    sortable: false,
    value: 'id',
  },
  { text: '제 목', value: 'title' },
  { text: '요 약', value: 'description' },
  { text: '수정일', value: 'modify_dt' },
  { text: '작성자', value: 'owner' },
  { text: 'Actions', value: 'actions', sortable: false },
])
const posts = ref([])
const editedIndex = ref(-1)
const editedItem = ref({})
let resetItem = {}

const formTitle = computed(() => {
  return editedIndex.value === -1 ? 'New Post' : 'Edit Post'
})

onMounted(() => {
  fetchPostList()
})

function fetchPostList() {
  posts.value = [
    {
      id: '1',
      title: 'Django 5.0 Released',
      description: '2023년 10월 장고 5.0 발표함',
      modify_dt: '2024-07-01',
      owner: 'shkim',
    },
    {
      id: 'Ice cream sandwich',
      title: 237,
      description: 9.0,
      modify_dt: 37,
      owner: 4.3,
    },
    {
      id: 'Eclair',
      title: 262,
      description: 16.0,
      modify_dt: 23,
      owner: 6.0,
    },
  ]
}

function dialogOpen(action, item) {
  console.log("dialogOpen()...", action, item)
  if (action === 'create') {
    editedIndex.value = -1
    editedItem.value = {}
  } else {
    editedIndex.value = posts.value.indexOf(item)
    editedItem.value = Object.assign({}, item)
  }
  dialog.value = true
  resetItem = Object.assign({}, item)
}

function deleteItem(item) {
  if (!confirm('Are you sure to delete ?')) return
  editedIndex.value = posts.value.indexOf(item)
  posts.value.splice(editedIndex.value, 1)
}

function close() {
  dialog.value = false
}

function reset() {
  console.log("reset()...")
  editedItem.value = Object.assign({}, resetItem)
}

function save() {
  if (editedIndex.value > -1) {
    Object.assign(posts.value[editedIndex.value], editedItem.value)
  } else {
    posts.value.push(editedItem.value)
  }
  close()
}
</script>

<style></style>