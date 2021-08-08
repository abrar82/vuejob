<template>
  <li>
    {{ job.job_name }}
    <!-- <button @click="$emit('remove', todo.id)">
      X
    </button> -->
  </li>
</template>

<script>
export default {
props: {
    job: {
      type: Object,
      required: true
    }
  }
}
</script>

<style>

</style>